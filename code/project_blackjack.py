import sys, random, re

from app import qlearninghandler
from app import constantshandler
from app import testsuite
from app import graphhandler



#-- Synopsis of Program --#
#I am going to be implementing a program that plays Blackjack against a dealer with a set policy.
#As the player plays the game, he will learn to improve his play using Reinforcement learning.
#I will be using the Q-Learning algorithm to accomplish this.
#Actions will be determined by an epsilon-greedy policy for the player.
#The Dealer's policy will be based on a set policy determined by the numerical value of his hand.
#A Player, and dealer's hand is determined by a tuple.
#This Tuple represents, the total numerical value of the hand, and a Boolean determining if there is an ace or not.
#Aces are treated with this special condition because they can either be valued at 1, or 10.
#My solution is based off this paper: http://www.cs.ou.edu/~granville/paper.pdf

print("Running Q-Learning Algorithm on Toy Blackjack game with Alpha: " + str(constantshandler.Alpha) + ", Epison: " + str(constantshandler.Epsilon) + ", Iterations: " + str(constantshandler.Iterations) + ", Games To Play: " + str(constantshandler.Games_To_Play) + "." )
Q_Values, Sampling1, Sampling2, Sampling3, Sampling4 = qlearninghandler.Q_Learning_Algorithm()
Winnings_List = qlearninghandler.Winnings_Calculator(Q_Values)
qlearninghandler.Calculate_Best_Policy(True, Q_Values)
qlearninghandler.Calculate_Best_Policy(False, Q_Values)
#graphhandler.Curve_Graph(Winnings_List, constantshandler.Winnings_Curve_File_Name, "Winnings Graph")
#graphhandler.Curve_Graph(Sampling1, constantshandler.Sampling1_File_Name, "Q Value Sampling 1: (5, 20, False), False")
#graphhandler.Curve_Graph(Sampling2, constantshandler.Sampling2_File_Name, "Q Value Sampling 2: (2, 16, True), True)")
#graphhandler.Curve_Graph(Sampling3, constantshandler.Sampling3_File_Name, "Q Value Sampling 3: (3, 21, True), False)")
#graphhandler.Curve_Graph(Sampling4, constantshandler.Sampling4_File_Name, "Q Value Sampling 4: (10, 11, False), False)")

testsuite.Tests()
