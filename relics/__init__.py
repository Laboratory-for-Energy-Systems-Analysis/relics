__all__ = (
    "add_relics",
    "check_biosphere_database",
)

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"

import bw2data
import bw2io
from bw2data import Method

from .biosphere import check_biosphere_database, check_biosphere_version
from .version import version as __version__

LIST_METALS = [
    "Aluminium",
    "Antimony",
    "Beryllium",
    "Boron",
    "Brass",
    "Cadmium",
    "Cerium",
    "Chromium",
    "Cobalt",
    "Copper",
    "Dysprosium",
    "Erbium",
    "Europium",
    "Gadolinium",
    "Gallium",
    "Germanium",
    "Gold",
    "Graphite",
    "Hafnium",
    "Indium",
    "Iridium",
    "Lanthanum",
    "Lead",
    "Lithium",
    "Magnesium",
    "Manganese",
    "Molybdenum",
    "Neodymium",
    "Nickel",
    "Niobium",
    "Palladium",
    "Phosphorous",
    "Platinum",
    "Potassium",
    "Praseodymium",
    "Rhenium",
    "Rhodium",
    "Ruthenium",
    "Samarium",
    "Scandium",
    "Selenium",
    "Silicon",
    "Silver",
    "Sulfur",
    "Strontium",
    "Tantalum",
    "Tellurium",
    "Terbium",
    "Tin",
    "Titanium",
    "Tungsten",
    "Vanadium",
    "Ytterbium",
    "Yttrium",
    "Zinc",
    "Zirconium",
]


def add_relics():
    for metal in LIST_METALS:
        try:
            flow = [
                f
                for f in bw2data.Database("biosphere3")
                if metal.lower() in f["name"].lower()
                and f["categories"] == ("natural resource", "in ground")
            ]
        except IndexError:
            print(f"Can't find {metal} in biosphere3. Skiping, but you should check.")
            continue

        if len(flow) == 0:
            print(f"Can't find {metal} in biosphere3. Skiping, but you should check.")
            continue

        cf = [[(f["database"], f["code"]), 1.0] for f in flow]

        method_key = ("RELICS", "metals extraction", metal)

        my_method = Method(method_key)
        my_method.validate(cf)
        metadata = {
            "unit": f"kg {metal.lower()}",
            "description": f"Extraction of {metal} from the ground",
        }
        my_method.register(**metadata)
        my_method.write(cf)

        print(f"Added {method_key} to project {bw2data.projects.current}.")

    print("Done.")
