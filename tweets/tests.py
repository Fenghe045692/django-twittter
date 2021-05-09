from django.test import TestCase
from django.contrib.auth.models import User
from tweets.models import Tweet
from utils.time_helpers import utc_now
from datetime import timedelta

class TweetTests(TestCase):

    def test_hours_now(self):
        jason = User.objects.create_user(username='jason@edu.com')
        tweet = Tweet.objects.create(user=jason, content='test hours now')
        tweet.created_at = utc_now() - timedelta(hours=10)
        tweet.save()
        self.assertEqual(tweet.hours_to_now, 10)
