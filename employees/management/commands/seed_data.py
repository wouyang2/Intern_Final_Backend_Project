from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee, Performance
from attendance.models import Attendance
from departments.models import Department
import random
from datetime import date

# Seed with at least 30–50 fake employees and related data using a management command.
class Command (BaseCommand):
    
    help =  "Run command to generate the seeding data"

    def handle(self, *args, **options):

        #!!!! DELETE ALL THE EXISTING DATA EACH TIME BEFORE SEEDING THE NEW FAKE DATA
        Employee.objects.all().delete()
        Department.objects.all().delete()
        Attendance.objects.all().delete()
        Performance.objects.all().delete()

        self.stdout.write("Seeding fake data...")

        faker = Faker('en_US')

        """
        Department:
            Department Name
        """
        departments = []
        department_name = ["IT", "HR", "Sales", "Finance", "Accounting", "Marketing", "Customer Service"]

        for name in department_name:
            dep = Department.objects.create(Name = name)
            departments.append(dep)
        

        """
        Employee:
        Name, Email, Phone Number, Address, 
        Date of Joining, Department (FK)
        """

        employees = []
        for _ in range(50):
            first_name = faker.first_name()
            last_name = faker.last_name()
            full_name = f"{first_name} {last_name}"

            email_username = f"{first_name[0]}{last_name}{random.randint(1, 99)}"
            email_domain = "outlook.com" 
            custom_email = f"{email_username}@{email_domain}"

            employ_instance = Employee.objects.create(Name = full_name, Email = custom_email, 
                                                     Phone_Number = faker.phone_number(),
                                                     Address = faker.address(), 
                                                     Date_of_join = faker.date_between(start_date='-5y', end_date='today'),
                                                     Dept = random.choice(departments))
            employees.append(employ_instance)
    


        # Generate some fake Attendance and Performance
        Status_ = ["Present", " Absent", "Late"]

        for emp in employees:

            """
            Attendance:
            Employee (FK), Date, Status (Present/Absent/Late)
            """

            for _ in range(15):

                Attendance.objects.create(Name = emp, Date = faker.date_this_year(), Status= random.choice(Status_))


            """
            Performance
            Employee (FK), Rating (1-5), Review Date
            """

            for _ in range(5):
                Performance.objects.create(Name = emp, Rating = faker.random_int(min=1, max = 5), Review_date = faker.date_this_year())


        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))