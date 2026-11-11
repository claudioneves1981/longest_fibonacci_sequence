def lenLongestFibSubseq(arr):
    dp, s = {}, set(arr)
    ans = 0
    for c in arr:
        for b in arr:
            if b >= c: break
            a = c - b
            if a < b and a in s:
                n = dp.get((a, b), 2) + 1
                dp[b, c] = n
                ans = max(ans, n)
    return ans

arr = [1,2,3,4,5,6,7]
print(lenLongestFibSubseq(arr))