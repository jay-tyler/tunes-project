import json
from classes import Tune, Set

#######################################################################
# Setup
#######################################################################

with open('reels.json') as file:
    reels_serialized = json.load(file)

reels = dict()

for _, tune_dict in reels_serialized.items():
    new_tune = Tune(**tune_dict)
    reels[tune_dict['name']] = new_tune
