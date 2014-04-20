
import logging

from os import path
from os import access
from os import W_OK
from os import getcwd

from git import Repo


def load_state_files(state):

    print state.file_location
    # check if we're loading from git first
    if _is_git_file_loc(state.file_location):

        try:
            _load_git_files(state)
        except:
            logging.info('Failed to load Git')

    _set_state_file_path(state)


def _set_state_file_path(state):

    if _is_git_file_loc(state.file_location):
        state.file_path = path.join(getcwd(), state.name)
    else:
        state.file_path = state.file_location

    # check if the directory is readable
    if not path.isdir(state.file_path):
        raise Exception("Path %s is not a directory" % state.file_path)

    # check if the write out directory is writeable
    if not access(state.file_path, W_OK):
        raise Exception("tailorscad does not have write permissions")


# TODO: This needs to be more robust
def _is_git_file_loc(file_location):

    if 'git' in file_location:
        return True


def _load_git_files(state):
    Repo(state.file_location)
