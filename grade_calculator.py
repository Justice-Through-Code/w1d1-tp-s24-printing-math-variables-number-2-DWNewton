import math
def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    """ I first reset all variables to 0 or to a common "Unknown" value 
    before prompting user. This is in case of a bug in a loop or if something 
    tries to use previously entered data."""
    student_name = "Unknown"
    student_name = input("Enter your first and last name: ")
    
    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    # Reset data in variables to 0
    math_score = 0
    science_score = 0
    english_score = 0
    # Then perform prompts
    math_score = int(input("Enter your Math score: "))
    science_score = int(input("Enter your Science score: "))
    english_score = int(input("Enter your English score: "))

    # Zero out the variable data
    average_grade = int(0)
    """ Calculate the average grade 
    Using PEMDAS, I group the sum of the three scores in parentheses 
    and then divide them to get the average.
    I wish I knew an efficient method to count number of test scores, 
    instead of using a hard "3" in the code, to allow for flexibility 
    in the number of courses. """
    average_grade = int((math_score + science_score + english_score) / 3)
    
    # Return the student's name and their average grade as string
    return student_name, average_grade
    
if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"{student_name}, {average_grade}")