
import unittest

from tailorscad.arg_parser import parse_args


# TODO: Making the config require required some changes I don't like to this
class TestArgParser(unittest.TestCase):

    def test_parse_args_known(self):

        args = []
        argv = ['-c', 'test']

        args = parse_args(argv)

        self.assertTrue(args)
        self.assertEqual(args.config, 'test')

    def test_parse_args_unkown_and_known(self):
        args = []
        argv = ['-a', 'word', '-c', 'test']

        args = parse_args(argv)

        self.assertTrue(args)
        self.assertEqual(args.config, 'test')
