import json
import re

def parse_dwm(filename, verbose):

    file = open(filename, 'r')

    dwm_regex = re.compile(r"^\s*\{\s*(?P<mod>0|((MODKEY)(\|ShiftMask)?(\|Mod4Mask)?(\|ControlMask)?))\s*,\s*XK_(?P<key>[^\s]+)\s*,\s*(?P<precommand>[^\s]+)\s*,\s*(?P<command>.+)\s*\}.*") 

    shcmd_regex = re.compile(r"^SHCMD\(\"(?P<command>.*)\"\)")

    for line in file:

        match = dwm_regex.search(line)

        if match is not None:

            context = "Global"
            mod = match.group("mod")
            key =  match.group("key")
            precommand = match.group("precommand")
            command = match.group("command")

            match = shcmd_regex.search(command)

            if precommand == "spawn" and match is not None:
                command = match.group("command")
            else:
                command = precommand + command

            if verbose > 0:
                print(mod + " " + key + " " + " " + command)


