-- Write query to get number of graded assignments for each student:
  SELECT student_id, COUNT(*) AS graded_count
  FROM assignments
  WHERE state is "GRADED"
  GROUP BY student_id;
  -- ORDER BY student_id ASC;
  