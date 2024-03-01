# import random

# list_of_nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# result = random.choice(list_of_nums)

# print(result)

# from datetime import date
 
# # calling the today function of date class
# today = date.today()
 
# print("Today's date is", today)




# # Importing the NumPy library with an alias 'np'
# import numpy as np

# # Creating an array of integers from 30 to 70 using np.arange()
# array = np.arange(30, 71)

# # Printing a message indicating an array of integers from 30 to 70
# print("Array of the integers from 30 to 70")

# # Printing the array of integers from 30 to 70
# print(array) 



# imports NumPy using the np alias, which is a common convention that saves you a few keystrokes.
import numpy as np

CURVE_CENTER = 80
# creates your first NumPy array, which is one-dimensional 
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12])
def curve(grades):
    # takes the average of all the scores using .mean(). Arrays have a lot of methods.
    average = grades.mean()
    change = CURVE_CENTER - average
    new_grades = grades + change
    # you limit, or clip, the values to a set of minimums and maximums. In this case, you need a function that takes an array and makes sure the values don’t exceed a given minimum or maximum. clip() does exactly that.For the second argument to clip(), you pass grades, ensuring that each newly curved grade doesn’t go lower than the original grade. But for the third argument, you pass a single value: 100. NumPy takes that value and broadcasts it against every element in new_grades, ensuring that none of the newly curved grades exceeds a perfect score.
    return np.clip(new_grades, grades, 100)

curve(grades)
array([ 91.25,  54.25,  83.25, 100.  ,  70.25, 100.  ,  93.25,  31.25])