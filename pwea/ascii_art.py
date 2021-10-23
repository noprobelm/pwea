import json
from pathlib import Path

json_path = f"{Path(__file__).parent}"
with open(f'{json_path}/ascii.json', 'r') as f:
    ascii_art = json.load(f)
