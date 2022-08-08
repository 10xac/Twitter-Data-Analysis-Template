import pandas as pd

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = self.df[self.df['retweet_count'] == 'retweet_count' ].index
        self.df.drop(unwanted_rows , inplace=True)
        self.df = self.df[self.df['polarity'] != 'polarity']
        return df

    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        self.df.drop_duplicates().drop_duplicates(subset='original_text', inplace=True)
        return df

    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        self.df['created_at'] = pd.to_datetime(self.df['created_at'], errors='coerce')
        self.df = self.df[self.df['created_at'] >= '2020-12-31']        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df['id'] = pd.to_numeric(self.df['id'], errors='coerce')
        self.df['subjectivity'] = pd.to_numeric(self.df['subjectivity'],
                                                errors='coerce')
        self.df['listed_count'] = pd.to_numeric(self.df['listed_count'],
                                                errors='coerce')
        self.df['retweet_count'] = pd.to_numeric(self.df['retweet_count'],
                                                 errors='coerce')
        self.df['friends_count'] = pd.to_numeric(self.df['friends_count'],
                                                 errors='coerce')
        self.df['favorite_count'] = pd.to_numeric(self.df['favorite_count'],
                                                  errors='coerce')
        self.df['statuses_count'] = pd.to_numeric(self.df['statuses_count'],
                                                  errors='coerce')
        self.df['followers_count'] = pd.to_numeric(self.df['followers_count'],
                                                   errors='coerce')
        self.df['polarity'] = pd.to_numeric(self.df['polarity'],
                                            errors='coerce')
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        df = ----
        
        return df
