
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
SELECT `STATE`, `FEC ID` AS "FEC_ID", `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`Apportionment population` AS "Apportionment_pop",`"` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2008

-- Data to be transferred 2012

CREATE TABLE Transfer_table_2012 AS
SELECT `STATE`, `FEC ID` AS "FEC_ID", `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`2010: Apportionment population` AS "Apportionment_pop",`"2010:` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2012

-- Data to be transferred 2016

CREATE TABLE Transfer_table_2016 AS
SELECT `STATE`, `FEC ID` AS "FEC_ID", `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`2010: Apportionment population` AS "Apportionment_pop",`"2010:` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2016

-- Data to be transferred 2020

CREATE TABLE Transfer_table_2020 AS
SELECT `STATE`, `FEC ID` AS "FEC_ID", `LAST NAME;  FIRST` AS "Candidate_Name", `GENERAL RESULTS` AS "Candidate_Votes",
`2010: Apportionment population` AS "Apportionment_pop",`"2010:` AS "Num_Reps_Capped", VOTE_TOTALS AS "State_Vote_Total"
FROM Cleaned_Elect_2020

```

<!-- into Python
Out of Python -->


```SQL

-- Create Remainder Table 2008

CREATE TABLE Remainder2008
AS
SELECT STATE, Num_Reps_Capped - SUM(CapEC_NE_CanVotes)as "CapEC_NE_CanRemVote", 
(Num_Reps_Capped + 2) - SUM(CapEC_Full_CanVotes) as "CapEC_Full_CanRemVote",
Num_Reps_Uncapped - SUM(UnCapEC_NE_CanVotes) as "UnCapEC_NE_CanRemVote", 
(Num_Reps_Uncapped + 2) - SUM(UnCapEC_Full_CanVotes) as "UnCapEC_Full_CanRemVote"
FROM LG_Elect2008
GROUP BY STATE


-- Create Remainder Table 2012

CREATE TABLE Remainder2012
AS
SELECT STATE, Num_Reps_Capped - SUM(CapEC_NE_CanVotes)as "CapEC_NE_CanRemVote", 
(Num_Reps_Capped + 2) - SUM(CapEC_Full_CanVotes) as "CapEC_Full_CanRemVote",
Num_Reps_Uncapped - SUM(UnCapEC_NE_CanVotes) as "UnCapEC_NE_CanRemVote", 
(Num_Reps_Uncapped + 2) - SUM(UnCapEC_Full_CanVotes) as "UnCapEC_Full_CanRemVote"
FROM LG_Elect2012
GROUP BY STATE


-- Create Remainder Table 2016

CREATE TABLE Remainder2016
AS
SELECT STATE, Num_Reps_Capped - SUM(CapEC_NE_CanVotes)as "CapEC_NE_CanRemVote", 
(Num_Reps_Capped + 2) - SUM(CapEC_Full_CanVotes) as "CapEC_Full_CanRemVote",
Num_Reps_Uncapped - SUM(UnCapEC_NE_CanVotes) as "UnCapEC_NE_CanRemVote", 
(Num_Reps_Uncapped + 2) - SUM(UnCapEC_Full_CanVotes) as "UnCapEC_Full_CanRemVote"
FROM LG_Elect2016
GROUP BY STATE


-- Create Remainder Table 2020

CREATE TABLE Remainder2020
AS
SELECT STATE, Num_Reps_Capped - SUM(CapEC_NE_CanVotes)as "CapEC_NE_CanRemVote", 
(Num_Reps_Capped + 2) - SUM(CapEC_Full_CanVotes) as "CapEC_Full_CanRemVote",
Num_Reps_Uncapped - SUM(UnCapEC_NE_CanVotes) as "UnCapEC_NE_CanRemVote", 
(Num_Reps_Uncapped + 2) - SUM(UnCapEC_Full_CanVotes) as "UnCapEC_Full_CanRemVote"
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

-- Adding_UnCapEC_Full_Remainder 2008 Table

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

-- Adding_UnCapEC_Full_Remainder 2012 Table

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

-- Adding_UnCapEC_Full_Remainder 2016 Table

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

