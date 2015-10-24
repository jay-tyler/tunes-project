import pytest

from classes import Tune, Set

@pytest.fixture()
def tunes_non_cyclic():
    """
    Return dict of five tunes with the following relationships
    A -> B -> C
    A -> D
    B -> C
    E -> A
    """
    A = Tune("A", key=None, tunetype="Reel", played=None, source_code="TC",
        next_in_set=["B", "D"])
    B = Tune("B", key=None, tunetype="Reel", played=None, source_code="TC",
        next_in_set=["C"])
    C = Tune("C", key=None, tunetype="Reel", played=None, source_code="TC")
    D = Tune("D", key=None, tunetype="Reel", played=None, source_code="TC")
    E = Tune("E", key=None, tunetype="Reel", played=None, source_code="TC",
        next_in_set=["A"])
    tunes = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E
        }
    return tunes

#####
# Set class methods
#####


def test_gen_all_sets_1(tunes_non_cyclic):
    catalog = tunes_non_cyclic
    result = Set.gen_all_sets("A", catalog)
    assert len(result) == 2
    assert ["A", "B", "C"] in result
    assert ["A", "D"] in result


def test_gen_all_sets_2(tunes_non_cyclic):
    catalog = tunes_non_cyclic
    result = Set.gen_all_sets("B", catalog)
    assert len(result) == 1
    assert ["B", "C"] in result
