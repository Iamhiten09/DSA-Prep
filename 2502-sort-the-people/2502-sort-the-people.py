class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a1 = []
        for i in range(len(names)):
            a1.append([heights[i],names[i]])
        a1.sort(reverse = True)
        b1 = []
        for i in range(len(names)):
            b1.append(a1[i][1])
        return b1
