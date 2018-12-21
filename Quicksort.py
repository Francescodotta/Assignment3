class Quicksort_2(object):
    def __init__(self):
        self.mylist = []
        self.size = 0

    def add(self, value):
        self.mylist.append(value)
        self.size += 1

    def quick_sort(self):
        if len(self.mylist) > 1:
            x = self.mylist[0]
            self.left = Quicksort_2()
            self.right = Quicksort_2()

            for i in range(1, len(self.mylist)):
                if (self.mylist[i] < x):
                    self.left.add(self.mylist[i])
                else:
                    self.right.add(self.mylist[i])

            return self.left.quick_sort() + [x] + self.right.quick_sort()

        else:
            return self.mylist

    def get_min(self):
        new = self.quick_sort()
        return new[0]

    def get_max(self):
        new = self.quick_sort()
        leng = self.size - 1
        return new[leng]

    def get_list(self):
        return self.mylist


c = Quicksort_2()
c.add(5)
c.add(2)
c.add(4)
print(c.get_max())
print(c.get_min())
print(c.quick_sort())
print(c.mylist)

import matplotlib.pyplot as plt
import random

for r in range(100):
    num = random.randint(0,1000)
    c.add(num)
    my_min = c.get_min()
    my_max = c.get_max()

import time
def measure_time(a,rounds):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for r in range(rounds):

        num = random.randint(0, 100)
        start = time.time()
        my_add = a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        my_min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        my_max = a.get_max()
        tot_time_max += (time.time() - start)

    tot_time_add /= rounds
    tot_time_min /= rounds      ### doing the average by dividing by the number of rounds. so that we can the time needed for 1 round
    tot_time_max /= rounds

    return tot_time_add, tot_time_min, tot_time_max

for rounds in range(100,500,100):
    print(rounds, measure_time(c,rounds))

values_add, values_min, values_max = [], [], []
for rounds in range(100,500,100):
    a= Quicksort_2()
    my_add, my_min, my_max = measure_time(a, rounds)
    values_add.append(my_add * 1000)
    values_min.append(my_min * 1000)
    values_max.append(my_max * 1000)


xlabels = range(100,500,100)

plt.plot(xlabels, values_add, label='Add')
plt.legend()
plt.plot(xlabels, values_min, label='Get Min')
plt.legend()
plt.plot(xlabels, values_max, label='Get Max')
plt.legend()
plt.xlabel("Number of Operations")
plt.ylabel("Execution time (msec)")
plt.title("Performance of QuickSort Solution")
plt.show()
