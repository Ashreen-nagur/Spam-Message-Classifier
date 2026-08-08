import pandas as pd

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

spam_data = pd.DataFrame(data)

print("Spam Dataset")
print(spam_data)

print("\nMissing Values")
print(spam_data.isnull().sum())

spam_data = spam_data.drop_duplicates()

print("\nAfter Removing Duplicates")
print(spam_data)

messages = spam_data["message"]
labels = spam_data["label"]

print("\nMessages")
print(messages)

print("\nLabels")
print(labels)
