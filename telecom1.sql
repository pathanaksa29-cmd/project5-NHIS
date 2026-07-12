CREATE DATABASE telecom1;
USE telecom1;
SHOW DATABASES;
CREATE TABLE user_satisfaction (

    user_id BIGINT PRIMARY KEY,

    engagement_score DOUBLE,

    experience_score DOUBLE,

    satisfaction_score DOUBLE

);
SHOW TABLES;

DESCRIBE user_satisfaction;

USE telecom_project;

SELECT * FROM user_satisfaction;

SELECT COUNT(*) AS Total_Users
FROM user_satisfaction;

#Average score
SELECT
AVG(engagement_score) AS Avg_Engagement,
AVG(experience_score) AS Avg_Experience,
AVG(satisfaction_score) AS Avg_Satisfaction
FROM user_satisfaction;

#10 satisfied user
SELECT *
FROM user_satisfaction
ORDER BY satisfaction_score DESC
LIMIT 10;

#Engagement score
SELECT *
FROM user_satisfaction
ORDER BY engagement_score DESC
LIMIT 10;

#Experience score
SELECT *
FROM user_satisfaction
ORDER BY experience_score DESC
LIMIT 10;

#Lowest satisfaction score
SELECT *
FROM user_satisfaction
ORDER BY satisfaction_score ASC
LIMIT 10;

#Maximum satisfaction score
SELECT
MAX(engagement_score) AS Max_Engagement,
MAX(experience_score) AS Max_Experience,
MAX(satisfaction_score) AS Max_Satisfaction
FROM user_satisfaction;

#Minimum Score
SELECT
MIN(engagement_score) AS Min_Engagement,
MIN(experience_score) AS Min_Experience,
MIN(satisfaction_score) AS Min_Satisfaction
FROM user_satisfaction;

#Above satisfaction
SELECT *
FROM user_satisfaction
WHERE satisfaction_score >
(
SELECT AVG(satisfaction_score)
FROM user_satisfaction
);
