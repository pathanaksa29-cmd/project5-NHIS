CREATE DATABASE telecom1_project;

USE telecom1_project;
#Create table
CREATE TABLE user_satisfaction (

    MSISDN_Number VARCHAR(30),

    engagement_score DOUBLE,

    experience_score DOUBLE,

    satisfaction_score DOUBLE

);
 
USE telecom1_project;

#Top 10 records
SELECT * FROM user_satisfaction
LIMIT 10;

#Total record count
SELECT COUNT(*) AS Total_Records
FROM user_satisfaction;

#Average Satisfaction score
SELECT AVG(satisfaction_score) AS Average_Satisfaction
FROM user_satisfaction;

#Top 10 satisfier user
SELECT *
FROM user_satisfaction
ORDER BY satisfaction_score DESC
LIMIT 10;

#Miximum
SELECT MAX(satisfaction_score) AS Maximum_Satisfaction
FROM user_satisfaction;

#Minimum
SELECT MIN(satisfaction_score) AS Minimum_Satisfaction
FROM user_satisfaction;

#Top 10 satisfier user
SELECT *
FROM user_satisfaction
ORDER BY satisfaction_score DESC
LIMIT 10;

#Average Engagement score
SELECT AVG(engagement_score) AS Average_Engagement
FROM user_satisfaction;

#Average Experience score
SELECT AVG(experience_score) AS Average_Experience
FROM user_satisfaction;

#Top 5 score by experience
SELECT
MSISDN_Number,
engagement_score
FROM user_satisfaction
ORDER BY engagement_score DESC
LIMIT 5;

#Top 5 experience score
SELECT
MSISDN_Number,
experience_score
FROM user_satisfaction
ORDER BY experience_score DESC
LIMIT 5;

# Users Having Satisfaction Score Greater Than Average
SELECT *
FROM user_satisfaction
WHERE satisfaction_score >
(
SELECT AVG(satisfaction_score)
FROM user_satisfaction 
);
