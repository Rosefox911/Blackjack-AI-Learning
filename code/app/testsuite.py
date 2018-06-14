import sys

import cardhandler
import actionhandler
import qlearninghandler
import statehandler


#---- CardHandler Tests ----#

def Tests():
    try:
        print("Running Card Handler Tests...")
        print("Testing to see what Determine_Value_Of_Hand returned if we have an Ace and value is 11: " + str(cardhandler.Determine_Value_Of_Hand((11, True))))
        print("Testing to see what Determine_Value_Of_Hand returned if we do not have an Ace and value is 10: " + str(cardhandler.Determine_Value_Of_Hand((10, False))))
        print("Testing to see what Determine_Value_Of_Hand returned if we have an Ace and value is 20: " + str(cardhandler.Determine_Value_Of_Hand((20, True))))
        print("Testing to see what Determine_Value_Of_Hand returned if we do not have an Ace and value is 20: " + str(cardhandler.Determine_Value_Of_Hand((20, False))))
        print("Testing to see what Initial_hand Returns: " + str(cardhandler.Initial_Hand()))
        print("Testing to see what Draw_Card returns: " + str(cardhandler.Draw_Card()))
        print("Testing to see what Calculate_Face_Value returns with input of 1: " + str(cardhandler.Calculate_Face_Value(1)))
        print("Testing to see what Calculate_Face_Value returns with input of 3: " + str(cardhandler.Calculate_Face_Value(3)))
        print("Testing to see what Calculate_Face_Value returns with input of 10: " + str(cardhandler.Calculate_Face_Value(10)))
        print("Testing to see what Calculate_Face_Value returns with input of 11: " + str(cardhandler.Calculate_Face_Value(11)))
        print("Testing to see what Add_Card_To_Hand returns with a Hand of (False, 10) and a card of 1: " + str(cardhandler.Add_Card_To_Hand((False, 10), 1)))
        print("Testing to see what Add_Card_To_Hand returns with a Hand of (True, 10) and a card of 1: " + str(cardhandler.Add_Card_To_Hand((True, 10), 1)))
        print("Testing to see what Add_Card_To_Hand returns with a Hand of (False, 20) and a card of 1: " + str(cardhandler.Add_Card_To_Hand((False, 20), 1)))
        print("Testing to see what Add_Card_To_Hand returns with a Hand of (True, 20) and a card of 1: " + str(cardhandler.Add_Card_To_Hand((True, 20), 1)))
        print("Testing to see what Add_Card_To_Hand returns with a Hand of (False, 20) and a card of 2: " + str(cardhandler.Add_Card_To_Hand((False, 20), 2)))
        print("Testing to see what Add_Card_To_Hand returns with a Hand of (False, 20) and a card of 2: " + str(cardhandler.Add_Card_To_Hand((True, 20), 2)))
        print("Testing to see what Draw_Player_Hand returns: " + str(cardhandler.Draw_Player_Hand()))
        print("Testing to see what Draw_Dealer_Hand returns: " + str(cardhandler.Draw_Dealer_Hand()))
        print("Testing to see what Play_Dealer returns with a hand of (False, 10): " + str(cardhandler.Play_Dealer((False, 10))))
        print("Testing to see what Play_Dealer returns with a hand of (False, 16): " + str(cardhandler.Play_Dealer((False, 16))))
        print("Testing to see what Play_Dealer returns with a hand of (False, 17): " + str(cardhandler.Play_Dealer((False, 17))))
        print("Testing to see what Play_Dealer returns with a hand of (True, 10): " + str(cardhandler.Play_Dealer((True, 10))))
        print("Testing to see what Play_Dealer returns with a hand of (True, 16): " + str(cardhandler.Play_Dealer((True, 16))))
        print("Testing to see what Play_Dealer returns with a hand of (True, 17): " + str(cardhandler.Play_Dealer((True, 17))))
        print("Testing to see what Reward_For_State returns with a player hand of (22, False) and a dealer hand of (10, True): " + str(cardhandler.Reward_For_State((22, False), (10, False))))
        print("Testing to see what Reward_For_State returns with a player hand of (10, False) and a dealer hand of (22, True): " + str(cardhandler.Reward_For_State((10, False), (22, False))))
        print("Testing to see what Reward_For_State returns with a player hand of (9, False) and a dealer hand of (10, False): " + str(cardhandler.Reward_For_State((9, False), (10, False))))
        print("Testing to see what Reward_For_State returns with a player hand of (10, True) and a dealer hand of (10, False): " + str(cardhandler.Reward_For_State((10, True), (10, False))))
        print("Testing to see what Reward_For_State returns with a player hand of (10, False) and a dealer hand of (10, False): " + str(cardhandler.Reward_For_State((10, False), (10, False))))
        print("Testing to see what Reward_For_State returns with a player hand of (10, False) and a dealer hand of (10, True): " + str(cardhandler.Reward_For_State((10, False), (10, True))))

        print("Running Q Learning Handler Tests...")
        Q_Values, Sampling1, Sampling2, Sampling3, Sampling4 = qlearninghandler.Q_Learning_Algorithm()
        print("Testing to see what is returned from Q_Learning_Algorithm: " + str(Q_Values))
        print("Testing to see what is returned from Winnings_Calculator: " + str(qlearninghandler.Winnings_Calculator(Q_Values)))
        print("Testing to see what is returned from Calculate_Best_Policy: ")
        qlearninghandler.Calculate_Best_Policy(True, Q_Values)
        print("Testing to see what is returned from Calculate_Best_Policy: ")
        qlearninghandler.Calculate_Best_Policy(False, Q_Values)

        print("Running Action Handler Tests...")
        print("Testing to see what is returned from Action_Handler: " + str(actionhandler.Action_Handler(Q_Values, (1, 15, True))))
        print("Testing to see what is returned from Select Q_Value_Maximizing_Action: " + str(actionhandler.Select_Q_Value_Maximizing_Action(Q_Values, (1, 15, True))))
        print("Testing to see what is returned from Select_Random_Action: " + str(actionhandler.Select_Random_Action()))

        print("Running State Handler Tests...")
        Possible_States = statehandler.Possible_State_List_Creator()
        print("Testing to see what is returned from Possible_State_List_Creator: " + str(Possible_States))
        print("Testing to see what is returned from Random_State: " + str(statehandler.Random_State(Possible_States)))
        print("Testing to see what is returned from Map_States_To_Actions: " + str(statehandler.Map_States_To_Actions()))
        print("Testing to see what is returned from Extract_Values_From_Hands_To_States: " + str(statehandler.Extract_Values_From_Hands_To_States(1, (10, True))))
        print("Testing to see what is returned from Extract_Values_From_State_To_Hands: " + str(statehandler.Extract_Values_From_State_To_Hands(Possible_States[0])))

        print("All tests completed successfully.")
    except Exception as e:
        print("Error encountered during running of tests.")
        print(e)