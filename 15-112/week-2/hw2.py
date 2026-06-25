#################################################
# hw2.py
# name:
# andrew id:
#################################################

import cs112_f22_week2_linter

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal


def roundHalfUp(d): #helper-fn
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
    count = 1
    while (n // 10) != 0:
        n //= 10
        count += 1
    return count

def hasConsecutiveDigits(n):
    """
    编写函数 `hasConsecutiveDigits(n)`，该函数接收一个整数 `n`（可能是负数），
    如果该数包含两个相同的相邻数字，则返回 `True`，否则返回 `False`。
    """
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
    if source_int == reversed_int:
        return True
    return False

def isPrimeNum(n):
    m = int(n / 2) + 1
    while m > 1:
        if n % m == 0:
            return True
        m -= 1
    return False

def nthPalindromicPrime(n):
    """
    编写函数 `nthPalindromicPrime(n)`，该函数接收一个非负整数 `n` 并返回第 `n` 个回文素数（即既是素数又是回文数的数）。
    前十个回文素数依次为 2、3、5、7、11、101、131、151、181、191，因此 `nthPalindromicPrime(0)` 应返回 2，
    `nthPalindromicPrime(1)` 应返回 3，依此类推。
    """
    start_digit = 2
    while n < 0:
        if isPrimeNum(start_digit) and isPalindromicNumber(start_digit):
            n -= 1
        start_digit += 1
    return start_digit

def mostFrequentDigit(n):
    """
    编写函数 mostFrequentDigit(n)，该函数接受一个可能为负数的整数 n，
    并返回 0 到 9 中出现频率最高的数字，如果出现频率相同的数字，则返回较小的数字。
    """
    return 42

def findZeroWithBisection(f, x0, x1, epsilon):
    return 42

def carrylessAdd(x, y):
    return 42

def longestDigitRun(n):
    return 42

def playPig():
    return 42

#################################################
# Bonus/Optional
#################################################

def bonusCarrylessMultiply(x1, x2):
    return 42

############################
# bonus: integerDataStructures
############################

def intCat(n, m): pass
def lengthEncode(value): pass
def lengthDecode(encoding): pass
def lengthDecodeLeftmostValue(encoding): pass
def newIntList(): pass
def intListLen(intList): pass
def intListGet(intList, i): pass
def intListSet(intList, i, value): pass
def intListAppend(intList, value): pass
def intListPop(intList): pass
def newIntSet(): pass
def intSetAdd(intSet, value): pass
def intSetContains(intSet, value): pass
def newIntMap(): pass
def intMapGet(intMap, key): pass
def intMapContains(intMap,key): pass
def intMapSet(intMap, key, value): pass
def newIntFSM(): pass
def isAcceptingState(fsm, state): pass
def addAcceptingState(fsm, state): pass
def setTransition(fsm, fromState, digit, toState): pass
def getTransition(fsm, fromState, digit): pass
def accepts(fsm, inputValue): pass
def states(fsm, inputValue): pass
def encodeString(s): pass
def decodeString(intList): pass

#################################################
# Test Functions
#################################################

def testDigitCount():
    print('Testing digitCount()...', end='')
    assert(digitCount(3) == 1)
    assert(digitCount(33) == 2)
    assert(digitCount(3030) == 4)
    assert(digitCount(-3030) == 4)
    assert(digitCount(0) == 1)
    print('Passed!')

def testHasConsecutiveDigits():
    print('Testing hasConsecutiveDigits()...', end='')
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print('Passed!')

def testIsPalindromicNumber():
    print('Testing isPalindromicNumber()...', end='')
    assert isPalindromicNumber(0) == True
    assert isPalindromicNumber(4) == True
    assert isPalindromicNumber(10) == False
    assert isPalindromicNumber(101) == True
    assert isPalindromicNumber(1001) == True
    assert isPalindromicNumber(10010) == False
    print('Passed!')


def testNthPalindromicPrime():
    print('Testing nthPalindromicPrime()...', end='')
    assert nthPalindromicPrime(0) == 2
    assert nthPalindromicPrime(4) == 11
    assert nthPalindromicPrime(10) == 313
    assert nthPalindromicPrime(15) == 757
    assert nthPalindromicPrime(20) == 10301
    print('Passed!')

def testMostFrequentDigit():
    print('Testing mostFrequentDigit()...', end='')
    assert mostFrequentDigit(0) == 0
    assert mostFrequentDigit(1223) == 2
    assert mostFrequentDigit(12233) == 2
    assert mostFrequentDigit(-12233) == 2
    assert mostFrequentDigit(1223322332) == 2
    assert mostFrequentDigit(123456789) == 1
    assert mostFrequentDigit(1234567789) == 7
    assert mostFrequentDigit(1000123456789) == 0
    print('Passed!')

def testFindZeroWithBisection():
    print('Testing findZeroWithBisection()... ', end='')
    def f1(x): return x*x - 2 # root at x=sqrt(2)
    x = findZeroWithBisection(f1, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.41421356192))
    def f2(x): return x**2 - (x + 1)  # root at x=phi
    x = findZeroWithBisection(f2, 0, 2, 0.000000001)
    assert(almostEqual(x, 1.61803398887))
    def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0
    x = findZeroWithBisection(f3, 1, 2, 0.000000001)
    assert(almostEqual(x, 1.17727855081))
    print('Passed!')

