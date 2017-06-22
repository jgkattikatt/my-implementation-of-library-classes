#MATHS OPERATIONS 
#jgkattikatt@gmail.com

import random
import numpy as np

num_list = [random.randrange(start=1, stop=10) for tmp in range(6)]

class MyMathLib:
    '''match function implementations
       mean, median, standard deviation, variance
    '''
    def __init__(self, list_to_process=[]):
        self.list_to_process = list_to_process
        self.list_size = len(self.list_to_process)
        self.mean = 0
        self.median = 0
        self.sd = 0
        self.variance = 0
        self.calculate()

    def find_mean(self):
        '''
        Find mean of a data set
        '''
        sum = 0.0
        for val in self.list_to_process:
            sum += val

        self.mean = sum / self.list_size        

    def find_median(self):
        '''
        Find median of a data set
        '''
        if self.list_size % 2 != 0:
            self.median = self.list_to_process[self.list_size/2]
        else: 
            self.median = (self.list_to_process[self.list_size/2-1] + self.list_to_process[self.list_size/2]) / 2.0

    def find_sd(self):
        '''
        Find standard deviation of a data set
        '''
        self.sd = np.sqrt(sum([((val - self.median)**2) for val in self.list_to_process]) / self.list_size - 1) 
    
    def find_variance(self):
        '''
        Find variance of a data set
        '''
        self.variance = self.sd ** 2

    def calculate(self):
        '''
        Base method
        '''
        self.find_mean()
        self.find_median()
        self.find_sd()
        self.find_variance()
        


if __name__ == '__main__':
    mymath = MyMathLib(num_list)
    print "-" * 40
    print "samples  : " + str(num_list)
    print "-" * 40
    print "mean     : " + str(mymath.mean)
    print "median   : " + str(mymath.median)
    print "sd       : " + str(mymath.sd)
    print "num sd   : " + str(np.std(num_list))
    print "variance : " + str(mymath.variance)
    print "-" * 40
