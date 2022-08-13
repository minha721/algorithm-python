for _ in range(4):
    albx, alby, artx, arty, blbx, blby, brtx, brty = map(int, input().split())

    if artx < blbx or brtx < albx or alby > brty or arty < blby:
        print('d')
        continue
    elif albx == brtx or blbx == artx:
        if arty == blby or brty == alby:
            print('c')
            continue
        else:
            print('b')
            continue
    elif arty == blby or brty == alby:
            print('b')
            continue
    else:
        print('a')
        continue