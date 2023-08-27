import os
import webbrowser

# Set console color
os.system('color 0a')
print('''
      math     :   mathmatics
      eng1     :   first flight
      eng2     :   foot print
      sci      :   science
      sst1     :   contemporary india
      sst2     :   understanding economic devlopment
      sst3     :   India and the contermporary world ||
      sst4     :   Democratic politcs
      ''')
# Define subject names and corresponding abbreviations
subject_names = {
    'math': 'math',
    'eng1': 'english1',
    'eng2': 'english2',
    'sci': 'science',
    'sst1': 'sst1',
    'sst2': 'sst2',
    'sst3': 'sst3',
    'sst4': 'sst4'
}

# Take subject name from the user
user = input("Enter subject name: ").lower().strip()
print()

# Validate the subject name
if user in subject_names:
    subject = subject_names[user]
else:
    print('Invalid input')
    exit()

try:
    # Take input for lesson number
    lesson = int(input("Enter lesson number or enter 0 for answer: "))
except ValueError:
    lesson = 1

# Define valid lesson ranges for each subject
lesson_ranges = {
    'math': range(1, 15),
    'english1': range(1, 10),
    'english2': range(1, 10),
    'science': range(1, 14),
    'sst1': range(1, 8),
    'sst2': range(1, 6),
    'sst3': range(1, 6),
    'sst4': range(1, 6)
}

# Validate the lesson number based on subject
if lesson != 0 and lesson not in lesson_ranges.get(subject, [1]):
   lesson = 1

print()

# Define the book and answer URLs
book_urls = {
    'math': f'jemh1={lesson}-14',
    'english1': f'jeff1={lesson}-9',
    'english2': f'jefp1={lesson}-9',
    'science': f'jesc1={lesson}-13',
    'sst1': f'jess1={lesson}-7',
    'sst2': f'jess2={lesson}-5',
    'sst3': f'jess3={lesson}-5',
    'sst4': f'jess4={lesson}-5'
}

answer_urls = {
    'math': 'jemh1=an',
    'sci': 'jesc1=an'
}

# Determine the URL based on lesson input
if lesson != 0:
    url = f"https://ncert.nic.in/textbook.php?{book_urls[subject]}"
else:
   if subject in answer_urls:
        url = f"https://ncert.nic.in/textbook.php?{answer_urls[subject]}"
   else:
      print("No answers are present for this subject")
      quit()
      
try:
    # Open the URL in a web browser
    webbrowser.open(url)
except Exception:
    print('Please check your internet connection')
    exit()

print('Press anything except Enter to not exit.......')

