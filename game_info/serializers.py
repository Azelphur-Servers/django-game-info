from rest_framework import serializers
from .models import Server, Info, Rule, Player


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        exclude = ("server", )


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        exclude = ("id", "server")


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = ("id", "server")


class ServerSerializer(serializers.ModelSerializer):
    info = InfoSerializer(read_only=True)
    players = PlayerSerializer(source='player_set', many=True)
    rules = RuleSerializer(source='rule_set', many=True)

    class Meta:
        model = Server
        exclude = ("get_info", "get_players", "get_rules")
