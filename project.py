import csv
from typing import List, Tuple

class StudentData:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.students = []
        self.load_data()

    def load_data(self) -> None:
        """Load student data from a CSV file and calculate averages."""
        with open(self.file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Calculate the average grade for each student
                grades = [
                    float(row['english.grade']),
                    float(row['math.grade']),
                    float(row['sciences.grade']),
                    float(row['language.grade'])
                ]
                average = sum(grades) / len(grades)
                student = {
                    'name': row['name'],
                    'nationality': row['nationality'],
                    'age': int(row['age']),
                    'average': average
                }
                self.students.append(student)

    def save_averages_with_names(self, output_file: str) -> None:
        """Save the averages along with the names of each student in the same order as the input file."""
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'average'])
            for student in self.students:
                writer.writerow([student['name'], student['average']])

    def save_sorted_averages(self, output_file: str) -> None:
        """Save the averages sorted in ascending order with the names."""
        sorted_students = sorted(self.students, key=lambda x: x['average'])
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'average'])
            for student in sorted_students:
                writer.writerow([student['name'], student['average']])

    def save_top_three_averages(self, output_file: str) -> None:
        """Save the top three averages with the names.""" #################
        top_three = sorted(self.students, key=lambda x: x['average'], reverse=True)[:3]
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'average'])
            for student in top_three:
                writer.writerow([student['name'], student['average']])

    def save_bottom_three_averages(self, output_file: str) -> None:
        """Save the bottom three averages without the names."""
        bottom_three = sorted(self.students, key=lambda x: x['average'])[:3]
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['average'])
            for student in bottom_three:
                writer.writerow([student['average']])

    def calculate_overall_average(self) -> float:
        """Calculate and return the overall average of all student averages."""
        total_average = sum(student['average'] for student in self.students)
        return total_average / len(self.students)

    def save_student_details_by_average(self, output_file: str) -> None:
        """Save the name, nationality, and age of each student sorted by average."""
        sorted_students = sorted(self.students, key=lambda x: x['average'])
        with open(output_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'nationality', 'age', 'average'])
            for student in sorted_students:
                writer.writerow([student['name'], student['nationality'], student['age'], student['average']])


if __name__ == "__main__":
    
    student_data = StudentData('student_dataset.csv')
    

    student_data.save_averages_with_names('averages_with_names.csv')
    
    student_data.save_sorted_averages('sorted_averages.csv')
    
    student_data.save_top_three_averages('top_three_averages.csv')
    
    student_data.save_bottom_three_averages('bottom_three_averages.csv')
    
    overall_average = student_data.calculate_overall_average()
    print("Overall average of all students:", overall_average)
    
    student_data.save_student_details_by_average('student_details_by_average.csv')