-- Create All Remainder Table 2012

CREATE TABLE All_Remainder_2012
AS
SELECT Add_CapEC_NE_Remainder_2012.STATE, Add_CapEC_NE_Remainder_2012.Candidate_Name, 
CAST(Add_CapEC_NE_Remainder_2012.Adding_CapEC_NE_Remainder AS REAL) as "CapEC_NE_RemainAdd",
CAST(Add_CapEC_Full_Remainder_2012.Adding_CapEC_Full_Remainder AS REAL) AS "CapEC_Full_RemainAdd",
CAST(Add_UnCapEC_NE_Remainder_2012.Adding_UnCapEC_NE_Remainder AS REAL) AS "UnCapEC_NE_RemainAdd",
CAST(Add_UnCapEC_Full_Remainder_2012.Adding_UnCapEC_Full_Remainder AS REAL) AS "UnCapEC_Full_RemainAdd"
FROM Add_CapEC_NE_Remainder_2012
INNER JOIN Add_CapEC_Full_Remainder_2012
ON Add_CapEC_NE_Remainder_2012.STATE = Add_CapEC_Full_Remainder_2012.STATE
AND Add_CapEC_NE_Remainder_2012.Candidate_Name = Add_CapEC_Full_Remainder_2012.Candidate_Name
INNER JOIN Add_UnCapEC_NE_Remainder_2012
ON Add_CapEC_NE_Remainder_2012.STATE = Add_UnCapEC_NE_Remainder_2012.STATE
AND Add_CapEC_NE_Remainder_2012.Candidate_Name = Add_UnCapEC_NE_Remainder_2012.Candidate_Name
INNER JOIN Add_UnCapEC_Full_Remainder_2012
ON Add_CapEC_NE_Remainder_2012.STATE = Add_UnCapEC_Full_Remainder_2012.STATE
AND Add_CapEC_NE_Remainder_2012.Candidate_Name = Add_UnCapEC_Full_Remainder_2012.Candidate_Name
ORDER BY Add_CapEC_NE_Remainder_2012.STATE

-- Create All Remainder Table 2008

CREATE TABLE All_Remainder_2016
AS
SELECT Add_CapEC_NE_Remainder_2016.STATE, Add_CapEC_NE_Remainder_2016.Candidate_Name, 
CAST(Add_CapEC_NE_Remainder_2016.Adding_CapEC_NE_Remainder AS REAL) as "CapEC_NE_RemainAdd",
CAST(Add_CapEC_Full_Remainder_2016.Adding_CapEC_Full_Remainder AS REAL) AS "CapEC_Full_RemainAdd",
CAST(Add_UnCapEC_NE_Remainder_2016.Adding_UnCapEC_NE_Remainder AS REAL) AS "UnCapEC_NE_RemainAdd",
CAST(Add_UnCapEC_Full_Remainder_2016.Adding_UnCapEC_Full_Remainder AS REAL) AS "UnCapEC_Full_RemainAdd"
FROM Add_CapEC_NE_Remainder_2016
INNER JOIN Add_CapEC_Full_Remainder_2016
ON Add_CapEC_NE_Remainder_2016.STATE = Add_CapEC_Full_Remainder_2016.STATE
AND Add_CapEC_NE_Remainder_2016.Candidate_Name = Add_CapEC_Full_Remainder_2016.Candidate_Name
INNER JOIN Add_UnCapEC_NE_Remainder_2016
ON Add_CapEC_NE_Remainder_2016.STATE = Add_UnCapEC_NE_Remainder_2016.STATE
AND Add_CapEC_NE_Remainder_2016.Candidate_Name = Add_UnCapEC_NE_Remainder_2016.Candidate_Name
INNER JOIN Add_UnCapEC_Full_Remainder_2016
ON Add_CapEC_NE_Remainder_2016.STATE = Add_UnCapEC_Full_Remainder_2016.STATE
AND Add_CapEC_NE_Remainder_2016.Candidate_Name = Add_UnCapEC_Full_Remainder_2016.Candidate_Name
ORDER BY Add_CapEC_NE_Remainder_2016.STATE

-- Create All Remainder Table 2008

