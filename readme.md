## Package Status

| Bintray | Windows | Linux & macOS |
|:--------:|:---------:|:-----------------:|
|[![Download](https://api.bintray.com/packages/jinntechio/public-conan/package_name%3Abincrafters/images/download.svg) ](https://bintray.com/bincrafters/public-conan/package_name%3Abincrafters/_latestVersion)|[![Build status](https://ci.appveyor.com/api/projects/status/github/bincrafters/conan-package_name?svg=true)](https://ci.appveyor.com/project/bincrafters/conan-package_name)|[![Build Status](https://travis-ci.com/bincrafters/conan-package_name.svg)](https://travis-ci.com/bincrafters/conan-package_name)|

## Conan Information

Jinncrafters.com packages can be found in the following public Conan repository:

[jinncrafters.com Public Conan Repository on Bintray](https://bintray.com/jinncrafters/conan)

*Note: You can click the "Set Me Up" button on the Bintray page above for instructions on using packages from this repository.*

## Conan package recipe for [*sol2*](https://sol2.readthedocs.io/en/latest/)

sol is a C++ library binding to Lua. It currently supports all Lua versions 5.1+ (LuaJIT 2.x included). 
sol aims to be easy to use and easy to add to a project. The library is header-only for easy integration with projects.

## Issues

If you wish to report an issue or make a request for a package, please do so here:


## For Users

### Basic setup

    $ conan install sol2/2.20.6/@jinntechio/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    sol2/2.20.6/@jinntechio/stable

    [generators]
    cmake