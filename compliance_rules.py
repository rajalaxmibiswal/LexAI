import json

def load_rules():

    frameworks = {}

    files = {
        "GDPR": "data/gdpr_rules.json",
        "DPDP": "data/dpdp_rules.json",
        "ISO27001": "data/iso27001_rules.json"
    }

    for name, path in files.items():
        with open(path, "r", encoding="utf-8") as f:
            frameworks[name] = json.load(f)

    return frameworks