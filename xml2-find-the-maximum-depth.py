def rec(elem, level):
    # print('Elem: {}, Level: {}, Children: {}'.format(elem.tag, level, bool(elem)))
    if not elem:
        return level
    else:
        return max([rec(c, level+1) for c in elem])

maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth = rec(elem, 0)
