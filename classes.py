import sys
import json
from random import sample
from collections import namedtuple, deque


tune_files = ['data/reels.json']
tunetypes = set(["Reel", "Jig", "Hornpipe", "Polka", "Barndance"])
source_codes = set(["TC", "AL", "RB"])
musical_keys = set(["Dmaj", "Gmaj", "Emin"])
musical_modes = set([])
catalogue = dict()



class Tune(object):
    def __init__(self, name, key=None, tunetype=None, played=None, next_in_set=None, source_code=None, heard=None, mode=None, abc=None):
        """Define the Tune with all reasonable parameters

        str:            name --> human readable name; will be used as a hash
        list[(datetime, object)]: played --> list of all times where tune has been played; object is reference to Tune or Set when played
        list[(datetime, object)]: heard --> list of all times where tune has been heard; object is reference to Tune or Set when heard
        str:            key --> name of key which tune is played in
        str:            mode --> name of mode; e.g. Dorian, Myxolydian
        str:            tunetype --> type of tune, i.e. jig or reel etc
        list[str]:      next_in_set --> list of name(s) for tune that reasonably follows playing this one; used to construct on the fly sets
        str:            source_code --> code for where tune is from; use TC for 'tune class', AL for 'album', RB for 'from Randal Bays lesson'
        str:            abc --> String for ABC notation
        """

        self.name = name
        self.played = list() if not played else [played]
        self.heard = list() if not heard else [heard]
        self.key = key if key in musical_keys else None
        self.mode = mode if mode in musical_modes else None
        self.tunetype = tunetype if tunetype in tunetypes else None
        self.next_in_set = list() if not next_in_set else next_in_set
        self.source_code = source_code if source_code in source_codes else None
        self.abc = abc


def load_tunes(tune_files):
    tunes = dict()
    for filename in tune_files:
        with open(filename) as file:
            serialized_tunes = json.load(file)

        for _, tune_dict in serialized_tunes.items():
            new_tune = Tune(**tune_dict)
            tunes[tune_dict['name']] = new_tune
    return tunes


new_tunes = load_tunes(tune_files)
catalogue.update(new_tunes)


def get_tune(substr, catalogue=catalogue):
    matches = [tune for tune_name, tune in catalogue.items() if substr.lower() in tune_name.lower()]
    if matches:
        return sample(matches, 1)[0]
    else:
        return None


def set_from_tune(tune, nmax=3):
    tune_set = [tune]
    while len(tune_set) < nmax:
        try:
            next_tune = sample(tune.next_in_set, 1)
        except ValueError: # No other tune
            return tune_set if len(tune_set) > 1 else None
        else:
            get_tune()
            tune_set.append(next_tune)
            tune = next_tune
    return tune_set