CREATE TABLE All_Remainder_2020
AS
SELECT Add_CapEC_NE_Remainder_2020.STATE, Add_CapEC_NE_Remainder_2020.Candidate_Name, 
CAST(Add_CapEC_NE_Remainder_2020.Adding_CapEC_NE_Remainder AS REAL) as "CapEC_NE_RemainAdd",
CAST(Add_CapEC_Full_Remainder_2020.Adding_CapEC_Full_Remainder AS REAL) AS "CapEC_Full_RemainAdd",
CAST(Add_UnCapEC_NE_Remainder_2020.Adding_UnCapEC_NE_Remainder AS REAL) AS "UnCapEC_NE_RemainAdd",
CAST(Add_UnCapEC_Full_Remainder_2020.Adding_UnCapEC_Full_Remainder AS REAL) AS "UnCapEC_Full_RemainAdd"
FROM Add_CapEC_NE_Remainder_2020
INNER JOIN Add_CapEC_Full_Remainder_2020
ON Add_CapEC_NE_Remainder_2020.STATE = Add_CapEC_Full_Remainder_2020.STATE
AND Add_CapEC_NE_Remainder_2020.Candidate_Name = Add_CapEC_Full_Remainder_2020.Candidate_Name
INNER JOIN Add_UnCapEC_NE_Remainder_2020
ON Add_CapEC_NE_Remainder_2020.STATE = Add_UnCapEC_NE_Remainder_2020.STATE
AND Add_CapEC_NE_Remainder_2020.Candidate_Name = Add_UnCapEC_NE_Remainder_2020.Candidate_Name
INNER JOIN Add_UnCapEC_Full_Remainder_2020
ON Add_CapEC_NE_Remainder_2020.STATE = Add_UnCapEC_Full_Remainder_2020.STATE
AND Add_CapEC_NE_Remainder_2020.Candidate_Name = Add_UnCapEC_Full_Remainder_2020.Candidate_Name
ORDER BY Add_CapEC_NE_Remainder_2020.STATE

```

```SQL

-- Added Remainder Table 2008

CREATE TABLE After_addRem_2008
AS
Select LG_Elect2008.STATE, LG_Elect2008.FEC_ID, LG_Elect2008.Candidate_Name, LG_Elect2008.Candidate_Votes, LG_Elect2008.Num_Reps_Capped,
LG_Elect2008.Num_Reps_Uncapped,
CAST((LG_Elect2008.CapEC_NE_CanVotes + All_Remainder_2008.CapEC_NE_RemainAdd) AS REAL) AS CapEC_NE_CanVote_ARem,
CAST((LG_Elect2008.CapEC_Full_CanVotes + All_Remainder_2008.CapEC_Full_RemainAdd) AS REAL) AS CapEC_Full_CanVote_ARem, 
CAST((LG_Elect2008.UnCapEC_NE_CanVotes + All_Remainder_2008.UnCapEC_NE_RemainAdd) AS REAL) AS UnCapEC_NE_CanVote_ARem, 
CAST((LG_Elect2008.UnCapEC_Full_CanVotes + All_Remainder_2008.UnCapEC_Full_RemainAdd) AS REAL) AS UnCapEC_Full_CanVote_ARem
FROM LG_Elect2008
LEFT JOIN All_Remainder_2008
ON LG_Elect2008.STATE = All_Remainder_2008.STATE
AND LG_Elect2008.Candidate_Name = All_Remainder_2008.Candidate_Name

-- Added Remainder Table 2012

