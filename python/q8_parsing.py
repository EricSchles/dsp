# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored
# 79 goals against opponents, and had 36 goals scored against them).
# Write a program to read the file, then print the name of the team
# with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional. You can use it or you can write the script
# with an approach of your choice.

import pandas as pd

# Reading the data into a dataframe
football_data = pd.read_csv('football.csv')

# Adding a column to dataframe to find the difference
football_data['Goal Difference'] = abs(football_data['Goals'] - football_data['Goals Allowed'])

# Determining which team has the lowest in goal difference
return (football_data[['Team', 'Goal Difference']][football_data['Goal Difference'] == football_data['Goal Difference'].min()])