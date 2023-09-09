#include <Python.h>
/**
 */
void print_python_list_info(PyObject *p)
{
	PyObject *pyobj;
	int i, n, alloc;

	n = Py_SIZE(p);
	alloc = ((PyListObject *) p)->allocated;
	printf("[*] Size of the Python List = %d\n", n);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < n; i++)
	{
		printf("Element %d: ", i);
		pyobj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(pyobj)->tp_name);
	}
}
