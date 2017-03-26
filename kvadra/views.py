from annoying.decorators import render_to
from .models import Text


@render_to('add_text.html')
def uploadText(request):
    """
    Форма добавления текста
    :param request:
    :return:
    """

    return {}


@render_to('list.html')
def getText(request):
    """
    Список текстов
    :param request:
    :return:
    """
    text_list = Text.objects.all()

    return {'text_list': text_list}
