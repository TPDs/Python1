import sys

def main(name):
    print("hej " + name)
    a = "vi tester nu"
    b = len(a)
    print(a)
    print(b)
    a = a + " og nu stopper vi"
    print(a)
    print(f'{b} +{a}')

main(sys.argv[1])
