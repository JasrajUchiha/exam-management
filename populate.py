import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'portal.settings')

import csv
csvFile = open('Test.csv')
fileReader = csv.reader(csvFile)

import django
django.setup()

#import the models for the specific app here e.g main.models, student.models, prof.models to work with em
from main.models.question import Question_DB

#import Faker
from faker import Faker
#instantiate the Faker object
fake = Faker()

#import random
import random

from django.contrib.auth.models import User # using this since professor field is foreugnkey from user table
mayu = User.objects.get(username="Mayuri")
nik = User.objects.get(username="Nikhil")
atharva = User.objects.get(username="Atharva")
#retrieve the data first for populating
allData = []
i = 0
for row in fileReader:
    if i > 2:
        allData.append(row)
    if i == 602:
        break
    i += 1

# print(allData)
# professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE, null=True)
# qno = models.AutoField(primary_key=True)
# question = models.CharField(max_length=100)
# optionA = models.CharField(max_length=100)
# optionB = models.CharField(max_length=100)
# optionC = models.CharField(max_length=100)
# optionD = models.CharField(max_length=100)
# answer = models.CharField(max_length=200)

#the non correct options have to have fake sentences with a random number of words
# words = random.randint(4,12)
#i'll take 600 questions and assign them to 3 teachers
#the correct answer should also go into a random option :( if else se karenge? okay.
# print(fake.sentence(nb_words=random.randint(4,12))) this shit working. good.

for i in range(400, len(allData)):
    print("populating", i)
    corrChoice = random.randint(1,4)
    if corrChoice == 1:
        qb = Question_DB.objects.get_or_create(professor=atharva, question=allData[i][0], optionA=allData[i][1], optionB=fake.sentence(nb_words=random.randint(4,12)), optionC=fake.sentence(nb_words=random.randint(4,12)), optionD=fake.sentence(nb_words=random.randint(4,12)), answer=allData[i][1])[0]
    elif corrChoice == 2:
        qb = Question_DB.objects.get_or_create(professor=atharva, question=allData[i][0], optionA=fake.sentence(nb_words=random.randint(4,12)), optionB=allData[i][1], optionC=fake.sentence(nb_words=random.randint(4,12)), optionD=fake.sentence(nb_words=random.randint(4,12)), answer=allData[i][1])[0]
    elif corrChoice == 3:
        qb = Question_DB.objects.get_or_create(professor=atharva, question=allData[i][0], optionA=fake.sentence(nb_words=random.randint(4,12)), optionB=fake.sentence(nb_words=random.randint(4,12)), optionC=allData[i][1], optionD=fake.sentence(nb_words=random.randint(4,12)), answer=allData[i][1])[0]
    elif corrChoice == 4:
        qb = Question_DB.objects.get_or_create(professor=atharva, question=allData[i][0], optionA=fake.sentence(nb_words=random.randint(4,12)), optionB=fake.sentence(nb_words=random.randint(4,12)), optionC=fake.sentence(nb_words=random.randint(4,12)), optionD=allData[i][1], answer=allData[i][1])[0]

#this can horribly wrong, but lets goooooooooooo. IT FUCKING WORKEDDDDDDDDDDDDDDDDDDDDDDDD!!!!!!!!!!!!!
