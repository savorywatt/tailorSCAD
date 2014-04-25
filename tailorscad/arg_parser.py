import argparse


def parse_args(argv):
    """Takes a sys.argv and parses it."""

    parser = argparse.ArgumentParser(prefix_chars='-')

    config_help = 'Must be a path to a tailor config file'
    parser.add_argument('-c', '--config', type=str, help=config_help,
                        required=True)

    args, unknown = parser.parse_known_args(argv)

    return args
