def lenLongestFibSubseq(arr):
    dp, s = {}, set(arr)
    temp = 0
    ans = 0
    fib = set({1})
    for c in arr:
        for b in arr:
            if b >= c: break
            a = c - b
            if a < b and a in s:
                n = dp.get((a, b), 2) + 1
                if n > temp:
                    temp = n
                    fib.add(b)
                    fib.add(c)
                dp[b, c] = n
                ans = max(ans, n)
    return f"Longest Fib Sequence Quantity: {ans}", f"Sequence Encountred: {fib}"

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
print(arr)
print(lenLongestFibSubseq(arr))