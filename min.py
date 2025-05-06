"""
Implements function to find index of minimum element.
"""

from icecream import ic # type: ignore

def indexOfMin(lyst):
    """Returns the index of the minimum item"""
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

# Example
lyst = lyst = [3, 2, 1, 6, 5]
index_of_min = indexOfMin(lyst)
ic(index_of_min)

"""
indexOfMin(lyst)
Input: a non-empty list
Output: the index of the minimum item

The algorithm goes through each element in the list, so time complexity is O(n)
- We assume first element is at minIndex
- We set currentIndex to the second element, and start comparing.
- If element at currentIndex is smaller that element at minIndex, we set minIndex as the new minimum index
- When while loop terminates, after having visited all elements in the lyst, we return minIndex
"""