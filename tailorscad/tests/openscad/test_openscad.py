import unittest
import os


from tailorscad.state import State
from tailorscad.builder.openscad import build_args_from_state


class OpenSCADTestCase(unittest.TestCase):

    def test_build_args_from_state(self):

        raw = {'main': 'the.scad',
               'scad_type': 'openscad',
               'output_directory': '/data/',
               'params': {'w': 1},
               'working_directory': os.getcwd()}

        state = State(raw)

        args = build_args_from_state(state)

        expected = ['openscad', '-o', '/data/', '-D', 'w:1',
                    'the.scad']

        self.assertEqual(expected, args)
