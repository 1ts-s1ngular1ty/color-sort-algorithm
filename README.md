# Color Sort Algorithm (Prototype)

## Package Link
[pypi.org](https://pypi.org/project/color-sort-algorithm/)

## Install
```
pip install color_sort_algorithm
```

## Usage Example 1 (Numerical)
```python
from color_sort_prototype import ColorSort

# Array filled with a variable amount of random/unsorted numbers
unsortedData = []

# First True = Ascending/Descending order
# Second True/False = Numerical/Alphabetical sorting
sortedData = ColorSort(unsortedData, True, True)
```
## Usage Example 2 (Alphabetical)
```python
from color_sort_prototype import ColorSort

# Dictionary of names with numerical indexes
unsortedData = {
  5: "Charlie",
  3: "Macy",
  4: "Nancy",
  1: "Joe",
  2: "John"
}

# First True = Ascending/Descending order
# Second True/False = Numerical/Alphabetical sorting
sortedData = ColorSort(unsortedData, True, False)
