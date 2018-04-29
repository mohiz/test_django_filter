from django.db import models

class Person(models.Model):
        first_name = models.CharField(max_length=20)
        last_name = models.CharField(max_length=20)

class PersonSession(models.Model):
    start_time = models.DateTimeField(null=False,
                                      blank=False)
    end_time = models.DateTimeField(null=True,
                                    blank=True)
    person = models.ForeignKey(Person, related_name='sessions')

class Billing(models.Model):
    DEBT = 'DE'
    BALANCED = 'BA'
    CREDIT = 'CR'

    session = models.OneToOneField(PersonSession,
                                   blank=False,
                                   null=False,
                                   related_name='billing')
    STATUS = ((BALANCED, 'Balanced'),
              (DEBT, 'Debt'),
              (CREDIT, 'Credit'))

    status = models.CharField(max_length=2,
                              choices=STATUS,
                              blank=False,
                              default=BALANCED)
