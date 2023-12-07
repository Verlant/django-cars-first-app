from django.db import models
# La marque
# Le modèle
# L’année de construction
# La cylindrée
# La version (break, coupé etc.)
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.


class Car(models.Model):
    marque = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    annee_construction = models.DateField('annee_construction')
    cylindree = models.CharField(max_length=200)
    version = models.CharField(max_length=200)

    def __str__(self):
        return self.marque + " " + self.model