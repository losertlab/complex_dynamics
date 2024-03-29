from pathlib import Path
import sys
import inspect

# Test script for complex_dynamics.example_module.example_function.

src_file_path = inspect.getfile(lambda: None)
sys.path.append(str(Path(src_file_path).parents[2]))
print(str(Path(src_file_path).parents[2]))
from example_module import example_function
print(example_function(1, 2))