CREATE TABLE After_addRem_2012
AS
Select LG_Elect2012.STATE, LG_Elect2012.FEC_ID, LG_Elect2012.Candidate_Name, LG_Elect2012.Candidate_Votes, LG_Elect2012.Num_Reps_Capped,
LG_Elect2012.Num_Reps_Uncapped,
CAST((LG_Elect2012.CapEC_NE_CanVotes + All_Remainder_2012.CapEC_NE_RemainAdd) AS REAL) AS CapEC_NE_CanVote_ARem,
CAST((LG_Elect2012.CapEC_Full_CanVotes + All_Remainder_2012.CapEC_Full_RemainAdd) AS REAL) AS CapEC_Full_CanVote_ARem, 
CAST((LG_Elect2012.UnCapEC_NE_CanVotes + All_Remainder_2012.UnCapEC_NE_RemainAdd) AS REAL) AS UnCapEC_NE_CanVote_ARem, 
CAST((LG_Elect2012.UnCapEC_Full_CanVotes + All_Remainder_2012.UnCapEC_Full_RemainAdd) AS REAL) AS UnCapEC_Full_CanVote_ARem
FROM LG_Elect2012
LEFT JOIN All_Remainder_2012
ON LG_Elect2012.STATE = All_Remainder_2012.STATE
AND LG_Elect2012.Candidate_Name = All_Remainder_2012.Candidate_Name

-- Added Remainder Table

CREATE TABLE After_addRem_2016
AS
Select LG_Elect2016.STATE, LG_Elect2016.FEC_ID, LG_Elect2016.Candidate_Name, LG_Elect2016.Candidate_Votes, LG_Elect2016.Num_Reps_Capped,
LG_Elect2016.Num_Reps_Uncapped,
CAST((LG_Elect2016.CapEC_NE_CanVotes + All_Remainder_2016.CapEC_NE_RemainAdd) AS REAL) AS CapEC_NE_CanVote_ARem,
CAST((LG_Elect2016.CapEC_Full_CanVotes + All_Remainder_2016.CapEC_Full_RemainAdd) AS REAL) AS CapEC_Full_CanVote_ARem, 
CAST((LG_Elect2016.UnCapEC_NE_CanVotes + All_Remainder_2016.UnCapEC_NE_RemainAdd) AS REAL) AS UnCapEC_NE_CanVote_ARem, 
CAST((LG_Elect2016.UnCapEC_Full_CanVotes + All_Remainder_2016.UnCapEC_Full_RemainAdd) AS REAL) AS UnCapEC_Full_CanVote_ARem
FROM LG_Elect2016
LEFT JOIN All_Remainder_2016
ON LG_Elect2016.STATE = All_Remainder_2016.STATE
AND LG_Elect2016.Candidate_Name = All_Remainder_2016.Candidate_Name

-- Added Remainder Table

CREATE TABLE After_addRem_2020
AS
Select LG_Elect2020.STATE, LG_Elect2020.FEC_ID, LG_Elect2020.Candidate_Name, LG_Elect2020.Candidate_Votes, LG_Elect2020.Num_Reps_Capped,
LG_Elect2020.Num_Reps_Uncapped,
CAST((LG_Elect2020.CapEC_NE_CanVotes + All_Remainder_2020.CapEC_NE_RemainAdd) AS REAL) AS CapEC_NE_CanVote_ARem,
CAST((LG_Elect2020.CapEC_Full_CanVotes + All_Remainder_2020.CapEC_Full_RemainAdd) AS REAL) AS CapEC_Full_CanVote_ARem, 
CAST((LG_Elect2020.UnCapEC_NE_CanVotes + All_Remainder_2020.UnCapEC_NE_RemainAdd) AS REAL) AS UnCapEC_NE_CanVote_ARem, 
CAST((LG_Elect2020.UnCapEC_Full_CanVotes + All_Remainder_2020.UnCapEC_Full_RemainAdd) AS REAL) AS UnCapEC_Full_CanVote_ARem
FROM LG_Elect2020
LEFT JOIN All_Remainder_2020
ON LG_Elect2020.STATE = All_Remainder_2020.STATE
AND LG_Elect2020.Candidate_Name = All_Remainder_2020.Candidate_Name


```

```SQL

-- Create Sen_Count2008

CREATE TABLE SenCount2008
AS
SELECT *,
CAST((Num_Reps_Capped + 2) AS REAL) AS CapEC_Standard,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapEC_Standard,
CAST((2) AS REAL) AS SenNum
FROM After_addRem_2008
GROUP BY STATE
ORDER BY Candidate_Votes DESC

-- Create Sen_Count2012

