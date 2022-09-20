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

### Adding Your Code

The `complex_dynamics` package has a tree structure starting from the `src/complex_dynamics` node. The folders within `src/complex_dynamics` organize code into areas of analysis techniques. For example, `src/complex_dynamics/image_analysis` contains code related to the analysis of images.

To add your own code to the toolbox, first create a new branch.

`git branch my_feature_branch`

Switch to the newly created branch.

`git checkout my_feature_branch`

Push your local branch to the remote repository.

`git push --set-upstream origin my_feature_branch`

Add your code to the appropriate folder in the package. If necessary, create a new folder in the `src/complex_dynamics/` folder, along with an empty `__init__.py` file. This will allow your code to be used as part of a library.

When your changes are complete, stage, commit, and push your changes.

`git add --all`
`git commit -m "Descriptive comment here."`
`git push`

Create a pull request on Github to merge your changes into the stable branch. The pull request should be into `master` from `my_feature_branch`. Add a reviewer to the pull request. They will look over your changes and merge the pull request.

### Comments

This repo is a work in progress. There will be issues using it at first, but this should be a good starting place to sharing code.
