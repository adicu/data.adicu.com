
from mock import patch
import flask

from template import MockingTemplate, TestingTemplate
from auth import user
from errors import errors

test_email = 'test@test.com'
test_user = 'tester'
test_token = '12345'
test_rate_limit = 100
test_record = {
    'email': test_email,
    'token': test_token,
    'name': test_user,
    'rate_limit': test_rate_limit
}


class TestUser(MockingTemplate):

    @patch.object(user, 'generate_token')
    @patch.object(user, 'g')
    def test_create_user(self, mock_g, mock_token):
        """ test that create_user() calls the db correctly """
        mock_token.return_value = test_token
        mock_g.redis.sismember.return_value = False
        outcome = user.create_user(test_email, test_user)

        # check return token
        self.assertEqual(outcome, test_token)

        # check that the correct query was called
        self.check_query(
            mock_g.cursor.execute,
            ('INSERT INTO users_t (email, token, name, rate_limit) '
             'VALUES (%s, %s, %s, %s);'),
            [test_email, test_token, test_user]
        )
        # check that commit() was called
        self.assertTrue(mock_g.pg_conn.commit.called)

    @patch.object(user, 'g')
    def test_get_existing_user(self, mock_g):
        """ test that get_user() calls the db correctly with existing users """
        mock_g.cursor.fetchone.return_value = test_record
        outcome = user.get_user(test_email, test_user)

        # check return val
        self.assertEqual(outcome, test_token)

        # check that the correct query was called
        self.check_query(
            mock_g.cursor.execute,
            'SELECT * FROM users_t WHERE email = %s;',
            [test_email]
        )

        # check that commit() was called
        self.assertTrue(mock_g.cursor.fetchone.called)

    @patch.object(user, 'generate_token')
    @patch.object(user, 'g')
    def test_get_new_user(self, mock_g, mock_token):
        """ test that get_user() operates correctly with new users """
        mock_token.return_value = test_token
        mock_g.cursor.fetchone.return_value = None
        mock_g.redis.sismember.return_value = False

        outcome = user.get_user(test_email, test_user)

        # check return val
        self.assertEqual(outcome, test_token)

        self.check_queries(
            mock_g.cursor.execute,
            ['SELECT * FROM users_t WHERE email = %s;',
             ('INSERT INTO users_t (email, token, name, rate_limit) '
              'VALUES (%s, %s, %s, %s);')],
            [[test_email], [test_email, test_token, test_user]]
        )

        # check that commit() was called
        self.assertTrue(mock_g.pg_conn.commit.called)

        # check that commit() was called
        self.assertTrue(mock_g.cursor.fetchone.called)

    @patch.object(user, 'g')
    def test_valid_token_decorator(self, mock_g):
        """ test that the decorator throws errors appropriately """
        app = flask.Flask(__name__)
        app.before_request(user.check_token_validity)

        with self.assertRaises(errors.AppError):
            with app.test_request_context('/'):
                user.check_token_validity()

        mock_g.redis.sismember.return_value = False
        with app.test_request_context('/?token=123'):
            with self.assertRaises(errors.AppError):
                user.check_token_validity()

        mock_g.redis.sismember.return_value = True
        with app.test_request_context('/?token=123'):
            user.check_token_validity()

    @patch.object(user, 'g')
    def test_rate_limit_mocking(self, mock_g):
        """ test that Redis methods are called at appropriate times """
        app = flask.Flask(__name__)
        app.before_request(user.check_token_validity)

        # test the key is created properly
        mock_g.redis.sismember.return_value = True
        mock_g.redis.exists.return_value = False
        mock_g.cursor.fetchone.return_value = test_record
        with app.test_request_context('/?token=123'):
            user.rate_limit()
        self.assertEqual(
            ('rate:123', 25, 60**2/user.SPLIT_FACTOR),
            mock_g.redis.setex.call_args[0]
        )

        # test if it throws error when rate limited
        mock_g.redis.sismember.return_value = True
        mock_g.redis.exists.return_value = True
        mock_g.redis.get.return_value = 0
        with app.test_request_context('/?token=123'):
            with self.assertRaises(errors.AppError):
                user.rate_limit()


class TestUserIntegration(TestingTemplate):

    def test_generate_token(self):
        """ test that it is supported by the system """
        user.generate_token()

    def test_rate_limit_via_integration(self):
        """ test that the rate limiting operates properly """
        # do N requests to max out token
        for _ in range(100/user.SPLIT_FACTOR):
            resp = self.app.get('/housing/rooms?token=integration_test')
            self.assertEqual(200, resp.status_code)

        resp = self.app.get('/housing/rooms?token=integration_test')
        self.check_error(resp, 'RATE_LIMIT')
