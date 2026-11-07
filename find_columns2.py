import pymssql

def list_columns():
    print("Connecting to database to find columns in the 'name_counts' table...")
    try:
        conn = pymssql.connect(
            server='cisdbss.pcc.edu',
            user='275student',
            password='275student',
            database='NAMES'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'name_counts'")

        print("\nColumns found in the 'name_counts' table:")
        columns = cursor.fetchall()
        for row in columns:
            print(f"- {row[0]}")

        conn.close()
    except Exception as e:
        print("\nError connecting to the database:")
        print(e)


if __name__ == "__main__":
    list_columns()