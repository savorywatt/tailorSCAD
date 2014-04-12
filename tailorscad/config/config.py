import json
import logging


def parse_config_arg(parsed_command_line_args):
    """Uses the results of the argparser to build an in memory representation
    of the config file.
    """
    with open(parsed_command_line_args.config, 'r') as config_file:
        return _parse_config_file(config_file)


def _parse_config_file(config_file):

    try:
        return json.load(config_file)
    except:
        logging.info("Unable to parse config file")


def parse_config_string(config_string):
    """Takes a config that is a str and turns it into a dictionary
    """

    return json.loads(config_string)
