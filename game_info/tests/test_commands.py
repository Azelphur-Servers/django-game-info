from django.core.management import call_command
from django.test import TestCase
from game_info.models import Server


class CommandTest(TestCase):
    def create_server(self, title="Test Server", host="example.org", port=27015):
        return Server.objects.create(title=title, host=host, port=port)

    def test_update_game_info(self):
        self.create_server().save()
        call_command('update_game_info')
