#ifndef APPLICATION_H_
#define APPLICATION_H_

#include<string>
#include<vector>
#include<unordered_map>
#include<iostream>

#include"Types.h"

class Aplication {
private:
    std::string name;
    std::unordered_map<int, std::unordered_map<std::string, std::string>> shortcuts;
    std::pair<Modkey, std::string> leader_key;
    // Theme theme;
public:
    Aplication(std::string _name) : name(_name) {};
    void insert(Modkey mod, std::string key, std::string command);
    void set_leader(Modkey mod, std::string key);
    //void print();
 };

#endif // APPLICATION_H_
