FROM continuumio/anaconda3:latest
#FROM python:3.7


CMD mkdir /opt/results
WORKDIR /opt/results

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

#CMD python baseline.py ./data/test.csv
CMD python baseline.py ./data/test.csv > ./output/res.csv
# CMD python baseline.py /tmp/data/test.tsv
# CMD python baseline.py /tmp/data/test.tsv > /opt/results/result.tsv
