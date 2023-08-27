import webbrowser

# Define subject names and corresponding abbreviations
subject_names = {
    'm': 'math',
    'e': 'english',
    'p': 'physics',
    'c': 'chemistry'
}

# Take subject name from the user
user = input("Enter subject name: ").lower().strip()
print()

# Validate the subject name
if user in subject_names.values():
    subject = user
else:
    # Check the first letter of the input and map it to subject name
    abbreviation = user[0]
    subject = subject_names.get(abbreviation)
    if subject is None:
        print('Invalid input')
        exit()

part = int(input("part 1 or part 2:"))
if part in [1,2]:
    pass
else:
    print("Invalid input")

# Create the subject and part combination
subject_part = f'{subject}{part}'

print()

try:
    # Take input for lesson number
    lesson = int(input("Enter lesson number or enter 0 for answer: "))
except ValueError:
    lesson = 1

# Define valid lesson ranges for each subject and part
lesson_ranges = {
    'math1': range(1, 7),
    'math2': range(1, 8),
    'english1': range(1, 15),
    'english2': range(1, 9),
    'physics1': range(1, 9),
    'physics2': range(1, 7),
    'chemistry1': range(1, 10),
    'chemistry2': range(1, 8)
}

# Validate the lesson number based on subject and part
if lesson != 0 and lesson not in lesson_ranges.get(subject_part, [1]):
    lesson = 1

print()

# Define the book and answer URLs
book_urls = {
    'math1': f'lemh1={lesson}-6',
    'math2': f'lemh2={lesson}-7',
    'english1': f'lefl1={lesson}-14',
    'english2': f'levt1={lesson}-8',
    'physics1': f'leph1={lesson}-8',
    'physics2': f'leph2={lesson}-6',
    'chemistry1': f'lech1={lesson}-9',
    'chemistry2': f'lech2={lesson}-7'
}

answer_urls = {
    'math1': 'lemh1=an-6',
    'math2': 'lemh2=an-7',
    'english1': 'lefl1=ps-14',
    'english2': 'levt1=ps-8',
    'physics1': 'leph1=an-8',
    'physics2': 'leph2=an-6',
    'chemistry1': 'lech1=an-9',
    'chemistry2': 'lech2=an-7'
}

# Determine the URL based on lesson input
if lesson != 0:
    url = f"https://ncert.nic.in/textbook.php?{book_urls[subject_part]}"
else:
    url = f"https://ncert.nic.in/textbook.php?{answer_urls[subject_part]}"

try:
    # Open the URL in a web browser
    webbrowser.open(url)
except Exception:
    print('Please check your internet connection')
    exit()

