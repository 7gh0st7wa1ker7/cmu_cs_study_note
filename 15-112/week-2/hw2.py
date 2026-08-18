#################################################
# hw2.py
# name:
# andrew id:
#################################################

import decimal
import random

# from ast import Return
import cs112_f22_week2_linter

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):  # helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return abs(d2 - d1) < epsilon


def roundHalfUp(d):  # helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#################################################
# Functions for you to write
#################################################


def digitCount(n):
    """
    请编写函数 `digitCount(n)`，该函数接收一个整数（可能是负数）并返回其包含的数字位数。
    例如，`digitCount(12323)` 应返回 5，`digitCount(0)` 应返回 1，`digitCount(-111)` 应返回 3。
    虽然可以通过返回 `len(str(abs(n)))` 来实现，但你不能这样做，因为此处不允许使用字符串！
    这个问题虽然可以用对数求解，但鉴于本周的主题是“循环（loops）”，你应该采用的方法是：不断去掉个位上的数字，直到无法继续为止。
    """
    n = abs(n)
    if abs(n) < 10:
        return 1
    count = 0
    while abs(n) > 0:
        n //= 10
        count += 1
    return count


def hasConsecutiveDigits(n):
    """
    编写函数 `hasConsecutiveDigits(n)`，该函数接收一个整数 `n`（可能是负数），
    如果该数包含两个相同的相邻数字，则返回 `True`，否则返回 `False`。
    """
    n = abs(n)
    while (n // 10) != 0:
        if (n % 10) == (n // 10 % 10):
            return True
        n //= 10
    return False


def isPalindromicNumber(n):
    """
    编写函数 `isPalindromicNumber(n)`，该函数接收一个非负整数 `n`，
    如果该数是回文数则返回 `True`，否则返回 `False`（回文数是指正读和反读都相同的数）。
    例如，以下数字是回文数：0、1、99、12321、123321；而以下数字不是：1211、112、10010。
    """
    source_int = n
    reversed_int = 0
    while n != 0:
        reversed_int = reversed_int * 10 + n % 10
        n //= 10

    return source_int == reversed_int


def isPrimeNum(n):
    if n < 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def nthPalindromicPrime(n):
    """
    编写函数 `nthPalindromicPrime(n)`，该函数接收一个非负整数 `n` 并返回第 `n` 个回文素数（即既是素数又是回文数的数）。
    前十个回文素数依次为 2、3、5、7、11、101、131、151、181、191，因此 `nthPalindromicPrime(0)` 应返回 2，
    `nthPalindromicPrime(1)` 应返回 3，依此类推。
    """
    num = 1
    while n >= 0:
        num += 1
        if isPrimeNum(num) and isPalindromicNumber(num):
            n -= 1
    return num


def mostFrequentDigit(n):
    """
    编写函数 mostFrequentDigit(n)，该函数接受一个可能为负数的整数 n，
    并返回 0 到 9 中出现频率最高的数字，如果出现频率相同的数字，则返回较小的数字。
    """
    n = abs(n)
    maxCount = 0
    mostFreqDigit = 0

    digit = 0
    while digit <= 9:
        count = 0
        temp = n
        while temp > 0:
            if temp % 10 == digit:
                count += 1
            temp //= 10

        if n == 0 and digit == 0:
            count = 1

        if count > maxCount:
            maxCount = count
            mostFreqDigit = digit
        digit += 1
    return mostFreqDigit


def findZeroWithBisection(f, x0, x1, epsilon):
    if f(x0) * f(x1) >= 0:
        return None

    while (x1 - x0) > epsilon:
        xmid = (x1 + x0) / 2
        if f(xmid) == 0:
            return xmid
        elif f(x0) * f(xmid) > 0:
            x0 = xmid
        else:
            x1 = xmid
    return (x0 + x1) / 2


def carrylessAdd(x, y):
    result = 0
    place = 0
    while x > 0 or y > 0:
        result += (x % 10 + y % 10) % 10 * 10**place
        x //= 10
        y //= 10
        place += 1
    return result


def longestDigitRun(n):
    """
    编写函数 longestDigitRun(n)，该函数接受一个可能为负数的整数 n 作为参数，返回拥有最长连续序列的数字；
    若存在多个数字的连续序列长度相同，则返回其中最小的那个数字。
    例如，longestDigitRun(117773732) 返回 7（因为存在 3 个连续的 7），longestDigitRun(-677886) 的返回结果同样是 7。
    """
    n = abs(n)
    if n < 10:
        return n

    bestDigit = 0
    bestCount = 0
    currentDigit = -1
    currentCount = 0

    while n > 0:
        digit = n % 10
        if digit == currentDigit:
            currentCount += 1
        else:
            currentDigit = digit
            currentCount = 1

        if (currentCount > bestCount) or (
            currentCount == bestCount and currentDigit <= bestDigit
        ):
            bestCount = currentCount
            bestDigit = currentDigit

        n //= 10

    return bestDigit


def playPig():
    user1Scores = 0
    user2Scores = 0
    userTurn = 0

    print("Let's start playPig!")

    while (user1Scores < 100) and (user2Scores < 100):
        print(f"Player {userTurn + 1}'s turn!")
        print(f"Current scores - Player 1: {user1Scores}, Player 2: {user2Scores}")
        scoresCount = 0
        print(f"Turn total: {scoresCount}")
        while True:
            isHold = input("Do you want hold?")
            if isHold == "hold":
                if userTurn == 0:
                    user1Scores += scoresCount
                    userTurn = 1
                    scoresCount = 0
                else:
                    userTurn = 0
                    user2Scores += scoresCount
                    scoresCount = 0
                continue
            scores = random.randint(1, 6)
            print(f"this turn scores is {scores}")
            if scores == 1:
                if userTurn == 0:
                    userTurn = 1
                    scoresCount = 0
                else:
                    userTurn = 0
                    scoresCount = 0
                continue
            scoresCount += scores
    if user1Scores >= 100:
        return "user1 is winner."
    return "user2 si winner."


#################################################
# Bonus/Optional
#################################################


def bonusCarrylessMultiply(x1, x2):
    result = 0
    place = 0

    while x2 > 0:
        count = 0
        turn = x2 % 10
        while turn > 0:
            count = carrylessAdd(count, x1)
            turn -= 1
        result = carrylessAdd(result, count * 10**place)
        x2 //= 10
        place += 1
    return result


############################
# bonus: integerDataStructures
############################


def intCat(n, m):
    "收两个非负整数并返回它们的拼接结果"
    if n < 0 or m < 0:
        return "n,m must Greater than or equal to 0."

    return n * 10 ** digitCount(m) + m


def lengthEncode(value):
    "函数接收一个可能为负数的 Python 整数，并按照上述规则返回经过长度前缀编码的整数"
    valueLen = digitCount(value)

    if value >= 0:
        isPositive = 1
    else:
        isPositive = 2

    if valueLen >= 10:
        result = intCat(isPositive, 2)
    else:
        result = intCat(isPositive, 1)

    return intCat(intCat(result, valueLen), abs(value))


def substring(digit, m, n):
    "来提取整数的第m到n的数值"
    digitLen = digitCount(digit)
    return digit % 10 ** (digitLen - m) // 10 ** (digitLen - 1 - n)


def lengthDecode(encoding):
    "lengthEncode 的解码函数"
    result, _ = lengthDecodeLeftmostValue(encoding)
    return result


def lengthDecodeLeftmostValue(encoding):
    "接收一个包含一个或多个编码值的数字，并仅解码最左侧的值。此函数必须返回两个值：解码后的值以及剩余的编码值"
    isPositive = substring(encoding, 0, 0)
    numPlace = substring(encoding, 1, 1)

    if numPlace == 1:
        numLen = substring(encoding, 2, 2)
    else:
        numLen = substring(encoding, 2, 3)

    if numLen >= 10:
        num = substring(encoding, 4, numLen + 3)
    else:
        num = substring(encoding, 3, numLen + 2)

    if isPositive != 1:
        num = num * -1

    return num, encoding % 10 ** (digitCount(encoding) - numLen - 3)


def newIntList():
    "返回一个空列表"
    return 1110


def intListLen(intList):
    "接收一个列表，返回其长度（最左侧的编码值）。"
    return lengthDecode(intList)


def intListGet(intList, i):
    "接收一个列表和一个索引，返回该索引处解码后的值。必要时返回字符串'索引超出范围'。"
    lenList, intSource = lengthDecodeLeftmostValue(intList)

    if i >= lenList and lenList == 0:
        return "index out of range"

    intLen = 0
    while i >= 0:
        intLen, intSource = lengthDecodeLeftmostValue(intSource)
        i -= 1
    return intLen


def intListSet(intList, i, value):
    "接收一个列表和一个索引，返回一个新列表，该列表中给定索引处的值被替换为 v 的编码后的值。必要时返回字符串'索引超出范围'。"
    listLen, sourceList = lengthDecodeLeftmostValue(intList)
    if i >= listLen:
        return "index out of range"

    newList = 0
    for idx in range(listLen):
        element, sourceList = lengthDecodeLeftmostValue(sourceList)
        if idx == i:
            newList = intCat(newList, lengthEncode(value))
        else:
            newList = intCat(newList, lengthEncode(element))

    return intCat(lengthEncode(listLen), newList)


def intListAppend(intList, value):
    "接收一个列表和一个值，返回一个将该值（经编码后）追加到末尾的新列表。"
    listLen, sourceList = lengthDecodeLeftmostValue(intList)
    listLen = lengthEncode(listLen + 1)
    sourceList = intCat(sourceList, lengthEncode(value))
    return intCat(listLen, sourceList)


def intListPop(intList):
    "接收一个列表并移除最后一个值（“弹出”该值）。随后返回两个值：移除弹出值后的列表，以及被弹出的那个值本身"
    listLen, sourceList = lengthDecodeLeftmostValue(intList)
    newLen = listLen - 1

    newList = 0
    idx = 0
    lastElement = 0
    while listLen > idx:
        element, sourceList = lengthDecodeLeftmostValue(sourceList)
        if idx < newLen:
            newList = intCat(newList, lengthEncode(element))
        else:
            lastElement = element
        idx += 1

    return intCat(lengthEncode(newLen), newList), lastElement


def newIntSet():
    "返回一个新的空集合（等同于新的空列表，也等同于长度前缀编码的 0 值）"
    return 1110


def intSetAdd(intSet, value):
    "接收一个集合和一个值，若该值已在集合中则返回原集合，否则返回一个将值追加到集合 s 末尾的新集合。"
    if intSetContains(intSet, value):
        return intSet
    else:
        return intListAppend(intSet, value)


def intSetContains(intSet, value):
    "接受一个集合和一个值，若该集合包含此值则返回 True，否则返回 False。"
    setLen, sourceSet = lengthDecodeLeftmostValue(intSet)
    while setLen > 0:
        element, sourceSet = lengthDecodeLeftmostValue(sourceSet)
        if element == value:
            return True
        setLen -= 1
    return False


def newIntMap():
    "不接受任何参数，返回一个空映射，即空列表"
    return 1110


def intMapGet(intMap, key):
    "接收一个映射和一个键，返回该映射中与该键关联的值，或在适当时返回字符串“无此键”。"
    mapLen, mapList = lengthDecodeLeftmostValue(intMap)
    i = 0
    while i < mapLen:
        k, mapList = lengthDecodeLeftmostValue(mapList)
        v, mapList = lengthDecodeLeftmostValue(mapList)
        if k == key:
            return v
    return "no such key"


def intMapContains(intMap, key):
    "接收一个映射和一个键，若该映射包含该键（作为键而非值），则返回 True，否则返回 False"
    mapLen, mapStr = lengthDecodeLeftmostValue(intMap)
    i = 0
    while i < mapLen:
        k, mapStr = lengthDecodeLeftmostValue(mapStr)
        _, mapStr = lengthDecodeLeftmostValue(mapStr)
        if k == key:
            return True
        i += 2
    return False


def intMapSet(intMap, key, value):
    "接收一个映射、一个键和一个值，返回一个新映射"
    if intMapContains(intMap, key):
        mapLen, mapStr = lengthDecodeLeftmostValue(intMap)
        i = 0
        while i < mapLen:
            k, mapStr = lengthDecodeLeftmostValue(mapStr)
            _, mapStr = lengthDecodeLeftmostValue(mapStr)
            if k == key:
                return intListSet(intMap, i + 1, value)
            i += 2
    else:
        intMap = intListAppend(intMap, key)
        intMap = intListAppend(intMap, value)
        return intMap


def newIntFSM():
    "无参数，返回一个空的有限状态机（FSM），该状态机包含一个空的转换映射和一个空的接受状态集合。"
    return 111211411101141110


def isAcceptingState(fsm, state):
    "接收一个有限状态机（fsm）和一个状态，如果该状态位于接受状态集合中则返回 True，否则返回 False"


def addAcceptingState(fsm, state):
    "接收一个有限状态机（fsm）和一个状态，返回一个新的有限状态机，该有限状态机与原有限状态机的唯一区别是将指定状态添加到了接受状态集合中。"
    pass


def setTransition(fsm, fromState, digit, toState):
    "返回一个新的有限状态机（FSM），该有限状态机与给定的有限状态机（fsm）相同，只是添加了这个新的转换"
    pass


def getTransition(fsm, fromState, digit):
    "返回由该起始状态在该数字上映射到的目标状态"
    pass


def accepts(fsm, inputValue):
    "接收一个有限状态机（FSM）和一个输入值，如果该有限状态机接受该输入值则返回 True，否则返回 False"
    pass


def states(fsm, inputValue):
    "接收一个有限状态机（fsm）和一个输入值（inputValue），其功能与 accepts(fsm, inputValue) 基本一致，区别在于本函数不返回 True 或 False，而是返回一个列表（长度编码前缀列表）"
    pass


def encodeString(s):
    "接收一个 Python 字符串 s，并返回一个长度前缀形式的列表，该列表包含 s 中各字符的序数值"
    sLen = 0
    sList = 0

    for i in s:
        sLen += 1
        sEncodeInt = ord(i)
        sList = intCat(sList, lengthEncode(sEncodeInt))

    return intCat(lengthEncode(sLen), sList)


def decodeString(intList):
    "接收一个长度前缀列表 L，并返回对应的 Python 字符串"
    result = ""
    strLen, sourceStr = lengthDecodeLeftmostValue(intList)

    while strLen > 0:
        element, sourceStr = lengthDecodeLeftmostValue(sourceStr)
        result = result + chr(lengthDecode(element))
        strLen -= 1

    return result


#################################################
# Test Functions
#################################################


def testDigitCount():
    print("Testing digitCount()...", end="")
    assert digitCount(3) == 1
    assert digitCount(33) == 2
    assert digitCount(3030) == 4
    assert digitCount(-3030) == 4
    assert digitCount(0) == 1
    print("Passed!")


def testHasConsecutiveDigits():
    print("Testing hasConsecutiveDigits()...", end="")
    assert hasConsecutiveDigits(0) == False
    assert hasConsecutiveDigits(123456789) == False
    assert hasConsecutiveDigits(1212) == False
    assert hasConsecutiveDigits(1212111212) == True
    assert hasConsecutiveDigits(33) == True
    assert hasConsecutiveDigits(-1212111212) == True
    print("Passed!")


def testIsPalindromicNumber():
    print("Testing isPalindromicNumber()...", end="")
    assert isPalindromicNumber(0) == True
    assert isPalindromicNumber(4) == True
    assert isPalindromicNumber(10) == False
    assert isPalindromicNumber(101) == True
    assert isPalindromicNumber(1001) == True
    assert isPalindromicNumber(10010) == False
    print("Passed!")


def testNthPalindromicPrime():
    print("Testing nthPalindromicPrime()...", end="")
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print("Passed!")


def testMostFrequentDigit():
    print("Testing mostFrequentDigit()...", end="")
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print("Passed!")


def testFindZeroWithBisection():
    print("Testing findZeroWithBisection()... ", end="")

    def f1(x):
        return x * x - 2  # root at x=sqrt(2)

    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert almostEqual(x, 1.41421356192)

    def f2(x):
        return x**2 - (x + 1)  # root at x=phi

    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert almostEqual(x, 1.61803398887)

    def f3(x):
        return x**5 - 2**x  # f(1)<0, f(2)>0

    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert almostEqual(x, 1.17727855081)
    print("Passed!")


def testCarrylessAdd():
    print("Testing carrylessAdd()... ", end="")
    assert carrylessAdd(785, 376) == 51
    assert carrylessAdd(0, 376) == 376
    assert carrylessAdd(785, 0) == 785
    assert carrylessAdd(30, 376) == 306
    assert carrylessAdd(785, 30) == 715
    assert carrylessAdd(12345678900, 38984034003) == 40229602903
    print("Passed!")


def testLongestDigitRun():
    print("Testing longestDigitRun()... ", end="")
    assert longestDigitRun(117773732) == 7
    assert longestDigitRun(-677886) == 7
    assert longestDigitRun(5544) == 4
    assert longestDigitRun(1) == 1
    assert longestDigitRun(0) == 0
    assert longestDigitRun(22222) == 2
    assert longestDigitRun(111222111) == 1
    print("Passed!")


def testPlayPig():
    print("** Note: You need to manually test playPig()")
    playPig()


def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert bonusCarrylessMultiply(643, 59) == 417
    assert bonusCarrylessMultiply(6412, 387) == 807234
    print("Passed!")


# Integer Data Structures


def testLengthEncode():
    print("Testing lengthEncode()...", end="")
    assert lengthEncode(789) == 113789
    assert lengthEncode(-789) == 213789
    assert lengthEncode(1234512345) == 12101234512345
    assert lengthEncode(-1234512345) == 22101234512345
    assert lengthEncode(0) == 1110
    print("Passed!")


def testLengthDecodeLeftmostValue():
    print("Testing lengthDecodeLeftmostValue()...", end="")
    assert lengthDecodeLeftmostValue(111211131114) == (2, 11131114)
    assert lengthDecodeLeftmostValue(112341115) == (34, 1115)
    assert lengthDecodeLeftmostValue(111211101110) == (2, 11101110)
    assert lengthDecodeLeftmostValue(11101110) == (0, 1110)
    print("Passed!")


def testLengthDecode():
    print("Testing lengthDecode()...", end="")
    assert lengthDecode(113789) == 789
    assert lengthDecode(213789) == -789
    assert lengthDecode(12101234512345) == 1234512345
    assert lengthDecode(22101234512345) == -1234512345
    assert lengthDecode(1110) == 0
    print("Passed!")


def testIntList():
    print("Testing intList functions...", end="")
    a1 = newIntList()
    assert a1 == 1110  # length = 0, list = []
    assert intListLen(a1) == 0
    assert intListGet(a1, 0) == "index out of range"

    a1 = intListAppend(a1, 42)
    assert a1 == 111111242  # length = 1, list = [42]
    assert intListLen(a1) == 1
    assert intListGet(a1, 0) == 42
    assert intListGet(a1, 1) == "index out of range"
    assert intListSet(a1, 1, 99) == "index out of range"

    a1 = intListSet(a1, 0, 567)
    assert a1 == 1111113567  # length = 1, list = [567]
    assert intListLen(a1) == 1
    assert intListGet(a1, 0) == 567

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert a1 == 111211191148888  # length = 2, list = [9, 8888]
    assert intListLen(a1) == 2
    assert intListGet(a1, 0) == 9
    assert intListGet(a1, 1) == 8888

    a1, poppedValue = intListPop(a1)
    assert poppedValue == 8888
    assert a1 == 11111119  # length = 1, list = [9]
    assert intListLen(a1) == 1
    assert intListGet(a1, 0) == 9
    assert intListGet(a1, 1) == "index out of range"

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert a2 == 11111110
    a2 = intListAppend(a2, 0)
    assert a2 == 111211101110
    print("Passed!")


def testIntSet():
    print("Testing intSet functions...", end="")
    s = newIntSet()
    assert s == 1110  # length = 0
    assert intSetContains(s, 42) == False
    s = intSetAdd(s, 42)
    assert s == 111111242  # length = 1, set = [42]
    assert intSetContains(s, 42) == True
    s = intSetAdd(s, 42)  # multiple adds --> still just one
    assert s == 111111242  # length = 1, set = [42]
    assert intSetContains(s, 42) == True
    print("Passed!")


def testIntMap():
    print("Testing intMap functions...", end="")
    m = newIntMap()
    assert m == 1110  # length = 0
    assert intMapContains(m, 42) == False
    assert intMapGet(m, 42) == "no such key"
    m = intMapSet(m, 42, 73)
    assert m == 11121124211273  # length = 2, map = [42, 73]
    assert intMapContains(m, 42) == True
    assert intMapGet(m, 42) == 73
    m = intMapSet(m, 42, 98765)
    assert m == 11121124211598765  # length = 2, map = [42, 98765]
    assert intMapGet(m, 42) == 98765
    m = intMapSet(m, 99, 0)
    assert m == 11141124211598765112991110  # length = 4,
    # map = [42, 98765, 99, 0]
    assert intMapGet(m, 42) == 98765
    assert intMapGet(m, 99) == 0
    print("Passed!")


def testIntFSM():
    print("Testing intFSM functions...", end="")
    fsm = newIntFSM()
    assert fsm == 111211411101141110  # length = 2,
    # [empty stateMap, empty startStateSet]
    assert isAcceptingState(fsm, 1) == False

    fsm = addAcceptingState(fsm, 1)
    assert fsm == 1112114111011811111111
    assert isAcceptingState(fsm, 1) == True

    assert getTransition(fsm, 0, 8) == "no such transition"
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert fsm == 1112122411121114121211121115111611811111111
    assert getTransition(fsm, 4, 5) == 6

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert getTransition(fsm, 4, 5) == 6
    assert getTransition(fsm, 4, 7) == 8
    assert getTransition(fsm, 5, 7) == 9

    fsm = newIntFSM()
    assert fsm == 111211411101141110  # length = 2,
    # [empty stateMap, empty startStateSet]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert fsm == 111212241112111012121112111511161141110
    assert getTransition(fsm, 0, 5) == 6

    print("Passed!")


def testAccepts():
    print("Testing accepts()...", end="")
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1)  # At state 1, receive 6, move to state 1
    fsm = setTransition(fsm, 1, 7, 2)  # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 7, 2)  # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 8, 3)  # At state 1, receive 8, move to state 3
    assert accepts(fsm, 78) == True
    assert states(fsm, 78) == 1113111111121113  # length = 3, list = [1,2,3]
    assert accepts(fsm, 678) == True
    assert states(fsm, 678) == 11141111111111121113  # length = 4,
    # list = [1,1,2,3]

    assert accepts(fsm, 5) == False
    assert accepts(fsm, 788) == False
    assert accepts(fsm, 67) == False
    assert accepts(fsm, 666678) == True
    assert accepts(fsm, 66667777777777778) == True
    assert accepts(fsm, 7777777777778) == True
    assert accepts(fsm, 666677777777777788) == False
    assert accepts(fsm, 77777777777788) == False
    assert accepts(fsm, 7777777777778) == True
    assert accepts(fsm, 67777777777778) == True
    print("Passed!")


def testEncodeDecodeStrings():
    print("Testing encodeString and decodeString...", end="")
    assert encodeString("A") == 111111265  # length = 1, str = [65]
    assert encodeString("f") == 1111113102  # length = 1, str = [102]
    assert encodeString("3") == 111111251  # length = 1, str = [51]
    assert encodeString("!") == 111111233  # length = 1, str = [33]
    assert encodeString("Af3!") == 1114112651131021125111233  # length = 4,
    # str = [65,102,51,33]
    assert decodeString(111111265) == "A"
    assert decodeString(1114112651131021125111233) == "Af3!"
    assert decodeString(encodeString("WOW!!!")) == "WOW!!!"
    print("Passed!")


def testIntegerDataStructures():
    testLengthEncode()
    testLengthDecode()
    testLengthDecodeLeftmostValue()
    testIntList()
    testIntSet()
    testIntMap()
    testIntFSM()
    testAccepts()
    testEncodeDecodeStrings()


#################################################
# testAll and main
#################################################


def testAll():
    # comment out the tests you do not wish to run!
    testDigitCount()
    testHasConsecutiveDigits()
    testIsPalindromicNumber()
    testNthPalindromicPrime()
    testMostFrequentDigit()
    testFindZeroWithBisection()
    testCarrylessAdd()
    testLongestDigitRun()
    testPlayPig()

    # Bonus:
    # testBonusCarrylessMultiply()
    # testIntegerDataStructures()


def main():
    cs112_f22_week2_linter.lint()
    testAll()


if __name__ == "__main__":
    main()
