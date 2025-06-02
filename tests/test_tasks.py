import unittest
from app import create_app

class TaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_create_and_list_task(self):
        res = self.app.post('/tasks', json={'title': 'Test'})
        self.assertEqual(res.status_code, 201)
        res = self.app.get('/tasks')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Test', res.get_data(as_text=True))

    def test_missing_title(self):
        res = self.app.post('/tasks', json={})
        self.assertEqual(res.status_code, 400)

    def test_update_task(self):
        self.app.post('/tasks', json={'title': 'Initial'})
        res = self.app.put('/tasks/1', json={'title': 'Updated'})
        self.assertEqual(res.status_code, 200)
        self.assertIn('Updated', res.get_data(as_text=True))

    def test_delete_task(self):
        self.app.post('/tasks', json={'title': 'Delete Me'})
        res = self.app.delete('/tasks/1')
        self.assertEqual(res.status_code, 204)

    def test_patch_update_title(self):
        self.app.post('/tasks', json={'title': 'Original'})
        res = self.app.patch('/tasks/1', json={'title': 'Patched Title'})
        self.assertEqual(res.status_code, 200)
        self.assertIn('Patched Title', res.get_data(as_text=True))

    def test_patch_with_no_valid_fields(self):
        self.app.post('/tasks', json={'title': 'Keep Me'})
        res = self.app.patch('/tasks/1', json={'invalid': 'nope'})
        self.assertEqual(res.status_code, 400)
        self.assertIn('No valid fields', res.get_data(as_text=True))
