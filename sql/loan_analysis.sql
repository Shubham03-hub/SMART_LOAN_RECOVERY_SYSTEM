SELECT COUNT(*) FROM loans;

-- Default rate --
SELECT default, COUNT(*)  FROM loans
GROUP BY default;

-- Average loan amount--
SELECT AVG(loan_amount)
FROM loans;

-- Defaults by employment status--
SELECT employment_status,
COUNT(*) AS total_loans,
SUM(default) AS total_defaults
 FROM loans
 GROUP BY employment_status;

-- High risk customers--
SELECT *
FROM loans
WHERE credit_score < 600
AND past_due_payments > 3;