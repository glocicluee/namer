def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var11 = func3(var7, arg2)
    var42 = func5(var11, arg1)
    var59 = func8(var42, arg2)
    var64 = func9(var59, arg2)
    var65 = var11 ^ (var42 + var7 - arg1 - var59) | -888 ^ ((1816346545 & (arg2 - (var7 + var11 - arg2 | (var11 - (-924 & (-266 | (var64 + arg2 + var64))))) | var42) - var64) + var11) - arg1
    result = var11 + ((var42 - -1581039691 | (var65 ^ var42)) + var7 & var11 - (-229 | var64) & var11) ^ var64 | var11
    return result
def func9(arg60, arg61):
    var62 = 0
    for var63 in range(28):
        var62 += var63 + var63 - var62
    return var62
def func8(arg43, arg44):
    var45 = 1564415009 ^ -769
    var46 = -318 ^ arg43 ^ (arg44 ^ 430)
    var47 = -843 ^ (-799 - var45) & -725
    var48 = var47 | 768 ^ var47
    if var47 < var46:
        var49 = 303327292 ^ 1770570105 & var46 + var46
    else:
        var49 = var46 ^ var45
    var50 = var47 & var47
    var51 = -1999224334 - (arg44 - var48) & var46
    var52 = var45 & var50 + var46
    var53 = (arg44 | 141042688 - arg43) + var45
    var54 = (var47 & var45) - var47 | var48
    var55 = arg44 ^ arg43
    var56 = arg44 | var55
    var57 = (var47 + -310 + arg43) + arg44
    var58 = (var50 - var45 + var53) & var51
    result = var51 - var50
    return result
def func7(arg14, arg15):
    var16 = (arg15 + (-422846236 - 1494073193)) & arg14
    if arg14 < arg15:
        var17 = ((arg14 + arg14) ^ var16) + -1540786074
    else:
        var17 = arg15 | (504 | arg15) ^ 765
    var18 = 1712759868 - -562 + var16 + -708582677
    if var18 < arg15:
        var19 = -236 + 134
    else:
        var19 = arg14 | var18
    var20 = arg15 + arg15
    var21 = ((arg14 - arg15) & var20) + var16
    var22 = var18 - var21 - arg15 + var18
    var23 = var20 ^ arg15 | var21 ^ var18
    var24 = var22 & var20
    var25 = var22 | var21 | var23 - var23
    var26 = (77 - var23) ^ arg14 + var23
    var27 = arg15 | -494 + var21 + var16
    var28 = -263 - var21
    var29 = (var27 & var16) & var25 ^ var25
    var30 = var27 + -255 + var24 | var21
    var31 = ((arg15 & var27) ^ var23) | -790
    var32 = var26 ^ var28 + var27
    var33 = var25 ^ 527728046
    var34 = var28 ^ var31
    var35 = var16 | var16
    var36 = var16 ^ var26 & arg14 + var18
    var37 = (var31 + var21 & var31) - var18
    if var37 < var25:
        var38 = -1023286618 + (var32 & var25)
    else:
        var38 = var31 | (var33 & var18) + var23
    var39 = var24 & var16 + var27
    var40 = var31 & (arg15 - var21 + var36)
    result = (var39 + var16 ^ (var31 - var18 - var32) + var34) & ((var37 - (var23 + var33)) & var23 & var21 & var25)
    return result
def func2(arg3, arg4):
    var5 = 0
    for var6 in xrange(33):
        var5 += (arg3 | 4) ^ var6
    return var5
def func3(arg8, arg9):
    closure = [0]
    def func4(acc, rest):
        var10 = (-8 + acc) | (acc ^ ((3 | 3 + rest) + acc))
        closure[0] += var10
        if acc == 0:
            return var10
        else:
            result = func4(acc - 1, var10)
            return result
    result = func4(10, 0)
    return result
def func5(arg12, arg13):
    def func6(acc, rest):
        var41 = func7(rest, -3)
        if acc == 0:
            return var41
        else:
            result = func6(acc - 1, var41)
            return result
    result = func6(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 66'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
