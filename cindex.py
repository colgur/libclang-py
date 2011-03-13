#!/usr/bin/env python

# TODO: Robust import
import libclang

class Index(object):
    """
    The Index type provides the primary interface to the Clang CIndex library,
    primarily by providing an interface for reading and parsing translation
    units.
    """

    @staticmethod
    def create(excludeDecls=False):
        """
        Create a new Index.
        Parameters:
        excludeDecls -- Exclude local declarations from translation units.
        """
        return Index(libclang.createIndex(excludeDecls, 0))

    def __init__(self, ptr):
        self.ptr = ptr

    def dispose(self):
        """
        Clean-up Index resources
        """
        libclang.disposeIndex(self.ptr)

    def parse(self, path):
#    def parse(self, path, args = [], unsaved_files = [], options = 0):
        """
        Load the translation unit from the given source code file by running
        clang and generating the AST before loading. Additional command line
        parameters can be passed to clang via the args parameter.

        In-memory contents for files can be provided by passing a list of pairs
        to as unsaved_files, the first item should be the filenames to be mapped
        and the second should be the contents to be substituted for the
        file. The contents may be passed as strings or file objects.
        """
        return TranslationUnit(libclang.parseTranslationUnit(self.ptr, path))

class TranslationUnit(object):
    def __init__(self, ptr):
        self.ptr = ptr
