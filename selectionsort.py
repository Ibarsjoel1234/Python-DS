def SelectionSort(l):
  for i in range(len(l)):           
    minpos = i
    for j in range(i+1, len(l)):
      if l[j] < l[minpos]:
        minpos= j
    l[i],l[minpos] = l[minpos],l[i]

x = []                              # Creating a empty list
k = int(input("Enter the size: ")). # asking the user for size of the list
print("Enter the number")           # Displaying to the user
for h in range(0,k):                # iterating 0 to k where k is the size that we enter
  h = int(input())                  # storing the value in h 
  x.append(h)                       # and appending to the list
SelectionSort(x)                    # calling selection sort function 
print(x)
