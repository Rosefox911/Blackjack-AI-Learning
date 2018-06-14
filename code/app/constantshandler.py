#The number of iterations to run when using Q-Learning
Iterations = 1000000

#The value of Epsilon
#Since we are using an Epsilon-greedy policy, we are setitng it to 0.1
#As stated in this paper: http://people.inf.elte.hu/lorincz/Files/RL_2006/SuttonBook.pdf
Epsilon = 0.1

#Alpha Value for Q-Learning
#Set to 1 for no discount
Alpha = 1

#List of all Possible Shown Card in Blackjack
Possible_Shown_Card_Values = range(1,12)

#List of all Possible Hand Value combinations
#we only consider up to 22, because after 21 it is a bust
Possible_Hand_Values = range(11,22)

#Number of Games to play
Games_To_Play = 100000

#Loss Reward
Loss_Reward = -1.0

#Win Reward
Win_Reward = 1.0

#Tie Reward
Tie_Reward = 0.0

#Seen Increase Rate determines the amount of increase when a state action combination has been seen
Seen_Increase_Rate = 1.0

#Winnings Curve File Name
Winnings_Curve_File_Name = "graphs/winnings_curve.png"

#Q Values for State -> Action Sampling
Sampling1_File_Name = "graphs/sampling1_q_value.png"
Sampling2_File_Name = "graphs/sampling2_q_value.png"
Sampling3_File_Name = "graphs/sampling3_q_value.png"
Sampling4_File_Name = "graphs/sampling4_q_value.png"