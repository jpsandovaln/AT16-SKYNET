#
# @booking.py Copyright (c)
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

# Query commands
class SqlQuery:

    # Query commands to create tables in psql
    @staticmethod
    def create_table():
        sql_query = '''
            DROP TABLE IF EXISTS Booking;
            DROP TABLE IF EXISTS Person;
            DROP TABLE IF EXISTS Resources;
            CREATE TABLE Resources (
                id SERIAL NOT NULL PRIMARY KEY,
                resource_name TEXT,
                resource_type TEXT,
                resource_model TEXT,
                resource_state TEXT
            );
            CREATE TABLE Person (
                id SERIAL NOT NULL PRIMARY KEY,
                person_full_name TEXT,
                person_country TEXT,
                person_city TEXT,
                person_gender TEXT,
                person_age INTEGER
            );
             CREATE TABLE Booking (
                id SERIAL NOT NULL PRIMARY KEY,
                date DATE,
                start_time TIME,
                end_time TIME,
                state TEXT,
                resource_id INTEGER REFERENCES Resources (id) ON DELETE SET NULL,
                person_id INTEGER REFERENCES Person (id) ON DELETE SET NULL
            )
        '''
        return sql_query

    # Query commands to join tables in psql
    @staticmethod
    def join_tables():
        sql_query_join = '''
            SELECT Booking.date, Booking.start_time, Booking.end_time,
            Booking.state, Resources.resource_name, Resources.resource_type,
            Resources.resource_model, Resources.resource_state,
            Person.person_full_name, Person.person_age, Person.person_country,
            Person.person_city, Person.person_gender
            FROM Booking JOIN Resources ON Booking.person_id = Resources.id
            JOIN Person ON Booking.person_id = Person.id;
        '''
        return sql_query_join
