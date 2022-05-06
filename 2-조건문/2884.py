H, M = map(int, input().split())

_M = M - 45

if _M < 0:
    _M = _M + 60
    if H==0:
        H = 23
    else:
        H = H - 1
print(H, _M)