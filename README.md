# ArraySlicer

A python class for slicing arrays into sub arrays.

## Installation

To install:

```bash
$ git clone git@github.com:kenmclennan/array-slicer.git
$ pip install ./array-slicer
```

## Usage

This module provides a wrapper class for an array. Calling slice_into with an
integer N will attempt to evenly distribute the wrapped array elements into N
sub arrays.


```python
from array_slicer import ArraySlicer

slicer = ArraySlicer([1,2,3])
slicer.slice_into(2)
# [[1, 2], [3]]
```

N arrays will always be returned. Where there are insufficient wrapped array
elements the return value is padded with empty arrays.


```python
slicer = ArraySlicer([1,2,3])
slicer.slice_into(4)
# [[1], [2], [3], []]
```

Negative values for N will raise a ValueError exception

```python
slicer.slice_into(-2)
# ValueError: was asked for -2 slices, expected a minimum of 0
```

Benign values are returned in casses of N = 0 and empty arrays.

```python
ArraySlicer([1,2]).slice_into(0)
# []

ArraySlicer([]).slice_into(2)
# [[], []]
```

## Tests

Tests can be run with from the module directory

```bash
$ python setup.py test
```