

# Load Config
# Create individual states
# - repository or folder
# - collection of arguments (combine global and local)
# - working directory
# - output folder (so needs config object passed in)
# - Final state is the main one
# For each state
# - get files
# - Attempt to build using a builder denoted by the scad_type
#   - Builder needs to handle replacements and output
#   - Builder is then consumed by another process


from process.load import load_state_files
from builder import build_from_state


def process_state(state):

    # Pull down git files or ensure folders exist
    load_state_files(state)

    # Make the subprocess calls to the appropriate SCAD package
    build_from_state(state)
