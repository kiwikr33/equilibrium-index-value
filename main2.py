def eq_val(n):

    arr =[1]*n + [n] + [1]*n

    for i in range (len(arr)):

        left = 0
        right = 0

        for j in range (i):
            left += arr[j]

        for j in range (i+1, len(arr)):
            right += arr[j]

        if left == right:
            return arr [i]
    return -1
n = int (input("Enter n:"))

print("Equilibrium value", eq_val(n))