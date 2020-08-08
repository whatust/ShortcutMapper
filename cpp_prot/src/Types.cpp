#include"Types.h"

Shortcut::Shortcut(std::string _key, std::string _cmd)
    : key(_key), command(_cmd) {};

Modkey&
Modkey::operator+=(const enum _modkey& mk) {
    this->code += mk;
    return *this;
}

Modkey&
Modkey::operator=(const enum _modkey& mk) {

    this->code = mk;
    return *this;
}

std::ostream& operator<<(std::ostream& os, const Modkey& mk) {

    std::string str;

    if(mk.code == 0)
        str = "None";

    if(mk.code % 2)
        str += "Ctrl";

    if((mk.code >> 2) % 2){
        if(str.length() != 0)
            str += "+";
        str += "Alt";
    }

    if((mk.code >> 1) % 2){
        if(str.length() != 0)
            str += "+";
        str += "Shift";
    }

    if((mk.code >> 3) % 2){
        if(str.length() != 0)
            str += "+";
        str += "Super";
    }

    if((mk.code >> 4) % 2){
        if(str.length() != 0)
            str += "+";
        str += "Leader";
    }

    os << str;

    return os;
}

VimMode&
VimMode::operator=(const enum _vimmodes& vm) {

    this->mode = vm;
    return *this;
}

std::ostream& operator<<(std::ostream& os, const VimMode& mk) {

    std::string str;

    if(mk.mode == 0)
        str += "Normal";

    if(mk.mode == 1)
        str += "Insert";

    if(mk.mode == 2)
        str += "Visual";

    if(mk.mode == 3)
        str += "Replace";

    if(mk.mode == 4)
        str += "All";

    os << str;

    return os;
}


