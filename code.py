# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how to a read it.

data_ipl = np.genfromtxt(path, delimiter=',', skip_header=1, dtype=str)

# Number of unique matches 

# How many matches were held in total we need to know so that we can analyze further statistics keeping that in mind.
len(set(data_ipl[:,0]))

# Number of unique teams

# this exercise deals with you getting to know that which are all those six teams that played in the tournament.
team1_set = set(data_ipl[:, 3])
team2_set = set(data_ipl[:, 4])
unique_teams = team1_set.union(team2_set)
print(unique_teams)

# Sum of all extras

# An exercise to make you familiar with indexing and slicing up within data.
extras = data_ipl[:, 17]
extras_int = extras.astype(np.int16)
print(extras_int.sum())

# Delivery number when a given player got out

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
wicket_filter = (data_ipl[:, 20] == 'SR Tendulkar')
wickets_arr = data_ipl[wicket_filter]
print(wickets_arr[:, 11])
print(wickets_arr[:, 21])

# Number of times Mumbai Indians won the toss

# this exercise will help you get the statistics on one particular team
team_records = data_ipl[data_ipl[:, 5] == 'Mumbai Indians']
unique_matches = set(team_records[:, 0])
print(len(unique_matches))

# Filter record where batsman scored six and player with most number of sixex

# An exercise to know who is the most aggresive player or maybe the scoring player 
sixes = data_ipl[data_ipl[:, 16].astype(np.int16) == 6]
from collections import Counter
most_sixes_scored = Counter(sixes[:,13],)
print(most_sixes_scored.most_common(3))



