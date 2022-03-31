import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'portal.settings')

import django
django.setup()

from main.models.question import Question_DB
questions = Question_DB.objects.all()

#pseudo code for accessing one Question at a time and updating the answer to a single alphabet
for i in questions:
    print(i.answer)
    if i.optionA == i.answer:
        i.answer = "A"
    elif i.optionB == i.answer:
        i.answer = "B"
    elif i.optionC == i.answer:
        i.answer = "C"
    elif i.optionD == i.answer:
        i.answer = "D"
    else:
        pass
    i.save()
    print(i.answer)

# professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete=models.CASCADE, null=True)
# qno = models.AutoField(primary_key=True)
# question = models.CharField(max_length=100)
# optionA = models.CharField(max_length=100)
# optionB = models.CharField(max_length=100)
# optionC = models.CharField(max_length=100)
# optionD = models.CharField(max_length=100)
# answer = models.CharField(max_length=200)
