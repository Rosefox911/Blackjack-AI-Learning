import actionhandler
import cardhandler
import constantshandler
import statehandler


 #Q Learning Dictionary of Values
#Map State, Action combinations to Q Values
#We stay on 19, 20 and 21.
#Otherwise, hit.
def Q_Learning_State_Action_Value_Mapping():
    #Initializing it
    Q_Learning_Map = {}

    #Possible States so we iterate through them
    Possible_States = statehandler.Possible_State_List_Creator()

    #Iterate through all possibvle states
    for State in Possible_States:
        Shown_Card, Hand_Value, Ace_Status = State

        #We prefer hitting
        if(Hand_Value < 19):
            Q_Learning_Map[(State, True)] = 0.0001
            Q_Learning_Map[(State, False)] = -0.0001
        #Otherwise, we prefer staying
        else:
            Q_Learning_Map[(State, True)] = -0.0001
            Q_Learning_Map[(State, False)] = 0.0001
    return Q_Learning_Map


def Q_Learning_Algorithm():

    #Initialize Q Values
    Q_Values = Q_Learning_State_Action_Value_Mapping()

    #Keep track of the number of times each State -> Action mapping has been seen
    Count = statehandler.Map_States_To_Actions()

    #List of all possible states
    Possible_States = statehandler.Possible_State_List_Creator()


    #Random Q_Values Samplings
    QA_Values1 = []
    QA_Values2 = []
    QA_Values3 = []
    QA_Values4 = []

    for iteration in range(0, constantshandler.Iterations):

        #Extract Current State from iteration
        Current_State = statehandler.Random_State(Possible_States)

        #Extract values from state and convert to hands
        Shown_Card, Dealer_Current_Hand, Player_Hand = statehandler.Extract_Values_From_State_To_Hands(Current_State)

        while(1 == 1):

            #Pick Action (e-greedy policy)
            Action = actionhandler.Action_Handler(Q_Values, Current_State)

            #State Action
            SA = (Current_State, Action)

            #If we want to hit
            if(Action == True):

                #Add cared to player hand, since we hit.
                Player_Hand = cardhandler.Add_Card_To_Hand(Player_Hand, cardhandler.Draw_Card())
                #Assuming we didn't bust
                if(cardhandler.Determine_Value_Of_Hand(Player_Hand) <= 21):

                    #Grab next state
                    Next_State = statehandler.Extract_Values_From_Hands_To_States(Shown_Card, Player_Hand)

                    #Determine what the best Q Value is
                    Q_Best = Q_Values[(Next_State, True)]

                    #Assuming the next state Q Value for staying is MORE than that of staying, pick it.
                    if(Q_Values[Next_State, False] > Q_Best):

                        #Picking it and setting it to False
                        Q_Best = Q_Values[(Next_State, False)]

                    #Otherwisxe, make sure its set to hitting
                    else:
                        Q_Best = Q_Values[(Next_State, True)]

                    #Update the amount of times we have seen this State Action mapping.
                    Count[SA] = Count[SA] + constantshandler.Seen_Increase_Rate

                    #Based on the expected Q value, update the Q_Value entries
                    Q_Values[SA] = Q_Values[SA] + constantshandler.Alpha/Count[SA] * (Q_Best - Q_Values[SA])

                    if (SA == ((5, 20, False), False)):
                        QA_Values1.append(Q_Values[SA])
                    if (SA == ((2, 16, True), True)):
                        QA_Values2.append(Q_Values[SA])
                    if (SA == ((3, 21, True), False)):
                        QA_Values3.append(Q_Values[SA])
                    if (SA == ((10, 11, False), False)):
                        QA_Values4.append(Q_Values[SA])

                    #Move on to the next state
                    Current_State = Next_State

                # Busted
                elif (cardhandler.Determine_Value_Of_Hand(Player_Hand) > 21):

                    # Update this state action mapping so we know we visited it.
                    Count[SA] = Count[SA] + constantshandler.Seen_Increase_Rate

                    # Update Q Value to the Loss Rate since we lost.
                    Q_Values[SA] = Q_Values[SA] + constantshandler.Alpha / Count[SA] * (
                    constantshandler.Loss_Reward - Q_Values[SA])

                    if (SA == ((5, 20, False), False)):
                            QA_Values1.append(Q_Values[SA])
                    if (SA == ((2, 16, True), True)):
                            QA_Values2.append(Q_Values[SA])
                    if (SA == ((3, 21, True), False)):
                            QA_Values3.append(Q_Values[SA])
                    if (SA == ((10, 11, False), False)):
                            QA_Values4.append(Q_Values[SA])

                    break
            #If the action is to stay
            else:
                #Update dealer's hand
                Dealer_Current_Hand = cardhandler.Play_Dealer(Dealer_Current_Hand)

                #Update the expected reward for the game since we are staying
                Reward = cardhandler.Reward_For_State(Player_Hand, Dealer_Current_Hand)

                #Update the amount of times we have seen this state action mapping
                Count[SA] = Count[SA] + constantshandler.Seen_Increase_Rate

                #Update the Q Value entries based on our reward based on the current state and staying
                Q_Values[SA] = Q_Values[SA] + constantshandler.Alpha/Count[SA] * (Reward - Q_Values[SA])

                if (SA == ((5, 20, False), False)):
                    QA_Values1.append(Q_Values[SA])
                if (SA == ((2, 16, True), True)):
                    QA_Values2.append(Q_Values[SA])
                if (SA == ((3, 21, True), False)):
                    QA_Values3.append(Q_Values[SA])
                if (SA == ((10, 11, False), False)):
                    QA_Values4.append(Q_Values[SA])

                break


    return Q_Values, QA_Values1, QA_Values2, QA_Values3, QA_Values4

