class UnionFind():
    def __init__(self,n):
        self.root =[i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self,x):
        if x!=self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x] 

    def union(self,x,y):
        root_x = self.find(x)
        root_y=self.find(y)
        if root_x==root_y: return
        if self.rank[root_x]<self.rank[root_y]:
            root_x,root_y = root_y,root_x
        self.root[root_y] = root_x
        if self.rank[root_x]==self.rank[root_y]:
            self.rank[root_x]+=1


class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        uf = UnionFind(n)
        sets = defaultdict(lambda:defaultdict(int)) #{root:{val:freq}}
        ans =0
        for x,y in allowedSwaps:
            root_x = uf.find(x)
            root_y = uf.find(y)
            uf.union(root_x,root_y)


        for i in range(n):
            root_i = uf.find(i)
            sets[root_i][source[i]] +=1

        for i in range(n):
            root_i = uf.find(i)
            if sets[root_i][target[i]]>0:
                sets[root_i][target[i]]-=1
            else:
                ans+=1

        return ans