class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        ta.add_student(self)
    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)
class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1
        
        
        
class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items = []
        self.size = 0
    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
    def pop(self):
        """ Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        self.items.pop()
        
        
        
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    def __init__(self):
        self.clients = {}
        
    def send(self, email):
        client = self.clients[email.recipient_name]
        client.receive(email)
    def register_client(self, client, client_name):
        self.clients[client_name] = client
    
class Client:
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name 
        self.server.register_client(self, self.name)
        
    def compose(self, msg, recipient_name):
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)
    def receive(self, email):
        self.inbox.append(email)