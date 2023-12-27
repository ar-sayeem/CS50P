import sys
from saying import hello
# 'saying' is our self creat library
# import 'hello' function from saying library
if len(sys.argv) == 2:
    hello(sys.argv[1])
    

from saying import goodbye
if len(sys.argv) == 2:
    goodbye(sys.argv[1])
# import 'goodbye' function from saying library