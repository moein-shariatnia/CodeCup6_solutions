-- Section1
SELECT p.title as p_title, c.title as c_title
FROM problems p
JOIN submissions s
	ON s.problem_id = p.id
JOIN contests c
	ON p.contest_id = c.id
GROUP BY p.id
ORDER BY COUNT(p.id) DESC, p_title ASC, c_title ASC;


-- Section2
SELECT c.title as title, COUNT(DISTINCT s.user_id) as amount
FROM contests c
JOIN problems p
	ON p.contest_id = c.id
JOIN submissions s
	ON s.problem_id = p.id
GROUP BY c.id
ORDER BY COUNT(DISTINCT s.user_id) DESC, c.title ASC;

-- Section3
SELECT u.name AS name, SUM(t.p_score) AS score
FROM (
SELECT s.user_id AS user_id, p.id, MAX(s.score) AS p_score
FROM contests c
JOIN problems p
	ON p.contest_id = c.id
JOIN submissions s
	ON p.id = s.problem_id
WHERE c.title = 'mahale'
GROUP BY s.user_id, p.id) t
JOIN users u
	ON t.user_id = u.id

GROUP BY t.user_id
ORDER BY SUM(t.p_score) DESC, u.name ASC;

-- Section4
SELECT u.name as name, SUM(ta.c_sum) as score
FROM 
(SELECT t.c_id, t.u_id, SUM(t.p_score) AS c_sum
FROM
(SELECT c.id AS c_id, s.user_id AS u_id, p.id AS p_id, MAX(s.score) AS p_score
FROM contests c
JOIN problems p
	ON p.contest_id = c.id
JOIN submissions s
	ON p.id = s.problem_id

GROUP BY c.id, s.user_id, p.id) t
GROUP BY t.p_id) ta
JOIN users u
	ON ta.u_id = u.id
GROUP BY ta.c_id
ORDER BY score DESC, name ASC;

-- Section5
UPDATE contests
SET title = 'Mosabeghe Mahale'
WHERE title = 'mahale';

-- Section6
DELETE FROM contests
WHERE contests.id IN (SELECT cid FROM (
SELECT c.id as cid
FROM contests c
LEFT JOIN problems p
	ON p.contest_id = c.id
LEFT JOIN submissions s
	ON p.id = s.problem_id
GROUP BY c.id
HAVING COALESCE(COUNT(s.id), 0) = 0) t);
