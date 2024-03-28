import bisect


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
        it = bisect.bisect_left([x[0] for x in s], idx)
        if it == len(s):
            it -= 1
        elif s[it][0] > idx:
            if it > 0:
                it -= 1
        l1, r1 = s.pop(it)
        assert (r1 - l1 + 1, l1) in dif
        dif.remove((r1 - l1 + 1, l1))

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
            it = bisect.bisect_left([x[0] for x in s], idx + 1)
            r = s.pop(it)[1]
            assert (r - l + 1, l) in dif
            dif.remove((r - l + 1, l))
        if idx - 1 >= 0 and S[idx] == S[idx - 1]:
            it = bisect.bisect_left([x[0] for x in s], idx)
            if it == len(s):
                it -= 1
            elif s[it][0] > idx:
                if it > 0:
                    it -= 1
            l = s.pop(it)[0]
            assert (r - l + 1, l) in dif
            dif.remove((r - l + 1, l))
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

