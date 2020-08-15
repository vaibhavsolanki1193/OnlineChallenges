n = int(input().strip())

numbers = str(bin(n)[2:]).split('0')
length = [len(num) for num in numbers]
print(max(length))