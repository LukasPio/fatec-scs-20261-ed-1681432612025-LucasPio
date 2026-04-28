""""------------------------------------------ *
Fatec
São
Caetano
do
Sul
Atividade
B2 - 2

Author[1681432612025]
Objetivo: Implementar um sistema de impressão escolar, com filas prioritárias
data: 28 / 04 / 2026
*------------------------------------------ * """

from collections import deque

generic_queue = deque()
print_queue = deque()

class PrintRequest:
    def __init__(self, file_name, pages, is_admin):
        self.file_name = file_name
        self.pages = pages
        self.is_admin = is_admin

# Arquivos de exemplo
generic_queue.append(PrintRequest("math_exam.pdf", 3, 1))
generic_queue.append(PrintRequest("world_map_image.png", 1, 0))
generic_queue.append(PrintRequest("english_text.pdf", 23, 1))
generic_queue.append(PrintRequest("history_homework.pdf", 2, 0))

while True:
    try:
        opt = int(input(
            "1- Request a print\n"
            "2- Reorganize queue\n"
            "3- Process a print request\n"
            "4- List all queues\n"
            "5- Get quantity of files in wait\n"
            "6- Exit program\n\n"
        ))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if opt == 1:
        file_name = input("Enter the file name (with extension): ")

        try:
            pages = int(input("Enter the total of pages in the file: "))
            is_admin = int(input("Role (0 = student, 1 = admin): "))
        except ValueError:
            print("Invalid input! Pages and role must be numbers.")
            continue

        if is_admin not in (0, 1):
            print("Invalid role")
            continue

        if pages <= 0:
            print("Invalid quantity of pages")
            continue

        generic_queue.append(PrintRequest(file_name, pages, is_admin))

    elif opt == 2:
        print("Reorganizing the queue...")

        admins = [req for req in generic_queue if req.is_admin]
        students = [req for req in generic_queue if not req.is_admin]

        generic_queue.clear()
        print_queue.clear()

        print_queue.extend(admins)
        print_queue.extend(students)

    elif opt == 3:
        if not print_queue:
            print("No requests in the organized queue!")
            continue

        request = print_queue.popleft()

        role = "admin" if request.is_admin else "student"
        print(f"Printing {role} file '{request.file_name}' with {request.pages} pages")

    elif opt == 4:
        print("\nQueue without organization:")
        if not generic_queue:
            print("Empty")
        for request in generic_queue:
            role = "admin" if request.is_admin else "student"
            print(f"{role} file '{request.file_name}' with {request.pages} pages")

        print("\nOrganized queue with admin priority:")
        if not print_queue:
            print("Empty")
        for request in print_queue:
            role = "admin" if request.is_admin else "student"
            print(f"{role} file '{request.file_name}' with {request.pages} pages")

    elif opt == 5:
        admin_counter = 0
        student_counter = 0

        for request in print_queue:
            if request.is_admin:
                admin_counter += 1
            else:
                student_counter += 1

        print(f"There are {student_counter} student files and {admin_counter} admin files waiting")

    elif opt == 6:
        print("Closing the program...")
        break

    else:
        print("Invalid option!")

    print("=============================================")