# ***************************************************************************
#
# Author: Paul Littrell
# Lab:    CIS-133Y Lab 7
# Desc:   Business logic layer module containing the Name class. Handles
#         data encapsulation and provides getters/setters.
#
# ***************************************************************************

import Database as db

class Name:

    def __init__(self, name, year, gender, count):
        self.__name = name
        self.__year = year
        self.__gender = gender
        self.__count = count

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_count(self):
        return self.__count

    def set_count(self, count):
        self.__count = count

    @staticmethod
    def readNames(year, gender):
        """Calls the Database layer and returns a list of Name objects."""
        # Pass the filter parameters down to the database
        raw_data = db.Database.readNames(year, gender)

        name_objects = []
        # Convert each database dictionary into a Name object
        for row in raw_data:
            name_obj = Name(row["Name"], row["Year"], row["Gender"], row["NameCount"])
            name_objects.append(name_obj)

        return name_objects