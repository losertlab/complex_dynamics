# Complex Dynamics

Complex dynamics toolbox built by Dr. Losert's research group. This package exposes relevant computational tools.

## Installation

Follow these steps to use the complex dynamics toolbox.

### Prerequisites

- git
- anaconda

### Installation Steps

Clone the repo at REPO NAME.

`git clone <reponame>`

Move to the `complex_dynamics` directory.

`cd /path/to/comple_dynamics/`

Create environment for the toolbox.

`conda env create -f complex_dynamics_env.yml`

Activate the environment.

`conda activate complex_dynamics_env`

If you have existing conda environments you need, merge them.

`conda-merge complex_dynamics_env.yml [env1.yml env2.yml ... envn.yml] > local/localenv.yml`

### Usage

Activate the complex dynamics environment, or your merged environment.

`conda activate complex_dynamics_env` or `conda activate path/to/local/localenv.yml`

In your python program, import sys if not already imported.

`import sys`

Add the path to the `src` directory in the complex dynamics repository.

`sys.path.append('/path/to/complex_dynamics/src/')`

Import and use modules and functions, for example:

```
from complex_dynamics.image_analysis.locate_centroids import locate_centroids
print(locate_centroids());
```
