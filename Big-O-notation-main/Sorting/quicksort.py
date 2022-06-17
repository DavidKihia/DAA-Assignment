# Quicksort

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)

data = []
size = int(input('Input array size: '))
print("Input elements:\n")

for i in range(0,size):
    element = int(input())
    data.append(element)

print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
