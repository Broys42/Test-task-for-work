str1 = input()
str2 = input()

slice1, slice2, allAnswers = [],[],[]
takenSymbol = ""
flag = False


for index, i in enumerate(str1):
    if str1[index] != str2[index]:
        slice1 = str1[index:]
        slice2 = str2[index:]
        takenSymbol = str1[index]
        break

if slice1[1:] == slice2[:len(slice2) - 1] and slice1[0] == takenSymbol and slice2[len(slice2)-1]:
    flag = True
else:
    for index in range(len(slice1)):
        if (index + 1) != len(slice1):
            if slice2[index] != slice1[index+1] and slice2[index] == takenSymbol:
                if slice2[index+1:] == slice1[index+1:]:
                    flag = True

print("YES" if flag else "NO")
