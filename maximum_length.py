def maximum_length(N, S, Q, X, Y):
    ans = []
    s = set()
    dif = set()
    mx = 0
    
    for i in range(len(S)):
        l = i
        r = i
        while i + 1 < len(S) and S[i] == S[i + 1]:
            i += 1
            r += 1
        s.add((l, r))
        dif.add((r - l + 1, l))
        mx = max(mx, r - l + 1)
    
    for i in range(Q):
        idx = X[i] - 1
        ch = Y[i]
        if S[idx] == ch:
            assert dif
            ans.append(max(dif)[0])
            continue
        assert s
        it = s.lower_bound((idx, -1))
        if it == s.end():
            assert it != s.begin()
            it -= 1
        elif it[0] > idx:
            assert it != s.begin()
            it -= 1
        l1 = it[0]
        r1 = it[1]
        assert (r1 - l1 + 1, l1) in dif
        dif.remove((r1 - l1 + 1, l1))
        s.remove(it)

        if l1 < idx:
            s.add((l1, idx - 1))
            dif.add((idx - 1 - l1 + 1, l1))
        if idx < r1:
            s.add((idx + 1, r1))
            dif.add((r1 - idx - 1 + 1, idx + 1))

        S[idx] = ch
        l = idx
        r = idx
        if idx + 1 < len(S) and S[idx] == S[idx + 1]:
            it = s.lower_bound((idx + 1, -1))
            assert it != s.end()
            r = it[1]
            assert (it[1] - it[0] + 1, it[0]) in dif
            dif.remove((it[1] - it[0] + 1, it[0]))
            s.remove(it)
        if idx - 1 >= 0 and S[idx] == S[idx - 1]:
            it = s.lower_bound((idx, -1))
            assert it != s.begin()
            it -= 1
            assert (it[1] - it[0] + 1, it[0]) in dif
            dif.remove((it[1] - it[0] + 1, it[0]))
            s.remove(it)
        s.add((l, r))
        dif.add((r - l + 1, l))
        ans.append(max(dif)[0])
    return ans

if __name__ == "__main__":
    t = int(input())
    sumn = 0
    sumq = 0
    assert 1 <= t <= 1e4
    
    for _ in range(t):
        N = int(input())
        assert 1 <= N <= 1e5
        S = input()
        assert all('a' <= i <= 'z' for i in S)
        Q = int(input())
        sumn += N
        sumq += Q
        assert 1 <= Q <= 1e5
        X = list(map(int, input().split()))
        assert all(1 <= xi <= N for xi in X)
        Y = list(input().strip())
        assert all('a' <= yi <= 'z' for yi in Y)
        ans = maximum_length(N, S, Q, X, Y)
        print(*ans)
    
    assert 1 <= sumn <= 1e5
    assert 1 <= sumq <= 1e5
