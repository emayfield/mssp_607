from build_states import build_states_csv

# This file shows how we can use functions from a Python file and 
# call them from any other file using imports.
# 
# We want to use the if __name__ == "__main__" syntax so that
# we can give direct instructions on the code we want to actually run,
# not just define. This code will not run if this file is imported elsewhere.
if __name__ == "__main__":
    build_states_csv("state_sizes.csv")
    print("Success")

