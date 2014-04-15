import json
import logging

from tailorscad.state import State


def parse_config_arg(parsed_command_line_args):
    """Uses the results of the argparser to build an in memory representation
    of the config file.
    """
    with open(parsed_command_line_args.config, 'r') as config_file:
        return _parse_config_file(config_file)


def _parse_config_file(config_file):
    """Private function that takes a file object and parses it using the json
    library. Helps with testing reading files from the command line."""

    loaded_json = None
    try:
        loaded_json = json.load(config_file)
    except:
        logging.info("Unable to parse config file")

    loaded_json['states'] = _parse_states(loaded_json)

    return loaded_json


# TODO: Make this obey DRY
def _parse_states(loaded_json):
    """Creates a list of State objects with the work to be done. The main
    file is in the final position of the state list.
    """

    states = []
    global_params = loaded_json.get('global_params')
    require_params = loaded_json.get('required_params')
    requires = loaded_json.get('requires')

    for key, state in requires.iteritems():

            state['output_directory'] = loaded_json.get('output_directory')
            state['working_directory'] = loaded_json.get('working_directory')
            state['params'] = require_params.get(key) + global_params

            states.append(_parse_state(key, state))

    main_state = {'main_file': loaded_json.get('main')}
    main_state['scad_type'] = loaded_json.get('scad_type')
    main_state['output_directory'] = loaded_json.get('output_directory')
    main_state['working_directory'] = loaded_json.get('working_directory')
    main_state['params'] = global_params

    states.append(_parse_state('main', main_state))

    return states


def _parse_state(name, state):
    """Build a new State object"""

    new_state = {'name': name}
    new_state.update(state)
    return State(new_state)


def parse_config_string(config_string):
    """Takes a config that is a str and turns it into a dictionary
    """

    return json.loads(config_string)
