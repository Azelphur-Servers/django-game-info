from django.db import models
import valve.source.a2s

SERVER_TYPES = (
    (68, 'Dedicated'),
    (100, 'Dedicated'),
    (108, 'Non-dedicated'),
    (112, 'SourceTV'),
)

PLATFORMS = (
    (76, 'Linux'),
    (108, 'Linux'),
    (109, 'Mac OS X'),
    (111, 'Mac OS X'),
    (119, 'Windows')
)


class Server(models.Model):
    title = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    port = models.IntegerField()

    # Whether we should run a2s_info queries.
    get_info = models.BooleanField(default=True)

    # Whether we should get a list of players.
    get_players = models.BooleanField(default=True)

    # Whether we should get the servers rules (cvars).
    get_rules = models.BooleanField(default=True)

    # True if the server is contactable, otherwise False.
    up = models.BooleanField(default=True, editable=False)

    updated_at = models.DateTimeField(auto_now=True)

    def update_info(self):
        a2s = valve.source.a2s.ServerQuerier((self.host, self.port))
        try:
            info = a2s.get_info()
        except valve.source.a2s.NoResponseError:
            self.up = False
            self.save()
            return False
        info_model = Info(server=self)
        info_model.server_name = info['server_name']
        info_model.map = info['map']
        info_model.folder = info['folder']
        info_model.game = info['game']
        info_model.app_id = info['app_id']
        info_model.player_count = info['player_count']
        info_model.max_players = info['max_players']
        info_model.bot_count = info['bot_count']
        info_model.server_type = info['server_type'].value
        info_model.platform = info['platform'].value
        info_model.password_protected = info['password_protected']
        info_model.vac_enabled = info['vac_enabled']
        info_model.version = info['version']
        info_model.save()
        return True

    def update_players(self):
        a2s = valve.source.a2s.ServerQuerier((self.host, self.port))
        try:
            players = a2s.get_players()
        except valve.source.a2s.NoResponseError:
            self.up = False
            self.save()
            return False

        player_models = []
        for player in players['players']:
            player_models.append(Player(
                name=player['name'],
                score=player['score'],
                duration=player['duration']
            ))
        self.player_set.all().delete()
        self.player_set = player_models
        return True

    def update_rules(self):
        a2s = valve.source.a2s.ServerQuerier((self.host, self.port))
        try:
            rules = a2s.get_rules()
        except valve.source.a2s.NoResponseError:
            self.up = False
            self.save()
            return False

        rule_models = []
        for cvar, value in rules['rules'].items():
            rule_models.append(Rule(
                cvar=cvar,
                value=str(value)
            ))
        self.rule_set.all().delete()
        self.rule_set = rule_models
        return True

    def __unicode__(self):
        return self.title


class Info(models.Model):
    """
        Stores a game servers response to a2s_info, this contains
        General information about the server, such as player count and
        the current map.
    """

    server = models.OneToOneField(
        Server,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    # The name of the server as returned by a2s_info
    server_name = models.CharField(max_length=256)

    # The name of the map the server is currently running
    map = models.CharField(max_length=64)

    # The gamedir of the mod being ran by the server, E.g "tf" or "csgo"
    folder = models.CharField(max_length=64)

    # A string identifying the game being ran by the server
    game = models.CharField(max_length=64)

    # The numberic application ID of the game ran by the server, note that the
    # ID of the client is returned, not the server. For example TF2 is 440
    # instead of 232250 which is the server software
    app_id = models.IntegerField()

    player_count = models.IntegerField()
    max_players = models.IntegerField()
    bot_count = models.IntegerField()
    server_type = models.IntegerField(choices=SERVER_TYPES)
    platform = models.IntegerField(choices=PLATFORMS)
    password_protected = models.BooleanField()
    vac_enabled = models.BooleanField()
    version = models.IntegerField()


class Player(models.Model):
    """
        Stores a game servers response to a2s_player, this contains
        a list of who is playing, their score, etc.
    """
    server = models.ForeignKey(Server)
    name = models.CharField(max_length=64)
    score = models.IntegerField()
    duration = models.FloatField()

    def __unicode__(self):
        return self.name


class Rule(models.Model):
    """
        Stores a subset of a server's console variables (often referred to as
        'cvars',) specifically those which have the ``FCVAR_NOTIFY`` flag set
        on them. These cvars are used to indicate game mode's configuration,
        such as the gravity setting for the map or whether friendly fire is
        enabled or not. You could also use this to transmit data from the
        server to django by having your plugin create a cvar.
    """
    server = models.ForeignKey(Server)
    cvar = models.CharField(max_length=64)
    value = models.CharField(max_length=64)

    def __unicode__(self):
        return self.cvar
