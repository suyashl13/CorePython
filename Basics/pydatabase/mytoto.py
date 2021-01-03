import db_helper

def main():
    run = 1 
    db_helper.create_table()

    while run:
        print("\n")
        print(
            "1.Insert new task in todo list \n"
            "2.View Todo list. \n"
            "3.Delete the task\n"
            "4.exit\n")
        x = input("Chose option from above >>> ")

        if x == "1":
            task = input("Write your Todo >>> ")
            db_helper.dataEntry(task)

        elif x == "2":
            db_helper.printData()
        
        elif x == "3":
            indexToDelete = int(input("index of task to delete >> "))
            db_helper.deleteTask(indexToDelete)

        elif x == "4":
            run = 0      
        
        else:
            print("Choose a valid option")

if __name__ == "__main__":
    main()