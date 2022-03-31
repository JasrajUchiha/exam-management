import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'portal.settings')

import django
django.setup()

from django.contrib.auth.models import User, Group
grpobj = Group.objects.get(name="Student")

from faker import Faker
fake = Faker()

# first, last = fake.name().split()
# username = first.lower()
# password = first[0:4].lower() + "pass"
# usrobj = User.objects.create_user(username=username, first_name=first, last_name=last, password=password)
# usrobj.groups.add(grpobj)
# # print(first, last, username, password)

usernames = [] #for having unique usernames only

# creating 70 students and splitting them into two divisions
i = 0
while i < 70:
    name = fake.name().split()
    first = name[0]
    last = name[1]
    username = first.lower()
    password = first[0:4].lower() + "pass"
    if username in usernames:
        continue
    else:
        usrobj = User.objects.create_user(username=username, first_name=first, last_name=last, password=password)
        usrobj.groups.add(grpobj)
        usernames.append(username)
        i += 1
    print("creating user" , first, i+1)

#lessee
