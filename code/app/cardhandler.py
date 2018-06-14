import random

import constantshandler

#Determine the value of the current hand
def Determine_Value_Of_Hand(Hand):
    Current_Value, Ace_Status = Hand
    if(Determine_If_Hand_Has_Usable_Ace(Hand) == True):
        #If an Ace is usable,m increase value by 10
        #Note: An Ace grants a +1 value automatically
        return (Current_Value + 10)
    else:
        return Current_Value

#Set the Initial Hand
def Initial_Hand():
    return (0, False)

#Helper function that determines if the hand has a usable ace
#An ace is usable if it doesn't go over 21, and we have an ace in hand
def Determine_If_Hand_Has_Usable_Ace(Hand):
    Current_Value, Ace_Status = Hand
    if(Current_Value <= 11 and Ace_Status == True):
        return True
    else:
        return False

#Draw from a deck with 4 of each card
#Cards are valued at their face value between 2-10
#Kings, Queens, and Jacks are valued at 10.
#Ace card can either be 1, or 11 of value.
#However, I consider it a + 10 because we assume it as an initial value of 1.
def Draw_Card():
    #Picking a card from an unbaised deck
    #Total of 13 types of cards
    RandomCard = random.randint(1,13)
    return Calculate_Face_Value(RandomCard)

#Calculate The Face Value of the selected card
def Calculate_Face_Value(RandomCard):
    #If the card is a 10, Joker, Queen or King
    if(RandomCard == 10 or RandomCard == 11 or RandomCard == 12 or RandomCard == 13):
        RandomCardValue = 10
    #Otherwise, assign it its corresponding value
    else:
        RandomCardValue = RandomCard
    return RandomCardValue

#Draw a card to existing hand
def Add_Card_To_Hand(Hand, Card):
    Hand_Value, Ace_Status = Hand
    #Update the hand value with the drawn card
    #Once we hit we MUST update the hand value
    Hand_Value = Hand_Value + Card

    #Card #1 is an Ace
    if(Card == 1):
        Ace_Status = True

    return (Hand_Value, Ace_Status)

#Draw the player's hand
def Draw_Player_Hand():

    #Initializing hand as empty
    Hand = Initial_Hand()

    #Running first 2 draw hands, as per Blackjack rules.
    Hand = Add_Card_To_Hand(Hand, Draw_Card())
    Hand = Add_Card_To_Hand(Hand, Draw_Card())

    #While the value of the hand is less than 11, keep hitting
    while(Determine_Value_Of_Hand(Hand) < 11):
        Hand = Add_Card_To_Hand(Hand, Draw_Card())
    return Hand

#Draw the dealer's hand
def Draw_Dealer_Hand():

    #Initializing hand as empty
    Hand = Initial_Hand()

    #We need to keep track of the drawn card for the dealer
    NewCard = Draw_Card()

    #Drawing new card and adding it to the hand
    Hand = Add_Card_To_Hand(Hand, NewCard)
    return Hand, NewCard


#Playing the dealer's turn based on a fix policy
#The policy states that while the value of the hand is less than 17, keep hidding.
#As discribed here: https://www.youtube.com/watch?v=idB-7FUaC-g
def Play_Dealer(Hand):
    while(Determine_Value_Of_Hand(Hand) < 17):
        Hand = Add_Card_To_Hand(Hand, Draw_Card())
    return Hand

#Determines reward for current state
#You win 1 for every "win"
#For a tie you gain nothing
#For a loss you lose 1
def Reward_For_State(Current_Player_Hand, Current_Dealer_Hand):

    #Calculate Player Hand Value
    Player_Hand_Value = Determine_Value_Of_Hand(Current_Player_Hand)

    #Calculate Dealer Hand Value
    Dealer_Hand_Value = Determine_Value_Of_Hand(Current_Dealer_Hand)

    #Dealer Busts
    if (Dealer_Hand_Value > 21):
        return constantshandler.Win_Reward
    #Player Busts
    elif (Player_Hand_Value > 21):
        return constantshandler.Loss_Reward
    #Dealer Wins
    elif (Player_Hand_Value < Dealer_Hand_Value):
        return constantshandler.Loss_Reward
    #Player Wins
    elif (Player_Hand_Value > Dealer_Hand_Value):
        return constantshandler.Win_Reward
    #A tie
    elif(Player_Hand_Value == Dealer_Hand_Value):
        return constantshandler.Tie_Reward