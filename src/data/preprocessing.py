import pandas as pd


class BehaviorParser:
    """
    Utilities for converting the MIND behavior logs into
    recommendation-ready interaction data.
    """

    @staticmethod
    def parse_impressions(behaviors: pd.DataFrame) -> pd.DataFrame:

        interactions = []

        for _, row in behaviors.iterrows():

            user = row["user_id"]

            impressions = str(row["impressions"]).split()

            for impression in impressions:

                news_id, clicked = impression.split("-")

                interactions.append(
                    {
                        "user_id": user,
                        "news_id": news_id,
                        "clicked": int(clicked),
                    }
                )

        interactions = pd.DataFrame(interactions)

        return interactions

    @staticmethod
    def positive_interactions(interactions: pd.DataFrame) -> pd.DataFrame:
        return interactions[interactions["clicked"] == 1]

    @staticmethod
    def negative_interactions(interactions: pd.DataFrame) -> pd.DataFrame:
        return interactions[interactions["clicked"] == 0]