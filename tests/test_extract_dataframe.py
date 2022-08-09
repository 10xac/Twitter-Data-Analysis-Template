import os
import sys
import unittest
import pandas as pd
from defaults import *

#sys.path.append(os.path.abspath(os.path.join("../..")))
sys.path.append("..")

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below

_, tweet_list = read_json(processed_global_data)

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        # tweet_df = self.df.get_tweet_df()

    def test_find_status_count(self):
        """
        Test case for the find status count method
        """
        # error test
        # self.assertEqual(self.df.find_statuses_count(),
        # [204051, 3462, 6727, 45477, 277957])

        # the edited error test
        self.assertEqual(self.df.find_status_count(),
                         [40, 40, 40, 40, 40])

    def test_find_full_text(self):
        """
        Test case for hte find full text method
        """
        # error test case
        error_text = ['🚨Africa is "in the midst of a full-blown third wave" of coronavirus, the head of @WHOAFRO has warned\n\nCases have risen across the continent by more than 20% and deaths have also risen by 15% in the last week\n\n@jriggers reports ~ 🧵\nhttps://t.co/CRDhqPHFWM', 'Dr Moeti is head of WHO in Africa, and one of the best public health experts and leaders I know. Hers is a desperate request for vaccines to Africa. We plead with Germany and the UK to lift patent restrictions and urgently transfer technology to enable production in Africa. https://t.co/sOgIroihOc', "Thank you @research2note for creating this amazing campaign &amp; turning social media #red4research today. @NHSRDFORUM is all about sharing the talent, passion  &amp; commitment of individuals coming together as a community for the benefit of all. You've done this. Well done 👋", 'Former Pfizer VP and Virologist, Dr. Michael Yeadon, is one of the most credentialed medical professionals speaking out about the dangers of the #Covid19 vaccines, breaks down his “list of lies” that keeps him up at night. https://t.co/LSE8CrKdqn', 'I think it’s important that we don’t sell COVAX short. It still has a lot going for it and is innovative in its design. But it needs more vaccines to share.  We’re hoping our low cost @TexasChildrens recombinant protein COVID19 vaccine with @biological_e will help fill some gaps']

        # the edited test case
        text = ['RT @nikitheblogger: Irre: Annalena Baerbock sagt, es bricht ihr das Herz, dass man nicht bedingungslos schwere Waffen liefert.\nMir bricht e\u2026',
                'RT @sagt_mit: Merkel schaffte es in 1 Jahr 1 Million \"Fl\u00fcchtlinge\" durchzuf\u00fcttern, jedoch nicht nach 16 Jahren 1 Million Rentner aus der Ar\u2026',
                'RT @Kryptonoun: @WRi007 Pharma in Lebensmitteln, Trinkwasser, in der Luft oder in der Zahnpasta irgendwo muss ein Beruhigungsmittel bzw. Be\u2026',
                'RT @WRi007: Die #Deutschen sind ein braves Volk!. Mit #Spritpreisen von 2 Euro abgefunden. Mit #inflation abgefunden. Mit h\u00f6heren #Abgaben\u2026',
                'RT @RolandTichy: Baerbock verk\u00fcndet mal so nebenhin in Riga das Ende der Energieimporte aus Russland. Habeck rudert schon zur\u00fcck, Scholz sc\u2026']
        self.assertEqual(self.df.find_full_text(), text)

    def test_find_sentiments(self):
        """
        Test case for the find sentiments method
        """
        # error test case
        error_sentiment_values = ([0.16666666666666666, 0.13333333333333333,
                                  0.3166666666666667, 0.08611111111111111,
                                  0.27999999999999997],
                                  [0.18888888888888888, 0.45555555555555555,
                                  0.48333333333333334, 0.19722222222222224,
                                  0.6199999999999999])

        # the edited error test
        sentiment_values = ([0.0, 0.0, 0.0, 0.0, 0.0],
                            [0.0, 0.0, 0.0, 0.0, 0.0])
        self.assertEqual(self.df.find_sentiments(self.df.find_full_text()),
                         sentiment_values)

    def test_find_created_time(self):
        """
        Test case for the find created time method
        """
        # error test case
        created_at = ['Fri Jun 18 17:55:49 +0000 2021',
                      'Fri Jun 18 17:55:59 +0000 2021',
                      'Fri Jun 18 17:56:07 +0000 2021',
                      'Fri Jun 18 17:56:10 +0000 2021',
                      'Fri Jun 18 17:56:20 +0000 2021']

        # the edited test case
        really_created_at = ['Fri Apr 22 22:20:18 +0000 2022',
                             'Fri Apr 22 22:19:16 +0000 2022',
                             'Fri Apr 22 22:17:28 +0000 2022',
                             'Fri Apr 22 22:17:20 +0000 2022',
                             'Fri Apr 22 22:13:15 +0000 2022']
        self.assertEqual(self.df.find_created_time(), really_created_at)

    def test_find_screen_name(self):
        """
        Test case for the find screen name method
        """
        # error test case
        error_name_test_Case = ['ketuesriche', 'Grid1949',
                                'LeeTomlinson8', 'RIPNY08', 'pash22']
        # the edited error test
        name = ['McMc74078966', 'McMc74078966', 'McMc74078966',
                'McMc74078966', 'McMc74078966']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        """
        Test case for the find followers count method
        """
        # error test
        error_f_count = [551, 66, 1195, 2666, 28250]

        # the edited error test
        f_count = [3, 3, 3, 3, 3]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        """
        Test case for the find friends count method
        """
        # error test
        error_friends_count = [351, 92, 1176, 2704, 30819]

        # edited error test
        friends_count = [12, 12, 12, 12, 12]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(), <provide a list of the first five is_sensitive values>)


    # def test_find_hashtags(self):
    #     self.assertEqual(self.df.find_hashtags(), )

    # def test_find_mentions(self):
    #     self.assertEqual(self.df.find_mentions(), )



if __name__ == "__main__":
    unittest.main()

