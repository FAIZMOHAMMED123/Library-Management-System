class document:
    def __init__(self, id, title):
        self.__id = id
        self.__title = title
        self.__is_available = True
    
    def getId(self):
        return self.__id
    
    def getTitle(self):
        return self.__title
    
    def getIs_available(self):
        return self.__is_available
    
    def display_info(self):
        print(" ID  : ", self.__id)
        print("le titre : ", self.__title)
    
    def change_availability(self, status):
        self.__is_available = status


class Book(document):
    def __init__(self, id, title, author, page_count):
        super().__init__(id, title)
        self.__author = author
        self.__page_count = page_count

    def display_info(self):
        super().display_info()
        print("l auteur : ", self.__author)
        print("le nombre de page : ", self.__page_count)
 

class Magazine(document):
    def __init__(self, id, title, issue_number):
        super().__init__(id, title)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print("the specific issue number of the magazine : ", self.issue_number)


class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__borrowed_documents = []

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getBorrowed_documents(self):
        return self.__borrowed_documents

    def add_document(self, document):
        self.__borrowed_documents.append(document)

    def remove_document(self, document):
        self.__borrowed_documents.remove(document)

    def display_info(self):
        print("ID : ", self.__id)
        print("Nom : ", self.__name)
        for i in self.__borrowed_documents:
            print("le titre des documents emprunte : ", i.getTitle())


class Library:
    def __init__(self, name):
        self.__name = name
        self.__documents_list = []
        self.__students_list = []

    def getNom(self):
        return self.__name

    def getDocuments_list(self):
        return self.__documents_list

    def getStudents_list(self):
        return self.__students_list

    def add_document(self, document):
        self.__documents_list.append(document)

    def add_student(self, student):
        self.__students_list.append(student)
    
    def display_all_documents(self):
        for i in self.__documents_list:
            i.display_info()

    def find_student_by_id(self, student_id):
        for i in self.__students_list:
            if i.getId() == student_id:
                return i
        return None
    
    def find_document_by_id(self, document_id):
        for i in self.__documents_list:
            if i.getId() == document_id:
                return i
        return None
            
    def borrow_document(self, student_id, document_id):
        d = self.find_document_by_id(document_id)
        s = self.find_student_by_id(student_id)
        if s is None:
            print("erreur : l etudiant n existe pas ")
            return
        if d is None:
            print("erreur : le document n existe pas  ")
            return
        if d.getIs_available() == False:
            print("document deja emprunter ")
            return
        else:
            d.change_availability(False)
            s.add_document(d)

    def return_document(self, student_id, document_id):
        d = self.find_document_by_id(document_id)
        s = self.find_student_by_id(student_id)
        if s is None:
            print("erreur : l etudiant n existe pas")
            return
        if d is None:
            print("erreur : le document n existe pas")
            return
        if d in s.getBorrowed_documents():
            s.remove_document(d)
            d.change_availability(True)


# --- Execution Control Base ---
l = Library("library A")
b1 = Book(11, "python advanced", "Boulmal", 250)
m1 = Magazine(22, "AI Trends", 5)
s1 = Student(1, "amine")

l.add_document(b1)
l.add_document(m1)
l.add_student(s1)
l.display_all_documents()
l.borrow_document(1, 11)

s1.display_info()
print(b1.getIs_available())
l.borrow_document(1, 11)
l.borrow_document(1, 999)
l.return_document(1, 11)
print(b1.getIs_available())
s1.display_info()
