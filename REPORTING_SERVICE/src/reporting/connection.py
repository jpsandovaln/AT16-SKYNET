#
# @connection.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft , Confidential Information "). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft
#
from sql_query import SqlQuery
import psycopg2
from change_mongo_pandas import Mongo_2_pandas

DB_NAME = 'root'
HOST = 'localhost'
USER = 'root'
PASSWORD = 'root'

conn = psycopg2.connect(database=DB_NAME, user=USER,
                        password=PASSWORD, host=HOST)
conn.autocommit = True
cur = conn.cursor()
# Do some setup
sql_query = SqlQuery.create_table()
cur.execute(sql_query)

data_mongo = Mongo_2_pandas()
data_mongo_extract = data_mongo.extract_data()
for index, row in data_mongo_extract.iterrows():
    postgres_insert_query = '''
         INSERT INTO Resources (name, type_rsc,
             model, state_rsc) VALUES (%s, %s, %s, %s)'''
    record_to_insert = (
     row.name, row.type_rsc, row.model, row.state_rsc)
    cur.execute(postgres_insert_query, record_to_insert)

    postgres_insert_query = '''
                    SELECT id FROM Resources WHERE name = (%s)'''
    record_to_insert = (data_mongo_extract['name'][index],)
    cur.execute(postgres_insert_query, record_to_insert)
    resource_id = cur.fetchone()

    postgres_insert_query = '''
                        INSERT INTO Person (person_first_name,
                            person_age, person_country, person_city, person_gender)
                            VALUES (%s, %s, %s, %s, %s)'''
    record_to_insert = (row.person_full_name,
                        row.person_age, row.person_country,
                        row.person_city,
                        row.person_gender)
    cur.execute(postgres_insert_query, record_to_insert)

    postgres_insert_query = '''
                    SELECT id FROM Person WHERE person_first_name = (%s)'''
    record_to_insert = (data_mongo_extract['person_full_name'][index],)
    cur.execute(postgres_insert_query, record_to_insert)
    person_id = cur.fetchone()

    postgres_insert_query = '''
                        INSERT INTO Booking (date, start_time, end_time, state,resource_id, 
                            person_id) VALUES (%s, %s, %s, %s, %s, %s)'''
    record_to_insert = (
        data_mongo_extract['schedule.date'][index], data_mongo_extract['schedule.start_time'][
            index], data_mongo_extract['schedule.end_time'][index], row.state,resource_id,person_id)

    cur.execute(postgres_insert_query, record_to_insert)
            
conn.commit()
# Closing the connection
cur.close()
conn.close()

