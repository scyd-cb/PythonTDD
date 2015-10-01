from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_html(self):
        request = HttpRequest()         # http request made by the user
        response = home_page(request)   # htpp response send by the view it returns a HttpResponse object
        expected_html = render_to_string('home.html')
        self.assertEqual(expected_html, response.content.decode())
        #print('content' + repr(response.content))
        #self.assertTrue(response.content.startswith(b'<html>'))  # response.content is html page 
        #self.assertIn(b'<title>To-Do lists</title>', response.content)
        #self.assertTrue(response.content.strip().endswith(b'</html>'))



