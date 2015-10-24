import sys
from random import sample
from collections import namedtuple, deque


tunetypes = set(["Reel", "Jig", "Hornpipe", "Polka", "Barndance"])
source_codes = set(["TC", "AL", "RB"])
musical_keys = set(["Dmaj", "Gmaj", "Emin"])
musical_modes = set([])


class Tune(object):
    def __init__(self, name, key=None, tunetype=None, played=None, next_in_set=None, source_code=None, heard=None, mode=None):
        """Define the Tune with all reasonable parameters

        str:            name --> human readable name; will be used as a hash
        list[(datetime, object)]: played --> list of all times where tune has been played; object is reference to Tune or Set when played
        list[(datetime, object)]: heard --> list of all times where tune has been heard; object is reference to Tune or Set when heard
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
    def set_gen(start_tune, catalog, target_length=3, _preceeding=None):
        """Return a generator containing Tunes, regardless of whether they belong to a current Set object.

        Tunes are randomly chosen by next_in_set reference.
        Number of tunes will be equal to or less than target_length.

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

    @staticmethod
    def gen_all_sets(start_tune, catalog):
        """Return a list of all sets from start_tune hash; inner lists consist of Tune hashes corresponding to a set.

        This method returns all potential sets regardless of whether they exist as Set objects currently.

        Currently implemented as using 'next_in_set' node edges

        Implemented after non-recursive approach psuedocode from
        https://en.wikipedia.org/wiki/Breadth-first_search
        """
        #  Set up records for non-recursive breadth first search
        Node = nametuple('Node', ['distance', 'parent', 'self'])
        records = {tune.name: Node(distance=sys.maxint, parent=None, self=tune) for tune in catalog}

        #  grab start_tune record and initialize to queue
        start_record = records[start_tune]
        start_record.distance = 0
        to_travel = deque(start_record)

        #  ordered structure to place processed tune references
        travelled = []

        # TODO: add check for cycles; i.e. if a reference points to the start_record, terminate it
        while to_travel:
            current = to_travel.popleft()
            for tune in current.self.next_in_set:
                tune = records[tune]
                if tune.distance == sys.maxint:
                    tune.distance = current.distance + 1
                    tune.parent = current
                    to_travel.append(tune)
            travelled.append(current)

        # TODO: splay out tunes into lists in lists
        to_return = []
        for tune in travelled:
            if not tune.self.next_in_set:
                # In this case, tune is at the end of a set
                pass
