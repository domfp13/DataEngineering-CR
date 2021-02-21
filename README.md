# DataEngineering-CR

This is a simple data pipeline process that reads data from a CSV file and transforms it into a DataFrame object, once the data has been transformed broadcasting operations for cleanups might be applied, once the data cleanup is complete the data is inserted into a database table.

## Prerequisite 
* Installed python 3.7.
* Understand virtual environments.
* DataFrames and boolean masking and columnar operations for broad casting.

## Note
* [Anaconda](https://docs.anaconda.com/anaconda/) - Anaconda allows us to keep python virtual environments organize and it is the best setup tool for data analysis.
* [cx_Oracle](https://cx-oracle.readthedocs.io/en/latest/user_guide/introduction.html#) - Take a look at the official Oracle-Python library

## Steps

### 1.- Clone repository
```sh
$ git clone git@github.com:domfp13/DataEngineering-CR.git
```
### 2.- Create virtual environment
```sh
$ cd DataEngineering-CR
$ conda create -n CR python=3.7
$ conda activate CR
```
### 3.- Installing requirements
```sh
$ pip install requirements.txt
```

### 4.- Add database credentials
Modify [db_connection.py](etl/db_connection.py) __init__ method adding your own credentials.

### 5.- Create db object
Using [ddl_creation.sql](sql/ddl_creation.sql) create table.

### 6.- Run process
```sh
$ python main.py
```

# Author
* **Enrique Plata** - *2021/02/21*