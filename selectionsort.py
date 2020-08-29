numbers = [4,9,3,5,2]
for i in range(len(numbers)):
    mini_index = i
    for j in range(i+1,len(numbers)):
        if numbers[j] < numbers[mini_index]:
            mini_index = j
    numbers[i],numbers[mini_index] = numbers[mini_index],numbers[i]

print(numbers)
print(len(numbers))