#Calculate best Policy Based on Q Values
def Calculate_Best_Policy(Ace_Status, Q_Values):
    print("Optimal Policy with Ace Status of: " + str(Ace_Status))
    for Hand_Value in constantshandler.Possible_Hand_Values:
        for Shown_Card in constantshandler.Possible_Shown_Card_Values:
            if(Q_Values[((Shown_Card, Hand_Value, Ace_Status), True)] > Q_Values[((Shown_Card, Hand_Value, Ace_Status), False)]):
                print("Where Hand Value is: " + str(Hand_Value) + " and Shown Card is: " + str(Shown_Card) +" Player should: Hit")
            else:
                print("Where Hand Value is: " + str(Hand_Value) + " and Shown Card is: " + str(Shown_Card) + " Player should: Stay")
    print('\n')


#Calculate expected winnings based on Q Values
def Winnings_Calculator(Q_Values):
    #Initialize Winnings as a float
    Winnings = 0.0

    Winnings_List = []

    #Iterate through the amount of times we are playing the game
    for n in range(0, constantshandler.Games_To_Play):

        #Draw the player's hand
        Player_Hand_Value = cardhandler.Draw_Player_Hand()

        #Draw the Dealer's Hand
        Dealer_Hand_Value, Shown_Card = cardhandler.Draw_Dealer_Hand()

        #Extract the current state from hands
        Current_State = statehandler.Extract_Values_From_Hands_To_States(Shown_Card, Player_Hand_Value)

        #Grab trhe expected value of this state and hitting
        Expected_Value = Q_Values[(Current_State, False)]

        #If you gain more from staying than from hitting again
        if (Q_Values[(Current_State, True)] > Expected_Value):

            #Update the Expected Winnings to the higher value
            Expected_Value = Q_Values[(Current_State, True)]

        #Update our winnings to be increased by current winnings, plus the expected value of this state action combination
        Winnings = Winnings + Expected_Value

        Winnings_List.append(Winnings)


    Expected_Winning_Per_Game = Winnings / float(constantshandler.Games_To_Play)

    print("Expected winnings per game is: " + str(Expected_Winning_Per_Game))
    return Winnings_List