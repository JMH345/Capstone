
```SQL
-- 2008_2000_combination

CREATE TABLE Elect_2020_comb
AS
SELECT *
FROM Gen_Elect_Results_2020_csv
LEFT JOIN "2010_appro_table_csv"
ON Gen_Elect_Results_2020_csv.State = "2010_appro_table_csv".State

-- 2012_2010_combination

CREATE TABLE Elect_2012_comb
AS
SELECT *
FROM Gen_Elect_Results_2012_csv
LEFT JOIN "2010_appro_table_csv"
ON Gen_Elect_Results_2012_csv.State = "2010_appro_table_csv".State

-- 2016_2010_combination

CREATE TABLE Elect_2016_comb
AS
SELECT *
FROM Gen_Elect_Results_2016_csv
LEFT JOIN "2010_appro_table_csv"
ON Gen_Elect_Results_2016_csv.State = "2010_appro_table_csv".State

-- 2020_2010_combination

CREATE TABLE Elect_2020_comb
AS
SELECT *
FROM Gen_Elect_Results_2020_csv
LEFT JOIN "2010_appro_table_csv"
ON Gen_Elect_Results_2020_csv.State = "2010_appro_table_csv".State

```

```SQL
-- get_total_votes_2008

CREATE TABLE TOTAL_V_2008
AS
SELECT STATE, `TOTAL VOTES #`
FROM Elect_2008_comb
WHERE `TOTAL VOTES #` IS NOT NULL

-- get_total_votes_2012

CREATE TABLE TOTAL_V_2012
AS
SELECT STATE, `TOTAL VOTES #`
FROM Elect_2012_comb
WHERE `TOTAL VOTES #` IS NOT NULL

-- get_total_votes_2016

CREATE TABLE TOTAL_V_2016
AS
SELECT STATE, `TOTAL VOTES #`
FROM Elect_2016_comb
WHERE `TOTAL VOTES #` IS NOT NULL

-- get_total_votes_2020

CREATE TABLE TOTAL_V_2020
AS
SELECT STATE, `TOTAL VOTES #`
FROM Elect_2020_comb
WHERE `TOTAL VOTES #` IS NOT NULL

```

```SQL
-- Returned total_votes_2008 as new columns

CREATE TABLE Elect_2008_ALL
AS
SELECT Elect_2008_comb.*, TOTAL_V_2008.State as "state2", TOTAL_V_2008.`TOTAL VOTES #` as "VOTE_TOTALS"
FROM Elect_2008_comb
LEFT JOIN TOTAL_V_2008
ON Elect_2008_comb.State = TOTAL_V_2008.State

-- Returned total_votes_2012 as new columns

CREATE TABLE Elect_2012_ALL
AS
SELECT Elect_2012_comb.*, TOTAL_V_2012.State as "state2", TOTAL_V_2012.`TOTAL VOTES #` as "VOTE_TOTALS"
FROM Elect_2012_comb
LEFT JOIN TOTAL_V_2012
ON Elect_2012_comb.State = TOTAL_V_2012.State

-- Returned total_votes_2016 as new columns

CREATE TABLE Elect_2016_ALL
AS
SELECT Elect_2016_comb.*, TOTAL_V_2016.State as "state2", TOTAL_V_2016.`TOTAL VOTES #` as "VOTE_TOTALS"
FROM Elect_2016_comb
LEFT JOIN TOTAL_V_2016
ON Elect_2016_comb.State = TOTAL_V_2016.State

-- Returned total_votes_2020 as new columns

CREATE TABLE Elect_2020_ALL
AS
SELECT Elect_2020_comb.*, TOTAL_V_2020.State as "state2", TOTAL_V_2020.`TOTAL VOTES #` as "VOTE_TOTALS"
FROM Elect_2020_comb
LEFT JOIN TOTAL_V_2020
ON Elect_2020_comb.State = TOTAL_V_2020.State

```

```SQL

-- Remove Rows not representing candidates 2008

CREATE TABLE Cleaned_Elect_2008
AS
Select *
FROM Elect_2008_ALL
WHERE `LAST NAME;  FIRST` IS NOT NULL

-- Remove Rows not representing candidates 2012

