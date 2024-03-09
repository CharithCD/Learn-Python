# import sys

# print("hello, my name is", sys.argv[1])

# import sys

# if len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# elif len(sys.argv) < 2:
#     sys.exit("Not enough arguments")

# print("hello, my name is", sys.argv[1])


import sys

if len(sys.argv) < 2:
    sys.exit("Not enough arguments")

# for arg in [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]:
#     print("hello, my name is", arg)
    
# for arg in sys.argv:
#     print("hello, my name is", arg)

# for i in range(1, len(sys.argv)):
#     print("hello, my name is", sys.argv[i])
    
for arg in sys.argv[1:]:
    print("hello, my name is", arg)