# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Luis Fuentes

from __future__ import annotations
from typing import Optional
from etl.cr import ChangeRequest
from etl.db_connection import OracleConnection

from os import getcwd
from pathlib import Path
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
loggin_file_path = str(Path('{path}/LOGGER.log'.format(path = getcwd())))
logging.basicConfig(filename = loggin_file_path,
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

logger = logging.getLogger()

if __name__ == "__main__":
    
    logging.info("--Begin--")

    logging.info("1.- Creating Dataframe on Object ChangeRequest")
    cr = ChangeRequest("USC_CHANGE_REQUESTS_012021.CSV")

    logging.info("2.- Cleaning Dataframe")
    cr.cleanDataFrame()

    logging.info("3.- Creating class to connect to oracle")
    oc = OracleConnection()

    logging.info("4.- Inserting Data into DW.CHANGE_REQUESTS_lf188653_STG")
    oc.insert_data_into_table(cr.transform_data_to_insert())
    