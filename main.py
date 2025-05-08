import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 101))
    
print("Random numbers:", numbers)

highest = max(numbers)
second_highest = -1

for num in numbers:
    if num != highest and num > second_highest:
        second_highest = num

print("2nd highest number:", second_highest)