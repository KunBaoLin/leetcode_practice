"""
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)> len(magazine):
            return False
        
        magazine_counts = collections.Counter(magazine)
        ransomNote_counts = collections.Counter(ransomNote)
        
        for char, count in ransomNote_counts.items():
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False
        return True
            