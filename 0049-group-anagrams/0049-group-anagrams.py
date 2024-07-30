class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list) #hashmap

        for i in strs:
            count = [0] * 26

            for letter in i :
                count[ord(letter)-ord('a')] += 1

            d[tuple(count)].append(i)
        
        return d.values()