user_input = int(input("整数を入力してください: "))
prime_numbers = []

for i in range(2, user_input + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)

print(prime_numbers)
