import pandas as pd


class PopularityRecommender:
    """
    Recommend the most-clicked news articles.
    """

    def __init__(self):
        self.popularity = None

    def fit(self, interactions: pd.DataFrame):

        self.popularity = (
            interactions.groupby("news_id")["clicked"]
            .sum()
            .sort_values(ascending=False)
        )

        return self

    def recommend(self, top_n=10):

        return self.popularity.head(top_n)