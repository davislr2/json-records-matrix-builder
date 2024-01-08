# Python script to convert json file of records against each team to a matrix of head to head matchups.

import json

""" 
Converts a json file of records against each team to a matrix of head to head matchups.
:param json_file: json file of records against each team
:return: 2D matrix of head to head matchups

"""
def json_to_matrix(json_file):
    # Read in the json file and get the list of teams
    data = json.load(json_file)
    teams = list(data.keys())

    # Create an empty 2D matrix with each axis keyed on the team name
    matrix = {team: {opponent: "-" for opponent in teams} for team in teams}

    # Fill in the matrix with the number of wins against each opponent
    for team in teams:
        for opponent in teams:
            if team != opponent:
                matrix[team][opponent] = f"{data[team][opponent]['W']}"

    return matrix
