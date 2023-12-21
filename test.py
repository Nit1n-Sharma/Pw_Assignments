t = int(input())        
#run a loop to accept 't' inputs
for i in range(t):      
    #accept 1 integer on the 1st line of each test case
    N = int(input())        
    #output the negative integer - i.e. (-N)
    if N > 0:
        print(-N)
    else:
        print(N)