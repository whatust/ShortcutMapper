#include"Parser.h"

std::shared_ptr<Aplication>
Parser::parse_nvim(std::string filename) {

    std::string buffer;
    std::ifstream filestream;
    std::shared_ptr<Aplication> aplication(new Aplication("nvim"));

    filestream.open(filename);

    for(int line=1; std::getline (filestream, buffer); line++) {

        std::smatch match;
        auto flag = std::regex_constants::match_continuous;

        std::regex nvim_regex("^\\s*([nvi])*(nore)?map\\s+((<silent>)?\\s*(<expr>)?\\s*([^\\s]*))\\s+(.*)");
        std::regex key_regex("^\\s*(<Leader>)?\\s*<?([CAS]-[CAS]-|[CAS]-)?([^>]*)>?");
        std::regex leader_regex("^\\s*let\\smapleader\\s+=\\s+\\\"([^\\s])\\\"");

        if(std::regex_search(std::cbegin(buffer), std::cend(buffer), match, leader_regex, flag)) {
            aplication->set_leader(Modkey(), match[1].str());
        }

        if(std::regex_search(std::cbegin(buffer), std::cend(buffer), match, nvim_regex, flag)) {

            /* for(auto m : match)
                std::cout << m << "|";
            std::cout << std::endl; */

            Modkey mod;
            VimMode mode;
            std::string key;
            std::string command;

            if(!match[1].compare("v")) {
                mode = VISUAL;
            }else if(!match[1].compare("n")) {
                mode = NORMAL;
            }else if(!match[1].compare("i")) {
                mode = INSERT;
            }else if(!match[1].compare("")) {
                mode = ALL;
            }else{
                std::cerr << "Unknown vim mode:" << match[1] << std::endl;
                std::cerr << "Ignoring line(" << line << ")" << std::endl;
                continue;
            }

            key = match[6].str();
            std::smatch key_match;

            if(regex_search(std::cbegin(key), std::cend(key), key_match, key_regex, flag)) {

                if(key_match[1].str().compare("<Leader>") == 0) {
                    mod = LEADER;
                }else{
                    if(key_match[2].str().find('C') != std::string::npos)
                        mod += CTRL;
                    if(key_match[2].str().find('A') != std::string::npos)
                        mod += ALT;
                    if(key_match[2].str().find('S') != std::string::npos)
                        mod += SHIFT;
                }
                key = to_upper(key_match[3].str());
            }
            command = match[7];
            //std::cout << mode << " MOD: " << mod << " KEY: " << key << " CMD: " << command << std::endl;
            aplication->insert(mod, key, command);
        }
    }

    return aplication;
};


std::shared_ptr<Aplication>
Parser::parse_tmux(std::string filename) {

    std::string buffer;
    std::ifstream filestream;
    filestream.open(filename);
    std::shared_ptr<Aplication> aplication(new Aplication("tmux"));

    for(int line=1; std::getline (filestream, buffer); line++) {

        std::smatch match;
        auto flag = std::regex_constants::match_continuous;

        std::regex leader_regex("^\\s*bind-key\\s+(([^-]-)*)(.+)\\s+send-prefix");
        std::regex bind_regex("^\\s*bind(\\s+-.)*(\\s+copy-mode-vi)?\\s+([^ ]+)\\s+(.+)");
        std::regex bindkey_regex("^\\s*bind-key(\\s+-.)*(\\s+(copy-mode-vi|edit-mode-vi))?\\s+(([^-]-)*)([^ ]+)\\s+(.+)");

        if(regex_search(std::cbegin(buffer), std::cend(buffer), match, leader_regex, flag)) {

            Modkey leader_mod;

            if(match[1].str().find("C-") != std::string::npos)
                leader_mod += CTRL;
            if(match[1].str().find("S-") != std::string::npos)
                leader_mod += SHIFT;
            if(match[1].str().find("A-") != std::string::npos)
                leader_mod += ALT;

            aplication->set_leader(leader_mod, match[3].str());
        }else if(regex_search(std::cbegin(buffer), std::cend(buffer), match, bind_regex, flag)) {

            std::string key;
            std::string command;

            key = match[3].str();
            command = match[4].str();

            //std::cout << "Key: " << key << " Command: " << command << std::endl;
            aplication->insert(Modkey(), key, command);
        }else if(regex_search(std::cbegin(buffer), std::cend(buffer), match, bindkey_regex, flag)) {

            Modkey mod;
            std::string key;
            std::string command;

            if(match[5].str().find("C-") != std::string::npos)
                mod += CTRL;
            if(match[5].str().find("S-") != std::string::npos)
                mod += SHIFT;
            if(match[5].str().find("M-") != std::string::npos)
                mod += ALT;

            key = match[6].str();
            command = match[7].str();

            aplication->insert(mod, key, command);
            //std::cout << " Mod: " << mod << " Key: " << key << " Command: " << command << std::endl;
        }
    }

    return aplication;
};


std::shared_ptr<Aplication>
Parser::parse_dwm(std::string filename) {

    std::string buffer;
    std::ifstream filestream;
    filestream.open(filename);
    std::shared_ptr<Aplication> aplication(new Aplication("dwm"));

    for(int line=1; std::getline (filestream, buffer); line++) {

        std::smatch match;
        auto flag = std::regex_constants::match_continuous;

        std::regex shortcut_regex("^\\s*\\{\\s*(0?(MODKEY)?\\|?(ShiftMask)?)\\s*,\\s*(XF86)?XK_([^ ]+)\\s*,\\s*([^\\s]+)\\s*,\\s*(.+)\\s*\\}");

        if(regex_search(std::cbegin(buffer), std::cend(buffer), match, shortcut_regex, flag)) {

            Modkey mod;
            std::string key;
            std::string command;

            key = to_upper(match[5].str());
            command = match[6].str() + " " + match[7].str();

            if(match[1].str().compare("0") == 0)
                mod = NONE;

            if(match[1].str().find("MODKEY") != std::string::npos)
                mod += SUPER;

            if(match[1].str().find("ShiftMask") != std::string::npos)
                mod += SHIFT;

            std::cout << "Mod: " << mod << " Key: " << key << " Command: " << command << std::endl;
            aplication->insert(mod, key, command);
        }
    }
    return aplication;
};


std::shared_ptr<Aplication>
Parser::parse_st(std::string filename) {

    std::string buffer;
    std::ifstream filestream;
    filestream.open(filename);

    while(std::getline (filestream, buffer)) {
        std::cout << buffer;
    }

    return std::shared_ptr<Aplication>(new Aplication("st"));
};


std::shared_ptr<Aplication>
Parser::parse_sxhkd(std::string filename) {

    std::string buffer;
    std::ifstream filestream;
    filestream.open(filename);

    while(std::getline (filestream, buffer)) {
        std::cout << buffer << std::endl;
    }

    return std::shared_ptr<Aplication>(new Aplication("sxhkd"));
};


std::shared_ptr<Aplication>
Parser::parse(std::string filename, std::string type) {

    std::shared_ptr<Aplication> aplication;

    if(type.compare("nvim") == 0) {
        aplication = parse_nvim(filename);
    } else if(type.compare("tmux") == 0) {
        aplication = parse_tmux(filename);
    } else if(type.compare("dwm") == 0) {
        aplication = parse_dwm(filename);
    } else if(type.compare("st") == 0) {
        aplication = parse_st(filename);
    } else if(type.compare("sxhkd") == 0) {
        aplication = parse_sxhkd(filename);
    } else {
        std::cerr << "Unknown configuration type:" << type << std::endl;
        aplication = std::shared_ptr<Aplication>(nullptr);
    }

    return aplication;
}

