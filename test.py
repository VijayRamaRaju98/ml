

# def solution(s:str, t:str):
#     if len(s) != len(t):
#         return False
#     else:
#         hashmaps = {}
#         hashmapt = {}
#         for i in range(len(s)):
#             hashmaps[s[i]] = 1+hashmaps.get(s[i],0)
#             hashmapt[t[i]] = 1+hashmapt.get(t[i],0)
#         if hashmaps == hashmapt:
#             return True
#         else:
#             return False
        
# print(solution('ant', 'tnx'))



class Solution:
    def isanagram(self, s:str,t:str):
        if len(s) != len(t):
            return False
        
        char_map = [0] * 26

        for i in range(len(s)):
            char_map[ord(s[i]) - ord('a')] += 1
            char_map[ord(t[i]) - ord('a')] -= 1
            

        return all(count == 0 for count in char_map)
    
sol = Solution()
print(sol.isanagram('anagram','nagaram'))