# Last updated: 1/12/2026, 3:13:11 PM
class Solution(object):
    def countOfSubstrings(self, word, k):
        vowels = set("aeiou")
        from collections import defaultdict

        ret = 0
        vowel_freq = defaultdict(int)
        num_consonants = 0
        distinct_vowels = 0

        l = 0
        for r in range(len(word)):
            ch = word[r]
            if ch in vowels:
                vowel_freq[ch] += 1
                if vowel_freq[ch] == 1:
                    distinct_vowels += 1
            else:
                num_consonants += 1

            # Shrink window if too many consonants
            while num_consonants > k:
                ch_l = word[l]
                if ch_l in vowels:
                    vowel_freq[ch_l] -= 1
                    if vowel_freq[ch_l] == 0:
                        distinct_vowels -= 1
                else:
                    num_consonants -= 1
                l += 1

            # If window has all vowels and exactly k consonants
            if distinct_vowels == 5 and num_consonants == k:
                # We can extend `l` rightward as long as same result holds
                temp_l = l
                while temp_l <= r and word[temp_l] in vowels and vowel_freq[word[temp_l]] > 1:
                    ret += 1
                    vowel_freq[word[temp_l]] -= 1
                    temp_l += 1

                # Count the first valid one
                ret += 1

                # Restore frequencies
                for i in range(l, temp_l):
                    vowel_freq[word[i]] += 1

        return ret
