def lcs(s1, s2):
    s1=''.join(set(s1))
    s2=''.join(set(s2))
    result=0
    for c in s1:
        if c in s2:
            result+=1
    return result
print(lcs('AGGTAB', 'GXTXAYB'))
