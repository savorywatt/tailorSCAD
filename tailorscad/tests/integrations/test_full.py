import unittest

from nose.plugins.attrib import attr

import subprocess
import os


@attr('slow')
class EndToEndTestCase(unittest.TestCase):

    def test_render_test_project(self):

        test_path = os.path.join(
            'tailorscad', 'tests', 'integrations', 'test_project',
            'test.config')

        args = ['./tailor', '-c', test_path]

        try:
            result = subprocess.check_call(args)

        except subprocess.CalledProcessError, e:
            self.assertTrue(False, msg='End to End failed:' + str(e))

        verify_path = os.path.join(
            'tailorscad', 'tests', 'integrations', 'test_project', 'bin',
            'main.stl')

        self.assertIsNotNone(result)

        self.assertTrue(os.path.exists(verify_path))
