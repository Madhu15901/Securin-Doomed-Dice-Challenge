Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

def calculate_probabilities(Die_A, Die_B):
    total_combinations = len(Die_A) * len(Die_B)
    sums = {i+j: 0 for i in Die_A for j in Die_B}
    for i in Die_A:
        for j in Die_B:
            sums[i+j] += 1
    probabilities = {key: val / total_combinations for key, val in sums.items()}
    return probabilities

print("\nOriginal Probabilities:")
original_probabilities = calculate_probabilities(Die_A, Die_B)
for key, val in original_probabilities.items():
    print(f"P(Sum = {key})  Probability = {val}")
print("\n")

def find_dice_possibility(number, temp, dice_list, limit):
    if number > limit or len(temp) > 6:
        return
    if len(temp) == 6 and temp not in dice_list:
        dice_list.append(temp)
    for i in range(number, limit + 1):
        find_dice_possibility(i, temp + [i], dice_list, limit)

def undoom_dice():
    diceA, diceB = [], []
    for i in range(1, 5):
        find_dice_possibility(i, [i], diceA, 5)
    for j in range(1, 11):
        find_dice_possibility(j, [j], diceB, 12)
    for i in diceA:
        for j in diceB:
            if calculate_probabilities(i, j) == original_probabilities:
                return i, j

New_Die_A, New_Die_B = undoom_dice()
print(f"New Dice A -> {New_Die_A}")
print(f"New Dice B -> {New_Die_B}")

print("\nProbability of Dice After Transforming:")
new_probabilities = calculate_probabilities(New_Die_A, New_Die_B)
for key, val in new_probabilities.items():
    print(f"P(Sum = {key})  Probability = {val}")
