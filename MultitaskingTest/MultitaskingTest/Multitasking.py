import threading
import multiprocessing
from Timer import *
class DoubleThread (threading.Thread):
    "Call the double function as a multithreading process"
    def __init__(self, name, matrix):
        threading.Thread.__init__(self)
        self.name = name
        self.matrix = matrix
    def run(self):
        timer=Timer()
        timer.reset()
        self.double()
        #print("       ",self.name, "processed its work in","%.20f" % timer.getTime(), "seconds")
        #print(self.matrix) #uncomment this if you want to see the result matrix
    def double(self):
        'double the value of each element in the matrix, one by one.'
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i,j]=self.matrix[i,j]*2

class DoubleProcess (multiprocessing.Process):
    "Call the double function as a multiprocessing process"
    def __init__(self, name, matrix):
        multiprocessing.Process.__init__(self)
        self.name = name
        self.matrix = matrix
    def run(self):
        timer=Timer()
        timer.reset()
        self.double()      
        print("       ",self.name, "processed its work in","%.20f" % timer.getTime(), "seconds")
        #print(self.matrix) #uncomment this if you want to see the result matrix
    def double(self): 
        'double the value of each element in the matrix, one by one.'
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i,j]=self.matrix[i,j]*2
