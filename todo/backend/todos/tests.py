from django.test import TestCase

from .models import Todo 

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) :
        Todo.objects.create(title = 'Understand CORS', body = 'Cross-Origin Resource Sharing is..')


    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_obj_name = f'{todo.title}'
        self.assertEquals(expected_obj_name, 'Understand CORS')

    
    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_result = f"{todo.body}"
        self.assertEquals(expected_result, "Cross-Origin Resource Sharing is..")

    

