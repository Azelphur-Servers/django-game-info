from django.core.management import call_command
from django.test import TestCase


class ServerTest(TestCase):
    def test_update_game_info(self):
        call_command('update_game_info')
