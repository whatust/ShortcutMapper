from os.path import basename
from os.path import join
import re

from json_helper import keyboard_json
from json_helper import update_apps
from util import translate_key
from util import command_truncate

def parse_dwm(filename, verbose, directory_path):

    application = "dwm"
    file = open(filename, 'r')
    jsondata = keyboard_json("dwm", ["OSKEY", "CONTROL", "SHIFT", "ALT"], "Global", verbose)

    ver_regex = re.compile(r"\/\*VERSION:(?P<version>[^\s]+)\*\/")
    os_regex = re.compile(r"\/\*OS:(?P<os>[^\s]+)\*\/")
    dwm_regex = re.compile(r"^\s*\{\s*(?P<mod>0|((MODKEY)(\|ShiftMask)?(\|Mod4Mask)?(\|ControlMask)?))\s*,\s*XK_(?P<key>[^\s]+)\s*,\s*(?P<precommand>[^\s]+)\s*,\s*(?P<command>.+)\s*\}.*")

    context = "Global"
    shcmd_regex = re.compile(r"^SHCMD\(\"(?P<command>.*)\"\)")

    for line in file:

        match = os_regex.search(line)
        if match is not None:
            jsondata.json["os"] = match.group("os")

        match = ver_regex.search(line)
        if match is not None:
            jsondata.json["version"] = match.group("version")

        match = dwm_regex.search(line)
        if match is not None:

            mod = match.group("mod")
            key =  match.group("key")
            precommand = match.group("precommand")
            command = match.group("command")

            match = shcmd_regex.search(command)

            if precommand == "spawn" and match is not None:
                command = match.group("command")
            else:
                command = precommand + command

            command = command_truncate(command)

            _mod = []
            if "MODKEY" in mod:
                _mod.append("OSKEY")
            if "ShiftMask" in mod:
                _mod.append("SHIFT")
            if "ControlMask" in mod:
                _mod.append("CONTROL")
            if "Mod4Mask" in mod:
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

    parse_dwm("../tests/dwm_config.h", 0, "../content/generated")


