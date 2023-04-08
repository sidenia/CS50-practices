import sys
from saying import hello, goodbye

if len(sys.argv) == 2:
    my_name = sys.argv[1]
    hello(my_name)
    goodbye(my_name)
