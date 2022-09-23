# Complex Dynamics

Complex dynamics toolbox built by Dr. Losert's research group. This package exposes relevant computational tools.

## Installation

Follow these steps to use the complex dynamics toolbox.

### Prerequisites/Packages

- git

### Installation Steps

Clone the repo at `git@github.com:losertlab/complex_dynamics.git`.

`git clone <reponame>`

Move to the `complex_dynamics` directory.

`cd /path/to/complex_dynamics/`

### Usage

In your python program, import sys if not already imported.

`import sys`

Add the path to the `src` directory in the complex dynamics repository.

`sys.path.append('/path/to/complex_dynamics/')`

Import and use modules and functions, for example:

```
from example_module import example_function
print(example_function(param1, param2));
```

### Documentation

This module is documented using [docstrings](https://www.datacamp.com/tutorial/docstrings-python).

### Adding Your Code

The `complex_dynamics` package has a tree structure starting from the `complex_dynamics` node. The folders within `complex_dynamics` organize code into areas of analysis techniques. For example, `complex_dynamics/image_analysis`.

To add your own code to the toolbox, first create a new branch.

`git branch my_feature_branch`

Switch to the newly created branch.

`git checkout my_feature_branch`

Push your local branch to the remote repository.

`git push --set-upstream origin my_feature_branch`

Add your code to the appropriate folder in the package. If necessary, create a new folder in the `complex_dynamics` folder, along with a new `__init__.py` file. This will allow your code to be used as part of a library. 

Connect your function to the module with a line in `/complex_dynamics/module_folder/__init__.py` such as:

`from example_module.example_function import example_function`

List all dependencies your code has in the **Prerequisites/Packages** section of `README.md`.

Next, stage, commit, and push your changes.

```
git add --all
git commit -m "Descriptive comment here."
git push
```

Create a pull request on Github to merge your changes into the stable branch. The pull request should be into `master` from `my_feature_branch`. Add a reviewer to the pull request. They will look over your changes and merge the pull request.

### Comments

This repo is a work in progress. It should be a good starting place to sharing code.
