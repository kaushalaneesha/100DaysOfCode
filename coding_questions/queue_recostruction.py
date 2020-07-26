"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
from typing import List


def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    result = [None] * len(people)
    people.sort(key=lambda x: (x[0], x[1]))
    for p in people:
        k, i = 0, 0
        while i < len(people) and k < p[1]:
            if result[i] is None or result[i][0] >= p[0]:
                k += 1
            i += 1
        while result[i] is not None:
            i += 1
        result[i] = p
    return result


print(reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
