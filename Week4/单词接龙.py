import collections
import string
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        def addWord(word):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp
        wordId = {}
        edge = defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1

            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)
        return 0

# 另一个思路：
class Solution1(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

# 3.
class Solution2:
    def ladderLength(self, beginWord, endWord, wordList):
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps

                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        wordList.append(beginWord)
        d = construct_dict(wordList)
        return bfs_words(beginWord, endWord, d)


class Solution3:
    def ladderLength(self, beginWord, endWord, wordList):
        word_dict = set(wordList)
        if endWord not in word_dict:
            return 0
        forward = {beginWord}
        backward = {endWord}
        layer = 2
        len_word = len(beginWord)
        letters = string.ascii_lowercase
        while forward:
            word_dict -= forward
            temp_forward = set() # 存储转换后在字典中有对应的词的set()

            for word in forward:
                for i in range(len_word):
                    x, y = word[:i], word[i+1:]
                    for letter in letters:
                        temp_word = x + letter + y
                        if temp_word in backward:
                            return layer
                        if temp_word in word_dict: # 如果转换的词在字典中
                            temp_forward.add(temp_word)
            layer += 1

            if len(temp_forward) < len(backward):
                # 如果temp_forward 为 空时
                forward = temp_forward
            else:
                # 不为空时，将backward 作为开始， temp_forward作为结尾
                forward, backward = backward, temp_forward
        return 0


class Solution4:
    def ladderLength(self, beginWord, endWord, wordList):
        def addWord(word):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        def addEdge(word):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = ''.join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp
        wordId = dict()
        edge = defaultdict(list)
        nodeNum = 0
        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        disBegin = [float("inf")] * nodeNum
        beginId = wordId[beginWord]
        disBegin[beginId] = 0
        queBegin = deque([beginId])

        disEnd = [float("inf")] * nodeNum
        endId = wordId[endWord]
        disEnd[endId] = 0
        queEnd = deque([endId])

        while queBegin or queEnd:
            queBeginSize = len(queBegin)
            for _ in range(queBeginSize):
                nodeBegin = queBegin.popleft()
                if disEnd[nodeBegin] != float("inf"):
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == float("inf"):
                        disBegin[it] = disBegin[nodeBegin] + 1
                        queBegin.append(it)

            queEndSize = len(queEnd)
            for _ in range(queEndSize):
                nodeEnd = queEnd.popleft()
                if disBegin[nodeEnd] != float("inf"):
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
                for it in edge[nodeEnd]:
                    if disEnd[it] == float("inf"):
                        disEnd[it] = disEnd[nodeEnd] + 1
                        queEnd.append(it)
        return 0
