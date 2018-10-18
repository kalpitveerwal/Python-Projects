import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--check_prime", type = int)
parser.add_argument("--range", nargs=2, type=int)
args = parser.parse_args()

e = "Error : Please enter a value between 1 and 1000 only"

def prime(val):
    if val >= 1  and val <= 1000 :
        if val == 1 :
            return False
        else :
            for x in range(2, val):
                if (val % x) == 0:
                    return False
                else:
                    continue
            return True
    else :
        return e

def total_prime(lower, upper):
    if (lower >= 1 and lower <= 1000) and (upper >= 1 and upper <= 1000) :
        i = 0
        for x in range(lower, upper+1):
            if prime(x) :
                i = i + 1
            else :
                continue
        return i
    else :
        return e

if args.check_prime == None and args.range == None :
    print ("Error : At least one of the following arguments are required: --check_prime, --range")
elif (not args.check_prime == None) and args.range == None :
    if prime(args.check_prime) == e :
        print (e)
    elif prime(args.check_prime) :
        print ("Yes")
    else :
        print ("No")
elif args.check_prime == None and (not args.range == None) :
    print (total_prime(args.range[0], args.range[1]))
else :
    if prime(args.check_prime) == e or total_prime(args.range[0], args.range[1]) == e :
        print (e)
    else :
        if prime(args.check_prime) :
            print ("Yes", total_prime(args.range[0], args.range[1]))
        else :
            print ("No", total_prime(args.range[0], args.range[1]))

