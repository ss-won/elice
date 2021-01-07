-- 아래에 미션을 수행하는 코드를 작성해 봅시다.
-- 1
SELECT * from shareholder;
-- 2
SELECT * from shareholder
WHERE stock >= 100000;
-- 3
SELECT stock from shareholder
WHERE name IN('Alexis', 'Craig', 'Fred');
-- 4
SELECT name, stock from shareholder
WHERE agree=0 and stock >= 100000;
-- 5
SELECT name, stock from shareholder
WHERE agree=1 and stock >= 100000;
-- 6
SELECT * from shareholder
WHERE stock >= 200000 or stock <= 100000;