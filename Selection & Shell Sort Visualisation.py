from tkinter import *
import random
import time

root = Tk()

root.title('shell sort vs Selection sort by Fiky Anggara | 1303180015')
root.maxsize(800,600)
root.config(bg='black')

data1 = []
data2 = []
time_start = time.time()

def selection_sort(data,drawArr,canvas):
    global time_start
    time_start = time.time()

    for i in range(0, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            drawArr(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))], canvas)
            updateTime(timer2,time_start)
            j -= 1
        data[j+1] = key
    drawArr(data, ['green' for x in range(len(data))], canvas)
    
def shell_sort(data,drawArr,canvas):
    global time_start
    time_start = time.time()
    gap = len(data) // 2
    
    while gap > 0:
