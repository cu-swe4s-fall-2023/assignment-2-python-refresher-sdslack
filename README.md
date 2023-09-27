# Overview

This project's source code enables the user to query a file containing
fire data by country, returning a user-specified (or default) column
of data from the file matching the input query.

# Installation

Python3 and bash are required to run this project.

This repository can be cloned, and then
print_fires.py (which imports the functions in my_utils.py) can be
run using a bash script, like the included example run.sh.

# Usage

The my_utils file contains the following:

```python
import src/my_utils as utils
docstring = utils.get_docstring()
print(docstring)
```

The print_fires file imports my_utils and requires the following inputs:

```bash
print("test")
```

```bash
python3 src/print_fires.py -h
```

The bash script run.sh includes three examples of how to use the source
code. The script and the output of all three tests is as follows:

```bash
cat run.sh
bash run.sh
```
