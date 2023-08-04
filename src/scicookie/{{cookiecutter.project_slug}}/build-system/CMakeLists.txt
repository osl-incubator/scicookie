{% if cookiecutter.build_system == "scikit-build-core" -%}
cmake_minimum_required(VERSION 3.15...3.26)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(skcdemo MODULE skcdemo.cpp)

install(TARGETS skcdemo DESTINATION .)

{% elif cookiecutter.build_system == "pybind11" -%}
cmake_minimum_required(VERSION 3.15...3.26)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(pybind11 MODULE pybind11.cpp)

install(TARGETS pybind11 DESTINATION .)

{%- endif %}                           