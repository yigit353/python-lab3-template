# ==========================================
# LAB 3: FUNCTIONS, DICTIONARIES, AND DATA STRUCTURES
# Advanced Python Course - Week 3
# ==========================================
#
# INSTRUCTIONS:
# - Section A: Complete the function bodies (skeleton provided)
# - Section B & C: Write entire functions from scratch
# - Function names MUST match exactly or tests will fail
# - Test your code by running: python test_lab3.py
# - Submit by pushing to your GitHub repository
# ==========================================

# ==========================================
# SECTION A: FUNCTIONS WITH GUIDANCE (6 points)
# Function skeleton provided - fill in the body
# ==========================================

# ==========================================
# EXERCISE 1: Temperature Converter (2 points)
# ==========================================
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: (celsius * 9/5) + 32

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit

    Example:
        celsius_to_fahrenheit(0) returns 32.0
        celsius_to_fahrenheit(100) returns 212.0
    """
    # TODO: Apply the formula (celsius * 9/5) + 32
    # TODO: Return the result

    fahrenheit = 0  # Replace this line

    return fahrenheit


# ==========================================
# EXERCISE 2: Dictionary Lookup with Default (2 points)
# ==========================================
def get_student_grade(grades, student_name):
    """
    Get a student's grade from the grades dictionary.
    If student not found, return 0.

    Args:
        grades (dict): Dictionary with student names as keys, grades as values
        student_name (str): Name of student to look up

    Returns:
        int: Student's grade, or 0 if not found

    Example:
        grades = {"Alice": 85, "Bob": 92}
        get_student_grade(grades, "Alice") returns 85
        get_student_grade(grades, "Charlie") returns 0
    """
    # TODO: Use the .get() method on the dictionary
    # TODO: Provide 0 as the default value if student not found
    # HINT: dictionary.get(key, default_value)

    grade = 0  # Replace this line

    return grade


# ==========================================
# EXERCISE 3: Format Person Information (2 points)
# ==========================================
def format_person(name, age, city):
    """
    Create a formatted string with person's information.

    Format: "Name: {name}, Age: {age}, City: {city}"

    Args:
        name (str): Person's name
        age (int): Person's age
        city (str): Person's city

    Returns:
        str: Formatted information string

    Example:
        format_person("Alice", 25, "Boston")
        returns "Name: Alice, Age: 25, City: Boston"
    """
    # TODO: Use an f-string to format the information
    # TODO: Make sure format matches exactly: "Name: X, Age: Y, City: Z"
    # HINT: f"Name: {name}, Age: {age}, City: {city}"

    formatted = ""  # Replace this line

    return formatted


# ==========================================
# SECTION B: WRITE COMPLETE FUNCTIONS (16 points)
# Write the entire function from scratch
# ==========================================

# ==========================================
# EXERCISE 4: Calculate Average (2 points)
# ==========================================
# Write a function called 'calculate_average' that:
# - Takes a list of numbers as parameter
# - Returns the average (sum divided by count)
#
# Function signature: def calculate_average(numbers):
# Parameter: numbers (list of int/float)
# Returns: float (the average)
#
# Example:
#   calculate_average([10, 20, 30]) returns 20.0
#   calculate_average([5, 10, 15, 20]) returns 12.5
#
# Hints:
# - Use sum() to add all numbers
# - Use len() to count numbers
# - Return sum / length

# TODO: Write the complete calculate_average function here


# ==========================================
# EXERCISE 5: Clean Filename (2 points)
# ==========================================
# Write a function called 'clean_filename' that:
# - Takes a filename string as parameter
# - Strips whitespace from both ends
# - Converts to lowercase
# - Returns the cleaned filename
#
# Function signature: def clean_filename(filename):
# Parameter: filename (str)
# Returns: str (cleaned filename)
#
# Example:
#   clean_filename("  MyFile.TXT  ") returns "myfile.txt"
#   clean_filename("REPORT.PDF") returns "report.pdf"
#
# Hints:
# - Use .strip() to remove whitespace
# - Use .lower() to convert to lowercase
# - Chain them together or use separate steps

# TODO: Write the complete clean_filename function here


# ==========================================
# EXERCISE 6: Count File Extensions (3 points)
# ==========================================
# Write a function called 'count_extensions' that:
# - Takes a list of filenames
# - Returns a dictionary counting how many files have each extension
# - Extension is the part after the last dot (e.g., "txt" from "file.txt")
#
# Function signature: def count_extensions(filenames):
# Parameter: filenames (list of str)
# Returns: dict with extensions as keys, counts as values
#
# Example:
#   count_extensions(["a.txt", "b.txt", "c.jpg"])
#   returns {"txt": 2, "jpg": 1}
#
# Hints:
# - Loop through each filename
# - Use .split('.')[-1] to get the extension (last part after splitting by dot)
# - Use a dictionary to count occurrences
# - Initialize count to 0 if extension not yet in dictionary

# TODO: Write the complete count_extensions function here


# ==========================================
# EXERCISE 7: Filter Passing Students (3 points)
# ==========================================
# Write a function called 'filter_passing_students' that:
# - Takes a dictionary of student names and their scores
# - Returns a new dictionary with only students who scored 60 or above
#
# Function signature: def filter_passing_students(grades):
# Parameter: grades (dict with str keys, int values)
# Returns: dict with only passing students (score >= 60)
#
# Example:
#   filter_passing_students({"Alice": 85, "Bob": 45, "Charlie": 70})
#   returns {"Alice": 85, "Charlie": 70}
#
# Hints:
# - Create a new empty dictionary
# - Loop through grades.items() to get both name and score
# - Check if score >= 60
# - Add to new dictionary if passing

# TODO: Write the complete filter_passing_students function here


# ==========================================
# EXERCISE 8: Analyze Numbers (3 points)
# ==========================================
# Write a function called 'analyze_numbers' that:
# - Takes a list of numbers
# - Returns a tuple containing (minimum, maximum, average)
#
# Function signature: def analyze_numbers(numbers):
# Parameter: numbers (list of int/float)
# Returns: tuple of (min, max, average)
#
# Example:
#   analyze_numbers([10, 50, 30, 70])
#   returns (10, 70, 40.0)
#
# Hints:
# - Use min() to find minimum
# - Use max() to find maximum
# - Calculate average as sum() / len()
# - Return all three values as a tuple: return (min_val, max_val, avg)

# TODO: Write the complete analyze_numbers function here


# ==========================================
# EXERCISE 9: Read Numbers from File (3 points)
# ==========================================
# Write a function called 'read_numbers_from_file' that:
# - Takes a filename as parameter
# - Reads the file (one number per line)
# - Returns a list of integers
#
# Function signature: def read_numbers_from_file(filename):
# Parameter: filename (str)
# Returns: list of int
#
# Example:
#   If file contains:
#   5
#   10
#   15
#   Then read_numbers_from_file("file.txt") returns [5, 10, 15]
#
# Hints:
# - Use 'with open(filename) as f:' to open the file
# - Loop through each line in the file
# - Use .strip() to remove newline characters
# - Use int() to convert string to integer
# - Append to a list

# TODO: Write the complete read_numbers_from_file function here


# ==========================================
# SECTION C: ADVANCED INTEGRATION (13 points)
# Complex functions combining multiple concepts
# ==========================================

# ==========================================
# EXERCISE 10: Shopping Cart Total (3 points)
# ==========================================
# Write a function called 'calculate_cart_total' that:
# - Takes a shopping cart dictionary
# - Each item in cart: key is item name, value is tuple of (price, quantity)
# - Returns the total cost (price × quantity for each item, summed)
#
# Function signature: def calculate_cart_total(cart):
# Parameter: cart (dict with str keys, tuple values of (float, int))
# Returns: float (total cost)
#
# Example:
#   cart = {
#       "apple": (1.5, 3),    # $1.50 each, quantity 3
#       "banana": (0.8, 5)    # $0.80 each, quantity 5
#   }
#   calculate_cart_total(cart) returns 8.5
#   Calculation: (1.5 × 3) + (0.8 × 5) = 4.5 + 4.0 = 8.5
#
# Hints:
# - Loop through cart.items() to get item name and (price, quantity) tuple
# - Unpack tuple: for item, (price, quantity) in cart.items():
# - Calculate cost for each item: price * quantity
# - Sum all costs

# TODO: Write the complete calculate_cart_total function here


# ==========================================
# EXERCISE 11: Generate Grade Report (5 points)
# ==========================================
# Write a function called 'generate_grade_report' that:
# - Takes a dictionary of student names and their numeric scores
# - Converts each score to a letter grade
# - Returns a formatted report string
#
# Grading scale:
#   A: 90-100
#   B: 80-89
#   C: 70-79
#   D: 60-69
#   F: below 60
#
# Function signature: def generate_grade_report(scores):
# Parameter: scores (dict with str keys, int values)
# Returns: str (formatted report with each student on a new line)
#
# Format for each line: "Student: {name}, Score: {score}, Grade: {letter}"
# Lines should be separated by newline character (\n)
#
# Example:
#   scores = {"Alice": 92, "Bob": 78, "Charlie": 85}
#   generate_grade_report(scores) returns:
#   "Student: Alice, Score: 92, Grade: A\nStudent: Bob, Score: 78, Grade: C\nStudent: Charlie, Score: 85, Grade: B"
#
# Hints:
# - Create a helper section or use if-elif-else to convert score to letter
# - Build the report string line by line
# - Use \n to separate lines
# - You can use a list and .join() or build string with +=

# TODO: Write the complete generate_grade_report function here


# ==========================================
# EXERCISE 12: Analyze Log File (5 points)
# ==========================================
# Write a function called 'analyze_log_file' that:
# - Reads a log file where each line is formatted as "LEVEL: message"
# - Returns a nested dictionary with statistics
#
# Function signature: def analyze_log_file(filename):
# Parameter: filename (str)
# Returns: dict with structure:
#   {
#       "total_lines": int,
#       "levels": {
#           "ERROR": count,
#           "WARNING": count,
#           "INFO": count
#       }
#   }
#
# Example:
#   If log.txt contains:
#   ERROR: Connection failed
#   INFO: Server started
#   ERROR: Timeout occurred
#   WARNING: Low memory
#
#   analyze_log_file("log.txt") returns:
#   {
#       "total_lines": 4,
#       "levels": {
#           "ERROR": 2,
#           "INFO": 1,
#           "WARNING": 1
#       }
#   }
#
# Hints:
# - Initialize result dictionary with total_lines and levels sub-dictionary
# - Initialize level counts (ERROR, WARNING, INFO) to 0
# - Open and read file line by line
# - Split each line by ": " to separate level and message
# - Use .strip() to clean lines
# - Increment appropriate counter
# - Some levels might not appear in file - keep count at 0

# TODO: Write the complete analyze_log_file function here


# ==========================================
# DO NOT MODIFY BELOW THIS LINE
# ==========================================
if __name__ == "__main__":
    print("Run 'python test_lab3.py' to test your solutions!")