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

