import os


def make_output_dir(state):

    if not state.output_directory:
        msg = "No Output Directory Specified for State:" + state.name
        raise Exception(msg)

    if os.path.exists(state.output_directory):
        return

    os.makedirs(state.output_directory)
