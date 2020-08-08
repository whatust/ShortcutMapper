#include"Aplication.h"

void
Aplication::insert(Modkey mod, std::string key, std::string command) {

    //std::cout << "Inserting command: " << command << " to hotkey: " << mod << "+"  << key << std::endl;

    if(shortcuts.find(mod.code) == std::end(shortcuts)) {
        shortcuts[mod.code] = std::unordered_map<std::string, std::string>();
    }

    if(shortcuts[mod.code].find(key) != std::end(shortcuts[mod.code])) {
        std::cout << "Overriding command: " << shortcuts[mod.code][key] << " with: " << command << " at hotkey: ";

        if(mod.code == 0){
            std::cout << key;
        }else{
            std::cout << mod << "+" << key;
        }
        std::cout << std::endl;
    }
    shortcuts[mod.code][key] = command;
}

void
Aplication::set_leader(Modkey mod, std::string key) {
    leader_key = std::pair<Modkey, std::string>(mod, key);
}

