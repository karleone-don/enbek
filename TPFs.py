import google.generativeai as genai
import re
import markdown

genai.configure(api_key = 'AIzaSyD5zwgunoO5T48ogN16dWPMt7DvDHGcBSc')
model = genai.GenerativeModel('gemini-1.5-flash')

def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html
    
def text_generation(gender, 
                    age, 
                    education, 
                    experience, 
                    information, 
                    project,
                    time_management,
                    situation
                    ):
    with open('sovet.txt', 'r', encoding='utf-8') as file:
        # Читаем содержимое файла
        example = file.read()
    with open('sovet2.txt', 'r', encoding='utf-8') as file:
        # Читаем содержимое файла
        offer = file.read()
    
    char = f'''Пол: {gender};
Возраст: {age};
Уровень образования: {education};
Опыт работы: {experience};
Навыки, хобби, предпочтительное направление по работе: {information};
Описание последнего проекта над которым работал человек и его роль там: {project};
Как человек организовывает свой рабочий день: {time_management};
Описание ситуации, когда человеку пришлось изменить свое мнение или подход к работе: {situation}'''
    
    print(char)


    response_conclusion = model.generate_content(f"""Сейчас я отправлю тебе данные человека,
        тебе нужно проанализировать информацию и написать про сильные
        стороны(от 2 до 5). Сейчас я отправлю тебе пример
        как ты должен будешь ответить, и больше никакой информации не будет,
        дай максимально точный совет и начни со слов '<h1><b>Из вашего описания
        можно сделать следующие выводы:</h1></b>'{example}. Вот информация о человеке: {char}""")
    response_advice = model.generate_content(f"""Сейчас я отправлю тебе данные человека,
        тебе нужно проанализировать информацию и написать про сильные
        стороны(от 2 до 5) как в примере {char} Сейчас я отправлю
        тебе пример как ты должен будешь ответить, и больше никакой информации не будет,
        дай максимально точный совет и начни со слов '<h1><b>Мы можем предложить вам:</h1></b>'{offer}
        предложение должно быть либо про найм в работу, либо практика. Вот информация о человеке: {char}""")
    response_conclusion = response_conclusion.text
    response_advice = response_advice.text
    # print(response_conclusion)
    # print(response_advice)

    response_conclusion = convert_markdown_to_html(response_conclusion)
    response_advice = convert_markdown_to_html(response_advice)   

    return response_conclusion, response_advice


# with open("new.doc", "w", encoding="utf-8") as f:
#     f.write(processed_text)

# print(model.count_tokens(chat.history))
