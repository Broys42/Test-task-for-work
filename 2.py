n = [int(x) for x in input() if int(x) >= 2 and int(x) <= 100000]

numbers_input = input()

numbers_list = [int(num) for num in numbers_input.split() if int(num) >= 1 and int(num) <= 1000000000]

slice1, slice2, slice3, answer = [], [], [], []

middle_index = len(numbers_list) // 2 if (len(numbers_list)) % 2 == 0 else len(numbers_list) // 2 + 1

for i in range(len(numbers_list)):
    if i > len(numbers_list) // 2:
        break

    if i == 0:
        slice1 = numbers_list[:middle_index]
        if sum(slice1) == sum(numbers_list[middle_index:]):
            answer.append(i)
            answer.append(middle_index)
            break
    else:
        slice1 = numbers_list[i:middle_index+i]
        slice2 = numbers_list[:i]
        slice3 = numbers_list[middle_index+i:]
        if (sum(slice2) + sum(slice3)) == sum(slice1):
            answer.append(i+1)
            answer.append(middle_index+i)
            break

print(answer if answer else "0 0")
