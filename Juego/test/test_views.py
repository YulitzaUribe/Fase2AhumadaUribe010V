from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from Juego.models import Post

class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cantidad_de_post = 13

        for Post_id in range(cantidad_de_post):
            Post.objects.create(
                title=f'Accion {Post_id}',
                content=f'Prueba {Post_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/Juego/posts/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Juego/post_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['post_list']) == 10)

    def test_lists_all_genres(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('posts')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['post_list']) == 3)
