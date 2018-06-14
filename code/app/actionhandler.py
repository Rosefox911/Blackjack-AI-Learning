import random
import constantshandler

#Action_Handler controls the action we take.
#A action is defined as either staying (not hitting) or hitting.
#When you hit, a card is drawn for the player.
#When you stay, the player does not draw a card.
#using e-greedy policy for now
def Action_Handler(Q_Value, Current_State):
    # If a random between 0.0 and 1.0 is lower than the set Epsilon, then explore
    if (random.random() > constantshandler.Epsilon):
        return Select_Q_Value_Maximizing_Action(Q_Value, Current_State)
    # Otherwise, take best action
    else:
        return Select_Random_Action()

#Select Q Value Maximizing Action selects the action believed to maximize Q
#on whether we should hit, or stay
def Select_Q_Value_Maximizing_Action(Q_Values, Current_State):
    Q_Value_Hitting = Q_Values[(Current_State, True)]
    Q_Value_Staying = Q_Values[(Current_State, False)]
    if(Q_Value_Hitting < Q_Value_Staying):
        return False
    #Otherwise, hit
    else:
        return True

#Select a random action
#Either hit (True) or stay (False)
def Select_Random_Action():
    return random.choice([True, False])
