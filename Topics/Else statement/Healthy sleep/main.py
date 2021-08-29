A = int(input())
B = int(input())
H = int(input())

if B >= H >= A:
    print('Normal')
elif A > H:
    print('Deficiency')
else:
    print('Excess')
