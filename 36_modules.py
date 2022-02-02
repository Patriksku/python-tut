# module =  a file containing python code. May contain functions, classes, etc.
# Used with modular programming, which is to seperate a program into parts.

# import messages
# import messages as m
# from messages import hello, bye
# from message import * (this one is dangerous)  // Naming conflicts, hard to navigate through the module etc.

import messages as m
from messages import hello, bye
# from messages import *

m.hello()
m.bye()

hello()
bye()

help("modules")










