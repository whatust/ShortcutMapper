import json

from util import eprint

class keyboard_json:

    def __init__(self, name, mods_used, default_context, verbose, version="1.0", os="linux"):

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
                warn_message = "Shortcut already used {} {}. Substituting entry".format(mod, key)
                eprint(warn_message, "warning")

        shortcut = {"name" : command, "mods" : mod}
        self.json["contexts"][context][key].append(shortcut)

        if self.verbose > 1:
            print(json.dumps(self.json, indent=2, sort_keys=True))

    def export_json(self, path):

        if self.verbose > 0:
            print("Saving JSON to {}".format(path))
            print(json.dumps(self.json, indent=2, sort_keys=True))

        with open(path, "w") as file:
            json.dump(self.json, file, indent=2, sort_keys=True)

    def print_json(self):
        print(json.dumps(self.json, indent=2, sort_keys=True))

def load_apps(filename):

    with open(filename, "r") as file:

        data = file.read()
        dict_data = data[data.find('[') : data.rfind(']')+1]
        json_data = json.loads(dict_data)

    return json_data

def find_app(apps_data, name):

    for indx, apps in enumerate(apps_data):
        if(apps["name"] == name):
            return indx

    return len(apps_data)

def add_app(apps_data, name, version, os, file):

    index = find_app(apps_data, name)

    if index ==  len(apps_data):
        app_dict = {"name": name, "data": { version: { os: file}}}

        apps_data.append(app_dict)
    else:
        if version in apps_data[index]["data"]:
            apps_data[index]["data"][version][os] = file
        else:
            apps_data[index]["data"][version] = { os: file}

def save_apps(filename, apps_data):

    apps_str = "var sitedata_apps = " + json.dumps(apps_data, indent=2)

    with open(filename, "w") as file:
        file.write(apps_str)

def update_apps(filename, name, version, os, file):

    try:
        apps_data = load_apps(filename)
    except:
        eprint("Unable to parse apps.js file starting from a blank file", "warning")
        apps_data = []
    add_app(apps_data, name, version, os, file)
    save_apps(filename, apps_data)

if __name__ == "__main__":

    my_key = keyboard_json("vim", ["CONTROL", "SHIFT"], "Global", 2)

    my_key.insert_shortcut_key("Normal", "F", ["CONTROL"], "Page Down")
    my_key.insert_shortcut_key("Normal", "F", ["CONTROL"], "Page Down")
    my_key.insert_shortcut_key("Normal", "B", ["CONTROL"], "Page Up")

    apps_data = load_apps("../content/generated/apps.js")

    add_app(apps_data, "vim", "1.0", "linux", "vim_1.0_linux.json")

    save_apps("../content/generated/apps.js", apps_data)

