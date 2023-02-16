#!/usr/bin/env python3
""" 
Best Team with no conflicts: https://leetcode.com/problems/best-team-with-no-conflicts/description/
"""

from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        maxscore= [None] * len(scores)
        team_score=0
        #wrangling the lists to create a sorted tuple and converting them back to lists!
        xylist = list(zip(scores,ages))
        res = sorted(xylist, key=lambda x:x[1])
        scores, ages = map(list,zip(*res))
        print("Scores:{} \n Ages:{}".format(scores,ages))


        def isConflict(x, y):
            if scores[x] >= scores[y] and ages[x] < ages[y]:
                print("Conflict {},{} with scores {},{}".format(x,y,scores[x],scores[y]) )
                print("Aged {}, {}".format(ages[x],ages[y]))
                return True
        
        for x in range(0,len(scores)):
            team_score=scores[x]
            # for y in range(0,len(scores)):
            for y in range(0,x):
                 if x != y:
                    if not isConflict(x,y):
                        team_score = team_score + scores[y]
                        print("x:{} , y:{}, team_score:{}".format(x,y,team_score))

            maxscore[x] = team_score
            print("Max: {}".format(maxscore))
        return max(maxscore) 



if __name__ == '__main__':
    print("-Best Team with no conflicts problem-")