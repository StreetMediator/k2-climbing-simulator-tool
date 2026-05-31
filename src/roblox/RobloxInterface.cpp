#include "RobloxInterface.h"
#include <iostream>

void RobloxInterface::sendInput(const std::string& input) {
    std::cout << "[Roblox] Sending input: " << input << "\n";
}

bool RobloxInterface::isGameActive() const {
    return true;
}