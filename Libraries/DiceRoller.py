from random import randint
from Libraries.MathCalculator import Calculate
from Libraries.Logger import writeLog, writeLogErr

class Dice():

    def __init__(self, min, max):
        try:
            self._minValue = min
            self._maxValue = max
            writeLog("Dice of {} faces created succesfully".format(max))
        except Exception as e:
            writeLogErr("Error creating dice ({}, {}).\n{}".format(min, max,e))

    def Roll(self, explode=False, rrtH = False, rrtL = False):
        res = randint(self._minValue, self._maxValue)

        if explode:
            total_res = res
            while res == self._maxValue:

                total_res += res
            res = total_res
            del total_res

        res = 0
        while res == 0 or explode:
            roll = randint(self._minValue, self._maxValue)
            if rrtH and not rrtL:
                #Like advantage in D&D 5e
                roll = max(roll, randint(self._minValue, self._maxValue))
            elif not rrtH and rrtL:
                #Like advantage in D&D 5e
                roll = min(roll, randint(self._minValue, self._maxValue))
            elif rrtH and rrtL:
                #Like hitos rolls
                l = [roll, randint(self._minValue, self._maxValue), randint(self._minValue, self._maxValue)]
                l.sort()
                roll = l[1]
                del l
            res += roll
            if roll == self._maxValue:
                continue
            break

        return res

class DiceRoller():

    def __init__(self):
        try:
            self._d10 = Dice(1,10)
            self._d5 = Dice(1, 5)
            self._d100 = Dice(1, 100)
            writeLog("Dices created succesfully")
        except Exception as e:
            writeLogErr("Error loading DiceRoller Class.\n{}".format(e))

    def GetDice(self, size=100):
        dice = None
        if size == '10':
            dice = self._d10
        elif size == '5':
            dice = self._d5
        elif size == '100':
            dice = self._d100

        return dice

    def MakeARoll(self, format="", explode = False, rrtH = False, rrtL = False):

        format.lower()
        if format == "":
            return None
        rolls = format.split("{")[1:]
        for roll in rolls:
            val = 0
            roll = roll.split('}')[0]
            n_dices, dice  = roll.split('d')[0], self.GetDice(roll.split('d')[1])

            for i in range(int(n_dices)):
                val += dice.Roll(explode=explode, rrtH=rrtH, rrtL=rrtL)

            format = format.replace("{" + roll + '}', str(val))

        return Calculate(format)

'''
TEST SIDE
'''
'''
from time import sleep

dr = DiceRoller()
for i in range(10):
    print(dr.MakeARoll("{1d10} + 3", explode=True, rrtH=True))
    sleep(2)

'''
'''
END OF TEST SIDE
'''