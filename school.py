class SchoolPortal:
    def __init__(self):
        self.students = {}
        self.resources = {}

    def add_student(self, student_id, name, fees_due):
        self.students[student_id] = {'name': name, 'fees_due': fees_due}

    def pay_fees(self, student_id, amount):
        if student_id in self.students:
            if amount >= self.students[student_id]['fees_due']:
                print(f"Payment successful! {self.students[student_id]['name']}'s fees are fully paid.")
                self.students[student_id]['fees_due'] = 0
            else:
                self.students[student_id]['fees_due'] -= amount
                print(f"Partial payment of {amount} received. Remaining fees: {self.students[student_id]['fees_due']}")
        else:
            print("Student not found.")

    def add_resource(self, resource_id, name, quantity, price):
        self.resources[resource_id] = {'name': name, 'quantity': quantity, 'price': price}

    def purchase_resource(self, resource_id, quantity, student_id):
        if resource_id in self.resources:
            if self.resources[resource_id]['quantity'] >= quantity:
                cost = quantity * self.resources[resource_id]['price']
                if student_id in self.students and self.students[student_id]['fees_due'] >= cost:
                    self.students[student_id]['fees_due'] -= cost
                    self.resources[resource_id]['quantity'] -= quantity
                    print(f"Resource purchased successfully! Remaining fees: {self.students[student_id]['fees_due']}")
                else:
                    print("Insufficient funds to purchase the resource.")
            else:
                print("Insufficient quantity of the resource.")
        else:
            print("Resource not found.")

    def display_students(self):
        print("Students:")
        for student_id, student_info in self.students.items():
            print(f"ID: {student_id}, Name: {student_info['name']}, Fees Due: {student_info['fees_due']}")

    def display_resources(self):
        print("Resources:")
        for resource_id, resource_info in self.resources.items():
            print(f"ID: {resource_id}, Name: {resource_info['name']}, Quantity: {resource_info['quantity']}, "
                  f"Price: {resource_info['price']}")

# Example usage
school_portal = SchoolPortal()

# Adding students