import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Exam_Score": [35, 40, 50, 55, 65, 70, 75, 85]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df)

X = df[["Hours_Studied"]]
y = df["Exam_Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("\nActual Scores:")
print(y_test.values)

print("\nPredicted Scores:")
print(predictions)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nEvaluation Metrics:")
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)
