from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        wordLeng = len(beginWord)

        if endWord not in wordList:
            return 0

        checkList = [False] * n  # wordList 인덱스 방문 여부

        # (현재 단어, 현재 단계 수)
        q = deque()
        q.append((beginWord, 1))

        while q:
            curWord, curCnt = q.popleft()

            if curWord == endWord:
                return curCnt

            # 현재 단어에서 한 글자 차이인 모든 단어를 다음 레벨로
            for i in range(n):
                if checkList[i]:
                    continue

                compareWord = wordList[i]

                # 한 글자 차이인지 체크 (JK님 방식 유지)
                sameCnt = 0
                for j in range(wordLeng):
                    if compareWord[j] == curWord[j]:
                        sameCnt += 1

                if sameCnt == wordLeng - 1:
                    checkList[i] = True         # ✅ 큐에 넣는 순간 방문 처리(되돌리지 않음)
                    q.append((compareWord, curCnt + 1))

        return 0