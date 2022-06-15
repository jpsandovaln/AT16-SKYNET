#
# @criteria.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import pandas as pd

from src.reporting.criteria.cache import Cache
from src.reporting.sql_query import SqlQuery
import psycopg2
from decouple import config

DB_NAME = config('DB_NAME')
HOST = config('HOST')
USER = config('USER')
PASSWORD = config('PASSWORD')


class Criteria:

    @staticmethod
    def get_df():
        try:
            conn = psycopg2.connect(database=DB_NAME, user=USER,
                                    password=PASSWORD, host=HOST)
            conn.autocommit = True
            cur = conn.cursor()
            # Do some setup
            sql_query_join = SqlQuery.join_tables()
            cur.execute(sql_query_join)
            result = cur.fetchall()
            df = pd.DataFrame(result,
                              columns=['date', 'start_time', 'end_time',
                                       'state',
                                       'resource_name', 'resource_type',
                                       'resource_model', 'resource_state',
                                       'person_full_name', 'person_age',
                                       'person_country', 'person_city',
                                       'person_gender'])
            conn.commit()
            # Closing the connection
            cur.close()
            conn.close()
            Cache.write_cache(df)

            return df
        except KeyError:
            print('Failed')
