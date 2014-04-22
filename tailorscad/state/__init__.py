from os import path

# This model is designed to allow async execution eventually


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
    def main_path(self):

        if not self.working_directory:
            return path.join('', self.main_file)

        return path.join(self.working_directory, self.main_file)

    @property
    def working_directory(self):

        return self._state.get('working_directory')

    @property
    def file_location(self):

        result = ''
        if not self.working_directory:
            return path.join(result, self.name)

        result = path.join(self.working_directory, self.name)

        return result

    @property
    def file_path(self):

        return self._state.get('file_path', '')

    @file_path.setter
    def file_path(self, path):

        new_path = {'file_path': path}
        self._state.update(new_path)

    @property
    def scad_type(self):

        return self._state.get('scad_type')

    @property
    def output_directory(self):

        return self._state.get('output_directory')

    @property
    def params(self):

        return self._state.get('params')
