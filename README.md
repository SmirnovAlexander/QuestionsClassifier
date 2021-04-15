# Questions Classifier

## Files

## Overview

## Usage

In [Dockerfile](./Dockerfile) specify what model you want to use by selecting one from [models](./models) directory, e.g. `tfidfvectorizer__votingclassifier`:

```
CMD python predict.py ./models/tfidfvectorizer__votingclassifier.pickle ./data/test.csv
```

Afterward build docker container:

```bash
sudo docker build -t questions_classifier .
```

Then execute prediction and write its output to the file:

```bash
sudo docker run questions_classifier > ./sample_output.csv
```

Model loading part takes a bit, but once it is loaded making predictions is blazingly fast.

## Team

- Penskaya Taisia
- Dranoshuk Artem
- Smirnov Alexander
