# coding=utf-8
# this code is to calculate the narcissistic number
i=100; r=0;s=0;t=0
while i<=1000:
    r=i//100  # get the hundreds digit
    s=(i-r*100)//10  # get the tens digit
    t=i-r*100-s*10    # get the ones digit
    if i==r**3+s**3+t**3:
        print(i)
    i+=1