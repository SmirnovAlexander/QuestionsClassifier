FROM continuumio/anaconda3:latest

CMD mkdir /opt/results
WORKDIR /opt/results

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD python predict.py ./models/tfidfvectorizer__votingclassifier.pickle ./data/test.csv
