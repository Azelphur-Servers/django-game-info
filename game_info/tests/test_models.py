from django.test import TestCase
from game_info.models import Server, Player, Rule

SERVER_DOWN_URL = "example.org"
SERVER_UP_URL = "Surf.TF2.Azelphur.com"

# models test
class ServerTest(TestCase):

    def create_server(self, title="Test Server", host=SERVER_UP_URL, port=27015):
        return Server.objects.create(title=title, host=host, port=port)

    def create_player(self, server, name="Bob", score=100, duration=1000.0):
        return Player.objects.create(server=server, name=name, score=score, duration=duration)

    def create_rule(self, server, cvar="sv_gravity", value="800"):
        return Rule.objects.create(server=server, cvar=cvar, value=value)

    def test_server_creation(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.__unicode__(), s.title)

    def test_update_info(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_info(), True)

    def test_update_players(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_players(), True)

    def test_update_rules(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_rules(), True)

    def test_update_info_exception(self):
        s = self.create_server(host=SERVER_DOWN_URL)
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_info(), False)

    def test_update_players_exception(self):
        s = self.create_server(host=SERVER_DOWN_URL)
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_players(), False)

    def test_update_rules_exception(self):
        s = self.create_server(host=SERVER_DOWN_URL)
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_rules(), False)

    def test_player(self):
        s = self.create_server()
        p = self.create_player(s)
        self.assertTrue(isinstance(p, Player))
        self.assertEqual(p.__unicode__(), p.name)

    def test_rule(self):
        s = self.create_server()
        r = self.create_rule(s)
        self.assertTrue(isinstance(r, Rule))
        self.assertEqual(r.__unicode__(), r.cvar)

