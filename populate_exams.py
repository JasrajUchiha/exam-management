#to populate exams, i need to import the question_paper.py models and take care of the ManyToManyFieldin it
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'portal.settings')

import django
django.setup()

#import the models for the specific app here e.g main.models, student.models, prof.models to work with em
from main.models.question import Question_DB
from main.models.question_paper import Question_Paper

from django.contrib.auth.models import User
mayu = User.objects.get(username="Atharva")
# for reference:
# professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE)
# qPaperTitle = models.CharField(max_length=100)
# questions = models.ManyToManyField(Question_DB)

qpmayu = Question_Paper(professor=mayu, qPaperTitle='Business 2')
qpmayu.save()

#i need to select a question and add it to the questions field of the Questoin Paper model.
#to retrieve, use Question_DB.objects.get and filter by qno which is an AutoField and primary key

#print(Question_DB.objects.get(qno=500).question) lovely jovely, this way of retrieving data is working so on to adding questions to
#question paper general knowledge 1

#use a random variable to select random questions from the entire jargon belonging to mayu, without repetition flag must be set.
# to get random numbers without replacement use sample(range(), k=sample_size)
import random
forgk1 = random.sample(range(424, 620), k=50)

#populating

for i in range(len(forgk1)):
    print("populating", forgk1[i], i)
    qbobj = Question_DB.objects.get(qno=forgk1[i])
    qpmayu.questions.add(qbobj)
    qpmayu.save()

#anotha dubbbbbb fammmmm les gooooooooooo!!!!!!!!!!!
