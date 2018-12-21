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



