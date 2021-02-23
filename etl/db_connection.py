# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional
import cx_Oracle

class OracleConnection():
    """This class returs an Oracle Connection
    """
    def __init__(self):
        self.server: str = ""       # **ADD**
        self.user_name: str = ""    # **ADD**
        self.password: str = ""     # **ADD**

    def insert_data_into_table(self, rows:list)->None:
        """Insert data into DW.CHANGE_REQUESTS_lf188653_STG

        Args:
            rows (list): List of Tuples (values to be inserted)
        """
        try:
            with cx_Oracle.connect(self.user_name, self.password, self.server, encoding="UTF-8") as connection:
                cursor = connection.cursor()
                cursor.executemany('''INSERT INTO DW.CHANGE_REQUESTS_lf188653_STG (CR_NUMBER, "TYPE") VALUES (:1,:2)''', rows)
                connection.commit()
        except Exception as e:
            print(e)
        
    def __del__(self):
        """Dunder method, this method is call implicitly once the python cleaner process starts
        """
        pass