CREATE TABLE SenCount2012
AS
SELECT *,
CAST((Num_Reps_Capped + 2) AS REAL) AS CapEC_Standard,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapEC_Standard,
CAST((2) AS REAL) AS SenNum
FROM After_addRem_2012
GROUP BY STATE
ORDER BY Candidate_Votes DESC

-- Create Sen_Count2016

CREATE TABLE SenCount2016
AS
SELECT *,
CAST((Num_Reps_Capped + 2) AS REAL) AS CapEC_Standard,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapEC_Standard,
CAST((2) AS REAL) AS SenNum
FROM After_addRem_2016
GROUP BY STATE
ORDER BY Candidate_Votes DESC

-- Create Sen_Count2020

CREATE TABLE SenCount2020
AS
SELECT *,
CAST((Num_Reps_Capped + 2) AS REAL) AS CapEC_Standard,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapEC_Standard,
CAST((2) AS REAL) AS SenNum
FROM After_addRem_2020
GROUP BY STATE
ORDER BY Candidate_Votes DESC



```

```SQL

-- Create After_AddSen_2008

CREATE TABLE After_AddSen_2008
AS
SELECT After_addRem_2008.*, SenCount2008.CapEC_Standard, SenCount2008.UnCapEC_Standard, SenCount2008.SenNum
FROM After_addRem_2008
LEFT JOIN SenCount2008
ON After_addRem_2008.STATE = SenCount2008.STATE
AND After_addRem_2008.Candidate_Name = SenCount2008.Candidate_Name

-- Create After_AddSen_2012

CREATE TABLE After_AddSen_2012
AS
SELECT After_addRem_2012.*, SenCount2012.CapEC_Standard, SenCount2012.UnCapEC_Standard, SenCount2012.SenNum
FROM After_addRem_2012
LEFT JOIN SenCount2012
ON After_addRem_2012.STATE = SenCount2012.STATE
AND After_addRem_2012.Candidate_Name = SenCount2012.Candidate_Name

-- Create After_AddSen_2016

CREATE TABLE After_AddSen_2016
AS
SELECT After_addRem_2016.*, SenCount2016.CapEC_Standard, SenCount2016.UnCapEC_Standard, SenCount2016.SenNum
FROM After_addRem_2016
LEFT JOIN SenCount2016
ON After_addRem_2016.STATE = SenCount2016.STATE
AND After_addRem_2016.Candidate_Name = SenCount2016.Candidate_Name

-- Create After_AddSen_2020

CREATE TABLE After_AddSen_2020
AS
SELECT After_addRem_2020.*, SenCount2020.CapEC_Standard, SenCount2020.UnCapEC_Standard, SenCount2020.SenNum
FROM After_addRem_2020
LEFT JOIN SenCount2020
ON After_addRem_2020.STATE = SenCount2020.STATE
AND After_addRem_2020.Candidate_Name = SenCount2020.Candidate_Name

```
```SQL
-- Remove Nulls from After_AddSen_2008

UPDATE After_AddSen_2008
SET
    CapEC_Standard  = COALESCE(CapEC_Standard, 0),
    UnCapEC_Standard = COALESCE(UnCapEC_Standard, 0),
    SenNum = COALESCE(SenNum, 0)
WHERE
    CapEC_Standard IS NULL OR UnCapEC_Standard IS NULL OR SenNum IS NULL;

-- Remove Nulls from After_AddSen_2012

UPDATE After_AddSen_2012
SET
    CapEC_Standard  = COALESCE(CapEC_Standard, 0),
    UnCapEC_Standard = COALESCE(UnCapEC_Standard, 0),
    SenNum = COALESCE(SenNum, 0)
WHERE
    CapEC_Standard IS NULL OR UnCapEC_Standard IS NULL OR SenNum IS NULL;


-- Remove Nulls from After_AddSen_2016

UPDATE After_AddSen_2016
SET
    CapEC_Standard  = COALESCE(CapEC_Standard, 0),
    UnCapEC_Standard = COALESCE(UnCapEC_Standard, 0),
    SenNum = COALESCE(SenNum, 0)
WHERE
    CapEC_Standard IS NULL OR UnCapEC_Standard IS NULL OR SenNum IS NULL;

-- Remove Nulls from After_AddSen_2020

