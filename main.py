"""Run the Student Performance Analytics System."""
from functions import SUBJECTS, analyze_data, get_summary, load_data

def main():
    try:
        raw_data = load_data()
        results = analyze_data(raw_data)
        summary = get_summary(results)

        print("=" * 58)
        print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
        print("=" * 58)
        print(f"Total students: {summary['total_students']}")
        print(f"Class average: {summary['class_average']:.2f}")
        print(f"Highest student average: {summary['highest_average']:.2f}")
        print(f"Lowest student average: {summary['lowest_average']:.2f}")
        print(f"Passed: {summary['passed']}")
        print(f"Failed: {summary['failed']}")
        print(f"Pass percentage: {summary['pass_percentage']:.2f}%")

        print("\nSUBJECT-WISE AVERAGES")
        for subject, average in summary["subject_averages"].items():
            print(f"{subject}: {average:.2f}")

        print("\nTOP 5 STUDENTS")
        print(summary["top_students"][["Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))

        print("\nSTUDENT RESULTS")
        columns = ["Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result"]
        print(results[columns].to_string(index=False))

        results.to_csv("student_analysis_results.csv", index=False)
        print("\nDetailed results saved to student_analysis_results.csv")
        print("Analysis completed successfully.")
    except FileNotFoundError:
        print("Error: students.csv was not found. Put it in the same folder as main.py.")
    except (ValueError, KeyError) as error:
        print(f"Data error: {error}")

if __name__ == "__main__":
    main()
