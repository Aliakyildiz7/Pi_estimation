
from math import pi


max_denumerator = 1000  # Maximum value of denumerator that will be checked. You can change this value to see results in a different upper limit of denumerator.
tolerance = 1  # Safe to say final tolerance will be lower than 1

# Initializing the searched values
searched_numerator = 0
searched_denumerator = 0

upper_limit = 3.2  # Apriori_1 : Pi is less than 3.2
# Maximum value of the fraction (numerator / denumerator) that will be checked.
# Denumerator will increase in the upcoming loop and if no fraction with difference smaller than the previous denumerator is obtained, while loop will break and next denumerator will be checked.

for denumerator in range(1, max_denumerator + 1):

    numerator = 3 * denumerator  # Apriori_2 : Pi is greater than 3


    while True:

        candidate = numerator / denumerator

        difference = abs(candidate - pi)



        if difference < tolerance:  # That means a closer fraction than the previos ones has been obtained.
            tolerance = difference  # Upcoming fractions will be required to be lower than this value

            searched_numerator = numerator
            searched_denumerator = denumerator

            upper_limit = candidate  # Upcooming fractions will be discarded if they are higher than this value.



        if numerator / denumerator > upper_limit:

            break

        else:  # Keeps searching for closer fractions in the same denumerator
            numerator += 1




print(f"Closest integer pairs are:{searched_numerator} and {searched_denumerator}")
print(f"Ratio of {searched_numerator}/{searched_denumerator} is {searched_numerator / searched_denumerator}")
print(f"Tolerance is {tolerance}")

