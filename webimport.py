import requests
import importlib.util
import sys

def webimport(url, module_name):
    response = requests.get(url)
    module_content = response.text
    spec = importlib.util.spec_from_loader(module_name, loader=None)
    module = importlib.util.module_from_spec(spec)
    exec(module_content, module.__dict__)
    sys.modules[module_name] = module
    return module
