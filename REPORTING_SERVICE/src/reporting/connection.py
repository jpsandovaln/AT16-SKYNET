#
# @connection.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from sql_query import SqlQuery
import psycopg2
from change_mongo_pandas import Mongo_2_pandas
from decouple import config

DB_NAME = config('DB_NAME')
HOST = config('HOST')
USER = config('USER')
PASSWORD = config('PASSWORD')


# Connect the database psql
class Connection:

    # Connect the psql
    @staticmethod
    def connection_psql():
        conn = psycopg2.connect(database=DB_NAME, user=USER,
                                password=PASSWORD, host=HOST)
        conn.autocommit = True
        cur = conn.cursor()
        return cur

    # Create tables in psql
    @staticmethod
    def create_table():
        cur = Connection.connection_psql()
        sql_query = SqlQuery.create_table()
        cur.execute(sql_query)
        return cur

    # Insert data into the tables
    @staticmethod
    def insert_data():
        cur = Connection.create_table()
        data_mongo = Mongo_2_pandas()
        data_mongo_extract = data_mongo.extract_data()

        for index, row in data_mongo_extract.iterrows():
            postgres_insert_query = '''
                 INSERT INTO Resources (resource_name, resource_type,
                     resource_model, resource_state) VALUES (%s, %s, %s, %s)'''
            record_to_insert = (row.resource_name, row.resource_type,
                                row.resource_model, row.resource_state)
            cur.execute(postgres_insert_query, record_to_insert)

            postgres_insert_query = '''
                            SELECT id FROM Resources WHERE resource_name = (%s)'''
            record_to_insert = (data_mongo_extract['resource_name'][index],)
            cur.execute(postgres_insert_query, record_to_insert)
            resource_id = cur.fetchone()

            postgres_insert_query = '''
                                INSERT INTO Person (person_full_name,
                                    person_age, person_country, person_city
                                    , person_gender) VALUES (%s, %s, %s, %s
                                    , %s)'''
            record_to_insert = (row.person_full_name,
                                row.person_age, row.person_country,
                                row.person_city,
                                row.person_gender)
            cur.execute(postgres_insert_query, record_to_insert)

            postgres_insert_query = '''
                            SELECT id FROM Person WHERE person_full_name
                                = (%s)'''
            record_to_insert = (data_mongo_extract['person_full_name'][index],)
            cur.execute(postgres_insert_query, record_to_insert)
            person_id = cur.fetchone()

            postgres_insert_query = '''
                                INSERT INTO Booking (date, start_time,
                                    end_time, state, resource_id, person_id)
                                    VALUES (%s, %s, %s, %s, %s, %s)'''
            record_to_insert = (
                data_mongo_extract['schedule.date'][index],
                data_mongo_extract['schedule.start_time'][
                    index], data_mongo_extract['schedule.end_time'][index],
                row.state, resource_id, person_id)

            cur.execute(postgres_insert_query, record_to_insert)
        return cur

    # Close connection
    @staticmethod
    def close_connection():
        cur = Connection.insert_data()
        conn = psycopg2.connect(database=DB_NAME, user=USER,
                                password=PASSWORD, host=HOST)
        conn.commit()
        cur.close()
        conn.close()
        return True
if __name__=='__main__':
    result = Connection.close_connection()
