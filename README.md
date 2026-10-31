# Student Performance Analytics System

A beginner-friendly Python data-analysis project using Pandas and NumPy. It analyzes student marks and attendance data stored in a CSV file.

## Features
- Reads and validates student records from `students.csv`
- Calculates total and average marks
- Assigns grades using a clearly defined example grading scale
- Marks a student as Pass when every subject mark is at least 40; otherwise Fail
- Calculates class and subject averages, highest/lowest averages, and pass percentage
- Displays the top five students
- Saves detailed results to `student_analysis_results.csv`

## Technologies
- Python 3
- Pandas
- NumPy
- CSV

## Setup
Open a terminal in this folder and install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Test
```bash
python -m unittest discover -s tests -v
```

## Dataset and rules
`students.csv` contains 20 fictional practice records. The example grade bands are A+ (90–100), A (80–89.99), B (70–79.99), C (60–69.99), D (50–59.99), and F (below 50). The pass rule is at least 40 in every subject. Replace these rules if your trainer specifies different ones.

## Project documentation
See `documentation/Project_Documentation.md`. Add your own details and screenshots before final submission.

## Author
Replace this line with your name and course details.
