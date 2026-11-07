import pymssql


def list_tables():
    print("Connecting to database to find tables...")
    try:
        conn = pymssql.connect(
            server='cisdbss.pcc.edu',
            user='275student',
            password='275student',
            database='NAMES'
        )
        cursor = conn.cursor()

        # Query the built-in SQL Server schema to list all tables
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")

        print("\nTables found in the NAMES database:")
        tables = cursor.fetchall()
        for row in tables:
            print(f"- {row[0]}")

        conn.close()
    except Exception as e:
        print("\nError connecting to the database:")
        print(e)


if __name__ == "__main__":
    list_tables()