from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data.loader import MINDDataLoader
from src.data.preprocessing import BehaviorParser
from src.recommenders.popularity import PopularityRecommender

loader = MINDDataLoader(PROJECT_ROOT / "data" / "raw" / "MINDsmall")

news, behaviors = loader.load()

interactions = BehaviorParser.parse_impressions(behaviors)

model = PopularityRecommender()
model.fit(interactions)

print(type(model.popular_articles))
print(model.popular_articles.head())