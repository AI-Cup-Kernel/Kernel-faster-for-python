"""
in this API client shows that it's ready to start the game 
that means it has a server on the port that it said in the login API
"""

import os

def ready_func(main_game, player_id):
    try:
        main_game.players[player_id].is_ready = True
        # disable proxy and vpn for the player IP 
        os.environ['NO_PROXY'] = main_game.players[player_id].ip
        output_dict = {"message": "every thing is ok, you should wait for other players to be ready"}
        main_game.check_all_players_ready()
        return output_dict

    except:
        output_dict = {"error": "this player_id doesn't exist"}
        return output_dict
