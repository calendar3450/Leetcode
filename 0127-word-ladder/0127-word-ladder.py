from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        all_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] +'*' + word[i+1:]
                all_dict[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            current_word, level = q.popleft()
            for i in range(L):
                pattern = current_word[:i] + '*' +current_word[i+1:]
                for word in all_dict[pattern]:
                    if word==endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        q.append((word, level+1))
                all_dict[pattern] = []
                
        return 0