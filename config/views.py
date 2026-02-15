from django.http import HttpResponse

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponse(
            f"Вы вошли как {request.user.email} | "
            "<a href='/accounts/logout/'>Выйти</a>"
        )
    else:
        return HttpResponse(
            "Вы не вошли | <a href='/accounts/login/'>Войти</a>"
        )
