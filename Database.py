# ***************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-133Y Lab 7
# Desc:   Data layer module containing the Database class. Connects to
#         the MSSQL database and handles queries with parameter binding.
#
# ***************************************************************************

import pymssql


class Database:
    __connection = None

    @classmethod
    def connect(cls):
        """Establishes and shares a single connection to the database."""
        if cls.__connection is None:
            cls.__connection = pymssql.connect(
                server='cisdbss.pcc.edu',
                user='275student',
                password='275student',
                database='NAMES'
            )

    @classmethod
    def readNames(cls, year, gender):
        """Fetches a list of dictionaries matching the year and gender."""
        cls.connect()

        # as_dict=True returns each row as a dictionary matching column names
        cursor = cls.__connection.cursor(as_dict=True)

        # Parameterized query to prevent SQL Injection
        # Fetching TOP 20 ordered descending to match the sample output
        query = """
                SELECT TOP 20 
                    ygt.Year, n.Name,
                    ygt.Gender,
                    nc.NameCount
                FROM name_counts nc
                JOIN names n ON nc.FK_NameID = n.NameID
                JOIN year_gender_totals ygt ON nc.FK_YearGenderTotalID = ygt.YearGenderTotalID
                WHERE ygt.Year = %s AND ygt.Gender = %s
                ORDER BY nc.NameCount DESC
                """

        cursor.execute(query, (year, gender))
        results = cursor.fetchall()
        return results
