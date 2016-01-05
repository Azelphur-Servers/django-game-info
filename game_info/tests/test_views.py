from django.test import TestCase
from django.core.urlresolvers import reverse
from game_info.views import ServerViewSet
from game_info.models import Server


class ViewTest(TestCase):
    def test_server_list_view(self):
        s = Server(title="Title", host="example.org", port=27015)
        s.save()
        url = reverse("server-list")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(s.title, resp.content)

