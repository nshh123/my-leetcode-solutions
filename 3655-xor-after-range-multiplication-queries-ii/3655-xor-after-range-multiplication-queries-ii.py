class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = 180 
        total_mult = [1] * n
        lazy = {}
        inv = {}
        for l, r, k, v in queries:
            if v == 1:
                continue
            if k > B:
                for i in range(l, r + 1, k):
                    total_mult[i] = (total_mult[i] * v) % MOD
            else:
                if k not in lazy:
                    lazy[k] = [1] * n
                if v not in inv:
                    inv[v] = pow(v, MOD - 2, MOD)
                
                lazy[k][l] = (lazy[k][l] * v) % MOD
                end_idx = l + ((r - l) // k + 1) * k
                if end_idx < n:
                    lazy[k][end_idx] = (lazy[k][end_idx] * inv[v]) % MOD
                    
        for k, curr_lazy in lazy.items():
            for i in range(n - k):
                if curr_lazy[i] != 1:
                    curr_lazy[i + k] = (curr_lazy[i + k] * curr_lazy[i]) % MOD
            for i in range(n):
                if curr_lazy[i] != 1:
                    total_mult[i] = (total_mult[i] * curr_lazy[i]) % MOD           
        res = 0
        for i in range(n):
            if total_mult[i] != 1:
                res ^= (nums[i] * total_mult[i]) % MOD
            else:
                res ^= nums[i]      
        return res