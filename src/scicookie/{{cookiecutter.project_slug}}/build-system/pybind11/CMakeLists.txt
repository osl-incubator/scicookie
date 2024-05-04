cmake_minimum_required(VERSION 3.15...3.26)

project({{ cookiecutter.package_slug }} VERSION {{ cookiecutter.project_version }} LANGUAGES CXX)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/main.cpp)

install(TARGETS _core DESTINATION src/main.cpp )
