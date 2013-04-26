# -*- coding: utf-8 -*-
"""
test this module

link -- http://docs.python.org/library/unittest.html

to run on the command line:
python -m unittest test_unidefy[.ClassTest[.test_method]]
"""
import unittest
import re
import string

import unidefy

class UnidefyTest(unittest.TestCase):

    def test_normalize(self):
        data = [
            ([u'Kl\xfcft skr\xe4ms'], u"Kluft skrams"),
            ([u'\u00f0'], u'\u00f0'),
            ([u'Here I am \u00f0'], u'Here I am \u00f0'),
            ([u'Here \xfc am \u00f0'], u'Here u am \u00f0'),
            ([u"\u0410", {u"\u0410": u'hedgehog'}], u'hedgehog'),
        ]

        for ival, oval in data:
            ret = unidefy.normalize(*ival)
            self.assertEqual(ret, oval)

        with self.assertRaises(UnicodeError):
            unidefy.normalize('this will throw an exception')
