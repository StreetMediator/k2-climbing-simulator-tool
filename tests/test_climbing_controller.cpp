#include "../src/climbing/ClimbingController.h"
#include "../src/roblox/RobloxInterface.h"
#include <cassert>

class MockRobloxInterface : public RobloxInterface {
public:
    void sendInput(const std::string& input) override {
        lastInput = input;
    }
    std::string lastInput;
};

int main() {
    MockRobloxInterface mock;
    ClimbingController controller(mock);

    controller.startClimbingSequence();
    assert(mock.lastInput == "Grip");

    return 0;
}