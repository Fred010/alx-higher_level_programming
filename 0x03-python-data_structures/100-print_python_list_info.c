#include <Python.h>

/**
 * print_python_list_info - shows info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyObject * obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject*) p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (ind = 0; ind < size; ind++)
	{
		printf("Element %d: ", ind);

		obj = PyList_GetItem(p, ind);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
