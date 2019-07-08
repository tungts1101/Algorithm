# Steinhaus - Johnson - Trotter
import sys
import random as rd
import time

class SteinhausJohnsonTrotter:
    def __init__(self,nums):
        self.nums = rd.sample([_ for _ in range(100)], nums)
        self.nums.sort()

        # RIGHT_TO_LEFT = True
        # LEFT_TO_RIGHT = False

        self.dirs = [True] * len(self.nums)
        self.perms = [self.nums]

    def largestMobile(self):
        _max = -sys.maxsize

        for i in range(len(self.nums)):
            if self.dirs[i] and i != 0:
                if self.nums[i] > self.nums[i-1] and self.nums[i] > _max:
                    _max = self.nums[i]
            if (not self.dirs[i]) and i != len(self.nums) - 1:
                if self.nums[i] > self.nums[i+1] and self.nums[i] > _max:
                    _max = self.nums[i]

        return _max

    def find_pos(self,lm):
        if lm == -sys.maxsize:
            return -1
        else:
            return self.nums.index(lm)
    
    def toggleDirections(self,num):
        for i in range(len(self.nums)):
            if self.nums[i] > num:
                self.dirs[i] = not self.dirs[i]

    def loop(self):
        lm = self.largestMobile()
        pos = self.find_pos(lm)

        while pos != -1:
            if self.dirs[pos]:
                self.nums[pos],self.nums[pos-1] = self.nums[pos-1],self.nums[pos]
                self.dirs[pos],self.dirs[pos-1] = self.dirs[pos-1],self.dirs[pos]
            else:
                self.nums[pos],self.nums[pos+1] = self.nums[pos+1],self.nums[pos]
                self.dirs[pos],self.dirs[pos+1] = self.dirs[pos+1],self.dirs[pos]
            
            self.perms.append(self.nums)
            self.toggleDirections(lm)
            
            lm = self.largestMobile()
            pos = self.find_pos(lm)

if __name__=='__main__':
    sjt = SteinhausJohnsonTrotter(7)
    sjt.loop()
    print(len(sjt.perms))
