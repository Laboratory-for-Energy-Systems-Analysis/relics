import bw2data
import bw2io

from relics import add_relics


def test_implementation():
    """
    Test that the method is properly registered.
    """

    bw2data.projects.set_current("test")
    bw2io.create_default_biosphere3()

    add_relics()

    # check that the new method exists
    new_method = ("RELICS", "metals extraction", "Aluminium")
    assert new_method in bw2data.methods

    al = [
        f
        for f in bw2data.Database("biosphere3")
        if "aluminium" in f["name"].lower()
        and f["categories"] == ("natural resource", "in ground")
    ][0]["code"]

    method = bw2data.Method(new_method)

    for cf in method.load():
        if cf[0] == al:
            assert cf[1] == -1
