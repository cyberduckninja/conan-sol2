cmake_minimum_required(VERSION 2.8.12)
project(test_package)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS OFF)

set(LUA_PC_CFG "lua;lua5.3;lua5.2;lua5.1" CACHE STRING "pkg-config Lua configuration file (or files, separated by ;)")

find_package(PkgConfig)
if(PKG_CONFIG_EXECUTABLE)
    pkg_search_module(LUA REQUIRED ${LUA_PC_CFG})
else()
    if(NOT LUA_INCLUDE_DIR)
        message(SEND_ERROR "LUA_INCLUDE_DIR is required if no PkgConfig is available!")
    endif()
    if(NOT LUA_LIBRARIES)
        message(SEND_ERROR "LUA_LIBRARIES is required if no PkgConfig is available!")
    endif()
endif()

find_package(Lua 5.3)

if(${LUA_INCLUDE_DIR})
    if(NOT EXISTS ${LUA_INCLUDE_DIR}/lua.h)
        message(SEND_ERROR "Can't find lua.h in ${LUA_INCLUDE_DIR}")
    endif()
endif()

include_directories(${LUA_INCLUDE_DIRS})

set(CMAKE_VERBOSE_MAKEFILE TRUE)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(${PROJECT_NAME} test_package.cpp)
target_link_libraries(${PROJECT_NAME} ${CONAN_LIBS})
