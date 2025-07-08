class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start by assuming the entire first string is the prefix
        prefix = strs[0]

        for s in strs[1:]:
            # Shorten the prefix until it matches the beginning of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix