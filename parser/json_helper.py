import json
from util import eprint

class keyboad_json:

    def __init__(self, name, version, os, mods_used, default_context, verbose):

        self.json = { "name" : name, "version" : version, "os" : os,
                    "mods_used" : mods_used, "default_context" : default_context,
                    "contexts" : {}}

        self.verbose = verbose

        if verbose > 0:
            print(json.dumps(self.json, indent=2, sort_keys=True))

    def insert_shortcut_key(self, context, key, mod, command):

        if context not in self.json["contexts"]:
            self.json["contexts"][context] = {}

        if key not in self.json["contexts"][context]:
            self.json["contexts"][context][key] = []

        for m in self.json["contexts"][context][key]:
            if m["mods"] == mod:
                warn_message = "Shortcut already used {} {}. Ignoring latest entry".format(mod, key)
                eprint(warn_message, "warning")
                return

        shortcut = {"name" : command, "mods" : mod}
        self.json["contexts"][context][key].append(shortcut)

        if self.verbose > 1:
            print(json.dumps(self.json, indent=2, sort_keys=True))

    def export_json(path):

        if self.verbose > 0:
            print("Saving JSON to {}".format(path))
            print(json.dump(self.json, indent=2, sort_keys=True))

        json.dump(self.json, path, indent=2, sort_keys=True)

if __name__ == "__main__":

    my_key = keyboad_json("vim", "1.0", "linux", ["CONTROL", "SHIFT"], "Global", 2)

    my_key.insert_shortcut_key("Normal", "F", ["CONTROL"], "Page Down")
    my_key.insert_shortcut_key("Normal", "F", ["CONTROL"], "Page Down")
    my_key.insert_shortcut_key("Normal", "B", ["CONTROL"], "Page Up")

