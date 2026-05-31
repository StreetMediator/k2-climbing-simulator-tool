#pragma once
#include "../roblox/RobloxInterface.h"

class ClimbingController {
public:
    ClimbingController(RobloxInterface& roblox);
    void startClimbingSequence();
    void handleObstacleDetection();

private:
    RobloxInterface& m_roblox;
    bool m_isClimbing = false;
};