def testCarrylessAdd():
    print('Testing carrylessAdd()... ', end='')
    assert(carrylessAdd(785, 376) == 51)
    assert(carrylessAdd(0, 376) == 376)
    assert(carrylessAdd(785, 0) == 785)
    assert(carrylessAdd(30, 376) == 306)
    assert(carrylessAdd(785, 30) == 715)
    assert(carrylessAdd(12345678900, 38984034003) == 40229602903)
    print('Passed!')

def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    print('Passed!')

def testPlayPig():
    print('** Note: You need to manually test playPig()')
    playPig()

def testBonusCarrylessMultiply():
    print("Testing bonusCarrylessMultiply()...", end="")
    assert(bonusCarrylessMultiply(643, 59) == 417)
    assert(bonusCarrylessMultiply(6412, 387) == 807234)
    print("Passed!")

# Integer Data Structures

def testLengthEncode():
    print('Testing lengthEncode()...', end='')
    assert(lengthEncode(789) == 113789)
    assert(lengthEncode(-789) == 213789)
    assert(lengthEncode(1234512345) == 12101234512345)
    assert(lengthEncode(-1234512345) == 22101234512345)
    assert(lengthEncode(0) == 1110)
    print('Passed!')

def testLengthDecodeLeftmostValue():
    print('Testing lengthDecodeLeftmostValue()...', end='')
    assert(lengthDecodeLeftmostValue(111211131114) == (2, 11131114))
    assert(lengthDecodeLeftmostValue(112341115) == (34, 1115))
    assert(lengthDecodeLeftmostValue(111211101110) == (2, 11101110))
    assert(lengthDecodeLeftmostValue(11101110) == (0, 1110))
    print('Passed!')

def testLengthDecode():
    print('Testing lengthDecode()...', end='')
    assert(lengthDecode(113789) == 789)
    assert(lengthDecode(213789) == -789)
    assert(lengthDecode(12101234512345) == 1234512345)
    assert(lengthDecode(22101234512345) == -1234512345)
    assert(lengthDecode(1110) == 0)
    print('Passed!')

def testIntList():
    print('Testing intList functions...', end='')
    a1 = newIntList()
    assert(a1 == 1110) # length = 0, list = []
    assert(intListLen(a1) == 0)
    assert(intListGet(a1, 0) == 'index out of range')

    a1 = intListAppend(a1, 42)
    assert(a1 == 111111242) # length = 1, list = [42]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 42)
    assert(intListGet(a1, 1) == 'index out of range')
    assert(intListSet(a1, 1, 99) == 'index out of range')

    a1 = intListSet(a1, 0, 567)
    assert(a1 == 1111113567) # length = 1, list = [567]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 567)

    a1 = intListAppend(a1, 8888)
    a1 = intListSet(a1, 0, 9)
    assert(a1 == 111211191148888) # length = 2, list = [9, 8888]
    assert(intListLen(a1) == 2)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 8888)

    a1, poppedValue = intListPop(a1)
    assert(poppedValue == 8888)
    assert(a1 == 11111119) # length = 1, list = [9]
    assert(intListLen(a1) == 1)
    assert(intListGet(a1, 0) == 9)
    assert(intListGet(a1, 1) == 'index out of range')

    a2 = newIntList()
    a2 = intListAppend(a2, 0)
    assert(a2 == 11111110)
    a2 = intListAppend(a2, 0)
    assert(a2 == 111211101110)
    print('Passed!')

def testIntSet():
    print('Testing intSet functions...', end='')
    s = newIntSet()
    assert(s == 1110) # length = 0
    assert(intSetContains(s, 42) == False)
    s = intSetAdd(s, 42)
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    s = intSetAdd(s, 42) # multiple adds --> still just one
    assert(s == 111111242) # length = 1, set = [42]
    assert(intSetContains(s, 42) == True)
    print('Passed!')

