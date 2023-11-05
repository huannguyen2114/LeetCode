/* Write your T-SQL query statement below */
SELECT S.student_id, S.student_name, Su.subject_name, COUNT(Examinations.subject_name) AS attended_exams from (Students AS S cross join Subjects AS Su) LEFT JOIN Examinations ON S.student_id = Examinations.student_id AND Su.subject_name = Examinations.subject_name GROUP BY S.student_id, S.student_name, Su.subject_name;