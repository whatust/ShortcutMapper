#ifndef PARSER_H_
#define PARSER_H_

#include<fstream>
#include<memory>
#include<regex>
#include<string>
#include<iostream>
#include<vector>

#include"Aplication.h"
#include"Types.h"
#include"Util.h"

class Parser {
private:
    std::shared_ptr<Aplication> parse_nvim(std::string filename);
    std::shared_ptr<Aplication> parse_tmux(std::string filename);
    std::shared_ptr<Aplication> parse_dwm(std::string filename);
    std::shared_ptr<Aplication> parse_st(std::string filename);
    std::shared_ptr<Aplication> parse_sxhkd(std::string filename);
public:
    std::shared_ptr<Aplication> parse(std::string filename, std::string type);
};

#endif // PARSER_H_
