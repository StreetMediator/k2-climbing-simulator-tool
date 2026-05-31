#include "climbing/ClimbingController.h"
#include "roblox/RobloxInterface.h"
#include <iostream>

int main() {
    RobloxInterface roblox;
    ClimbingController controller(roblox);

    std::cout << "K2 Climbing Simulator Tool - Initialized\n";
    controller.startClimbingSequence();

    return 0;
}