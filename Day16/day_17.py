################################## Day 17: 69 Days of Python #####################################



# To open a Python shell, type this command:

# py manage.py shell



#Insert data into database

'''
In [1]: from members.models import Member

In [2]: Member.objects.all()
Out[2]: <QuerySet []>

In [3]: member = Member(firstname='Emil', lastname='Refsnes')

In [4]: member.save()

In [5]: Member.objects.all().values()
Out[5]: <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>

In [6]: member1 = Member(firstname='Tobias', lastname='Refsnes')^M
   ...: >>> member2 = Member(firstname='Linus', lastname='Refsnes')^M
   ...: >>> member3 = Member(firstname='Lene', lastname='Refsnes')^M
   ...: >>> member4 = Member(firstname='Stale', lastname='Refsnes')^M
   ...: >>> member5 = Member(firstname='Jane', lastname='Doe')^M
   ...: >>> members_list = [member1, member2, member3, member4, member5]^M
   ...: >>> for x in members_list:^M
   ...: >>>   x.save()
   ...:

In [7]: Member.objects.all().values()
Out[7]: <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'}, {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'}, {'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'}, {'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>

In [8]:'''


# Update Records
'''

In [9]: from members.models import Member

In [10]: x = Member.objects.all()[4]

In [11]: x.firstname
Out[11]: 'Stale'

In [12]:  x.firstname = "Stalikken"

In [13]: x.save()

In [14]: Member.objects
Out[14]: <django.db.models.manager.Manager at 0x2740281bdd0>

In [15]: Member.objects.all().values()
Out[15]: <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'}, {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'}, {'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'}, {'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>

In [16]:
'''


# Delete Records
'''
In [16]: from members.models import Member

In [17]: x = Member.objects.all()[5]

In [18]: x.firstname
Out[18]: 'Jane'

In [19]: x.delete()
Out[19]: (1, {'members.Member': 1})

In [20]: Member.objects.all().values()
Out[20]: <QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}, {'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'}, {'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'}, {'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'}, {'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'}]>

In [21]:
'''

# Django Model and Data Management Tutorial

# Step 1: Update the Member Model
# File: members/models.py
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)  # Allow NULL values for phone
    joined_date = models.DateField(null=True)  # Allow NULL values for joined_date

# Step 2: Apply Migrations
# Run the following commands in your terminal:
# py manage.py makemigrations members
# py manage.py migrate

# Step 3: Insert Data Using the Python Shell
# Open the Python shell with this command:
# py manage.py shell

# Then execute the following steps in the shell:

# Import the Member model
# from members.models import Member

# View all members to ensure the table exists
# Member.objects.all().values()  # Should display existing records or an empty QuerySet

# Add a phone number and joined_date to the first record
# x = Member.objects.all()[0]  # Select the first record
# x.phone = 5551234  # Set the phone number
# x.joined_date = '2022-01-05'  # Set the joined date
# x.save()  # Save the updated record

# Verify the update
# Member.objects.all().values()

# Step 4: Add New Records
# Add new records with all fields populated:
# member1 = Member(firstname='Alice', lastname='Smith', phone=1234567890, joined_date='2023-01-15')
# member2 = Member(firstname='Bob', lastname='Johnson', phone=9876543210, joined_date='2023-02-20')

# Save the new members
# member1.save()
# member2.save()

# Verify all records in the database
# Member.objects.all().values()
