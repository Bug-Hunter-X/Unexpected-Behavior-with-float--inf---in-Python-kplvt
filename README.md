# Unexpected Behavior with float('inf') in Python

This repository demonstrates a potential issue when using `float('inf')` (infinity) in Python.  While seemingly straightforward, using infinity can lead to unexpected behavior in calculations and comparisons, particularly when not properly handled.

## The Bug

The `bug.py` file contains a function that returns infinity (`float('inf')`) under a specific condition. The problem arises when this infinity is then used in further computations or comparisons, potentially leading to unexpected outcomes or runtime errors.