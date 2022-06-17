#Bubblesort

def bubble_sort(array):
     for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = []

size = int(input('Enter size of array: '))

print("Enter elements: \n")

for i in range(0, size):
    element = int(input())
    array.append(element)


print("The unsorted array is :\n", array)

print("The sorted array is: \n")
bubble_sort(array)
print(array)