def testIntMap():
    print('Testing intMap functions...', end='')
    m = newIntMap()
    assert(m == 1110) # length = 0
    assert(intMapContains(m, 42) == False)
    assert(intMapGet(m, 42) == 'no such key')
    m = intMapSet(m, 42, 73)
    assert(m == 11121124211273) # length = 2, map = [42, 73]
    assert(intMapContains(m, 42) == True)
    assert(intMapGet(m, 42) == 73)
    m = intMapSet(m, 42, 98765)
    assert(m == 11121124211598765) # length = 2, map = [42, 98765]
    assert(intMapGet(m, 42) == 98765)
    m = intMapSet(m, 99, 0)
    assert(m == 11141124211598765112991110) # length = 4,
                                            # map = [42, 98765, 99, 0]
    assert(intMapGet(m, 42) == 98765)
    assert(intMapGet(m, 99) == 0)
    print('Passed!')

def testIntFSM():
    print('Testing intFSM functions...', end='')
    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2,
                                      # [empty stateMap, empty startStateSet]
    assert(isAcceptingState(fsm, 1) == False)

    fsm = addAcceptingState(fsm, 1)
    assert(fsm == 1112114111011811111111)
    assert(isAcceptingState(fsm, 1) == True)

    assert(getTransition(fsm, 0, 8) == 'no such transition')
    fsm = setTransition(fsm, 4, 5, 6)
    # map[5] = 6: 111211151116
    # map[4] = (map[5] = 6):  111211141212111211151116
    assert(fsm == 1112122411121114121211121115111611811111111)
    assert(getTransition(fsm, 4, 5) == 6)

    fsm = setTransition(fsm, 4, 7, 8)
    fsm = setTransition(fsm, 5, 7, 9)
    assert(getTransition(fsm, 4, 5) == 6)
    assert(getTransition(fsm, 4, 7) == 8)
    assert(getTransition(fsm, 5, 7) == 9)

    fsm = newIntFSM()
    assert(fsm == 111211411101141110) # length = 2,
                                      # [empty stateMap, empty startStateSet]
    fsm = setTransition(fsm, 0, 5, 6)
    # map[5] = 6: 111211151116
    # map[0] = (map[5] = 6):  111211101212111211151116
    assert(fsm == 111212241112111012121112111511161141110)
    assert(getTransition(fsm, 0, 5) == 6)

    print('Passed!')

def testAccepts():
    print('Testing accepts()...', end='')
    fsm = newIntFSM()
    # fsm accepts 6*7+8
    fsm = addAcceptingState(fsm, 3)
    fsm = setTransition(fsm, 1, 6, 1) # At state 1, receive 6, move to state 1
    fsm = setTransition(fsm, 1, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 7, 2) # At state 1, receive 7, move to state 2
    fsm = setTransition(fsm, 2, 8, 3) # At state 1, receive 8, move to state 3
    assert(accepts(fsm, 78) == True)
    assert(states(fsm, 78) == 1113111111121113) # length = 3, list = [1,2,3]
    assert(accepts(fsm, 678) == True)
    assert(states(fsm, 678) == 11141111111111121113) # length = 4,
                                                     # list = [1,1,2,3]

    assert(accepts(fsm, 5) == False)
    assert(accepts(fsm, 788) == False)
    assert(accepts(fsm, 67) == False)
    assert(accepts(fsm, 666678) == True)
    assert(accepts(fsm, 66667777777777778) == True)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 666677777777777788) == False)
    assert(accepts(fsm, 77777777777788) == False)
    assert(accepts(fsm, 7777777777778) == True)
    assert(accepts(fsm, 67777777777778) == True)
    print('Passed!')

def testEncodeDecodeStrings():
    print('Testing encodeString and decodeString...', end='')
    assert(encodeString('A') == 111111265) # length = 1, str = [65]
    assert(encodeString('f') == 1111113102) # length = 1, str = [102]
    assert(encodeString('3') == 111111251) # length = 1, str = [51]
    assert(encodeString('!') == 111111233) # length = 1, str = [33]
    assert(encodeString('Af3!') == 1114112651131021125111233) # length = 4,
                                                          # str = [65,102,51,33]
    assert(decodeString(111111265) == 'A')
    assert(decodeString(1114112651131021125111233) == 'Af3!')
    assert(decodeString(encodeString('WOW!!!')) == 'WOW!!!')
    print('Passed!')

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

if __name__ == '__main__':
    main()
