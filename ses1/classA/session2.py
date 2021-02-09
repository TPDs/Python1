import sys

def main():

    a = ['Hans', 'Michael', 'Anna']
    print(a)
    b = [a, 'elsker mig']
    print(b)
    print(a[2])
    s = 'He'
    print(s)
    print(len(s))
    print(a[len(s)])
    print(id(a))

    c = a+b
    print(c)
    for i in a:
        print(i)
    print('Hans' in a)
    a.append('Morten')
    print(a)
main()