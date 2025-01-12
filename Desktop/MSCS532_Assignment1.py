#Taking example array to be sorted
example_arr = [7, 3, 10, 22, 21, 9, 12, 5]
#defining Insortion Sort function
def insertion_sort_dec(example_arr):
    
    for i in range(1, len(example_arr)):
        current_element = example_arr[i]
        j = i-1 

        #Performing the check of each elements in array of the array
        while j >= 0 and example_arr[j] < current_element:
            example_arr[j+1] = example_arr[j]
            j -= 1

        example_arr[j+1] = current_element

    return example_arr
arr_sorted = insertion_sort_dec(example_arr)
print("Array sorted in decreasing order:", arr_sorted)