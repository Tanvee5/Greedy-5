# Problem 2 : Campus Bikes
# Time Complexity : O(n*m) where n is the number of workers and m is the number of bikes
# Space Complexity : O(n*m) where n is the number of workers and m is the number of bikes
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
from typing import List
from collections import defaultdict
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # get the length of the workers and bikes array
        n = len(workers)
        m = len(bikes)
        # define distMap dictionary where distance as key and pair of worker and bike as value
        distMap = defaultdict(list)
        # define minDist and maxDist and set to inf and -inf respectively
        minDist = float('inf')
        maxDist = float('-inf')
        
        # loop through workers and bike arrays
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                # get the distance for the wth worker and bth bike and store the value in dist value
                dist = self.calculateDist(w, b)
                # get the minimum value between minDist and dist and store it
                minDist = min(minDist, dist)
                # get the maximum value between maxDist and dist and store it
                maxDist = max(maxDist, dist)
                # append the pair of worker and bike to the distance key in the map
                distMap[dist].append((i, j))

        # define the assigned array with the length of the workers and set to False       
        assigned = [False] * n
        # define the occupied array with the length of the bikes and set to False
        occupied = [False] * m
        # define result array with length of n and set to 0
        result = [0] * n
        # define count variable to 0
        count = 0
        
        # loop from minDist to maxDist
        for dist in range(minDist, maxDist+1):
            # check if the count is greater than n then break
            if count >= n:
                break
            # check if the dist is in the map then loop through the list of pairs of worker and bike
            if dist in distMap:
                for w, b in distMap[dist]:
                    # check if the the values of wth worker in assigned and bth bike in occupied
                    if not assigned[w] and not occupied[b]:
                        # if the value is False for the array then set the values as True
                        assigned[w]  = True
                        occupied[b] = True
                        # Add the bth bike at wth position in the result
                        result[w] = b
                        # increment the count value
                        count += 1
        # return result
        return result
    # calculate the manhattan distance for the worker and bike
    def calculateDist(self, worker, bike):
        # return the manhattan distance between the worker and bike
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
