import sqlite3 as lite


# Functionality goes here

class DatabaseManage(object):

    def __init__(self):
        global conn
        try:
            conn = lite.connect('courses.db')
            with conn:
                cur = conn.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS course(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price TEXT,
                is_private BOOLEAN NOT NULL DEFAULT 1
                )''')
        except Exception:
            print("Unable to create a DB")


    # create data
    def insert_data(self, data):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute('''INSERT INTO course(name,description,price,is_private) VALUES(?,?,?,?)''',data)
                return True
        except Exception:
            return False

    # read data
    def fetch_data(self):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute('''SELECT id,name,description,price,is_private FROM course''')
                return cur.fetchall()

        except Exception:
            return False

    # delete data
    def delete_data(self, id):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute('''DELETE FROM course WHERE id = ?''',[id])
                return True

        except Exception:
            return False


# Provide interface to user

def main():
    while True:
        print("*"*40)
        print("\n:: Course Management ::\n ")
        print("*"*40)
        print("\n")

        print("#"*40)
        print("\n:: User Manual ::\n ")
        print("#"*40)
        print("\n")

        print("\nPRESS 1. Insert a new course\n")
        print("\nPRESS 2. Show all courses\n")
        print("\nPRESS 3. Delete a coure (Course ID required)\n")
        print("\nPRESS 4. To exit\n")

        print("#"*40)
        print("\n")

        db = DatabaseManage()

        choice = input("\nEnter a choice: ")

        if choice == '1':
            name = input("\nEnter course name: ")
            desc = input("\nEnter course description: ")
            price = input("\nEnter course price: ")
            is_private = input("\nIs this course private? (0/1): ")

            if db.insert_data([name,desc,price,is_private]):
                print("Course was inserted successfully")
            else:
                print("Something is wrong")

            re_do = input('Press 0 to continue: ')
            if re_do == '0':
                continue
            else:
                break

        elif choice == '2':
            print("\n:: Course List ::\n ")
            for index,item in enumerate(db.fetch_data()):
                print("\n Sr No: "+ str(index + 1))
                print("Course Id: "+ str(item[0]))
                print("Course Name: "+ str(item[1]))
                print("Course Description: "+ str(item[2]))
                print("Course Price: "+ str(item[3]))
                private = 'Yes' if item[4] else 'No'
                print("Is private?: "+ private)
                print("\n")

            re_do = input('Press 0 to continue: ')
            if re_do == '0':
                continue
            else:
                break



        elif choice == '3':
            record_id = input("Enter course ID: ")
            if db.delete_data(record_id):
                print("Successfully deleted")
            else:
                print("Something is wrong")

            re_do = input('Press 0 to continue: ')
            if re_do == '0':
                continue
            else:
                break

        elif choice == '4':
            break

        else:
            print("\nWrong selection")


if __name__ == "__main__":
    main()
