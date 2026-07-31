import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedRecommender:
    """
    Content-based news recommendation using TF-IDF.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_features=5000,
        )

        self.tfidf_matrix = None
        self.news = None

    def fit(self, news: pd.DataFrame):
        """
        Learn TF-IDF representations of all articles.
        """

        self.news = news.copy()

        self.news["text"] = (
            self.news["title"].fillna("")
            + " "
            + self.news["abstract"].fillna("")
        )

        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.news["text"]
        )

        return self

    def recommend(self, news_id, top_n=5):
        """
        Recommend articles similar to one article.
        """

        idx = self.news.index[
            self.news["news_id"] == news_id
        ][0]

        similarity = cosine_similarity(
            self.tfidf_matrix[idx],
            self.tfidf_matrix
        ).flatten()

        similar = np.argsort(similarity)[::-1]
        similar = similar[1 : top_n + 1]
        recommendations = self.news.iloc[similar][
            [
                "news_id",
                "title",
                "category",
                ]
            ].copy()
        recommendations["similarity"] = similarity[similar]
        return recommendations