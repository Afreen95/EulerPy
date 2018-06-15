target = 20
num = 2520
answer_found = False
while(True):
    for i in range(1, target +1):
        if num % i != 0:
            break
        if i == target:
            answer_found = True
    if answer_found:
        break
    num += 20
print(num)    