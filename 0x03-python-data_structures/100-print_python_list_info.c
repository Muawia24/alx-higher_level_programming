#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: A PyObject list.
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
    int list_size, allocate, i = 0;
    PyObject *obj;

    list_size = Py_SIZE(p);
    allocate = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", list_size);
    printf("[*] Allocated = %d\n", allocate);

    while (i < list_size)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	i++;
    }
}
