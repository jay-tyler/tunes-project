from datetime import datetime
from random import sample
import json


tunetypes = set(["Reel", "Jig", "Hornpipe", "Polka", "Barndance"])
source_codes = set(["TC", "AL", "RB"])
musical_keys = set(["Dmaj", "Gmaj"])
musical_modes = set([])


#######################################################################
# Setup
#######################################################################


with open('reels.json') as file:
    reels = json.load(file)


#######################################################################
# Objects
#######################################################################


class Tune(object):
    def __init__(self, name, key=None, tunetype=None, played=None, next_in_set=None, source_code=None, heard=None, mode=None):
        """Define the Tune with all reasonable parameters

        name --> human readable name
        played --> list of all times where tune has been played
        heard --> list of all times where tune has been heard
        key --> name of key which tune is played in
        mode --> name of mode; e.g. Dorian, Myxolydian
        tunetype --> type of tune, i.e. jig or reel etc
        next_in_set --> list of name(s) for tune that reasonably follows playing this one; used to construct on the fly sets
        source_code --> code for where tune is from; use TC for 'tune class', AL for 'album', RB for 'from Randal Bays lesson'
        """

        self.name = name
        self.played = list() if not played else [played]
        self.heard = list() if not heard else [heard]
        self.key = key if key in musical_keys else None
        self.mode = mode if mode in musical_modes else None
        self.tunetype = tunetype if tunetype in tunetypes else None
        self.next_in_set = list() if not next_in_set else [next_in_set]
        self.source_code = source_code if source_code in source_codes else None


class Set(object):

    @staticmethod
    def set_by_reference(cls, start_tune, preceeding=None, target_length=3):
        """Return a set generator randomly chosen from by next_in_set reference"""
        if not preceeding:
            preceeding = [start_tune.name]
        for i in range(target_length):
            yield preceeding
            try:
                preceeding = sample(preceeding.next_in_set, 1)
            except ValueError:
                raise StopIteration