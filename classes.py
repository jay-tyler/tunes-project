from random import sample


tunetypes = set(["Reel", "Jig", "Hornpipe", "Polka", "Barndance"])
source_codes = set(["TC", "AL", "RB"])
musical_keys = set(["Dmaj", "Gmaj", "Emin"])
musical_modes = set([])


#######################################################################
# Objects
#######################################################################


class Tune(object):
    def __init__(self, name, key=None, tunetype=None, played=None, next_in_set=None, source_code=None, heard=None, mode=None):
        """Define the Tune with all reasonable parameters

        str:            name --> human readable name
        list[datetime]: played --> list of all times where tune has been played
        list[datetime]: heard --> list of all times where tune has been heard
        str:            key --> name of key which tune is played in
        str:            mode --> name of mode; e.g. Dorian, Myxolydian
        str:            tunetype --> type of tune, i.e. jig or reel etc
        list[str]:      next_in_set --> list of name(s) for tune that reasonably follows playing this one; used to construct on the fly sets
        str:            source_code --> code for where tune is from; use TC for 'tune class', AL for 'album', RB for 'from Randal Bays lesson'
        """

        self.name = name
        self.played = list() if not played else [played]
        self.heard = list() if not heard else [heard]
        self.key = key if key in musical_keys else None
        self.mode = mode if mode in musical_modes else None
        self.tunetype = tunetype if tunetype in tunetypes else None
        self.next_in_set = list() if not next_in_set else next_in_set
        self.source_code = source_code if source_code in source_codes else None


class Set(object):

    @staticmethod
    def gen_set(start_tune, catalog, target_length=3, _preceeding=None):
        """Return a set generator randomly chosen from by next_in_set reference

        hash: start_tune --> hash to Tune object that begins the set
        dict: catalog --> a dict of Tune objects to select from
        int:  target_length --> set will be <= target_length

        Not yet fully implemented:
        Tune: _preceeding --> Tune object preceeding in set

        """
        if not _preceeding:
            _preceeding = catalog[start_tune]
        for i in range(target_length):
            yield _preceeding
            try:
                next_hash = sample(_preceeding.next_in_set, 1)[0]
                _preceeding = catalog[next_hash]
            except ValueError:
                raise StopIteration
