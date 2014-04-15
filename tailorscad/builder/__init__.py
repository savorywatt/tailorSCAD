from tailorscad.builder.openscad import build_with_openscad
from tailorscad.builder.coffeescad import build_with_coffeescad
from tailorscad.constants import OPENSCAD
from tailorscad.constants import COFFEESCAD


def build_from_state(state):

    if state.scad_type is OPENSCAD:
        build_with_openscad(state)

    if state.scad_type is COFFEESCAD:
        build_with_coffeescad(state)
