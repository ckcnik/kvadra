# Stdlib imports


# Core Django imports


# Third-party app imports
from rest_framework import generics, viewsets, pagination

# Internal apps imports
from .serializers import GetTextSerializer
from .models import Text


class GetTextViewSet(viewsets.ModelViewSet):
    """
    гейт для остановки тестовой кампании
    """
    serializer_class = GetTextSerializer
    queryset = Text.objects.all()
