import pandas as pd

# load datasets
fake = pd.read_csv("data/Fake.csv")
true = pd.read_csv("data/True.csv")

# add labels
fake["label"] = 0
true["label"] = 1

# combine datasets
data = pd.concat([fake, true])

# keep only required columns
data = data[["text", "label"]]

# save new dataset
data.to_csv("data/news.csv", index=False)

print("Dataset prepared successfully")