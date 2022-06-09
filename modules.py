#A module is a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager(eg Django) as well as custom modules.

import datetime
import time

today = datetime.date.today()
timestamp= time.time()
print(today)
print(timestamp)
