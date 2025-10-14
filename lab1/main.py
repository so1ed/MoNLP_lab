from src.text_cleaner import clean_text
from src.sentiment_analysis import analyze_sentiment

with open("data/text.txt", "r", encoding="utf-8") as f:
    text = f.read().strip()

print("Указанный текст:\n", text)

result = analyze_sentiment(text)
print("\nАнализ тональности:")
print(result)

compound = result['compound']
if compound >= 0.5:
    print("\nИтог:\nВаш текст - позитивный")
elif compound <= -0.5:
    print("\nИтог:\nВаш текст - негативный")
else:
    print("\nИтог:\nВаш текст - нейтральный")