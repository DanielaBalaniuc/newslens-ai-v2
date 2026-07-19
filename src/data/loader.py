from pathlib import Path
import pandas as pd


class MINDDataLoader:
    """Load the MIND dataset."""

    NEWS_COLUMNS = [
        "news_id",
        "category",
        "subcategory",
        "title",
        "abstract",
        "url",
        "title_entities",
        "abstract_entities",
    ]

    BEHAVIOR_COLUMNS = [
        "impression_id",
        "user_id",
        "time",
        "history",
        "impressions",
    ]

    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)

    def load_news(self):
        return pd.read_csv(
            self.data_dir / "news.tsv",
            sep="\t",
            names=self.NEWS_COLUMNS,
        )

    def load_behaviors(self):
        return pd.read_csv(
            self.data_dir / "behaviors.tsv",
            sep="\t",
            names=self.BEHAVIOR_COLUMNS,
        )

    def load(self):
        news = self.load_news()
        behaviors = self.load_behaviors()
        return news, behaviors