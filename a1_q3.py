t=int(input('How many numbers you want to check '))
if t>=1 and t<=10000:
    for i in range(t):
        n=int(input('Enter the numbers '))
        count=0
        i=1
        while(i<=n):
            if(n%i==0):
                count=count+1
            i=i+1
        if(count==2):
            print('Prime')
        else:
            print('Not Prime')
else:
    print('Please enter a valid number')