CREATE TABLE Cleaned_Elect_2012
AS
Select *
FROM Elect_2012_ALL
WHERE `LAST NAME;  FIRST` IS NOT NULL

-- Remove Rows not representing candidates 2016

CREATE TABLE Cleaned_Elect_2016
AS
Select *
FROM Elect_2016_ALL
WHERE `LAST NAME;  FIRST` IS NOT NULL

-- Remove Rows not representing candidates 2020

CREATE TABLE Cleaned_Elect_2020
AS
Select *
FROM Elect_2020_ALL
WHERE `LAST NAME;  FIRST` IS NOT NULL

```

```SQL

-- Data to be transferred 2008

CREATE TABLE Transfer_table_2008 AS
SELECT `STATE`, `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`Apportionment population` AS "Apportionment_pop",`"` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2008

-- Data to be transferred 2012

CREATE TABLE Transfer_table_2012 AS
SELECT `STATE`, `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`2010: Apportionment population` AS "Apportionment_pop",`"2010:` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2012

-- Data to be transferred 2016

CREATE TABLE Transfer_table_2016 AS
SELECT `STATE`, `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`2010: Apportionment population` AS "Apportionment_pop",`"2010:` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2016

-- Data to be transferred 2020

CREATE TABLE Transfer_table_2020 AS
SELECT `STATE`, `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`2010: Apportionment population` AS "Apportionment_pop",`"2010:` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2020

```

<!-- into Python
Out of Python -->


```SQL

-- Create Remainder Table 2008

CREATE TABLE Remainder2008
AS
SELECT STATE, CAST(FLOOR((SUM(CapEC_NE_CanRemainder)/CapEC_NE_VotePop)) AS REAL) as "CapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(CapEC_Full_CanRemainder)/CapEC_Full_VotePop)) AS REAL) as "CapEC_Full_CanRemVote",
CAST(FLOOR((SUM(UnCapEC_NE_CanRemainder)/UnCapEC_NE_VotePop)) AS REAL) as "UnCapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(UnCapEC_Full_CanRemainder)/UnCapEC_Full_VotePop)) AS REAL) as "UnCapEC_Full_CanRemVote"
FROM LG_Elect2008
GROUP BY STATE


-- Create Remainder Table 2012

CREATE TABLE Remainder2012
AS
SELECT STATE, CAST(FLOOR((SUM(CapEC_NE_CanRemainder)/CapEC_NE_VotePop)) AS REAL) as "CapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(CapEC_Full_CanRemainder)/CapEC_Full_VotePop)) AS REAL) as "CapEC_Full_CanRemVote",
CAST(FLOOR((SUM(UnCapEC_NE_CanRemainder)/UnCapEC_NE_VotePop)) AS REAL) as "UnCapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(UnCapEC_Full_CanRemainder)/UnCapEC_Full_VotePop)) AS REAL) as "UnCapEC_Full_CanRemVote"
FROM LG_Elect2012
GROUP BY STATE


-- Create Remainder Table 2016

CREATE TABLE Remainder2016
AS
SELECT STATE, CAST(FLOOR((SUM(CapEC_NE_CanRemainder)/CapEC_NE_VotePop)) AS REAL) as "CapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(CapEC_Full_CanRemainder)/CapEC_Full_VotePop)) AS REAL) as "CapEC_Full_CanRemVote",
CAST(FLOOR((SUM(UnCapEC_NE_CanRemainder)/UnCapEC_NE_VotePop)) AS REAL) as "UnCapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(UnCapEC_Full_CanRemainder)/UnCapEC_Full_VotePop)) AS REAL) as "UnCapEC_Full_CanRemVote"
FROM LG_Elect2016
GROUP BY STATE

GROUP BY STATE

-- Create Remainder Table 2020

CREATE TABLE Remainder2020
AS
SELECT STATE, CAST(FLOOR((SUM(CapEC_NE_CanRemainder)/CapEC_NE_VotePop)) AS REAL) as "CapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(CapEC_Full_CanRemainder)/CapEC_Full_VotePop)) AS REAL) as "CapEC_Full_CanRemVote",
CAST(FLOOR((SUM(UnCapEC_NE_CanRemainder)/UnCapEC_NE_VotePop)) AS REAL) as "UnCapEC_NE_CanRemVote", 
CAST(FLOOR((SUM(UnCapEC_Full_CanRemainder)/UnCapEC_Full_VotePop)) AS REAL) as "UnCapEC_Full_CanRemVote"
FROM LG_Elect2020
GROUP BY STATE


