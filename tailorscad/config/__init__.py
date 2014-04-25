import json


# TODO: Make this more robust, read a config file
class ScadConfig(object):

    def __init__(self):

        self.open_scad = 'openscad'


class ConfigData(object):

    def __init__(self, config):

        self._config = config

    def add(self, state):

        self.states.append(state)

    @property
    def main_scad(self):

        return self._config.get('main')

    @property
    def main_state(self):

        return self._config.get('main_state')

    @property
    def requires(self):

        return self._config.get('requires')

    @property
    def working_directory(self):

        return self._config.get('working_directory')

    @property
    def output_directory(self):

        return self._config.get('output_directory')

    @property
    def states(self):

        if 'states' not in self._config:
            self._config['states'] = []

        return self._config.get('states')

    @states.setter
    def states(self, states):

        self._config['states'] = states

    def from_json(self, config):

        self._config = json.loads(config)

    def to_json(self, config):

        return json.dumps(self._config)
