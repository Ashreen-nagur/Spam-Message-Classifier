import pandas as pd

# Sample dataset
data = {
    "message": [
        "Congratulations! You won a prize",
        "Hi, how are you?",
        "Claim your free gift now",
        "Let's meet tomorrow"
    ],
    "label": [
        "spam",
        "ham",
        "spam",
        "ham"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df)

# Features and Labels
X = df["message"]
y = df["label"]

print("\nFeatures:")
print(X)

print("\nLabels:")
print(y)
