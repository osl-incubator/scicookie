#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE({{ cookiecutter.package_slug }}, m) {
    m.def("hello", [](){
        py::print("Hello, scikit-build-core!");
    });
}
