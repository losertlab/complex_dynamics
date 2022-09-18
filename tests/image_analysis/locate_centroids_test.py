from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[2] / "src"))
from complex_dynamics.image_analysis.locate_centroids import locate_centroids
print(locate_centroids())
