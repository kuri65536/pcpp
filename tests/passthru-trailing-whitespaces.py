from __future__ import absolute_import, print_function
import unittest
import sys

shouldbe = r'''#line 1 "tests/passthru-trailing-whitespaces.h"
abc  

  aaa   
'''


class runner(object):
    def runTest(self):
        from pcpp import CmdPreprocessor
        p = CmdPreprocessor(['pcpp', '--passthru-trailing-ws',
                             '-o', 'tests/passthru-trailing-whitespaces.i',
                             'tests/passthru-trailing-whitespaces.h'])
        with open('tests/passthru-trailing-whitespaces.i', 'rt') as ih:
            output = ih.read()
        if output != shouldbe:
            print("Should be:\n" + shouldbe + "EOF\n", file=sys.stderr)
            print("\nWas:\n" + output + "EOF\n", file=sys.stderr)
        self.assertEqual(p.return_code, 0)
        self.assertEqual(output, shouldbe)


class multiple_input_files(unittest.TestCase, runner):
    pass
