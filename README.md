# Questions Classifier

Classifying questions if they were prepared by expert or not.

## Files

- [task.pdf](task.pdf): task description
- [naive_approach.ipynb](naive_approach.ipynb): classic ml solutions to given problem
- [auto_encoder_approach.ipynb](auto_encoder_approach.ipynb): autoencoder solution to given problem
- [predict.py](predict.py): model prediction wrapper
- [data/](data/): initial and test data
- [models/](models/): our pretrained models
- [output/](output/): output submissions


## Overview of the approach

### Naive

Naive approach consists of tuning several models, that have as input TF-IDF vectors, where tokens are sequences of chars.
The best score we got there is around `0.78` that was received from `GradientBoostingClassifier`.
All the training, model saving and outputs generations may be found in [naive_approach.ipynb](naive_approach.ipynb) notebook.

#### ToDo
- Bagging approaches for combining models
- Stacking approaches for combining models

### Autoencoder

Autoencoder approach encodes TF-IDF vectors with `char_wb` analyzer.
After encoding result codes are fitted into simple `LogisticRegression` model with balanced weights.
We filter a bunch of non-expert sentences to make training process more stable and dataset less imbalanced.
The best score we got there is around `0.78`.

#### ToDo
- Use TripletLoss with hard samples mining
- Use TripletLoss with multiple positive and negative samples and one anchor for more stable training
- Experiment with architecture and losses (maybe -MSE(anchore, negative) will work better, because it is possible that we don't need clusters) 

All the training, model saving may be found in [auto_encoder_approach.ipynb](auto_encoder_approach.ipynb) notebook.

### Summary

At the end we calculated mean of outputs from `LogisticRegression`, `GradientBoostingClassifier` and Autoencoder approach.
The score we received is aroun `0.794`.


## Usage

Clone this repository:
```bash
git clone https://github.com/SmirnovAlexander/QuestionsClassifier.git
cd QuestionsClassifier/
```

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

- [Penskaya Taisia](https://github.com/TayaPenskaya)
- [Dranoshuk Artem](https://github.com/Artem531)
- [Smirnov Alexander](https://github.com/SmirnovAlexander)
