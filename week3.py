import pandas as pd

messages = [
    "Congratulations! You won a free prize",
    "Hi, how are you?",
    "Claim your free gift now",
    "Let's meet tomorrow",
    "You have won a lottery prize",
    "Can you send me the notes?",
    "Get free cash by clicking this link",
    "Are we meeting today?",
    "Congratulations, you are a winner",
    "Please call me when you are free"
]

labels = [
    "spam",
    "ham",
    "spam",
    "ham",
    "spam",
    "ham",
    "spam",
    "ham",
    "spam",
    "ham"
]

df = pd.DataFrame({
    "message": messages,
    "label": labels
})

print("Spam Message Dataset:")
print(df)
print("\nNumber of messages:")
print(df["label"].value_counts())
