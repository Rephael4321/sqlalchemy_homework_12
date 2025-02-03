count_students_query = """
SELECT COUNT(*) FROM Students;
"""

average_ages_query = """
SELECT AVG(age) FROM Students;
"""

insert_student_query = """
INSERT INTO Students (name, age, email)  
VALUES (:name, :age, :email)
RETURNING id;
"""
