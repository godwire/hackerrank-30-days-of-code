n = int(input())
for _ in range(n):
    num = int(input())
    if num < 2:
        print("Not prime")
        continue
    if num == 2:
        print("Prime")
        continue
    if num % 2 == 0:
        print("Not prime")
        continue
    
    is_prime = True
    i = 3
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 2
    
    print("Prime" if is_prime else "Not prime")