```

```SQL

-- Join Remainder Tables to LG_tables 2008

CREATE TABLE LG_Remain2008
AS
SELECT LG_Elect2008.*, Remainder2008.CapEC_NE_CanRemVote, Remainder2008.CapEC_Full_CanRemVote,
Remainder2008.UnCapEC_NE_CanRemVote, Remainder2008.UnCapEC_Full_CanRemVote
FROM LG_Elect2008
LEFT JOIN Remainder2008
ON LG_Elect2008.State = Remainder2008.State

-- Join Remainder Tables to LG_tables 2012

CREATE TABLE LG_Remain2012
AS
SELECT LG_Elect2012.*, Remainder2012.CapEC_NE_CanRemVote, Remainder2012.CapEC_Full_CanRemVote,
Remainder2012.UnCapEC_NE_CanRemVote, Remainder2012.UnCapEC_Full_CanRemVote
FROM LG_Elect2012
LEFT JOIN Remainder2012
ON LG_Elect2012.State = Remainder2012.State

-- Join Remainder Tables to LG_tables 2016

CREATE TABLE LG_Remain2016
AS
SELECT LG_Elect2016.*, Remainder2016.CapEC_NE_CanRemVote, Remainder2016.CapEC_Full_CanRemVote,
Remainder2016.UnCapEC_NE_CanRemVote, Remainder2016.UnCapEC_Full_CanRemVote
FROM LG_Elect2016
LEFT JOIN Remainder2016
ON LG_Elect2016.State = Remainder2016.State

-- Join Remainder Tables to LG_tables 2008

CREATE TABLE LG_Remain2020
AS
SELECT LG_Elect2020.*, Remainder2020.CapEC_NE_CanRemVote, Remainder2020.CapEC_Full_CanRemVote,
Remainder2020.UnCapEC_NE_CanRemVote, Remainder2020.UnCapEC_Full_CanRemVote
FROM LG_Elect2020
LEFT JOIN Remainder2020
ON LG_Elect2020.State = Remainder2020.State

```
```SQL

-- Adding_CapEC_NE_Remainder 2008 Table

CREATE TABLE Add_CapEC_NE_Remainder_2008
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_NE_CanRemainder DESC) AS REAL) AS CapEC_NE_CanRemain_Rank,
CapEC_NE_CanRemVote
FROM LG_Remain2008
)
SELECT *,
CASE
WHEN Practice.CapEC_NE_CanRemain_Rank <= Practice.CapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_NE_Remainder
FROM Practice

-- Adding_CapEC_NE_Remainder 2012 Table

CREATE TABLE Add_CapEC_NE_Remainder_2012
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_NE_CanRemainder DESC) AS REAL) AS CapEC_NE_CanRemain_Rank,
CapEC_NE_CanRemVote
FROM LG_Remain2012
)
SELECT *,
CASE
WHEN Practice.CapEC_NE_CanRemain_Rank <= Practice.CapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_NE_Remainder
FROM Practice

-- Adding_CapEC_NE_Remainder 2016 Table

CREATE TABLE Add_CapEC_NE_Remainder_2016
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_NE_CanRemainder DESC) AS REAL) AS CapEC_NE_CanRemain_Rank,
CapEC_NE_CanRemVote
FROM LG_Remain2016
)
SELECT *,
CASE
WHEN Practice.CapEC_NE_CanRemain_Rank <= Practice.CapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_NE_Remainder
FROM Practice

-- Adding_CapEC_NE_Remainder 2020 Table

CREATE TABLE Add_CapEC_NE_Remainder_2020
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_NE_CanRemainder DESC) AS REAL) AS CapEC_NE_CanRemain_Rank,
CapEC_NE_CanRemVote
FROM LG_Remain2020
)
SELECT *,
CASE
WHEN Practice.CapEC_NE_CanRemain_Rank <= Practice.CapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_NE_Remainder
FROM Practice