UPDATE After_AddSen_2020
SET
    CapEC_Standard  = COALESCE(CapEC_Standard, 0),
    UnCapEC_Standard = COALESCE(UnCapEC_Standard, 0),
    SenNum = COALESCE(SenNum, 0)
WHERE
    CapEC_Standard IS NULL OR UnCapEC_Standard IS NULL OR SenNum IS NULL;

```
```SQL

-- Total2008

CREATE TABLE Total2008
AS
SELECT STATE, FEC_ID, Candidate_Name, CAST((Num_Reps_Capped + 2) AS REAL) AS Capped_Num_State_EC_Votes,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapped_Num_State_EC_Votes,
CapEC_Standard AS Capped_EC_Standard,
CAST((CapEC_NE_CanVote_ARem + SenNum) AS REAL) AS Capped_EC_NE_Candidate_Vote, 
CapEC_Full_CanVote_ARem AS Capped_EC_Full_Candidate_Vote, 
UnCapEC_Standard AS UnCapped_EC_Standard,
CAST((UnCapEC_NE_CanVote_ARem + SenNum) AS REAL) AS UnCapped_EC_NE_Candidate_Vote,
UnCapEC_Full_CanVote_ARem AS UnCapped_EC_Full_Candidate_Vote
FROM After_AddSen_2008


-- Total2012

CREATE TABLE Total2012
AS
SELECT STATE, FEC_ID, Candidate_Name, CAST((Num_Reps_Capped + 2) AS REAL) AS Capped_Num_State_EC_Votes,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapped_Num_State_EC_Votes,
CapEC_Standard AS Capped_EC_Standard,
CAST((CapEC_NE_CanVote_ARem + SenNum) AS REAL) AS Capped_EC_NE_Candidate_Vote, 
CapEC_Full_CanVote_ARem AS Capped_EC_Full_Candidate_Vote, 
UnCapEC_Standard AS UnCapped_EC_Standard,
CAST((UnCapEC_NE_CanVote_ARem + SenNum) AS REAL) AS UnCapped_EC_NE_Candidate_Vote,
UnCapEC_Full_CanVote_ARem AS UnCapped_EC_Full_Candidate_Vote
FROM After_AddSen_2012

-- Total2016

CREATE TABLE Total2016
AS
SELECT STATE, FEC_ID, Candidate_Name, CAST((Num_Reps_Capped + 2) AS REAL) AS Capped_Num_State_EC_Votes,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapped_Num_State_EC_Votes,
CapEC_Standard AS Capped_EC_Standard,
CAST((CapEC_NE_CanVote_ARem + SenNum) AS REAL) AS Capped_EC_NE_Candidate_Vote, 
CapEC_Full_CanVote_ARem AS Capped_EC_Full_Candidate_Vote, 
UnCapEC_Standard AS UnCapped_EC_Standard,
CAST((UnCapEC_NE_CanVote_ARem + SenNum) AS REAL) AS UnCapped_EC_NE_Candidate_Vote,
UnCapEC_Full_CanVote_ARem AS UnCapped_EC_Full_Candidate_Vote
FROM After_AddSen_2016

-- Total2020

CREATE TABLE Total2020
AS
SELECT STATE, FEC_ID, Candidate_Name, CAST((Num_Reps_Capped + 2) AS REAL) AS Capped_Num_State_EC_Votes,
CAST((Num_Reps_Uncapped + 2) AS REAL) AS UnCapped_Num_State_EC_Votes,
CapEC_Standard AS Capped_EC_Standard,
CAST((CapEC_NE_CanVote_ARem + SenNum) AS REAL) AS Capped_EC_NE_Candidate_Vote, 
CapEC_Full_CanVote_ARem AS Capped_EC_Full_Candidate_Vote, 
UnCapEC_Standard AS UnCapped_EC_Standard,
CAST((UnCapEC_NE_CanVote_ARem + SenNum) AS REAL) AS UnCapped_EC_NE_Candidate_Vote,
UnCapEC_Full_CanVote_ARem AS UnCapped_EC_Full_Candidate_Vote
FROM After_AddSen_2020



```