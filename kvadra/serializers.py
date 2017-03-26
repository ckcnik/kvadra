# Stdlib imports


# Core Django imports


# Third-party app imports
from rest_framework import serializers

# Internal apps imports
from .models import Text


class GetTextSerializer(serializers.ModelSerializer):
    """
    Серриализатор для получения текстовой строки
    """

    class Meta:
        model = Text
        fields = ('text', )

    # def __init__(self, *args, **kwargs):
    #     if 'data' in kwargs:
    #         kwargs['data'].update({'status': TestCompany.get_status_by_name(kwargs['data']['status'])})
    #
    #     super(GetTextSerializer, self).__init__(*args, **kwargs)