```

```SQL 

-- Adding_CapEC_Full_Remainder 2008 Table

CREATE TABLE Add_CapEC_Full_Remainder_2008
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_Full_CanRemainder DESC) AS REAL) AS CapEC_Full_CanRemain_Rank,
CapEC_Full_CanRemVote
FROM LG_Remain2008
)
SELECT *,
CASE
WHEN Practice.CapEC_Full_CanRemain_Rank <= Practice.CapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_Full_Remainder
FROM Practice


-- Adding_CapEC_Full_Remainder 2012 Table

CREATE TABLE Add_CapEC_Full_Remainder_2012
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_Full_CanRemainder DESC) AS REAL) AS CapEC_Full_CanRemain_Rank,
CapEC_Full_CanRemVote
FROM LG_Remain2012
)
SELECT *,
CASE
WHEN Practice.CapEC_Full_CanRemain_Rank <= Practice.CapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_Full_Remainder
FROM Practice

-- Adding_CapEC_Full_Remainder 2016 Table

CREATE TABLE Add_CapEC_Full_Remainder_2016
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_Full_CanRemainder DESC) AS REAL) AS CapEC_Full_CanRemain_Rank,
CapEC_Full_CanRemVote
FROM LG_Remain2016
)
SELECT *,
CASE
WHEN Practice.CapEC_Full_CanRemain_Rank <= Practice.CapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_Full_Remainder
FROM Practice

-- Adding_CapEC_Full_Remainder 2020 Table

CREATE TABLE Add_CapEC_Full_Remainder_2020
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
CapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY CapEC_Full_CanRemainder DESC) AS REAL) AS CapEC_Full_CanRemain_Rank,
CapEC_Full_CanRemVote
FROM LG_Remain2020
)
SELECT *,
CASE
WHEN Practice.CapEC_Full_CanRemain_Rank <= Practice.CapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_CapEC_Full_Remainder
FROM Practice

```

```SQL

-- Adding_UnCapEC_NE_Remainder 2008 Table

CREATE TABLE Add_UnCapEC_NE_Remainder_2008
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_NE_CanRemainder DESC) AS REAL) AS UnCapEC_NE_CanRemain_Rank,
UnCapEC_NE_CanRemVote
FROM LG_Remain2008
)
SELECT *,
CASE
WHEN Practice.UnCapEC_NE_CanRemain_Rank <= Practice.UnCapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_NE_Remainder
FROM Practice

-- Adding_UnCapEC_NE_Remainder 2012 Table

CREATE TABLE Add_UnCapEC_NE_Remainder_2012
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_NE_CanRemainder DESC) AS REAL) AS UnCapEC_NE_CanRemain_Rank,
UnCapEC_NE_CanRemVote
FROM LG_Remain2012
)
SELECT *,
CASE
WHEN Practice.UnCapEC_NE_CanRemain_Rank <= Practice.UnCapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_NE_Remainder
FROM Practice

-- Adding_UnCapEC_NE_Remainder 2016 Table

CREATE TABLE Add_UnCapEC_NE_Remainder_2016
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_NE_CanRemainder DESC) AS REAL) AS UnCapEC_NE_CanRemain_Rank,
UnCapEC_NE_CanRemVote
FROM LG_Remain2016
)
SELECT *,
CASE
WHEN Practice.UnCapEC_NE_CanRemain_Rank <= Practice.UnCapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_NE_Remainder
FROM Practice

-- Adding_UnCapEC_NE_Remainder 2020 Table

CREATE TABLE Add_UnCapEC_NE_Remainder_2020
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_NE_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_NE_CanRemainder DESC) AS REAL) AS UnCapEC_NE_CanRemain_Rank,
UnCapEC_NE_CanRemVote
FROM LG_Remain2020
)
SELECT *,
CASE
WHEN Practice.UnCapEC_NE_CanRemain_Rank <= Practice.UnCapEC_NE_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_NE_Remainder
FROM Practice

```

```SQL

-- Adding_UnCapEC_Full_Remainder 2020 Table

