import unittest
import pandas as pd
from functions import analyze_data, assign_grade, get_summary

class StudentAnalyticsTests(unittest.TestCase):
    def test_grade_boundaries(self):
        self.assertEqual(assign_grade(90), "A+")
        self.assertEqual(assign_grade(80), "A")
        self.assertEqual(assign_grade(70), "B")
        self.assertEqual(assign_grade(60), "C")
        self.assertEqual(assign_grade(50), "D")
        self.assertEqual(assign_grade(49.99), "F")

    def test_average_and_result(self):
        data = pd.DataFrame([{
            "Student_ID": 1, "Name": "Test", "Department": "CSE",
            "Python": 80, "Mathematics": 70, "Statistics": 90, "AI": 85,
            "Attendance": 90
        }])
        result = analyze_data(data)
        self.assertEqual(result.loc[0, "Total_Marks"], 325)
        self.assertEqual(result.loc[0, "Average_Marks"], 81.25)
        self.assertEqual(result.loc[0, "Result"], "Pass")

    def test_summary_counts(self):
        data = pd.DataFrame([{
            "Student_ID": 1, "Name": "Test", "Department": "CSE",
            "Python": 80, "Mathematics": 70, "Statistics": 90, "AI": 85,
            "Attendance": 90
        }])
        result = analyze_data(data)
        summary = get_summary(result)
        self.assertEqual(summary["total_students"], 1)
        self.assertEqual(summary["passed"], 1)
        self.assertEqual(summary["failed"], 0)

if __name__ == "__main__":
    unittest.main()
