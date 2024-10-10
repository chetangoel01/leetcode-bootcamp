class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_anagram = len(p)
        hash1 = hash(''.join(sorted(p)))
        returnArr = []
        len_string = len(s)
        for i in range(len_string - len_anagram + 1):
            substring = s[i:i+len_anagram]
            hash2 = hash(''.join(sorted(substring)))
            if hash1 == hash2:
                returnArr.append(i)
        return returnArr
