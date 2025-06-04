from src.model.sentiment import extract_sentiment
import pytest

testdata = [
    "Borussia Dortmund’s loss was heartbreaking as they failed to gain momentum from their two goals advantage. Very disappointing result for our Algerian player Bensebaini.",
    "Barcelona played brilliantly last Wednesday. Raphinha’s hat-trick was pure magic. Visca Barça!"
]


@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    neg_sentiment = extract_sentiment(sample)
    assert neg_sentiment <= 0
