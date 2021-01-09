def bubbleSort(array):
    
    # run loops two times: one for walking throught the array 
    # and the other for comparison
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):

            # To sort in descending order, change > to < in this line.
            if array[j] > array[j + 1]:
                
                # swap if greater is at the rear position
                (array[j], array[j + 1]) = (array[j + 1], array[j])


data = [-2, 45, 0, 11, -9]
print('Elements before sorting:')
print(data)

bubbleSort(data)

print('Elements before sorting:')
print(data)
