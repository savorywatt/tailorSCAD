import subprocess

#from tailorscad.config import ScadConfig


BASE_DIR = '/usr/bin/'
DEFAULT = BASE_DIR + 'openscad'


def build_with_openscad(state):

    args = build_args_from_state(state)

    try:
        subprocess.check_call(args, state.working_dir)
        return True
    except subprocess.CalledProcessError as (e):
        print str(e)
        return False


def build_args_from_state(state):

    #executable = ScadConfig.open_scad if ScadConfig.open_scad else DEFAULT
    executable = 'openscad'

    print state.params
    replace = [':'.join((key, str(value)))
               for key, value in state.params.iteritems()]

    args = [executable, '-o', state.output_directory, '-D'] + replace

    args.append(state.main_file)

    return args
