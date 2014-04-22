import os
import unittest

from nose.plugins.attrib import attr

from tailorscad.process.process_data import process_states
from tailorscad.config.config import parse_states


@attr('slow')
class TestFromLoadedJSONTestCase(unittest.TestCase):

    def setUp(self):

        working_directory = os.getcwd()
        working_directory = os.path.join(
            working_directory, 'tailorscad', 'tests', 'integrations',
            'test_project')

        update = {'working_directory': working_directory}

        update['output_directory'] = os.path.join(working_directory, 'bin')

        self.config = {
            'main': 'main.scad',
            'scad_type': 'openSCAD',
            'requires': {
                'square': {'scad_type': 'openSCAD', 'main': 'square.scad'},
                'cube': {'scad_type': 'openSCAD', 'main': 'cube.scad'}},

            'global_params': {'cube_width': 14},
            'require_params': {'square': {'square_base': 3}},
            'openSCAD_params': ['--render', '--imgsize=100']}

        self.config.update(update)

    def test_render_from_loaded_json(self):

        config = parse_states(self.config)

        process_states(config.states)

        self.assertTrue(False)
