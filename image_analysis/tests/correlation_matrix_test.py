from pathlib import Path
import sys
import inspect
src_file_path = inspect.getfile(lambda: None)
sys.path.append(str(Path(src_file_path).parents[2]))

from image_analysis import correlation_matrix
print(correlation_matrix())
