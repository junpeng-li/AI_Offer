def lengthstr(s:str) ->int:
    if not s:
        return 0
    lookup = []
    for i in range(len(s)):
        if s[i] in lookup:
            lookup.remove(s[i])
        lookup.append(s[i])
    print(lookup)
    return len(lookup)
