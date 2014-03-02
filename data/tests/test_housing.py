
import template
import json


class TestHousingRoutes(template.TestingTemplate):

    def test_rooms_two_valid_attr(self):
        """ test query for /rooms with 2 valid attr """
        resp = self.app.get('/housing/rooms?is_suite=false&point_value=10')
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(100, len(json_resp['results']))

    def test_rooms_page_too_far(self):
        """ test that an error is returned after paging too far """
        resp = self.app.get('/housing/rooms/5?is_suite=false&point_value=10')
        self.check_error(resp, 'NO_RESULTS')

        resp = self.app.get('/housing/rooms/100')
        self.check_error(resp, 'NO_RESULTS')

    def test_rooms_options_valid_attribute(self):
        """ test that the response is valid for an options request """
        resp = self.app.get('/housing/rooms/options/room_type')
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(len(json_resp['results']), 9)

    def test_rooms_options_invalid_attribute(self):
        """ test that an error is returned with an invalid attribute """
        attr = 'fake_attr'
        resp = self.app.get('/housing/rooms/options/{}'.format(attr))
        self.check_error(resp, 'INVALID_ATTRIBUTE',
                         options={'attr_name': attr})

        attr = 'another_fake_attr'
        resp = self.app.get('/housing/rooms/options/{}'.format(attr))
        self.check_error(resp, 'INVALID_ATTRIBUTE',
                         options={'attr_name': attr})

    def test_rooms_options_no_query_parameter(self):
        """
        Test that the response is valid for an options request w/o querystring
        filtering
        """
        resp = self.app.get('/housing/rooms/options/room_type')
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(len(json_resp['results']), 9)

    def test_rooms_options_valid_query_parameter(self):
        """
        Test that the response is valid for an options request with query
        parameter
        """
        resp = self.app.get('/housing/rooms/options/room_type?room_area=200')
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(len(json_resp['results']), 2)

    def test_buildings_two_valid_attr(self):
        """ test query for /rooms with 2 valid attr """
        resp = self.app.get(('/housing/buildings?corridor_style=false&'
                             'semi_private_kitchen=true'))
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(5, len(json_resp['results']))

    def test_buildings_page_too_far(self):
        """ test that an error is returned after paging too far """
        resp = self.app.get('/housing/buildings/5?private_bathroom=true')
        self.check_error(resp, 'NO_RESULTS')

        resp = self.app.get('/housing/rooms/100')
        self.check_error(resp, 'NO_RESULTS')

    def test_buildings_options_valid_attribute(self):
        """ test that the response is valid for an options request """
        resp = self.app.get('/housing/buildings/options/lounge')
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(len(json_resp['results']), 7)

    def test_buildings_options_invalid_attribute(self):
        """ test that an error is returned with an invalid attribute """
        attr = 'fake_attr'
        resp = self.app.get('/housing/buildings/options/{}'.format(attr))
        self.check_error(resp, 'INVALID_ATTRIBUTE',
                         options={'attr_name': attr})

        attr = 'another_fake_attr'
        resp = self.app.get('/housing/buildings/options/{}'.format(attr))
        self.check_error(resp, 'INVALID_ATTRIBUTE',
                         options={'attr_name': attr})

    def test_buildings_options_no_query_parameter(self):
        """
        Test that the response is valid for an options request w/o querystring
        filtering
        """
        resp = self.app.get('/housing/buildings/options/building')
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(len(json_resp['results']), 20)

    def test_buildings_options_valid_query_parameter(self):
        """
        Test that the response is valid for an options request with query
        parameter
        """
        resp = self.app.get('/housing/buildings/options/building?'
                            'private_bathroom=true')
        json_resp = json.loads(resp.data)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(200, json_resp['status'])
        self.assertEqual(len(json_resp['results']), 3)
