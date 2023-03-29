#Given a composition with different kinds of words,
# return a list of the top K most frequent words in the composition.

#the composition is not null and is not guaranteed to be sorted
# K >= 1 and K could be larger than the number of distinct words in the composition, in this case,
# just return all the distinct words
import heapq
from collections import Counter
class Solution(object):
    def topKFrequent(self,comb,k):
        '''
        :param comb string[]:
        :param k int:
        :return string[]:
        '''
        tmp_dic = {}
        for x in comb:
            tmp_dic[x] = tmp_dic.get(x,0) + 1
        tmp_h = []
        heapq.heapify(tmp_h)
        for key, val in tmp_dic.items():
            if len(tmp_h) <k:
                heapq.heappush(tmp_h,(val,key))
            elif tmp_h[0][0] < val:
                heapq.heappop(tmp_h)
                heapq.heappush(tmp_h, (val, key))
            else:
                continue
        sorted_h = sorted(tmp_h, key=lambda x: x[0], reverse=True)
        return  [sorted_h[i][1] for i in range(len(sorted_h))]


#time complexitt O(n + nlogn)
#space complexity O(n)

    def topKFrequent2(self,comb,k):
        '''
        :param comb string[]:
        :param k int:
        :return string[]:
        '''
        tmp_dic = {}
        for x in comb:
            tmp_dic[x] = tmp_dic.get(x, 0) + 1
        return sorted(tmp_dic.keys(), key=lambda w: tmp_dic[w], reverse = True)[:k]

    def topKFrequent3(self,comb,k):
        '''
        :param comb string[]:
        :param k int:
        :return string[]:
        '''
        c = Counter(comb)
        return sorted(c.keys(), key = lambda x : c[x], reverse = True)[:k]

#time complexitt O(n + nlogn)
#space complexity O(n)
#test
list1 = ['a','b','e','f','a','v','e','d']
list2 = ['a','b','a','a']
print(Solution().topKFrequent(list1,3))
print(Solution().topKFrequent2(list1,3))
print(Solution().topKFrequent3(list1,3))

print(Solution().topKFrequent(list2,3))
print(Solution().topKFrequent2(list2,3))
print(Solution().topKFrequent3(list2,3))



