import mock
import random
from django.test import TestCase
from game_info.models import Server, Player, Rule
from valve.source import messages, util, a2s


class MockServerQuerier():
    def __init__(self, address):
        pass

    def get_info(self):
        i = messages.InfoResponse()
        i['response_type'] = 73
        i['protocol'] = 17
        i['server_name'] = u'A test server'
        i['map'] = u'ctf_2fort'
        i['folder'] = u'tf'
        i['game'] = u'Team Fortress'
        i['app_id'] = 440
        i['player_count'] = 31
        i['max_players'] = 31
        i['bot_count'] = 0
        i['server_type'] = util.ServerType(100)
        i['platform'] = util.Platform(108)
        i['password_protected'] = 0
        i['vac_enabled'] = 1
        i['version'] = u'3200676'
        return i

    def get_players(self):
        players = messages.PlayersResponse()
        players['player_count'] = 32
        players['response_type'] = 68
        players['players'] = []
        for i in range(1, 33):
            player = messages.PlayerEntry()
            player['index'] = 0
            player['name'] = "Player %d" % (i)
            player['score'] = random.randrange(1000)
            player['duration'] = random.uniform(1, 10000)
            players['players'].append(player)
        return players

    def get_rules(self):
        r = messages.RulesResponse()
        r['rule_count'] = 2
        r['rules'] = {
            'sv_alltalk': u'0',
            'sv_voiceenable': u'1'
        }
        return r


class MockServerDownQuerier():
    def __init__(self, address):
        pass

    def get_info(self):
        raise a2s.NoResponseError("Timed out waiting for response")

    def get_players(self):
        raise a2s.NoResponseError("Timed out waiting for response")

    def get_rules(self):
        raise a2s.NoResponseError("Timed out waiting for response")


class ServerTest(TestCase):

    def create_server(self, title="Test Server", host="example.org", port=27015):
        return Server.objects.create(title=title, host=host, port=port)

    def create_player(self, server, name="Bob", score=100, duration=1000.0):
        return Player.objects.create(server=server, name=name, score=score, duration=duration)

    def create_rule(self, server, cvar="sv_gravity", value="800"):
        return Rule.objects.create(server=server, cvar=cvar, value=value)

    def test_server_creation(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.__unicode__(), s.title)

    @mock.patch('valve.source.a2s.ServerQuerier', MockServerQuerier)
    def test_update_info(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_info(), True)

    @mock.patch('valve.source.a2s.ServerQuerier', MockServerQuerier)
    def test_update_players(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_players(), True)

    @mock.patch('valve.source.a2s.ServerQuerier', MockServerQuerier)
    def test_update_rules(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_rules(), True)

    @mock.patch('valve.source.a2s.ServerQuerier', MockServerDownQuerier)
    def test_update_info_exception(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_info(), False)

    @mock.patch('valve.source.a2s.ServerQuerier', MockServerDownQuerier)
    def test_update_players_exception(self):
        s = self.create_server()
        self.assertTrue(isinstance(s, Server))
        self.assertEqual(s.update_players(), False)

    @mock.patch('valve.source.a2s.ServerQuerier', MockServerDownQuerier)
    def test_update_rules_exception(self):
        s = self.create_server()
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
