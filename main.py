# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional
from etl.cr import ChangeRequest
from etl.db_connection import OracleConnection

if __name__ == "__main__":
    
    cr = ChangeRequest("USC_CHANGE_REQUESTS_012021.CSV")
    cr.cleanDataFrame()
    oc = OracleConnection()
    oc.insert_data_into_table(cr.transform_data_to_insert())
    