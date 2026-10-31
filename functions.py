
"""Reusable functions for the Student Performance Analytics System."""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "Mathematics", "Statistics", "AI"]


def load_data(path="students.csv"):
    """Load and validate student data from a CSV file."""
    data = pd.read_csv(path)

    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing = [column for column in required if column not in data.columns]

    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    if data.empty:
        raise ValueError("The dataset contains no student records.")

    for column in SUBJECTS + ["Attendance"]:
        data[column] = pd.to_numeric(data[column], errors="raise")

        if not data[column].between(0, 100).all():
            raise ValueError(f"{column} values must be between 0 and 100.")

    return data


def assign_grade(average):
    """Assign a grade based on average marks."""
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def analyze_data(data):
    """Calculate totals, averages, grades and pass/fail results."""
    result = data.copy()

    result["Total_Marks"] = result[SUBJECTS].sum(axis=1)
    result["Average_Marks"] = np.round(result[SUBJECTS].mean(axis=1), 2)
    result["Grade"] = result["Average_Marks"].apply(assign_grade)

    # Example project rule: average of 50 or above is a pass.
    result["Result"] = result["Average_Marks"].ge(50).map(
        {True: "Pass", False: "Fail"}
    )

    return result


def get_summary(data):
    """Calculate class and subject-level statistics."""
    subjects = data[SUBJECTS]
    total = len(data)
    passed = int((data["Result"] == "Pass").sum())

    return {
        "total_students": total,
        "class_average": round(float(data["Average_Marks"].mean()), 2),
        "highest_average": round(float(data["Average_Marks"].max()), 2),
        "lowest_average": round(float(data["Average_Marks"].min()), 2),
        "passed": passed,
        "failed": total - passed,
        "pass_percentage": round(passed / total * 100, 2) if total else 0.0,
        "subject_averages": subjects.mean().round(2).to_dict(),
        "top_students": data.sort_values(
            "Average_Marks", ascending=False
        ).head(5),
    }

