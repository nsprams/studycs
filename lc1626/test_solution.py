import solution
import unittest
from typing import List


class Input:
    def __init__(self,scores: List[int], ages:List[int], highscore:int):
        self.scores = scores
        self.ages = ages
        self.highscore = highscore

    def score(self):
        return self.highscore

class SolutionTestCase(unittest.TestCase):
    def testcase_two(self):
        testcases = [
        ([1,3,5,10,15], [1,2,3,4,5], 34),
        ([4,5,6,5], [2,1,2,1], 16),
        ([1,2,3,4], [8,9,10,1], 6),
        ]
        for scores,ages,highscore in testcases:
            input = Input(scores,ages,highscore)
            self.obj = solution.Solution()
            self.result = self.obj.bestTeamScore(input.scores,input.ages)
            self.assertEqual(input.score(), self.result)

if __name__ == '__main__':
    unittest.main()