from unittest import TestCase

from flask import json

from api.__init__ import APP


class TestEndpoints(TestCase):
    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def create_record(self, createdBy, red_flag_title, red_flag_comment):
        post_data = self.client().post(
            '/api/v1/redflag/',
            data=json.dumps(dict(
                createdBy=createdBy,
                red_flag_title=red_flag_title,
                red_flag_comment=red_flag_comment
            )),
            content_type='application/json'
        )
        return post_data

    def test_create_record(self):
        post = self.create_record('masete', 'finance', 'malaria fund')
        response = json.loads(post.data.decode())
        self.assertIn(response['status'], 'Success')
        self.assertIn(response['message'], 'Redflag has been created')
        self.assertTrue(response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)
