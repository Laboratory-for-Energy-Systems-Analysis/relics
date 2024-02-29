"""
This module contains utility functions for the RELICS project.
"""

from .filesystem_constants import DATA_DIR
import bw2data
from bw2data import Method
import yaml
from .biosphere import check_biosphere_database, check_biosphere_version


RELICS_MAPPING = DATA_DIR / "relics_mapping.yaml"

def load_mappings(yaml_mappings):
    with open(yaml_mappings, "r", encoding="utf-8") as stream:
        mappings = yaml.safe_load(stream)
    return mappings


def add_relics(yaml_mappings=RELICS_MAPPING):
    mappings = load_mappings(yaml_mappings)

    for metal_mapping in mappings:
        metal_name = metal_mapping['name']
        print(f"Processing {metal_name}...")

        all_cfs = []

        for flow_mapping in metal_mapping['environmental flow']:
            flow_found = [
                f
                for f in bw2data.Database("biosphere3")
                if flow_mapping['name'].lower() == f['name'].lower()
                   and f['categories'] == tuple(flow_mapping['categories'].split("::"))
            ]

            if not flow_found:
                print(f"Can't find {flow_mapping['name']} in biosphere3. Skipping, but you should check.")
                continue

            cf = [((f["database"], f["code"]), flow_mapping['amount']) for f in flow_found]
            all_cfs.extend(cf)

        method_key = ("RELICS", "metals extraction", metal_name)
        if method_key not in bw2data.methods:
            my_method = Method(method_key)
            metadata = {
                "unit": "kilogram",
                "description": f"Extraction of {metal_name} from the ground"
            }
            my_method.register(**metadata)
        else:
            my_method = Method(method_key)

        my_method.write(all_cfs)
        print(f"Added characterization factors for {metal_name} to project {bw2data.projects.current}.")

    print("Done.")