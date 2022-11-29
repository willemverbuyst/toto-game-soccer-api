import json


def get_teams_from_json():
    with open('app/data/teams.json') as json_file:
        teams = json.load(json_file)
        return teams
