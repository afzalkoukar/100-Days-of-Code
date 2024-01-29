def prime_checker(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    
    if(count==2):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a non prime number")


n = int(input("Check this number : \n"))

prime_checker(n)