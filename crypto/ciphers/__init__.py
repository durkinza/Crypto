import glob
import importlib
import os

from collections import namedtuple

from .. import __version__

ciphers = {}

def init_ciphers(subparser):
    """
    Searches for the load function in modules in the Crypto/ciphers folder.
    :return:
    """
    modules = sorted(glob.glob(os.path.dirname(__file__) + "/*"))
    blacklist = {"__pycache__"}
    for module in modules:
        module_name = os.path.basename(module)
        if os.path.isdir(module) and module_name not in blacklist:
            module = "." + module_name
            module = importlib.import_module(module, package="crypto.ciphers")
            module.load_args(subparser)
            ciphers[module_name] = module
