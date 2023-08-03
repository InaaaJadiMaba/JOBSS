from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import MagangSerializers
from .models import magang


def jobstreet(request):
    return HttpResponse('oooolalala')

class MagangViewSet(viewsets.ModelViewSet):
    serializer_class = MagangSerializers
    queryset = magang.objects.all()