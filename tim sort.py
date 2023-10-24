def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and key_item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)

    return [right[0]] + merge(left, right[1:])

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = min((start + size - 1), (n - 1))
            end = min((start + size * 2 - 1), (n - 1))

            merged_array = merge(
                left=arr[start:start + size],
                right=arr[start + size:end + 1]
            )

            arr[start:start + len(merged_array)] = merged_array

        size *= 2

def main():
    # Input a list of numbers
    try:
        input_str = input("Enter a list of numbers separated by spaces: ")
        unsorted_list = [int(num) for num in input_str.split()]
    except ValueError:
        print("Invalid input. Please enter a list of numbers.")
        return

    # Call the timsort function to sort the list
    timsort(unsorted_list)

    # Display the sorted list
    print("Sorted List:", unsorted_list)

if __name__ == "__main__":
    main()
