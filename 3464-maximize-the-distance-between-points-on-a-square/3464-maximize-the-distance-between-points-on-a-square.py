class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        P = []
        for x, y in points:
            if x == 0:
                P.append(y)
            elif y == side:
                P.append(side + x)
            elif x == side:
                P.append(3 * side - y)
            else:
                P.append(4 * side - x)
                
        P.sort()
        N = len(P)
        P_double = P + [p + 4 * side for p in P]
        
        limit = 2 * N
        target = 4 * side
        
        def check(d: int) -> bool:
            nxt = [limit] * limit
            j = 0
            for i in range(limit):
                while j < limit and P_double[j] - P_double[i] < d:
                    j += 1
                nxt[i] = j
                
            max_dist = target - d
            for i in range(N):
                curr = i
                for _ in range(k - 1):
                    curr = nxt[curr]
                    if curr == limit:
                        break
                if curr != limit and P_double[curr] - P_double[i] <= max_dist:
                    return True
            return False

        low, high = 1, side
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans