import sys

av = int(sys.argv[1])

def even(av):
    if (av > 0):
        return True
    else:
        return False

def odd(av):
    if (av > 0):
        return True
    else:
        return False

def classify_nbr(av):
    iseven = None
    isodd = None
    if (av == 0):
        print("zero")
    else:
        if (av % 2 == 0):
            iseven = even(av)
        else:
            isodd = odd(av)
        if (iseven == True):
            print("Positive and even")
        elif (iseven == False):
            print("Negative and even")
        if (isodd == True):
            print("Positive and odd")
        elif (isodd == False):
            print("Negative and odd")

if __name__ == '__main__':
    classify_nbr(av)