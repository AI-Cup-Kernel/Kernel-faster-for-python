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


# Todo: Build Clients
from player0.src.game import Game as player0
p0 = player0(main_game)
print(p0.get_owners())

# Todo: run the server
