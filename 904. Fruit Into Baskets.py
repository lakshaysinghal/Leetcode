'''

'''
import itertools
class Solution:     
    def totalFruit(self, tree) -> int:
        queue = []
        i =0
        max_count = 0
        types={}
        while(i<len(tree)):
            if len(types)<2 or types.get(tree[i],0)>0:
                queue.append(tree[i])
                types[tree[i]]=1+types.get(tree[i],0)
            else:
                max_count=max(max_count,len(queue))
                types_list = list(types)
                toRemove = types_list[0] if types_list[0]!=tree[i-1] else types_list[1]
                while(toRemove in queue):
                    queue.pop(0)
                types = {tree[i-1]:len(queue),tree[i]:1}
                queue.append(tree[i])
            i+=1
        return max(max_count,len(queue))

print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))

