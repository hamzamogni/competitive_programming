'''
997. Find the Town Judge (leetcode)
------------------------
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''


class Solution:
    def findJudge(self, n: int, trust) -> int:
        trusting = set([person[0] for person in trust])

        suspected_judge = ((n*(n+1))//2) - sum(trusting)

        people_trusting_judge = set(
            person for person in trust if person[1] == suspected_judge)

        if len(people_trusting_judge) == n-1:
            return suspected_judge

        return -1
