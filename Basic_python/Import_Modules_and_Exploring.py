#from My_module import *
import sys
import Slicing_python
print("The Second module name is {}".format(__name__))
#sys.path.append()
from My_module import find_index, test
courses = ['Math', 'Biology', 'Computer Science']

index = find_index(courses, 'Computer Science')

print(index)

print(test)

print(sys.path)