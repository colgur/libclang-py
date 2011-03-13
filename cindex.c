#include "Python.h"

#include "clang-c/Index.h"

#include <string.h>

static PyObject *
enableStackTraces(PyObject *self, PyObject *args)
{
    clang_enableStackTraces();
    return (PyObject*)Py_BuildValue("");
}

static PyObject *
createIndex(PyObject *self, PyObject *args)
{
  int displayDiags, excludePch;
  CXIndex pCindex = NULL;

  if ( !PyArg_ParseTuple(args, "ii", &excludePch, &displayDiags) ) {
    return NULL;
  }

  // TODO: Exception Handling
  pCindex = clang_createIndex(excludePch, displayDiags);
  
  return (PyObject *)PyCObject_FromVoidPtr(pCindex, NULL);
}

static PyObject *
disposeIndex(PyObject *self, PyObject *args)
{
  CXIndex pCindex = NULL;
  PyObject *pPyCindex = NULL;

  if ( !PyArg_ParseTuple(args, "O", &pPyCindex) ) {
    return NULL;
  }

  pCindex = PyCObject_AsVoidPtr(pPyCindex);
  clang_disposeIndex(pCindex);

  Py_RETURN_NONE;
}

static PyObject *
parseTranslationUnit(PyObject *self, PyObject *args)
{
  PyObject *pPyCindex = NULL;
  const char *source_filename;
  CXIndex pCindex = NULL;
  CXTranslationUnit pTu = NULL;

  if ( !PyArg_ParseTuple(args, "Os", &pPyCindex, &source_filename) ) {
    return NULL;
  }

  pCindex = PyCObject_AsVoidPtr(pPyCindex);
  // TODO: Need to do better than this in the full solution
  pTu = clang_parseTranslationUnit(pCindex, source_filename, NULL, 0, NULL, 0, 0);

  return (PyObject *)PyCObject_FromVoidPtr(pTu, NULL);
}

static PyMethodDef
LibClangMethods[] =
{
  { "enableStackTraces", enableStackTraces, METH_VARARGS },
  { "createIndex", createIndex, METH_VARARGS },
  { "disposeIndex", disposeIndex, METH_VARARGS },
  { "parseTranslationUnit", parseTranslationUnit, METH_VARARGS },
  { NULL, NULL },
};

void initlibclang(void)
{
  Py_InitModule("libclang", LibClangMethods);
}
