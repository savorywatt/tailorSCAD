from tailorscad.config.config import parse_config_arg
from tailorscad.process.process_data import process_states


def render_scad(parsed_args):

    #Load Config
    config = parse_config_arg(parsed_args)

    #Call Process States
    process_states(config.states)
