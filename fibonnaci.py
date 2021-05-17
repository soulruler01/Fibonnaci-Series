#Python program to generate Fibonnaci Series until 'n' value
n = int(input("Enter the value of n: "))

#Taking first two values as 0 and 1
a = 0
b = 1
sum = 0
count = 1
print("Fibonnaci Series: ", end = " ")
#Using while Loop
while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a + b
