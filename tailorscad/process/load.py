
import logging

from os import path
from os import access
from os import W_OK
from os import getcwd

from git import Repo

from tailorscad.process.save import make_output_dir


def load_state_files(state):

    # check if we're loading from git first
    if _is_git_file_loc(state.file_location):

        try:
            _load_git_files(state)
        except:
            logging.info('Failed to load Git')

    _set_state_file_path(state)


def _set_state_file_path(state):
    """ This will determine the path to the file that the SCAD builder
    is supposed to call."""

    if _is_git_file_loc(state.file_location):
        state.file_path = path.join(getcwd(), state.name)

    if path.isfile(state.main_path):

        state.file_path = state.file_location

        # Make the output directory
        make_output_dir(state)

    else:
        msg = "Main file not found: " + state.main_path
        raise Exception(msg)

    # check if the write out directory is writeable
    if not access(state.output_directory, W_OK):
        msg = "no write permissions:" + state.output_directory
        raise Exception(msg)


# TODO: This needs to be more robust
def _is_git_file_loc(file_location):

    if 'git' in file_location:
        return True


def _load_git_files(state):
    Repo(state.file_location)
