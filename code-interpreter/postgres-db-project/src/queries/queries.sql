-- Get all errors for a specific user
SELECT * FROM error_logs 
WHERE user_id = :user_id 
ORDER BY created_at DESC;

-- Get error count by type
SELECT error_type, COUNT(*) as error_count 
FROM error_logs 
GROUP BY error_type;