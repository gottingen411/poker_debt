import pandas as pd
def poker_calc(l, w):
    assert sum(list(l.values())) == sum(list(w.values())), "counting error. Please recount chips dumbass"
    l = dict(sorted(l.items(), key=lambda item: item[1], reverse=True))
    w = dict(sorted(w.items(), key=lambda item: item[1], reverse=True))
    nl = len(l)
    nw = len(w)
    p = [[0 for i in range(nw) ] for j in range(nl)]
    l_vals = list(l.values())
    w_vals = list(w.values())
    print(l)
    print(w)
    for i in range(nl):
        for j in range(nw):
            if l_vals[i] > w_vals[j]:
                p[i][j] = w_vals[j]
                l_vals[i] = l_vals[i] - w_vals[j]
                w_vals[j] = 0
            elif l_vals[i] < w_vals[j]:
                p[i][j] = l_vals[i]
                w_vals[j] = w_vals[j] - l_vals[i]
                l_vals[i] = 0
            else: 
                p[i][j] = l_vals[i]
                l_vals[i] = 0
                w_vals[j] = 0
    return pd.DataFrame(p, columns=list(w.keys()), index=list(l.keys()))


