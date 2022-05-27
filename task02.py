a = 1
b = 1
c = 1
eq1 = input()
eq2 = input()
eq3 = input()

def uppering(n):
    n =+ 1

def check(mark, n1, n2):
    if mark == '=':
        n1 = n2
    if mark == '>':
        while n1 <= n2:
            uppering(n1)
    elif mark == '<':
        while n2 <= n1:
            uppering(n2)

check(eq1, a, b)
check(eq2, a, c)
check(eq3, b, c)

print(a, b, c)