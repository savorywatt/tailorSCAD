import subprocess
import os

#from tailorscad.config import ScadConfig


BASE_DIR = '/usr/bin/'
DEFAULT = BASE_DIR + 'openscad'


def build_with_openscad(state):

    args = build_args_from_state(state)

    out_call = ''

    for arg in args:

        out_call += ' ' + arg

    print 'args:', out_call
    try:

        print 'rendered output path:', state.name
        subprocess.check_call(args)
        return True
    except subprocess.CalledProcessError as (e):
        print str(e)
        return False


def build_args_from_state(state):

    #executable = ScadConfig.open_scad if ScadConfig.open_scad else DEFAULT
    executable = 'openscad'

    print state.params
    replace = ['-D']
    if state.params:
        replace = [':'.join((key, str(value)))
                   for key, value in state.params.iteritems()]

    print 'replace ', replace

    output = os.path.join(state.output_directory, state.name + ".stl")

    args = [executable, '-o', output]
    if len(replace) > 1:
        args.extend(replace)
    args.append(state.main_path)

    return args
