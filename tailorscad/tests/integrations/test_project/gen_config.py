import json

config_complex = {
    'main': 'assemble.scad',
    'scad_type': 'openSCAD',
    'requires': {
        'neat_finger': {'scad_type': 'openSCAD', 'main': 'finger.scad'},
        'rocking_palm': {'scad_type': 'openSCAD', 'main': 'palm.scad'}},

    'working_directory': '/home/uploads/whatever/',
    'output_directory': '/home/uploads/whatever/renders/1234241',
    'global_params': {'finger_width': 14, 'wrist_width': 50},
    'require_params': {'neat_finger': {'rubber_width': 3}},
    'openSCAD_params': ['--render', '--imgsize=100']}

config_test = {
    'main': 'main.scad',
    'scad_type': 'openSCAD',
    'requires': {
        'square': {'scad_type': 'openSCAD', 'main': 'square.scad'},
        'cube': {'scad_type': 'openSCAD', 'main': 'cube.scad'}},

    'global_params': {'cube_width': 14},
    'require_params': {'square': {'square_base': 3}},
    'openSCAD_params': ['--render', '--imgsize=100']}

json_string = json.dumps(config_test)
print json_string
