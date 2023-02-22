
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = MenuItem.objects.create(name='Pizza', price=10)
        self.menu2 = MenuItem.objects.create(name='Burger', price=5)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)



class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer




