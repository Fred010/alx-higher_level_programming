#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - output bytes information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int bsize, ind, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	bsize = ((PyVarObject*)(p))->ob_bsize;
	string = ((PyBytesObject*) p)->ob_sval;

	printf("  bsize: %ld\n", bsize);
	printf("  trying string: %s\n", string);

	if (bsize >= 10)
		limit = 10;
	else
		limit = bsize + 1;

	printf("  first %ld bytes:", limit);

	for (ind = 0; ind < limit; ind++)
		if (string[ind] >= 0)
			printf(" %02x", string[ind]);
		else
			printf(" %02x", 256 + string[ind]);

	printf("\n");
}

/**
 * print_python_list - output list information
 *
 * @p: Python Object
 * Return: no return
 */

void print_python_list(PyObject *p)
{
	long int bsize, ind;
	PyListObject * list;
	PyObject * obj;

	bsize = ((PyVarObject*)(p))->ob_bsize;
	list = (PyListObject*) p;

	printf("[*] Python list info\n");
	printf("[*] bsize of the Python List = %ld\n", bsize);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (ind = 0; ind < bsize; ind++)
	{
		obj = ((PyListObject*) p)->ob_item[ind];
		printf("Element %ld: %s\n", ind, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
