#include <Python.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * print_python_list_info - prints info about python lists
 * @p: address of pyobject struct
 */
void print_python_list_info(PyObject *p)
{
	int i = 0;

	list_size = py_size(p);
	allocate = ((PyListobject *)p)->allocate

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);
	while (i < list_size)
	{

		printf("Element %d: %s\n", i, py_type(PyList_GetItem(p, i))->tp_name);
		i++;
	}
}
