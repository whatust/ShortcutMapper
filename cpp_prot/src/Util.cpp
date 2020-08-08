#include"Util.h"

std::string to_upper(std::string str) {

    std::string new_str;

    for(auto c : str) {
        new_str.push_back(toupper(c));
    }

    return new_str;
}

