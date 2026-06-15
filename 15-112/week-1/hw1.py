#################################################
# hw1.py
# name:
# andrew id:
# Do not use string indexing, loops, lists, list indexing, or recursion this week.
#################################################

import math

import cs112_f22_week1_linter

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

def distance(x1, y1, x2, y2):
    relative_distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.sqrt(relative_distance)

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    return distance(x1, y1, x2, y2) <= (r1 + r2)

def getInRange(x, bound1, bound2):
    max_bound = max(bound1, bound2)
    min_bound = min(bound1, bound2)
    if x < min_bound:
        return min_bound
    elif x > max_bound:
        return max_bound
    else:
        return x

def eggCartons(eggs):
    box = decimal.Decimal(eggs) / decimal.Decimal('12')
    return int(decimal.Decimal(box).to_integral_value(rounding=decimal.ROUND_UP))

def pascalsTriangleValue(row, col):
    if isinstance(row, int) and isinstance(col, int):
        return math.factorial(row) / (math.factorial(col) * math.factorial(row - col))
    else:
        return None

def getKthDigit(n, k):
    if isinstance(n, int) and isinstance(k, int) and k > 0:
        return n // (10 ** k) % 10
    return None

def setKthDigit(n, k, d):
    if isinstance(d, int) and (0 <= d <= 9):
        return n - (getKthDigit(n, k) * 10 ** k) + d * 10 ** k
    else:
        return None

def nearestOdd(n):
    if isinstance(n, float):
        n = roundHalfUp(n)
    if n % 2 == 0:
        return n - 1
    return n

def numberOfPoolBalls(rows):
    if rows == 0:
        return 0
    if isinstance(rows, int) and (rows > 0):
        return int(rows * (rows + 1) / 2)
    return None

def numberOfPoolBallRows(balls):
    if isinstance(balls, int) and (balls > 0):
        rows = (math.sqrt(8 * balls + 1) - 1) / 2
        if rows > int(rows):
            return int(rows) + 1
        else:
            return int(rows)
    else:
        return None

def colorBlender(rgb1, rgb2, midpoints, n):
    if isinstance(rgb1, int) and isinstance(rgb2, int) and isinstance(midpoints, int) and isinstance(n, int):
        if rgb1 > 0 and rgb2 > 0 and n > 0 and midpoints > 0:
            if n in list(range(midpoints + 2)):
                rgb1red = rgb1 // 10 ** 6
                rgb1green = rgb1 // 10**3 % 10**3
                rgb1blue = rgb1 % 10**3
                rgb2red = rgb2 // 10 ** 6
                rgb2green = rgb2 // 10**3 % 10**3
                rgb2blue = rgb2 % 10**3
                rgbNred = roundHalfUp(rgb1red - abs(rgb1red - rgb2red) * (n / (midpoints + 1)))
                rgbNgreen = roundHalfUp(rgb1green - abs(rgb1green - rgb2green) * (n / (midpoints + 1)))
                rgbNblue = roundHalfUp(rgb1blue - abs(rgb1blue - rgb2blue) * (n / (midpoints + 1)))
                return rgbNred * 10 ** 6 + rgbNgreen * 10 ** 3 + rgbNblue
            else:
                return None
        else:
            return None
    else:
        return None

#################################################
# Bonus/Optional
#################################################

def bonusPlayThreeDiceYahtzee(dice):
    hand = dice % 1000
    dice_pool = dice // 1000
    hand_step1, dice_step1 = playStep2(hand, dice_pool)
    hand_step2, _ = playStep2(hand_step1, dice_step1)
    score_play = score(hand_step2)
    return hand_step2, score_play

