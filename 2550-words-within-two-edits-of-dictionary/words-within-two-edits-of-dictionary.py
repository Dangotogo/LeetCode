class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        result = []
        for q in queries:
            for d in dictionary:
                diff_count = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        diff_count += 1
                        if diff_count > 2:
                            break
                if diff_count <= 2:
                    result.append(q)
                    break
                    
        return result