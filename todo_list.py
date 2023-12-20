class List:
    def __init__(self,list):
        self.list = list

    def display_list(self):
        return self.list
    
    def add_task_to_list(self, task):
        self.list.append(task)
    
    def delete_task(self, index):
        self.list.pop(index-1)
    
    def edit_task(self, index, edit):
        self.list[index-1] = edit
        
list_a = List([])
while True:
    print("Todo List:")
    numbers = []
    for i, l in enumerate(list_a.display_list(), 1):
        print(f"{i}. {l}")
        numbers.append(str(i))
    print("a. Add")
    print("x. Exit")
    if list_a.display_list() != "No tasks have been added":
        choice = input("Pick a task: (or add a task): ")
        while True:
            if choice not in numbers and choice.lower() != "a" and choice.lower() != "x":
                choice = input("(Invalid) Pick a task: (or add a task): ")
            else:
                break

        if choice.lower() != "a" and choice.lower() != "x":
            print("1. Edit")
            print("2. Delete")
            print("3. Back")
            back = False
            task_choice = input("PicK an option: ")
            while True:
                if task_choice == "1":
                    edit = input("Enter your edited task: ")
                    list_a.edit_task(int(choice), edit)
                    break
                elif task_choice == "2":
                    sure = input("Are you sure? (Y/N): ")
                    if sure.lower() == "y" or sure.lower() == "yes":
                        list_a.delete_task(int(choice))
                    break
                elif task_choice == "3":
                    back = True
                    break
                else:
                    task_choice = input("(Invalid Option) Pick an option: ")
            if back:
                continue
        else:
            if choice == "a":
                added_task = input("Write your task: ")
                list_a.add_task_to_list(added_task)
            elif choice == "x":
                break
    else:
        choice = input("Add or Exit: ")
        final_choice = ""
        while True:
            if choice == "a":
                added_task = input("Write your task: ")
                list_a.add_task_to_list(added_task)
                break
            elif choice == "x":
                final_choice = "x"
                break
            else:
                choice = input("(Invalid Input) What would you like to do? ")
        if final_choice == "x":
            break

    
