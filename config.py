import json

def load_cfg(path):
    with open(path) as f:
        text = f.read()
    cfg = json.loads(text)
    return cfg
