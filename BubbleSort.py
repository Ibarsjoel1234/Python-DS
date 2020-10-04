def bubblesort(a):
  size = len(a)
  for i in range(size):
    for j in range(i+1,size):
      if a[i] > a[j]:
        a[i],a[j] = a[j],a[i]

a = []
s = int(input("Enter the size: "))
print("Enter the Numbers: ")
for f in range(0,s):
  f = int(input())
  a.append(f)
print(f'Before Swapping: {a}')
bubblesort(a)
print(f'After  Swapping: {a}')
