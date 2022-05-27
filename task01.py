error = 'Please enter only integers up to 10k'
while True:
    try:
        a = int(input())
        b = int(input())
        n = int(input())
        if a > 10000 or b > 10000 or n > 10000:
            print(error)
            continue
        elif a < 0 or b < 0 or n < 0:
            print(error)
            continue
        break
    except:
        print(error)
        continue

min_1st_students = a // n
min_2nd_students = b // n

if min_1st_students <= min_2nd_students:
    print ('NO')
else:
    print('YES')