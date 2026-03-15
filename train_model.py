import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# load dataset
data = pd.read_csv("dataset.csv")

# features
X = data[["area","bedrooms","bathrooms","age"]]

# target
y = data["price"]

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create model
model = LinearRegression()

# train model
model.fit(X_train, y_train)

# save model
joblib.dump(model,"model.pkl")

print("Model trained and saved")