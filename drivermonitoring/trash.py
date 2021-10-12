from main import *

run = videoOutput() # we instantiate the class


while(True):
    values = next(run.global_variables())
    print(values)