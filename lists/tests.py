from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_html(self):
        request = HttpRequest()         # http request made by the user
        response = home_page(request)   # htpp response send by the view it returns a HttpResponse object
        self.assertTrue(response.content.startswith(b'<html>'))  # response.content is html page 
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))


