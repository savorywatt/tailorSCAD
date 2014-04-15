

# These models are designed to allow async execution eventually

class State(object):

    def __init__(self, state):

        self._state = state

    @property
    def name(self):

        return self._state.get('name')

    @property
    def main_file(self):

        return self._state.get('main')

    @property
    def scad_type(self):

        return self._state.get('scad_type')

    @property
    def output_directory(self):

        return self._state.get('output_directory')

    @property
    def working_directory(self):

        return self._state.get('working_directory')

    @property
    def params(self):

        return self._state.get('params')
