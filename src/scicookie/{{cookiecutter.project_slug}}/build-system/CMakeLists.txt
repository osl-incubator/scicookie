cmake_minimum_required(VERSION 3.15...3.26)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION} LANGUAGES CXX)

{% if cookiecutter.build_system == "scikit-build-core" -%}

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(skcdemo MODULE skcdemo.cpp)

install(TARGETS skcdemo DESTINATION .)

{% elif cookiecutter.build_system == "pybind11" -%}

find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(_core MODULE src/{{cookiecutter.project_slug}}/main.cpp)

install(TARGETS _core DESTINATION src/{{cookiecutter.project_slug}}/main.cpp )

{%- endif %}                           
