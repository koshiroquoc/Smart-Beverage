-- Schema for May Dinh Duong (Smart-Beverage)
-- This file creates the database and minimum tables needed by ngay22.py.

CREATE DATABASE IF NOT EXISTS maydinhduong
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE maydinhduong;

-- Core users table
CREATE TABLE IF NOT EXISTS users (
  ID INT PRIMARY KEY,
  NAME VARCHAR(100) NOT NULL,
  PHONE VARCHAR(32),
  STATUS INT NULL,
  VAR INT NULL,
  HEALTH INT NULL
);

-- Weekly report table
CREATE TABLE IF NOT EXISTS weekreport (
  ID INT PRIMARY KEY,
  Monday VARCHAR(100) DEFAULT NULL,
  Tuesday VARCHAR(100) DEFAULT NULL,
  Wednesday VARCHAR(100) DEFAULT NULL,
  Thursday VARCHAR(100) DEFAULT NULL,
  Friday VARCHAR(100) DEFAULT NULL
);

-- Summary table (9 combinations: 3 drinks x 3 sugar levels)
CREATE TABLE IF NOT EXISTS tongket (
  TYPE VARCHAR(2) PRIMARY KEY,
  USED INT NOT NULL DEFAULT 0
);

-- Optional table used in some sample scripts
CREATE TABLE IF NOT EXISTS drink (
  `Sữa tươi` INT DEFAULT 0,
  `Sữa đậu` INT DEFAULT 0,
  `Nước cam` INT DEFAULT 0
);

-- Seed tongket rows if empty
INSERT INTO tongket (TYPE, USED)
SELECT * FROM (
  SELECT '00' AS TYPE, 0 AS USED UNION ALL
  SELECT '01', 0 UNION ALL
  SELECT '02', 0 UNION ALL
  SELECT '10', 0 UNION ALL
  SELECT '11', 0 UNION ALL
  SELECT '12', 0 UNION ALL
  SELECT '20', 0 UNION ALL
  SELECT '21', 0 UNION ALL
  SELECT '22', 0
) AS seed
WHERE NOT EXISTS (SELECT 1 FROM tongket);

-- Optional: sample row for drink table
INSERT INTO drink (`Sữa tươi`, `Sữa đậu`, `Nước cam`)
SELECT 0, 0, 0
WHERE NOT EXISTS (SELECT 1 FROM drink);
