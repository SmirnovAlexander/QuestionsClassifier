FROM continuumio/anaconda3:latest

CMD mkdir /opt/results
WORKDIR /opt/results
COPY baseline.py baseline.py

CMD python baseline.py /tmp/data/test.tsv > /opt/results/result.tsv
