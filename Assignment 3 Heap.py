import heapq
import matplotlib.pyplot as plt

class Heap(object):
    def __init__(self):
        self.min=[]
        self.max=[]

    def add(self, value):
       heapq.heappush(self.min, value)
       heapq.heappush(self.max, -value)
    def get_max(self):
        return -self.max[0]
    def get_min(self):
        return self.min[0]


b = Heap()

import random
for r in range(100):
    num = random.randint(0,1000)
    b.add(num)
    my_min = b.get_min()
    my_max = b.get_max()

import time


def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for num in this_list:
        start = time.time()
        a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.get_max()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max


if __name__ == '__main__':
    a = Heap()
    a.add(5)
    print(a.min, a.max, a.get_min(), a.get_max())
    a.add(7)
    print(a.min, a.max, a.get_min(), a.get_max())
    a.add(3)
    print(a.min, a.max, a.get_min(), a.get_max())
    a.add(9)
    print(a.min, a.max, a.get_min(), a.get_max())

    repetitions = 5
    max_operations = 20000
    step = 5000

    valuesheapadd, valuesheapmin, valuesheapmax = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 20000))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0

        for repetition in range(5):
           a = Heap()
           myadd, mymin, mymax = measure_time(a, this_list)
           tot_time_add += myadd
           tot_time_min += mymin
           tot_time_max += mymax

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        valuesheapadd.append(tot_time_add * 1000)
        valuesheapmin.append(tot_time_min * 1000)
        valuesheapmax.append(tot_time_max * 1000)



    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, valuesheapadd, label='Add')
    plt.plot(xlabels, valuesheapmin, label='Get Min')
    plt.plot(xlabels, valuesheapmax, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap Solution")
    plt.show()
