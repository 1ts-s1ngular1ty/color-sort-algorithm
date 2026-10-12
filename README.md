# Color Sort Algorithm (Prototype)

**A simple and competitively efficient prototyped unstable sorting algorithm which sorts data according to a predefined color gradient spectrum**

***`Requires Python >=3.14.4`***

## Package Link
[pypi.org/project/color-sort-algorithm](https://pypi.org/project/color-sort-algorithm/)

## Install
```
pip install color-sort-algorithm
```

## Usage Example 1 (Numerical)
```python
from color_sort_prototype import ColorSort

# Array filled with a variable amount of random/unsorted numbers
unsortedData = []

# First Bool = Ascending/Descending order
# Second Bool = Numerical/Alphabetical sorting
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

# First Bool = Ascending/Descending order
# Second Bool = Numerical/Alphabetical sorting
sortedData = ColorSort(unsortedData, True, False)
```
