-- Add more test users
INSERT INTO users (username, email) VALUES 
('testuser1', 'test1@example.com'),
('testuser2', 'test2@example.com'),
('testuser3', 'test3@example.com'),
('testuser4', 'test4@example.com');

-- Add comprehensive error log entries
INSERT INTO error_logs (user_id, error_type, error_message) VALUES 
-- NameError examples
(1, 'NameError', 'name variable is not defined'),
(2, 'NameError', 'name count is not defined'),

-- SyntaxError examples
(1, 'SyntaxError', 'invalid syntax'),
(3, 'SyntaxError', 'expected '':'' after function definition'),

-- TypeError examples
(2, 'TypeError', 'can''t multiply sequence by non-int of type ''float'''),
(4, 'TypeError', 'can only concatenate str (not "int") to str'),

-- IndexError examples
(1, 'IndexError', 'list index out of range'),
(3, 'IndexError', 'string index out of range'),

-- KeyError examples
(2, 'KeyError', 'dictionary key ''user'' not found'),
(4, 'KeyError', 'dictionary key ''settings'' not found'),

-- ZeroDivisionError examples
(1, 'ZeroDivisionError', 'division by zero'),
(3, 'ZeroDivisionError', 'integer division or modulo by zero'),

-- AttributeError examples
(2, 'AttributeError', 'str object has no attribute ''append'''),
(4, 'AttributeError', 'NoneType object has no attribute ''length'''),

-- ValueError examples
(1, 'ValueError', 'invalid literal for int() with base 10'),
(3, 'ValueError', 'could not convert string to float');