CREATE TABLE Add_UnCapEC_Full_Remainder_2008
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_Full_CanRemainder DESC) AS REAL) AS UnCapEC_Full_CanRemain_Rank,
UnCapEC_Full_CanRemVote
FROM LG_Remain2008
)
SELECT *,
CASE
WHEN Practice.UnCapEC_Full_CanRemain_Rank <= Practice.UnCapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_Full_Remainder
FROM Practice

-- Adding_UnCapEC_Full_Remainder 2020 Table

CREATE TABLE Add_UnCapEC_Full_Remainder_2012
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_Full_CanRemainder DESC) AS REAL) AS UnCapEC_Full_CanRemain_Rank,
UnCapEC_Full_CanRemVote
FROM LG_Remain2012
)
SELECT *,
CASE
WHEN Practice.UnCapEC_Full_CanRemain_Rank <= Practice.UnCapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_Full_Remainder
FROM Practice

-- Adding_UnCapEC_Full_Remainder 2020 Table

CREATE TABLE Add_UnCapEC_Full_Remainder_2016
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_Full_CanRemainder DESC) AS REAL) AS UnCapEC_Full_CanRemain_Rank,
UnCapEC_Full_CanRemVote
FROM LG_Remain2016
)
SELECT *,
CASE
WHEN Practice.UnCapEC_Full_CanRemain_Rank <= Practice.UnCapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_Full_Remainder
FROM Practice

-- Adding_UnCapEC_Full_Remainder 2020 Table

CREATE TABLE Add_UnCapEC_Full_Remainder_2020
AS
WITH Practice AS (
SELECT
STATE,
Candidate_Name,
UnCapEC_Full_CanRemainder,
CAST(ROW_NUMBER() OVER (PARTITION BY STATE ORDER BY UnCapEC_Full_CanRemainder DESC) AS REAL) AS UnCapEC_Full_CanRemain_Rank,
UnCapEC_Full_CanRemVote
FROM LG_Remain2020
)
SELECT *,
CASE
WHEN Practice.UnCapEC_Full_CanRemain_Rank <= Practice.UnCapEC_Full_CanRemVote
THEN 1
ELSE 0
END AS Adding_UnCapEC_Full_Remainder
FROM Practice

```

```SQL
-- Create All Remainder Table 2008

CREATE TABLE All_Remainder_2008
AS
SELECT Add_CapEC_NE_Remainder_2008.STATE, Add_CapEC_NE_Remainder_2008.Candidate_Name, 
CAST(Add_CapEC_NE_Remainder_2008.Adding_CapEC_NE_Remainder AS REAL) as "CapEC_NE_RemainAdd",
CAST(Add_CapEC_Full_Remainder_2008.Adding_CapEC_Full_Remainder AS REAL) AS "CapEC_Full_RemainAdd",
CAST(Add_UnCapEC_NE_Remainder_2008.Adding_UnCapEC_NE_Remainder AS REAL) AS "UnCapEC_NE_RemainAdd",
CAST(Add_UnCapEC_Full_Remainder_2008.Adding_UnCapEC_Full_Remainder AS REAL) AS "UnCapEC_Full_RemainAdd"
FROM Add_CapEC_NE_Remainder_2008
INNER JOIN Add_CapEC_Full_Remainder_2008
ON Add_CapEC_NE_Remainder_2008.STATE = Add_CapEC_Full_Remainder_2008.STATE
AND Add_CapEC_NE_Remainder_2008.Candidate_Name = Add_CapEC_Full_Remainder_2008.Candidate_Name
INNER JOIN Add_UnCapEC_NE_Remainder_2008
ON Add_CapEC_NE_Remainder_2008.STATE = Add_UnCapEC_NE_Remainder_2008.STATE
AND Add_CapEC_NE_Remainder_2008.Candidate_Name = Add_UnCapEC_NE_Remainder_2008.Candidate_Name
INNER JOIN Add_UnCapEC_Full_Remainder_2008
ON Add_CapEC_NE_Remainder_2008.STATE = Add_UnCapEC_Full_Remainder_2008.STATE
AND Add_CapEC_NE_Remainder_2008.Candidate_Name = Add_UnCapEC_Full_Remainder_2008.Candidate_Name
ORDER BY Add_CapEC_NE_Remainder_2008.STATE