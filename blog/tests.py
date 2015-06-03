from django.core.urlresolvers import reverse
from django.test import TestCase


class PostListViewTest(TestCase):
    def test_list(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(200, response.status_code)
        self.assertIn('David Moss', response.content)
