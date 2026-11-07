class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      string1counter = Counter(s)
      string2counter = Counter(t)

      return string1counter == string2counter