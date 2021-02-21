# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional
from pathlib import Path
from os import getcwd
import pandas as pd

class ChangeRequest:

    def __init__(self, file_name:str):
        self.path = Path(getcwd(), 'data', file_name)
        self.df = self.loadCSVFile()

    def loadCSVFile(self)->pd:
        """This method reads a CSV separated by pipes from local data dir 
           and loads it into a DataFrame.

        Returns:
            pd: DataFrame
        """
        return pd.read_csv(self.path, sep='|')
    
    def cleanDataFrame(self)->None:
        """Transforms the DataFrame
        """
        # TODO
        self.df = self.df[['number','type']].head(5)
    
    def transform_data_to_insert(self)->list:
        """Transforms dataframe into a list of tuples

        Returns:
            list: Returns a list of tuples of the self.df (dataframe)
        """
        return list(self.df.itertuples(index=False, name=None))

        