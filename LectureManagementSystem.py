class Lecture:
    def __init__(self, name, subject, course, num_lectures):
        self.name = name
        self.subject = subject
        self.course = course
        self.num_lectures = num_lectures

    def display(self):
        print("Lecturer Name:", self.name)
        print("Subject:", self.subject)
        print("Course:", self.course)
        print("Number of Lectures:", self.num_lectures)
        print("------------------------")

class LectureManagementSystem:
    def __init__(self):
        self.lectures = []

    def add_lecture(self):
        name = input("Enter Lecturer Name: ")
        subject = input("Enter Subject: ")
        course = input("Enter Course: ")
        num_lectures = int(input("Enter Number of Lectures: "))
        
        lecture = Lecture(name, subject, course, num_lectures)
        self.lectures.append(lecture)
        print("Lecture added successfully!")

    def show_lectures(self):
        if not self.lectures:
            print("No lectures to show.")
        else:
            print("\nAll Lectures:")
            for lecture in self.lectures:
                lecture.display()

def main():
    system = LectureManagementSystem()
    
    while True:
        print("\n1. Add Lecture")
        print("2. Show Lectures")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            system.add_lecture()
        elif choice == '2':
            system.show_lectures()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
