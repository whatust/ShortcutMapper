import re

from json_helper import keyboard_json
from util import translate_key

def parse_dwm(filename, verbose, export_filename):

    file = open(filename, 'r')

    dwm_regex = re.compile(r"^\s*\{\s*(?P<mod>0|((MODKEY)(\|ShiftMask)?(\|Mod4Mask)?(\|ControlMask)?))\s*,\s*XK_(?P<key>[^\s]+)\s*,\s*(?P<precommand>[^\s]+)\s*,\s*(?P<command>.+)\s*\}.*")

    context = "Global"
    shcmd_regex = re.compile(r"^SHCMD\(\"(?P<command>.*)\"\)")
    jsondata = keyboard_json("dwm", "1.0", "linux", ["OSKEY", "CONTROL", "SHIFT", "ALT"], "Global", verbose)

    for line in file:

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

    jsondata.export_json(export_filename)

if __name__ == "__main__":

    parse_dwm("../tests/config.h", 1, "../content/generated/dwm_1.0_linux.json")


