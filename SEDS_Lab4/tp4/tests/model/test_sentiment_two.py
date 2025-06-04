import csv
import pytest
from src.model.sentiment import extract_sentiment

testdata = []
with open('data/soccer_sentiment_analysis.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        testdata.append(row[0])  

# Test each text in the CSV file
@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    sentiment = extract_sentiment(sample)
    assert  sentiment <= 0
