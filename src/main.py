# author: Mohamad Mahdi Reisi

# this is the main file of the game that will run the game
# this file reads the map file and creates a game object and initializes it
# then make a server
# and add different APIs from blueprints to the server
# it also has a function to kill the server

from src.components.game import Game
import src.tools.read_config as read_config
import os
import argparse

# define argument parser
parser = argparse.ArgumentParser(description='choose map to play on')
parser.add_argument('-m', '--map', type=str, help='choose map to play on')
args = parser.parse_args()

# read map file 
main_game = Game()

# ask player to choose map from the list of maps
maps = os.listdir('maps')

## get the selected map from the player
selected_map = str(maps.index(args.map)) if args.map != None else "None"

while selected_map.isdigit() == False or int(selected_map) >= len(maps) or int(selected_map) < 0:
    ## show the list of maps from the maps folder
    print("Choose a map from the list of maps:")
    for i, map in enumerate(maps):
        print(i,'-', map)
    selected_map = input("Enter the number of the map you want to choose: ")

## read the selected map
main_game.read_map('maps/'+maps[int(selected_map)])

main_game.config = read_config.read_config()

# set the debug variable to True or False to see the debug messages and generate debug logs 
debug = main_game.config['debug']

main_game.debug = debug



# register the blueprints

# import blueprints
from src.blueprints.index import index
from src.blueprints.login import login
from src.blueprints.ready import ready
from src.blueprints.get_owners import get_owners
from src.blueprints.get_troops_count import get_troops_count
from src.blueprints.get_state import get_state
from src.blueprints.get_turn_number import get_turn_number
from src.blueprints.get_adj import get_adj
from src.blueprints.next_state import next_state
from src.blueprints.put_one_troop import put_one_troop
from src.blueprints.put_troop import put_troop
from src.blueprints.get_player_id import get_player_id
from src.blueprints.attack import attack
from src.blueprints.move_troop import move_troop
from src.blueprints.get_strategic_nodes import get_strategic_nodes
from src.blueprints.get_number_of_troops_to_put import get_number_of_troops_to_put
from src.blueprints.get_reachable import get_reachable
from src.blueprints.get_number_of_fort_troops import get_number_of_fort_troops
from src.blueprints.fort import fort

# Todo: Build Clients


# Todo: run the server
