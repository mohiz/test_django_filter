from rest_framework import generics
import django_filters
from models import Billing, Person
from serializers import PersonSerializer

class PersonFilter(django_filters.FilterSet):
    start_time = django_filters.DateFromToRangeFilter(name='sessions__start_time',
                                                      distinct=True)
    billing_status = django_filters.ChoiceFilter(name='sessions__billing__status',
                                                 choices=Billing.STATUS,
                                                 distinct=True)

    class Meta:
        model = Person
        fields = ('first_name', 'last_name')

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = PersonFilter
