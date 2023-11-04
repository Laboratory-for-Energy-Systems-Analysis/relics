__all__ = (
    "add_relics",
    "check_biosphere_database",
)

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

import bw2io
from bw2io import ExcelLCIAImporter

from .biosphere import check_biosphere_database, check_biosphere_version
from .version import version as __version__

LIST_METALS = [
    'Aluminium',
    'Antimony',
    'Beryllium',
    'Boron',
    'Brass',
    'Cadmium',
    'Cerium',
    'Chromium',
    'Cobalt',
    'Copper',
    'Dysprosium',
    'Erbium',
    'Europium',
    'Gadolinium',
    'Gallium',
    'Germanium',
    'Gold',
    'Graphite',
    'Hafnium',
    'Indium',
    'Iridium',
    'Lanthanum',
    'Lead',
    'Lithium',
    'Magnesium',
    'Manganese',
    'Molybdenum',
    'Neodymium',
    'Nickel',
    'Niobium',
    'Palladium',
    'Phosphorous',
    'Platinum',
    'Potassium',
    'Praseodymium',
    'Rhenium',
    'Rhodium',
    'Ruthenium',
    'Samarium',
    'Scandium',
    'Selenium',
    'Silicon',
    'Silver',
    'Sulfur',
    'Strontium',
    'Tantalum',
    'Tellurium',
    'Terbium',
    'Tin',
    'Titanium',
    'Tungsten',
    'Vanadium',
    'Ytterbium',
    'Yttrium',
    'Zinc',
    'Zirconium',
]
def add_relics():
    check_biosphere_database()
    bw2io_version = check_biosphere_version()

    # impact methods to create
    categories = {
        (
            ("RELICS", "metals extraction", metal),
            "kg",
            f"Resource extraction indicator for {metal}",
        ) for metal in LIST_METALS
    }


    categories = (
        categories_bw2io088 if bw2io_version >= (0, 8, 8) else categories_bw2io087
    )

    if bw2io_version >= (0, 8, 8):
        filepath = DATA_DIR / "RELICS_CF_088.xlsx"
    else:
        filepath = DATA_DIR / "RELICS_CF_087.xlsx"

    for c in categories:
        print("Adding {}".format(c[0]))
        category = ExcelLCIAImporter(
            filepath=filepath, name=c[0], unit=c[1], description=c[2]
        )

        # apply formatting strategies
        category.apply_strategies()

        # check that no flow is unlinked
        assert len(list(category.unlinked)) == 0, "Unlinked flows: {}".format(
            list(category.unlinked)
        )

        # write method
        category.write_methods(overwrite=True, verbose=True)
