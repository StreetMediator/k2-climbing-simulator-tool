#include "ClimbingController.h"
#include <iostream>

ClimbingController::ClimbingController(RobloxInterface& roblox) : m_roblox(roblox) {}

void ClimbingController::startClimbingSequence() {
    m_isClimbing = true;
    std::cout << "Starting K2 climbing sequence...\n";
    m_roblox.sendInput("Jump");
    m_roblox.sendInput("Grip");
}

void ClimingController::handleObstacleDetection() {
    if (m_isClimbing) {
        m_roblox.sendInput("AdjustGrip");
    }
}