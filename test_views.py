from unittest import TestCase

from flask import json

from run import app


class TestEndpoints(TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    def create_user(self, first_name, last_name, other_name, email, user_name, phone_number, password, is_admin):
        post_user = self.client().post(
            '/api/auth/user',
            data=json.dumps(dict(
                first_name=first_name,
                last_name=last_name,
                other_name=other_name,
                email=email,
                user_name=user_name,
                phone_number=phone_number,
                password=password,
                is_admin=is_admin

            )),
            content_type='application/json'
        )
        return post_user

    def test_register_user(self):
        new_user = self.create_user('masete', 'nicholas', 'joel', 'masete@gmail.com', 'jkl', '0775406407', '7846', 'false')
        response = json.loads(new_user.data.decode())
        self.assertIn(response['massage'], 'user created successfully')
        self.assertEqual(new_user.status_code, 201)

    def test_wrong_email(self):
        new_user = self.create_user('masete', 'nicholas', 'joel', 'masete_gmail.com', 'jkl', '0775406407', '7846', 'false')
        response = json.loads(new_user.data.decode())
        self.assertIn(response['error'], 'Please use a valid email address for example nich@gmail')
        self.assertEqual(new_user.status_code, 400)

    def create_record(self, created_by, flag_title, flag_latitude, flag_longitude, flag_comment):
        post_data = self.client().post(
            '/api/v1/red-flags/',
            data=json.dumps(dict(
                created_by=created_by,
                flag_title=flag_title,
                flag_latitude=flag_latitude,
                flag_longitude=flag_longitude,
                flag_comment=flag_comment
            )),
            content_type='application/json'
        )
        return post_data

    def test_create_record(self):
        post = self.create_record('masete', 'finance', 45.6, 35.7, 'malaria fund')
        response = json.loads(post.data.decode())
        self.assertIn(response['message'], 'Redflag has been created')
        self.assertTrue(response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 201)

    def test_empty_fields(self):
        post = self.create_record(' ', 'education', 78.9, 78.9, 'no corruption')
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], '400')
        self.assertTrue(post_response['error_message'], 'You have missing feilds ')
        self.assertFalse(post_response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_location_for_int(self):
        post = self.create_record('money', 'education', "jh", 67.4, 'no corruption')
        post_response = json.loads(post.data.decode())
        self.assertEquals(post_response['status'], '400')
        self.assertTrue(post_response['error_message'], 'Please an integer is needed here')
        self.assertFalse(post_response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_title_for_string(self):
        post = self.create_record('money', 8976, 6.4, 6.9, 'temangalo land')
        post_response = json.loads(post.data.decode())
        self.assertEquals(post_response['status'], '400')
        self.assertEquals(post_response['error_message'], 'Please a string is for redflag title and comment thanks')
        self.assertFalse(post_response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_comment_for_string(self):
        post = self.create_record('money', "no no", 67.4, 9.0, 5633)
        post_response = json.loads(post.data.decode())
        self.assertEquals(post_response['status'], '400')
        self.assertEquals(post_response['error_message'], 'Please a string is for redflag title and comment thanks')
        self.assertFalse(post_response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_record_with_invalid_data(self):
        post = self.create_record('university', 'education', 'masindi', 67.7, 'no corruption')
        post_response = json.loads(post.data.decode())
        self.assertTrue(post_response['status'], '400')
        self.assertTrue(post_response['error_message'], 'Please an integer is needed here')
        self.assertFalse(post_response['data'])
        self.assertTrue(post.content_type, 'application/json')
        self.assertEqual(post.status_code, 400)

    def test_get_redflags(self):
        self.create_record('books', 'okay', 45.7,7.87, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().get('/api/v1/red-flags/')

        response_data = json.loads(request_data.data.decode())
        self.assertTrue(response_data['status'], '200')
        self.assertTrue(request_data, dict)
        self.assertTrue(response_data['data'])
        self.assertEqual(request_data.status_code, 200)

    def test_get_redflag_that_exists(self):
        self.create_record('books', 'okay', 45.7, 65.8, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().get('/api/v1/red-flags/2/')

        response_data = json.loads(request_data.data.decode())
        self.assertIn(response_data['status'], '200')
        self.assertTrue(response_data['message'], 'redflag exists')
        self.assertTrue(response_data['data'])
        self.assertTrue(request_data, dict)
        self.assertEqual(request_data.status_code, 200)

    def test_get_redflag_not_existing(self):
        self.create_record('books', 'okay', 45.8, 45.7, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().get('/api/v1/red-flags/1008/')

        response_data = json.loads(request_data.data.decode())
        self.assertIn(response_data['status'], '404')
        self.assertIn(response_data['error_message'], 'redflag does not exist')
        self.assertTrue(request_data, dict)
        self.assertFalse(response_data['data'])
        self.assertEqual(request_data.status_code, 400)

    def test_edit_comment_absent(self):
        self.create_record('books', 'okay', 45.7, 67.3, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().put(
            '/api/v1/red-flags/30/',
            data=json.dumps(dict(
                type="all corruption",
                payload="red_flag_comment"
            )),
            content_type='application/json'
        )
        response_data = json.loads(request_data.data.decode())
        self.assertIn(response_data['message'], 'no record')
        self.assertEqual(request_data.status_code, 400)
        self.assertTrue(request_data, dict)

    def test_delete_data(self):
        self.create_record('books', 'okay', 45.7, 56.3, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().delete(
            '/api/v1/red-flags/1/')
        response_data = json.loads(request_data.data.decode())
        self.assertEqual(request_data.status_code, 200)
        self.assertTrue(response_data['data'])
        self.assertEqual(response_data['data'], [{'id': 1, 'message': 'redflag record has been deleted'}])

    def test_delete_data_not_existing(self):
        self.create_record('books', 'okay', 45.7, 67.4, 'zero no corruption')
        self.create_record('maj.masete', 'UPDF', 6758, 'stolen guns')

        request_data = self.client().delete(
            '/api/v1/red-flags/100/')

        response_data = json.loads(request_data.data.decode())
        self.assertIn(response_data['message'], 'no redflag to delete')
        self.assertTrue(response_data, dict)
        self.assertEqual(request_data.status_code, 400)











