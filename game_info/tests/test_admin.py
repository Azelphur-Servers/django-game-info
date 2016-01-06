from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from game_info.admin import ServerAdmin
from game_info.models import Server


class AdminTest(TestCase):

    def test_server_admin(self):
        server_admin = ServerAdmin(Server, AdminSite())

