import random


import cardhandler
import constantshandler

#Select a random state from the given state space
def Random_State(State_Space):
    Selected_State = State_Space[random.randint(0, len(State_Space)-1)]
    return Selected_State

#Returns a list of all possible states
#Since there are only a finite number of possible states in Blackjack, we can quantify it.
def Possible_State_List_Creator():

    #Initialize list of possible states
    Possible_States = []

    for Card in constantshandler.Possible_Shown_Card_Values:
        for Hand_Values in constantshandler.Possible_Hand_Values:
            #We add a case for both the ace being usable, and not to cover all possible states
            Possible_States.append((Card, Hand_Values, False))
            Possible_States.append((Card, Hand_Values, True))
    return Possible_States

#Mapping the outcome of a state and action combination to a dictionary. Initializing it at 0 reward
#This will be continiously updated
def Map_States_To_Actions():
    #Populating list of possible states
    Possible_States = Possible_State_List_Creator()

    #Initialize Map_Of_States_To_Actions_Q_Values
    Map_Of_States_To_Actions_Q_Values = {}
    #For every state in Possible_States, map it to a value and an action
    #Reminder: Actions are either Hit (True) or Stay (False)
    for Possible_State in Possible_States:
        Map_Of_States_To_Actions_Q_Values[(Possible_State, False)] = 0.0
        Map_Of_States_To_Actions_Q_Values[(Possible_State, True)] = 0.0
    return Map_Of_States_To_Actions_Q_Values



#Extract Values from current Player and Dealers hand and transform them into a state
#where the current player's hand value, dealer's shown card and Player's Ace Status is shown.
def Extract_Values_From_Hands_To_States(Shown_Card, Player_Hand_Value):
    Current_Hand_Value  = cardhandler.Determine_Value_Of_Hand(Player_Hand_Value)
    Ace_Status = cardhandler.Determine_If_Hand_Has_Usable_Ace(Player_Hand_Value)
    Together = (Shown_Card, Current_Hand_Value, Ace_Status)
    return Together

#Extract Values from State extracts the Player's hand value, Dealer's current shown card, and whether a player the player has an ace
#Return the Player's Hand Value, Dealer's Hand Value, and the currently shown Dealer's card in that order
def Extract_Values_From_State_To_Hands(CurrentState):
    Dealer_Shown_Card, Player_Hand_Value, Player_Ace_Status = CurrentState

    #If the player has a usable Ace, then lets reduce the value of the player's current hand by 10
    #This gives us the option to "use" it later
    if(Player_Ace_Status == True):
        Player_Hand_Value = Player_Hand_Value - 10

    #Update the Player's Hand
    Player_Current_Hand = (Player_Hand_Value, Player_Ace_Status)

    #Initialize and Update Dealer's hand based on shown card
    Dealer_Current_Hand = cardhandler.Initial_Hand()
    Dealer_Current_Hand = cardhandler.Add_Card_To_Hand(Dealer_Current_Hand, Dealer_Shown_Card)
    return Dealer_Shown_Card, Dealer_Current_Hand, Player_Current_Hand