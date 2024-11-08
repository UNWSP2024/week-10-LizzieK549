# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, IDnumber, department, JobTitle):
        self.__name = name
        self.__IDnumber = IDnumber
        self.__department = department
        self.__JobTitle = JobTitle

    def get_name(self):
        return self.__name

    def get_Department(self):
        return self.__department

    def get_JobTitle(self):
        return self.__JobTitle

    def get_IDnumber(self):
        return self.__IDnumber

def main():
   Employee1 = Employee('Susan Meyes', '47899', 'Accounting', 'Vice President')
   Employee2 = Employee('Mark Jones', '39119', 'IT', 'Programmer')
   Employee3 = Employee('Joy Rogers', '81774', 'Manufacturing',	'Engineer')

   print(f'Name: {Employee1.get_name()}, IDnumber: {Employee1.get_IDnumber()}, Department: {Employee1.get_Department()}, JobTitle: {Employee1.get_JobTitle()}')
   print(f'Name: {Employee2.get_name()}, IDnumber: {Employee2.get_IDnumber()}, Department: {Employee2.get_Department()}, JobTitle: {Employee2.get_JobTitle()}')
   print(f'Name: {Employee3.get_name()}, IDnumber: {Employee3.get_IDnumber()}, Department: {Employee3.get_Department()}, JobTitle: {Employee3.get_JobTitle()}')

if __name__ == '__main__':
    main()