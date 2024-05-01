-- Write query to get number of graded assignments for each student:
-- why count (*) ?? heres why! https://youtu.be/H6juZ8c_Nu8
  SELECT student_id, COUNT(*) AS graded_count
  FROM assignments
  WHERE state is "GRADED"
  GROUP BY student_id
  ORDER by student_id ASC;
 
  