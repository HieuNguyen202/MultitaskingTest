import numpy
import time
from Multitasking import *
from Timer import *
"if you want to change the matrix size, go to getMatrix() function"
def main():
    regular(getMatrix()) 
    multiTask("thread",getMatrix(),1)
    multiTask("thread",getMatrix(),2)
    multiTask("thread",getMatrix(),4)
    multiTask("thread",getMatrix(),8)
    multiTask("thread",getMatrix(),16)
    multiTask("process",getMatrix(),1)
    multiTask("process",getMatrix(),2)
    multiTask("process",getMatrix(),4)
    multiTask("process",getMatrix(),8)
    multiTask("process",getMatrix(),16)
def getMatrix():
    w, h=5000,5000
    intMatrix=numpy.arange(w*h).reshape(w, h)
    floatMattrix=intMatrix.astype(float)
    return intMatrix
def regular(inputMatrix):
    "call method double as a function calling"
    print()
    print("Started double as a regular function call.")
    then=time.time()
    double(inputMatrix)
    now=time.time()
    timeelapse=now-then
    print("Regular time elapse: ","%.20f" % timeelapse, " seconds")
    print(inputMatrix)
def multiTask(type,inputMatrix,numTasks):
    "call method double as a multithreading or a multiprocessing process"
    print() #For visual aid
    print("Started ",numTasks," multi"+str(type)+"ing.")
    timer=Timer()
    timer.reset()
    matrices=slice(inputMatrix,numTasks) #slices a big matrix into smaller equal width pieces
    tasks=list() #could be a list of processes or threads
    taskNum=1
    if type=="process":
        for matrix in matrices:
           tasks.append(DoubleProcess("Process"+str(taskNum),matrix))
           taskNum=taskNum+1
    elif type=="thread":
        for matrix in matrices:
           tasks.append(DoubleThread("Thread"+str(taskNum),matrix))
           taskNum=taskNum+1
    for t in tasks: #start all process/thread
        t.start()
    for t in tasks: #wait until each process/thread is done
        t.join()
    print(numTasks," multi"+str(type)+"ing", "processed the whole work in","%.20f" % timer.getTime(), "seconds")
def slice(wholeMatrix,numSlices):
    'Slice a wholeMatrix into several pieces'
    matrices=list()
    for i in range(numSlices):
        length=int(len(wholeMatrix)/numSlices) #length of a sliced matrix
        width=len(wholeMatrix[0])
        matrixRange=numpy.ix_(range(i*length,(i+1)*length), range(0,width))
        matrices.append(wholeMatrix[matrixRange])
    return matrices

def double(inputMatrix):
    'double the value of each element in the inputMatrix, one by one.'
    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i])):
            inputMatrix[i,j]=inputMatrix[i,j]*2

if __name__ == '__main__':
    main()