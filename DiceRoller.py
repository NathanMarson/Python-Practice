from random import randint

def main():
    statArray = generateStats()
    print("Your stats are Strength: {} Dexterity: {} Constitution: {} Intelligence: {} Wisdom: {} Charisma: {}".format(
        statArray[0], statArray[1], statArray[2], statArray[3], statArray[4], statArray[5]))

def generateStats():
    statArray = []
    rolls = []
    for i in range(1, 7, 1):
        for x in range(1, 5, 1):
            rolls.append(randint(1, 6))
        rolls.remove(min(rolls))
        statArray.append(sum(rolls))
        rolls.clear()
    return statArray


main()
