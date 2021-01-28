from Priority import Priority


class Person:
    def __init__(self, name, idNumber, phoneNumber, priority=Priority.LOW):
        self.name = name
        self.idNumber = idNumber
        self.phoneNumber = phoneNumber
        self.turn = None
        self.arrivedAt = None
        self.priority = priority
