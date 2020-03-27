from decimal import *
import math
"""
calculate pi with n decimals with Chudnovsky algorithm

"""
def main():
    getcontext().rounding = ROUND_FLOOR
    while True:
        try:
            decimal_counter=int(input("Please enter count of Deicimals you prefer:"))
        except ValueError:
            print("please provide an integer")
        else:
            break
    pi=calculate_pi(decimal_counter)
    print(Decimal(pi))


def calculate_pi(counter):
    getcontext().prec = counter
    c=Decimal(426880*math.sqrt(10005))
    l=13591409
    x=1
    m=1
    k=6
    s=13591409
    for k in range(1,70):
        l+=545140134
        x*=-1*(640320**3)
        m*=k**3-16*k // (k+1)**3
        s+=(Decimal((m*l))/Decimal(x))
        k+=12
    return Decimal(c/s)


if __name__ == '__main__':
    print("this program calculate pi with n decimals")
    main()
