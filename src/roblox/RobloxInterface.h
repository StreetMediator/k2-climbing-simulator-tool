#pragma once
#include <string>

class RobloxInterface {
public:
    void sendInput(const std::string& input);
    bool isGameActive() const;
};