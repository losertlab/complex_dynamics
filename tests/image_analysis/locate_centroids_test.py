from pathlib import Path
import sys
import inspect
src_file_path = inspect.getfile(lambda: None)
sys.path.append(str(Path(src_file_path).parents[2] / "src"))
from complex_dynamics.image_analysis import locate_centroids
print(locate_centroids())
