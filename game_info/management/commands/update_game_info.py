from django.core.management.base import BaseCommand, CommandError
from game_info.models import Server, Info, Player, Rule


class Command(BaseCommand):
    args = ''
    help = 'Update the game server information'

    def handle(self, *args, **options):
        for server in Server.objects.all():
            if server.get_info:
                server.update_info()
            if server.get_players:
                server.update_players()
            if server.get_rules:
                server.update_rules()
