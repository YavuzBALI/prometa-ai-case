import yaml
from types import SimpleNamespace


def dict_to_namespace(d):
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [dict_to_namespace(i) for i in d]
    else:
        return d


def load_config(yaml_path):
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    return dict_to_namespace(data)

config = load_config("config/config.yaml")