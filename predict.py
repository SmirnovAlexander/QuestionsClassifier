import sys
import pickle
import pandas as pd

model_path = str(sys.argv[1])
test_file_path = str(sys.argv[2])
questions_path = "./data/data.csv"

with open(model_path, "rb") as f:
    gs = pickle.load(f)

questions = pd.read_csv(questions_path, delimiter=";")
test = pd.read_csv(test_file_path, delimiter=";")
data = pd.merge(questions, test, on="ID")

prediction = gs.predict_proba(list(data["Question"]))[:, 1]

data["prediction"] = prediction

for i, row in data.iterrows():
    print(f"{row['ID']},{row['prediction']}")
