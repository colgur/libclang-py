#!/usr/bin/env python
"""Unit Tests for cindex classes and underlying libclang extension"""

__author__ = 'colgur@gmail.com'

import unittest
import os

import cindex

kInputsDir = os.path.join(os.path.dirname(__file__), 'TEST_INPUTS')

class CindexTest(unittest.TestCase):
    def test_createIndex(self):
        index = cindex.Index.create()
        self.assertNotEqual(index, None)

    def test_parse(self):
        index = cindex.Index.create()
        tu = index.parse(os.path.join(kInputsDir, 'hello.cpp'))
        # TODO: What can be asserted to be true about a TU?

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(CindexTest))
    return suite

suite = suite()
unittest.TextTestRunner().run(suite)
