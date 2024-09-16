# EXPERIMENT 3 - Python Data Analysis (PANDAS)
Name: **Cruz, Kathryn Angel S.**  
Section: **2ECE-A** 
## Intended Learning Outcomes
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a
Pandas library
## Instructions:
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter
notebook in the dedicated submission bin.  
> **Note**  
> A separate Jupyter file was also submitted to see the Python code for each problems.

> [!IMPORTANT]
> For this programming assignment, download the following file and save to your default user folder: [cars.csv](https://github.com/user-attachments/files/17017050/cars.csv)
## PROBLEM 1
> **Note**  
> Save your file as Surname_Pandas-P1.py

Using knowledge obtained from the experiment and demonstrations:  
- Load the corresponding .csv file into a data frame named cars using pandas
- Display the first five and last five rows of the resulting cars  

### Solution:  
Import the numpy and pandas libraries to execute the program properly.
```python
import numpy as np
import pandas as pd
```
Reading the csv file named 'cars.csv' to be sotred in the variable 'car'.
```python
cars = pd.read_csv('cars.csv')
cars
```
Where the result will be:
<p align="center">
  <img src="https://github.com/user-attachments/assets/5c95983f-4ff1-49b5-b455-57d70b1382ac" alt="Problem 1 Example"/>
</p>  

Displaying the first five rows of the resulting cars requires the use of the function .head()  
```python
cars.head()
```

Where the result will be:
<p align="center">
  <img src="https://github.com/user-attachments/assets/231cbff6-7ea8-4329-b836-bdab7ba210b7" alt="Problem 1 Example"/>
</p>  

Laslty, displaying the last five rows of the resulting cars requires the use of the function .tail()
```python
cars.tail()
```
Where the result will be:
<p align="center">
  <img src="https://github.com/user-attachments/assets/7ff6d50d-0443-4aec-9710-74817277dba1" alt="Problem 1 Example"/>
</p>    

## PROBLEM 2
> **Note**  
> Save your file as Surname_Pandas-P2.py

Using the dataframe cars in Problem 1, extract the following information using subsetting, slicing, and indexing operations.  

- Display the first five rows with odd-numbered columns (columns 1,3,5,7,...) of cars.
- Display the row that contains the ‘Model’ of ‘Mazda RX4’.
- How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
- Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have

### Solution: 
Displaying the first five rows with odd-numbered columns of cars by using .iloc, slicing through index 0 to 5 with an iteration of 2.
```python
cars.iloc[0:5,::2]
```
Where the result will be: 
<p align="center">
  <img src="https://github.com/user-attachments/assets/68de2c47-b657-4c55-a663-c855d0796056" alt="Problem 1 Example"/>
</p>

Displaying the row containing the Mazda RX4 Model by using .loc to locate 'Mazda RX4' from the 'Model'
```python
cars.loc[cars["Model"] == "Mazda RX4"]
```
Where the result will be:
<p align="center">
  <img src="https://github.com/user-attachments/assets/b6bc9910-5a16-4261-bf32-8833b24a355c" alt="Problem 1 Example"/>
</p>

Displaying the number of cylinders ('cyl') of the car model ‘Camaro Z28’
```python
cars.loc[(cars['Model'] == 'Camaro Z28'), ['Model','cyl']]
```
Where the result will be:
<p align="center">
  <img src="https://github.com/user-attachments/assets/ddfaa4d3-15c1-4561-9681-e65616aa6de2" alt="Problem 1 Example"/>
</p>  

Displaying the amount of cylinders ('cyl') and gear type ('gear') of the car models 'Mazda RX4 Wag', 'Ford Pantera L’ and ‘Honda Civic’  
```python
cars.loc[(cars['Model'] == 'Mazda RX4 Wag') |
          (cars['Model'] == 'Ford Pantera L') | 
          (cars['Model'] == 'Honda Civic'), ['Model', 'cyl', 'gear']]
```
Where the result will be:
<p align="center">
  <img src="https://github.com/user-attachments/assets/5f4ab14d-8170-41b3-a1fa-e8f24cb43e54" alt="Problem 1 Example"/>
</p>  

## Version History
* 1.02
  * README File has been updated
* 1.01
  * Jupyter Notebook File has been uploaded
  * Cruz_Pandas_P2.py has been uploaded
  * Cruz_Pandas_P1.py has been uploaded
* 1.00
  * A new repository has been created
