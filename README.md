# Color Sort Algorithm (Prototype)

**A simple and competitively efficient prototyped unstable sorting algorithm which sorts data according to a predefined color gradient spectrum**

***`Requires Python >=3.14.4`***

## Package Link
[pypi.org](https://pypi.org/project/color-sort-algorithm/)

## Install
```
pip install color-sort-algorithm
```

# Semi-Pseudocode Examples
### Example 1 (Numerical)
```python
from color_sort_prototype import ColorSort

# Example Input:
unsortedData = [3, 5, 6, 8, 7, 2, 1, 5, 6, 9, 10] # Array filled with a variable amount of unsorted numbers

# First Bool = Ascending/Descending order
# Second Bool = Numerical/Alphabetical sorting
sortedData = ColorSort(unsortedData, True, True)

# Output:
print(sortedData) # sortedData = [1, 2, 3, 5, 5, 6, 6, 7, 8, 9, 10]

```
### Example 2 (Alphabetical)
```python
from color_sort_prototype import ColorSort

# Example Input:
unsortedData = {
  5: "Charlie",
  3: "Macy",
  4: "Nancy",
  1: "Joe",
  2: "John"
} # Dictionary of names with numerical indexes

# First Bool = Ascending/Descending order
# Second Bool = Numerical/Alphabetical sorting
sortedData = ColorSort(unsortedData, True, False)

# Output:
print(sortedData) # sortedData = [1, 2, 3, 4, 5] <-- Important: returns the numerical indices, not the names (subject to change)
```
