from game import Game

parameters_dictionnary = {
    "x_len" : 20,
    "y_len" : 20,
    "shark_number" : 10,
    "fish_number" : 80,
    "shark_nmb_of_rounds_for_reproduction" : 9,
    "fish_nmb_of_rounds_for_reproduction" : 2,
    "energy_by_fish" : 3,
    "start_energy" : 4
}

my_game = Game(**parameters_dictionnary)

my_game.game_start()