import json
from classes import Tune, Set

#######################################################################
# Setup
#######################################################################

with open('reels.json') as file:
    reels_init_args = json.load(file)

reels = dict()

for _, tune_dict in reels.items():
    new_tune = Tune(tune_dict)
    reels[tune_dict['name']] = new_tune
