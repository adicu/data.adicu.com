
from mock import patch
from template import MockingTemplate

from auth import user

test_email, test_user, test_token = 'test@test.com', 'tester', '12345'
test_record = {
    'email': test_email,
    'token': test_token,
    'name': test_user
}


class TestUser(MockingTemplate):

    def test_generate_token(self):
        """ test that it is supported by the system """
        user.generate_token()

    @patch.object(user, 'generate_token')
    @patch.object(user, 'g')
    def test_create_user(self, mock_g, mock_token):
        """ test that create_user() calls the db correctly """
        mock_token.return_value = test_token
        mock_g.redis.exists.return_value = False
        outcome = user.create_user(test_email, test_user)

        # check return token
        self.assertEqual(outcome, test_token)

        # check that the correct query was called
        self.check_query(
            mock_g.cursor.execute,
            'INSERT INTO users_t (email, token, name) VALUES (%s, %s, %s);',
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
        mock_g.redis.exists.return_value = False

        outcome = user.get_user(test_email, test_user)

        # check return val
        self.assertEqual(outcome, test_token)

        self.check_queries(
            mock_g.cursor.execute,
            ['SELECT * FROM users_t WHERE email = %s;',
             'INSERT INTO users_t (email, token, name) VALUES (%s, %s, %s);'],
            [[test_email], [test_email, test_token, test_user]]
        )

        # check that commit() was called
        self.assertTrue(mock_g.pg_conn.commit.called)

        # check that commit() was called
        self.assertTrue(mock_g.cursor.fetchone.called)
