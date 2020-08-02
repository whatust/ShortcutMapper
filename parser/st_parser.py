from os.path import basename
from os.path import join
import re

from json_helper import keyboard_json
from json_helper import update_apps
from util import translate_key
from util import command_truncate

def parse_st(filename, verbose, directory_path):

    application = "st"
    file = open(filename, 'r')
    jsondata = keyboard_json("st", ["SHIFT", "ALT"], "Global", verbose)

    st_regex = re.compile(r"^\s*\{\s*(?P<mod>(TERMMOD)|(MODKEY))\s*,\s*XK_(?P<key>[^\s]+)\s*,\s*(?P<precommand>[^\s]+)\s*,\s*(?P<command>.+)\s*\}.*")

    context = "Global"

    for line in file:

        match = st_regex.search(line)
        if match is not None:

            mod = match.group("mod")
            key =  match.group("key")

            command = match.group("precommand") + " " + match.group("command")
            command = command_truncate(command)

            _mod = []
            if "TERMMOD" in mod:
                _mod.append("ALT")
                _mod.append("SHIFT")
            if "MODKEY" in mod:
                _mod.append("ALT")
            mod = _mod

            if len(key) == 1:
                key = key.upper()
            else:
                key = translate_key(key)
                if(key == ""):
                    continue

            if verbose > 1:
                print(str(mod) + " " + key + " " + " " + command)

            jsondata.insert_shortcut_key(context, key, mod, command)

    if verbose > 0:
        jsondata.print_json()

    export_filename = application+"_"+jsondata.json["version"]+"_"+\
                        jsondata.json["os"]+".json"

    jsondata.export_json(join(directory_path, export_filename))

    update_apps(join(directory_path, "apps.js"), application,
                jsondata.json["version"], jsondata.json["os"], export_filename)

if __name__ == "__main__":

    parse_st("../tests/st_config.h", 0, "../content/generated")


