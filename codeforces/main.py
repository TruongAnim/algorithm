def is_subarray(arr, subarr):
    index = 0
    for i in subarr:
        try:
            index = arr.index(i, index)
            print(i, index)
            index+=1

        except ValueError:
            return False
    return True


# Example usage
array = [8, 8, 0, 0, 5, 5, 5, 3, 5, 3, 5, 1, 2, 3, 4, 5, 6]
subarray = [5,1]

if is_subarray(array, subarray):
    print("Subarray belongs to the array")
else:
    print("Subarray does not belong to the array")