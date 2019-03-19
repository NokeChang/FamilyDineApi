from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory


class ProductTests(APITestCase):
    def test_can_get_article_list(self):
        # articles = Article.objects.create(name='Apple Watch', price=500, stock=3)
        response = self.client.get(f'/api/articles/')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, ProductSerializer(instance=product).data)


