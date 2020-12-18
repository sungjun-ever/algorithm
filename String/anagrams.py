import collections
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[str]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return anagrams.values()