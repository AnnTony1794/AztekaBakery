from .models import Link


def context_processor(request):
    context_dict = dict([(item.key, item.url) for item in Link.objects.all()])
    return context_dict