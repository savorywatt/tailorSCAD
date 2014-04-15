import unittest
from mock import Mock
from mock import patch
from mock import mock_open


from tailorscad.config import ConfigData
from tailorscad.config.config import _parse_config_file
from tailorscad.config.config import parse_config_string


class ConfigTestCase(unittest.TestCase):

    @unittest.skip('odd behavior')
    def test_parse_config_arg(self):

        data = '{"json":"obj"}'
        fake_arg = Mock()
        file_path = '/whatever/'
        fake_arg.config = file_path
        config = None
        m_open = mock_open(read_data=data)
        with patch('__main__.open', m_open, create=True) as m:

            with open(file_path) as config_file:
                config = _parse_config_file(config_file)

            m.assert_called_once_with(file_path)

            self.assertIsNotNone(config)
            self.assertTrue(config.get("json"))

    def test_parse_config_string(self):

        test = '{"json":"obj"}'

        result = parse_config_string(test)

        self.assertEqual(result['json'], "obj")


class ConfigDataTestCase(unittest.TestCase):

    def test_add_state(self):

        config = {'main': 'main.scad', 'requires': 'stuff'}

        data = ConfigData(config)
        new_state = 'a'
        data.add(new_state)

        self.assertEqual(data.states, [new_state])
