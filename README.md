
# T3020   Repo for ELEN3020

Name: Matthew Cresswell
Student Number: 1834243
Date: 7 June
Scott
# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.


-All Changes made to the program

*The file structure has been organised into a program directory and Test directory.
*The datamunger directory will contain an __init__.py file so that it can pull data from other directories, it will also have the code to the program.
*The Test file with have an __init__.py file, the sample data and the unit testing code. 

E1 
*the curr[2:9] had to be changed to curr[1:9] as the algorithm was not reading all the columns in the data.


E2 
*Changed the value in for i in range(9) to for i in range(8) as we did not want the last column to be included in the monotonic check.
*Monotomically means that the current number must be smaller than the previous number, the code wrote if curr[i] <= prev[i] which is incorrect as <= is inclusive where as monotomically is not inclusive. Therefore it should only have been < (less than) not <= (less than or equals to).

E3 
*Added an if statement so that the last column is not checked in the check_row check search.



