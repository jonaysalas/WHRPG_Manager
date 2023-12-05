from random import randint
from Libraries.MathCalculator import Calculate
from Libraries.Logger import writeLog, writeLogErr

class Dice():

    def __init__(self, min, max):
        '''
        Init of the Dice Class
        :param min: Min possible value of the dice.
        :param max: Max possible value of the dice
        '''
        try:
            self._minValue = min
            self._maxValue = max
            writeLog("Dice of {} faces created succesfully".format(max))
        except Exception as e:
            writeLogErr("Error creating dice ({}, {}).\n{}".format(min, max,e))

    def Roll(self, explode=False, rrtH = False, rrtL = False):
        '''
        Simulates a roll of the dice
        :param explode: If True, another dice will be roll every time the max value of the dice is rolled
        :param rrtH: If True, an additional dice will be roll and the highest will be chosen
        :param rrtL: If True, an additional dice will be roll and the lowest will be chosen
        :return: An int value of the total result of the roll(s)
        '''
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
        '''
        Init of the class used to simulate dice rolls
        '''
        try:
            self._d10 = Dice(1,10)
            self._d5 = Dice(1, 5)
            self._d100 = Dice(1, 100)
            writeLog("Dices created succesfully")
        except Exception as e:
            writeLogErr("Error loading DiceRoller Class.\n{}".format(e))

    def GetDice(self, size=100):
        '''
        Function that returns the Dice object of the size specified
        :param size: The size of the dice you want to get. Possible values: 5, 10 & 100
        :return: returns the Dice object of the size selected or None if the dice selected is not a possible value
        '''
        dice = None
        if size == '10':
            dice = self._d10
        elif size == '5':
            dice = self._d5
        elif size == '100':
            dice = self._d100

        return dice

    def MakeARoll(self, format="", explode = False, rrtH = False, rrtL = False):
        '''
        Given a "roll formula", simulates a roll and returns the total result of the roll
        The roll formula can contains fixed modifiers like +1 or -3 and rolls like {1d10} that must
        be between keys {}. The number before the 'd' indicates the number of dices and the number
        after the 'd' indicates the size of the dice.
        Example roll formula: {1d10} -3

        :param format: An string with the formar of the roll
        :param explode: If True, another dice will be roll every time the max value of the dice is rolled
        :param rrtH: If True, an additional dice will be roll and the highest will be chosen
        :param rrtL: If True, an additional dice will be roll and the lowest will be chosen
        :return: An int value of the result of the roll
        '''
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