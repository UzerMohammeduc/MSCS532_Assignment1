# insertion_sort.py

def insertion_sort_descending(arr):
    """
    Sorts an array in monotonically decreasing order using the Insertion Sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list in decreasing order.
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are smaller than key, to one position ahead
        # of their current position
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    # Example array to demonstrate the sorting function
    example_array = [12, 11, 13, 5, 6]
    sorted_array = insertion_sort_descending(example_array)
    print("Sorted array in descending order is:", sorted_array)
