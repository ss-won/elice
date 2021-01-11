-- 아래에 쿼리를 작성해 보세요.
SELECT stock FROM shareholder
WHERE name IN('Alexis', 'Craig', 'Fred');

SELECT name, stock FROM shareholder
WHERE agree = 0 and stock >= 100000;

SELECT name, stock FROM shareholder
WHERE agree = 1 and stock >= 100000;