def handToDice(hand):
    if isinstance(hand, int) and (hand > 100):
        return (hand // 100 % 10, hand // 10 % 10, hand % 10)
    return None

def diceToOrderedHand(a, b, c):
    max_dice = max(a, b, c)
    min_dice = min(a, b, c)
    mid_dice = a + b + c - max_dice - min_dice
    return max_dice * 100 + mid_dice * 10 + min_dice

def playStep2(hand, dice):
    hand_tuple = handToDice(hand)
    max_dice = max(hand_tuple[0], hand_tuple[1], hand_tuple[2])
    min_dice = min(hand_tuple[0], hand_tuple[1], hand_tuple[2])
    mid_dice = hand_tuple[0] + hand_tuple[1] + hand_tuple[2] - max_dice - min_dice
    dice_1 = dice % 10
    dice_2 = dice // 10 % 10
    if max_dice == min_dice:
        return hand, dice
    elif mid_dice == max_dice or mid_dice == min_dice:
        return diceToOrderedHand(dice_1, mid_dice, mid_dice), dice // 10
    else:
        return diceToOrderedHand(max_dice, dice_1, dice_2), dice // 100

def score(hand):
    dice_tuple = handToDice(hand)
    dice_a = dice_tuple[0]
    dice_b = dice_tuple[1]
    dice_c = dice_tuple[2]
    if dice_a == dice_b == dice_c:
        return 20 + dice_a * 3
    elif dice_a == dice_b or dice_a == dice_c or dice_b == dice_c:
        mid_dice = dice_a + dice_b + dice_c - max(dice_a, dice_b, dice_c) - min(dice_a, dice_b, dice_c)
        return 10 + mid_dice * 2
    else:
        return max(dice_a, dice_b, dice_c)

#################################################
# Test Functions
#################################################

def testDistance():
    print('Testing distance()... ', end='')
    assert(almostEqual(distance(0, 0, 3, 4), 5))
    assert(almostEqual(distance(-1, -2, 3, 1), 5))
    assert(almostEqual(distance(-.5, .5, .5, -.5), 2**0.5))
    print('Passed!')

def testCirclesIntersect():
    print('Testing circlesIntersect()... ', end='')
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    assert(circlesIntersect(3, 3, 3, 3, -3, 3) == True)
    assert(circlesIntersect(3, 3, 3, 3,- 3, 2.99) == False)
    print('Passed!')

def testGetInRange():
    print('Testing getInRange()... ', end='')
    assert(getInRange(5, 1, 10) == 5)
    assert(getInRange(5, 5, 10) == 5)
    assert(getInRange(5, 9, 10) == 9)
    assert(getInRange(5, 10, 10) == 10)
    assert(getInRange(5, 10, 1) == 5)
    assert(getInRange(5, 10, 5) == 5)
    assert(getInRange(5, 10, 9) == 9)
    assert(getInRange(0, -20, -30) == -20)
    assert(almostEqual(getInRange(0, -20.25, -30.33), -20.25))
    print('Passed!')

def testEggCartons():
    print('Testing eggCartons()... ', end='')
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print('Passed!')

def testPascalsTriangleValue():
    print('Testing pascalsTriangleValue()... ', end='')
    assert(pascalsTriangleValue(3,0) == 1)
    assert(pascalsTriangleValue(3,1) == 3)
    assert(pascalsTriangleValue(3,2) == 3)
    assert(pascalsTriangleValue(3,3) == 1)
    assert(pascalsTriangleValue(1234,0) == 1)
    assert(pascalsTriangleValue(1234,1) == 1234)
    assert(pascalsTriangleValue(1234,2) == 760761)
    assert(pascalsTriangleValue(3,-1) == None)
    assert(pascalsTriangleValue(3,4) == None)
    assert(pascalsTriangleValue(-3,2) == None)
    print('Passed!')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed!')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    # results must be int's not floats
    assert(isinstance(nearestOdd(13.0), int))
    assert(isinstance(nearestOdd(11.999), int))
    print('Passed!')

def testNumberOfPoolBalls():
    print('Testing numberOfPoolBalls()... ', end='')
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print('Passed!')

def testNumberOfPoolBallRows():
    print('Testing numberOfPoolBallRows()... ', end='')
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print('Passed!')

def testColorBlender():
    print('Testing colorBlender()... ', end='')
    # http://meyerweb.com/eric/tools/color-blend/#DC143C:BDFCC9:3:rgbd
    assert(colorBlender(220020060, 189252201, 3, -1) == None)
    assert(colorBlender(220020060, 189252201, 3, 0) == 220020060)
    assert(colorBlender(220020060, 189252201, 3, 1) == 212078095)
    assert(colorBlender(220020060, 189252201, 3, 2) == 205136131)
    assert(colorBlender(220020060, 189252201, 3, 3) == 197194166)
    assert(colorBlender(220020060, 189252201, 3, 4) == 189252201)
    assert(colorBlender(220020060, 189252201, 3, 5) == None)
    # http://meyerweb.com/eric/tools/color-blend/#0100FF:FF0280:2:rgbd
    assert(colorBlender(1000255, 255002128, 2, -1) == None)
    assert(colorBlender(1000255, 255002128, 2, 0) == 1000255)
    assert(colorBlender(1000255, 255002128, 2, 1) == 86001213)
    assert(colorBlender(1000255, 255002128, 2, 2) == 170001170)
    assert(colorBlender(1000255, 255002128, 2, 3) == 255002128)
    print('Passed!')

def testBonusPlayThreeDiceYahtzee():
    print('Testing bonusPlayThreeDiceYahtzee()...', end='')
    assert(handToDice(123) == (1,2,3))
    assert(handToDice(214) == (2,1,4))
    assert(handToDice(422) == (4,2,2))
    assert(diceToOrderedHand(1,2,3) == 321)
    assert(diceToOrderedHand(6,5,4) == 654)
    assert(diceToOrderedHand(1,4,2) == 421)
    assert(diceToOrderedHand(6,5,6) == 665)
    assert(diceToOrderedHand(2,2,2) == 222)
    assert(playStep2(413, 2312) == (421, 23))
    assert(playStep2(421, 23) == (432, 0))
    assert(playStep2(413, 2345) == (544, 23))
    assert(playStep2(544, 23) == (443, 2))
    assert(playStep2(544, 456) == (644, 45))
    assert(score(432) == 4)
    assert(score(532) == 5)
    assert(score(443) == 10+4+4)
    assert(score(633) == 10+3+3)
    assert(score(333) == 20+3+3+3)
    assert(score(555) == 20+5+5+5)
    assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
    assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
    assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
    assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
    assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
    assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))
    print('Passed!')


#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testDistance()
    testCirclesIntersect()
    testGetInRange()
    testEggCartons()
    testPascalsTriangleValue()
    testGetKthDigit()
    testSetKthDigit()
    testNearestOdd()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testColorBlender()
    # Bonus:
    # testBonusPlayThreeDiceYahtzee()

def main():
    cs112_f22_week1_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
