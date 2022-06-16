from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        prefix = ""
        for i in range(len(min(strs))):
            word = strs[0][i]
            if all(a[i] == word for a in strs):
                prefix += word
            else:
                break

        return prefix"""
        prefix = ""
        for i, string in enumerate(strs):
            print(prefix)
            new_prefix = ""
            if i == 0:
                prefix = string
            else:
                temp_prefix = ""
                for word in string:
                    temp_prefix += word
                    if prefix.startswith(temp_prefix):
                        new_prefix = temp_prefix
                prefix = new_prefix

        return prefix


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["dog","racecar","car"]))