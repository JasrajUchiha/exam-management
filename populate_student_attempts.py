import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")

import django
django.setup()

from main.models import *
from django.contrib.auth.models import User
from student.models import Stu_Question, StuExam_DB, StuResults_DB

# grstu = Group.objects.get(name="Student")
allUsers = User.objects.filter(groups__name="Student")
choices = ["A", "B", "C", "D"]


divb = Special_Students.objects.filter(category_name="Division B")
# print(diva)

for student in allUsers:
    diva = Special_Students.objects.filter(students = student)
    category = diva[0].category_name
    if category == "Division A":
        quespaper = Question_Paper.objects.get(qPaperTitle="General Knowledge 1")
        stuexam = StuExam_DB.objects.get_or_create(student=student, examname="General Knowledge 1", qpaper=quespaper)
        score = 0
        allquests = quespaper.questions
        for question in allquests:
            choiceat = random.choices(choices)
            quesfaced = Stu_Question(question=question, optionA=question.optionA, optionB=question.optionB,
                                            optionC=question.optionC, optionD=question.optionD,
                                            answer=question.answer, student=student, choice=choiceat)

            if choiceat == question.answer:
                score += 1

            quesfaced.save()
            stuexam.questions.add(quesfaced)
            stuexam.save()
        stuexam.completed = 1
        stuexam.score = score
        stuexam.save()
#second iteration to attempt SE exam
        quespaper = Question_Paper.objects.get(qPaperTitle="Software Engineering 1")
        stuexam = StuExam_DB.objects.get_or_create(student=student, examname="Software Engineering 1", qpaper=quespaper)
        score = 0
        allquests = quespaper.questions
        for question in allquests:
            choiceat = random.choice(choices)
            quesfaced = Stu_Question(question=question, optionA=question.optionA, optionB=question.optionB,
            optionC=question.optionC, optionD=question.optionD,
            answer=question.answer, student=student, choice=choiceat)
            quesfaced.save()
            stuexam.questions.add(quesfaced)
            stuexam.save()

            if choiceat == question.answer:
                score += 1

        stuexam.completed = 1
        stuexam.score = score
        stuexam.save()
        #third iteration to attempt Business
        quespaper = Question_Paper.objects.get(qPaperTitle="Business 1")
        stuexam = StuExam_DB.objects.get_or_create(student=student, examname="Business 1", qpaper=quespaper)
        score = 0
        allquests = quespaper.questions
        for question in allquests:
            choiceat = random.choice(choices)
            quesfaced = Stu_Question(question=question, optionA=question.optionA, optionB=question.optionB,
            optionC=question.optionC, optionD=question.optionD,
            answer=question.answer, student=student, choice=choiceat)
            quesfaced.save()
            stuexam.questions.add(quesfaced)
            stuexam.save()

            if choiceat == question.answer:
                score += 1
        stuexam.completed = 1
        stuexam.score = score
        stuexam.save()

    else:
        quespaper = Question_Paper.objects.get(qPaperTitle="General Knowledge 2")
        stuexam = StuExam_DB.objects.get_or_create(student=student, examname="General Knowledge 2", qpaper=quespaper)
        score = 0
        allquests = quespaper.questions
        for question in allquests:
            choiceat = random.choice(choices)
            quesfaced = Stu_Question(question=question, optionA=question.optionA, optionB=question.optionB,
                                            optionC=question.optionC, optionD=question.optionD,
                                            answer=question.answer, student=student, choice=choiceat)
            quesfaced.save()
            stuexam.questions.add(quesfaced)
            stuexam.save()

            if choiceat == question.answer:
                score += 1
        stuexam.completed = 1
        stuexam.score = score
        stuexam.save()
#second iteration to attempt SE 2
        quespaper = Question_Paper.objects.get(qPaperTitle="Software Engineering 2")
        stuexam = StuExam_DB.objects.get_or_create(student=student, examname="Software Engineering 2", qpaper=quespaper)
        score = 0
        allquests = quespaper.questions
        for question in allquests:
            choiceat = random.choice(choices)
            quesfaced = Stu_Question(question=question, optionA=question.optionA, optionB=question.optionB,
            optionC=question.optionC, optionD=question.optionD,
            answer=question.answer, student=student, choice=choiceat)
            quesfaced.save()
            stuexam.questions.add(quesfaced)
            stuexam.save()

            if choiceat == question.answer:
                score += 1
        stuexam.completed = 1
        stuexam.score = score
        stuexam.save()
        #third iteration to attempt Business 2
        quespaper = Question_Paper.objects.get(qPaperTitle="Business 2")
        stuexam = StuExam_DB.objects.get_or_create(student=student, examname="Business 2", qpaper=quespaper)
        score = 0
        allquests = quespaper.questions
        for question in allquests:
            choiceat = random.choice(choices)
            quesfaced = Stu_Question(question=question, optionA=question.optionA, optionB=question.optionB,
            optionC=question.optionC, optionD=question.optionD,
            answer=question.answer, student=student, choice=choiceat)
            quesfaced.save()
            stuexam.questions.add(quesfaced)
            stuexam.save()

            if choiceat == question.answer:
                score += 1
        stuexam.completed = 1
        stuexam.score = score
        stuexam.save()

# class Stu_Question(Question_DB):
#     professor = None
#     student = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
#     choice = models.CharField(max_length=3, default="E")
# class StuExam_DB(models.Model):
#     student = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
#     examname = models.CharField(max_length=100)
#     qpaper = models.ForeignKey(Question_Paper, on_delete=models.CASCADE, null=True)
#     questions = models.ManyToManyField(Stu_Question)
#     score = models.IntegerField(default=0)
#     completed = models.IntegerField(default=0)
# class StuResults_DB(models.Model):
#     student = models.ForeignKey(User, limit_choices_to={'groups__name': "Student"}, on_delete=models.CASCADE, null=True)
#     exams = models.ManyToManyField(StuExam_DB)
