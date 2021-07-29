from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

class BlogTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='ana', email='anastas@gmail.com', password='anas')
        self.post = Post.objects.create(title='A good title', body='Nice body content', author=self.user)

    def test_post_content(self):
        self.assertEqual(str(self.post.title), 'A good title')
        self.assertEqual(str(self.post.body), 'Nice body content')

    def test_post_list_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Nice body content')
        self.assertTemplateUsed(resp, 'home.html')

    def test_post_details(self):
        resp = self.client.get('/post/1/')
        no_resp = self.client.get('/post/100/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertTemplateUsed(resp, 'post_detail.html')