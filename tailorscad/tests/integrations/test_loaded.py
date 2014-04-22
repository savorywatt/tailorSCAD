import os
import unittest

from nose.plugins.attrib import attr

from tailorscad.process.process_data import process_states
from tailorscad.process.process_data import process_state

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
                'sphere': {'scad_type': 'openSCAD', 'main': 'sphere.scad'},
                'cube': {'scad_type': 'openSCAD', 'main': 'cube.scad'}},

            'global_params': {'cube_width': 14},
            'require_params': {'sphere': {'sphere_base': 3}},
            'openSCAD_params': ['--render', '--imgsize=100']}

        self.config.update(update)
        self.working_directory = working_directory
        self.output_directory = os.path.join(working_directory, 'bin')
        self.output_files = ['sphere.stl', 'cube.stl', 'main.stl']

    def tearDown(self):
        """Make sure we remove the rendered files between tests"""

        for stl in self.output_files:
            stl_path = os.path.join(self.output_directory, stl)

            os.remove(stl_path)

    def test_render_from_loaded_json(self):

        config = parse_states(self.config)

        process_states(config.states)
        process_state(config.main_state)

        for stl in self.output_files:
            stl_path = os.path.join(self.output_directory, stl)
            self.assertTrue(os.path.exists(stl_path))

        self.assertTrue(False)
