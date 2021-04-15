import sys
import pickle
import pandas as pd

test_file_path = str(sys.argv[1])
model_path = "./models/tfidfvectorizer__logisticregression.pickle"
questions_path = "./data/data.csv"

def text_preprocess(x):
    #x = x[0]
    x = x.lower()
    x = re.sub(r'https*\S+', ' ', x)                           # mentions
    x = re.sub(r'@\S+', ' ', x)                                # links
    x = re.sub(r'#\S+', ' ', x)                                # hashtags
    x = re.sub(r'\'\w+', '', x)                                # ticks and the next character
    x = re.sub('[%s]' % re.escape(string.punctuation), ' ', x) # punctuation
    x = re.sub(r'\w*\d+\w*', '', x)                            # numbers
    x = re.sub(r'\s{2,}', ' ', x)                              # over spaces
    x = x.replace('\xad', '')                                  # \xad
    x = x.replace('\t', '')                                    # \t
    x = x.replace('№', '')                                     # \t
    return x

with open(model_path, 'rb') as f:
    gs = pickle.load(f)


questions = pd.read_csv(questions_path, delimiter=";")
test = pd.read_csv(test_file_path, delimiter=";")

data = pd.merge(questions, test, on="ID")
prediction = gs.predict_proba(list(data["Question"]))[:, 1]
data["prediction"] = prediction
# data[["ID", "prediction"]].to_csv("./output/tfidfvectorizer__logisticregression.csv", index=False, header=False)

for i, row in data.iterrows():
    print(f"{row['ID']},{row['prediction']}")

# print(path)
