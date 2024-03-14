# 1. How many total combinations are possible? Show the math along with the code!
total_combinations = 6 * 6
print(f'\nTotal Combinations Possible with 2 Dice: C= n * n = {total_combinations}')

# 2. Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!

distribution = [[(i, j) for j in range(1, 7)] for i in range(1, 7)]

print('\nDistribution Matrix for 2 Dice:')
for row in distribution:
    print(row)

# 3. Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).

sum_distribution = [[i + j for j in range(1, 7)] for i in range(1, 7)]

print('\nSum Distribution Matrix for 2 Dice:')
for row in sum_distribution:
    print(row)

# Calculate and print the probability distribution for all possible sums
print('\nProbability Distribution for all possible Sums:')
for i in range(2, 13):
    combinations = sum(1 for row in sum_distribution for val in row if val == i)
    probability = combinations / total_combinations
    probability_percentage = format(probability * 100, '.2f')
    print(f'P(Sum = {i}): {probability} => {probability_percentage}')
