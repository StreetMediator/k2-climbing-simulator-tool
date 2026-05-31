cmake_minimum_required(VERSION 3.10)
project(k2-climbing-simulator-tool)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(k2_simulator
    src/main.cpp
    src/climbing/ClimbingController.cpp
    src/roblox/RobloxInterface.cpp
)

target_include_directories(k2_simulator PRIVATE src)
target_link_libraries(k2_simulator PRIVATE roblox_api)