from django.http import JsonResponse
from django.contrib.auth.models import User


def user_json(request):
    users = User.objects.all()
    data = [{'username': item.username, 'email': item.email} for item in users]
    return JsonResponse({'data': data})
