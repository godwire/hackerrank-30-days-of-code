T = int(input())

for _ in range(T):
    text = input()
    
    even_chars = text[::2]
    odd_chars = text[1::2]
    
    print(even_chars, odd_chars)
