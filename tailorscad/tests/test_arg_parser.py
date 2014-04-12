
import unittest

from tailorscad.arg_parser import parse_args


class TestArgParser(unittest.TestCase):

    def test_parse_args_none(self):

        args = []
        argv = []

        args = parse_args(argv)

        self.assertFalse(args)

    def test_parse_args_inknown(self):

        args = []
        argv = ['-a', 'word']

        args = parse_args(argv)

        self.assertFalse(args)

    def test_parse_args_known(self):

        args = []
        argv = ['-c', 'test']

        args = parse_args(argv)

        self.assertTrue(args)
        self.assertEqual(args, ['test'])

    def test_parse_args_unkown_and_known(self):
        args = []
        argv = ['-a', 'word', '-c', 'test']

        args = parse_args(argv)

        self.assertTrue(args)
        self.assertEqual(args, ['test'])
