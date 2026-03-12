-- Select the database
USE loan_datas;

-- Preview dataset
SELECT *
FROM loan_datas
LIMIT 10;

-- Total number of loans
SELECT COUNT(*) AS total_loans
FROM loan_datas;

-- Default distribution
SELECT `default`, COUNT(*) AS total
FROM loan_datas
GROUP BY `default`;

-- Top borrowers with highest missed payments
SELECT loan_id, credit_score, past_due_payments
FROM loan_datas
ORDER BY past_due_payments DESC
LIMIT 10;

-- Default rate percentage
SELECT 
AVG(`default`) * 100 AS default_rate_percent
FROM loan_datas;

-- Average income of defaulters
SELECT AVG(income) AS avg_income_defaulters
FROM loan_datas
WHERE `default` = 1;

-- Default rate by loan type
SELECT loan_type,
AVG(`default`) AS default_rate
FROM loan_datas
GROUP BY loan_type;

-- Credit score vs default
SELECT credit_score, `default`
FROM loan_datas
ORDER BY credit_score;