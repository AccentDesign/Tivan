from django.test import TestCase

# Create your tests here.


class LibraryTest(TestCase):
    def test_home_page(self):
        r = self.client.get('/')
        self.assertEqual(r.status_code, 200)

    def test_index(self):
        r = self.client.get('/library/')
        self.assertEqual(r.status_code, 200)
