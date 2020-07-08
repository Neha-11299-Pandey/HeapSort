#heapify
def heapify(array , n,i):
    largest = i
    left_child = 2*i + 1
    right_child = 2* i +2
    if left_child < n and array[i] < array[left_child]:
        largest = left_child
    if right_child < n and array[largest]< array[right_child]:
        largest = right_child
    if largest != i:
        array[i] ,array[largest] = array[largest] ,array[i]
        heapify( array ,n,largest)

#sort
def heapSort(array):
    n = len(array)

    # maxheap
    for i in range(n//2, -1 , -1):
      heapify(array , n,i)
    # element extraction
    for i in  range(n-1,0 ,-1):
      #swap
      array[i] , array[0] = array[0], array[i]

      #Heapify root element
      heapify(array , i, 0)

 #main
    array = [1,2,3,5,7,12,7,10]
    heapSort(array)
    n= len(array)
    print ("Sorted array is the")
    for i in  range(n):
        print ( "%d " % array[i], end = '' )
