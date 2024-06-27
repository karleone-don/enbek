import google.generativeai as genai
import re

genai.configure(api_key = 'AIzaSyD5zwgunoO5T48ogN16dWPMt7DvDHGcBSc')

with open('sovet.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    example = file.read()
with open('sovet2.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    offer = file.read()
with open('start.txt', 'r', encoding='utf-8') as file:
    # Читаем содержимое файла
    char = file.read()

def process_text(text):
    # Заменяем двойные звездочки на HTML-теги для жирного текста
    cleaned_text = re.sub(r'\d\.\s\*\*', '', text)
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<h2><b>\1</b></h2>', cleaned_text)
    return processed_text

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
response = chat.send_message("""Сейчас я отправлю тебе данные человека,
    тебе нужно проанализировать информацию и написать про сильные
    стороны(от 2 до 5) как в примере""" + char + """Сейчас я отправлю тебе пример
    как ты должен будешь ответить, и больше никакой информации не будет,
    дай максимально точный совет и начни со слов '<h1><b>Из вашего описания
    можно сделать следующие выводы:</h1></b>'б""" + example + """Сейчас я отправлю
    тебе пример как ты должен будешь продолжить, и больше никакой информации не будет,
    дай максимально точный совет и начни со слов '<h1><b>Мы можем предложить вам:</h1></b>'б""" + offer + """
    предложение должно быть либо про найм в работу, либо практика""")
print(response.text)

processed_text = process_text(response.text)

with open("new.doc", "w", encoding="utf-8") as f:
    f.write(processed_text)

print(model.count_tokens(chat.history))
