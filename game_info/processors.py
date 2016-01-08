from .models import Server

def servers(request):
    return {'game_info': Server.objects.all()}
