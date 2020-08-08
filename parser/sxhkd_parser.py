from os.path import basename
from os.path import join
import re

from json_helper import keyboard_json
from json_helper import update_apps
from util import translate_key
from util import command_truncate

def parse_sxhkd(filename, verbose, directory_path):

    application = "sxhkd"
    file = open(filename, 'r')
    jsondata = keyboard_json(application, ["CONTROL", "OSKEY", "SHIFT", "ALT"], verbose)






