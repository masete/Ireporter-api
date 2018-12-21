from unittest import TestCase

from flask import json

from api.__init__ import APP


class TestEndpoints(TestCase):
    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def create_record(self, createdBy, red_flag_title, red_flag_location, red_flag_comment):
        post_data = self.client().post(
            '/api/v1/redflags/',
            data=json.dumps(dict(
                createdBy=createdBy,
                red_flag_title=red_flag_title,
                red_flag_location=red_flag_location,
                red_flag_comment=red_flag_comment
            )),
            content_type='application/json'
        )
        return post_data

    def test_create_record(self):
        post = self.create_record('masete', 'finance', 456789, 'malaria fund')
        response = json.loads(post.data.decode())
        self.assertIn(response['message'], 'Redflag has been created')
        self.assertTrue(response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)

    def test_empty_fields(self):
        post = self.create_record('', 'education', 78979, 'no corruption')
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], '400')
        self.assertTrue(post_response['error_message'], 'You have missing feilds ')
        self.assertFalse(post_response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_record_with_invalid_data(self):
        post = self.create_record('university', 'education', 'masindi', 'no corruption')
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], '400')
        self.assertTrue(post_response['error_message'], 'Please an integer is needed here')
        self.assertFalse(post_response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_get_orders(self):
        self.create_record('books', 'okay', 4567, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().get('/api/v1/redflags/')

        response_data = json.loads(request_data.data.decode())
        self.assertTrue(response_data['status'], '200')
        self.assertTrue(response_data['data'])
        self.assertEqual(request_data.status_code, 200)

    def test_get_redflag_that_exists(self):
        self.create_record('books', 'okay', 4567, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().get('/api/v1/redflags/2/')

        response_data = json.loads(request_data.data.decode())
        self.assertIn(response_data['status'], '200')
        self.assertTrue(response_data['message'], 'redflag exists')
        self.assertTrue(response_data['data'])
        self.assertEqual(request_data.status_code, 200)

    def test_get_redflag_not_existing(self):
        self.create_record('books', 'okay', 4567, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().get('/api/v1/redflags/1008/')

        response_data = json.loads(request_data.data.decode())
        self.assertIn(response_data['status'], '404')
        self.assertIn(response_data['error_message'], 'redflag does not exist')
        self.assertFalse(response_data['data'])
        self.assertEqual(request_data.status_code, 400)





