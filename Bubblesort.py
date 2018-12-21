class Bubblesort_Min_Max(object):
    def __init__(self):
        self.content = []

    def bubble__sort(self):
        for passnum in range(len(self.content)-1,0,-1):
            for i in range(passnum):
                if self.content[i]>self.content[i+1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i+1]
                    self.content[i + 1] = temp
    def add(self,value):
        self.content.append(value)
        self.bubble__sort()

    def getmin(self):
        return self.content[0]
    def getmax(self):
        return self.content[-1]


m= Bubblesort_Min_Max()
m.add(2)
m.add(5)
m.add(4)
m.add(12)
print(m.getmax())
print(m.getmin())
print(m.bubble__sort())

import random
import matplotlib.pyplot as plt
for r in range(100):
    num = random.randint(0,1000)
    m.add(num)
    my_min = m.getmin()
    my_max = m.getmax()

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
        min = a.getmin()
        tot_time_min += (time.time() - start)

        start = time.time()
        max = a.getmax()
        tot_time_max += (time.time() - start)

    return tot_time_add, tot_time_min, tot_time_max

if __name__ == '__main__':
    m = Bubblesort_Min_Max()
    m.add(5)
    print(m.content, m.getmin(), m.getmax())
    m.add(7)
    print(m.content, m.getmin(), m.getmax())
    m.add(3)
    print(m.content, m.getmin(), m.getmax())
    m.add(9)
    print(m.content, m.getmin(), m.getmax())

    repetitions = 3
    max_operations = 500
    step= 100

    values_bubble, values_bubble_min, values_bubble_max = [], [], []
    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0, 500))

        tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
        for repetition in range(5):
            a = Bubblesort_Min_Max()
            my_add, my_min, my_max = measure_time(a, this_list)
            tot_time_add += my_add
            tot_time_min += my_min
            tot_time_max += my_max

        tot_time_add /= 5
        tot_time_min /= 5
        tot_time_max /= 5

        values_bubble.append(tot_time_add * 1000)
        values_bubble_min.append(tot_time_min * 1000)
        values_bubble_max.append(tot_time_max * 1000)

    xlabels = range(step, max_operations, step)
    plt.plot(xlabels, values_bubble, label='Add')
    plt.plot(xlabels, values_bubble_min, label='Get Min')
    plt.plot(xlabels, values_bubble_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of Operations")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of bubble's Solution")
    plt.show()
