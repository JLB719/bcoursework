from cvbuilder.models import SkillItem
from django.test import TestCase
from django.urls import resolve
from cvbuilder.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):

        response = self.client.get('/')

        self.assertTemplateUsed(response, 'template.html')

    def test_can_save_a_POST_request(self) :
        response = self.client.post('/', data={'skill': 'A new skill'})
        self.assertEqual(SkillItem.objects.count(), 1)
        new_item = SkillItem.objects.first()
        self.assertEqual(new_item.text, 'A new skill')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],'/')

    def test_only_saves_items_when_necessary(self) :
        self.client.get('/')
        self.assertEqual(SkillItem.objects.count(), 0)

    def test_displays_all_list_items(self) :
        SkillItem.objects.create(text='itemskill 1')
        SkillItem.objects.create(text='itemskill 2')

        response = self.client.get('/')

        self.assertIn('itemskill 1', response.content.decode())
        self.assertIn('itemskill 2', response.content.decode())
class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = SkillItem()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = SkillItem()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = SkillItem.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
