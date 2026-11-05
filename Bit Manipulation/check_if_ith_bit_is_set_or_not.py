n = 13 
i = 2

# check if ith bit is set or not using lift shift

if ( n & ( 1 << i )) != 0:
    print("Yes! ith bit is set")
else:
    print("No! ith bit is not set")