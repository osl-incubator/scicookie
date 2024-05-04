#include <Python.h>

static PyObject* foo(PyObject* self)
{
    return PyUnicode_FromString("bar");
}

static PyMethodDef methods[] = {
    {"foo", (PyCFunction)foo, METH_NOARGS, NULL},
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "{{ cookiecutter.package_slug }}",
    NULL,
    -1,
    methods,
};

PyMODINIT_FUNC PyInit_{{ cookiecutter.package_slug }}(void)
{
    return PyModule_Create(&module);
}
