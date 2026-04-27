import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import json
import os

# 1. Предопределённый список цитат
quotes = [
    {"text": "Будь изменением, которое хочешь видеть в мире.", "author": "Махатма Ганди", "topic": "Мотивация"},
    {"text": "Жизнь — это 10% то, что с тобой происходит, и 90% — как ты на это реагируешь.", "author": "Чарльз Р. Свиндолл", "topic": "Жизнь"},
    {"text": "Самое лучшее время для посадки дерева — двадцать лет назад. Второе лучшее — сегодня.", "author": "Китайская пословица", "topic": "Мотивация"},
    {"text": "Только тот, кто рискует, пьёт шампанское.", "author": "Ричард Брэнсон", "topic": "Риск"},
    {"text": "Успех — это сумма маленьких усилий, повторяемых день за днём.", "author": "Роберт Колльер", "topic": "Мотивация"},
]

# Глобальные переменные
history = []
filtered_quotes = quotes.copy()

# 5. Функции для сохранения и загрузки истории
def save_history():
    with open('history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def load_history():
    global history
    if os.path.exists('history.json'):
        with open('history.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
            
# 2. Генерация случайной цитаты
def generate_quote():
    global filtered_quotes
    if not filtered_quotes:
        messagebox.showinfo("Информация", "Нет цитат для отображения")
        return
    quote = random.choice(filtered_quotes)
    display_quote(quote)
    # 3. Добавление в историю
    history.append(quote)
    save_history()

# 3. Отображение цитаты
def display_quote(quote):
    quote_text.set(f'"{quote["text"]}"\n\nАвтор: {quote["author"]}\nТема: {quote["topic"]}')

# 3. Показать историю
def show_history():
    if not history:
        messagebox.showinfo("История", "История пуста.")
        return
    hist_str = ""
    for i, q in enumerate(history, 1):
        hist_str += f"{i}. \"{q['text']}\" - {q['author']} (Тема: {q['topic']})\n"
    messagebox.showinfo("История цитат", hist_str)

# 4. Фильтрация цитат
def filter_quotes():
    global filtered_quotes
    author_filter = simpledialog.askstring("Фильтр", "Введите автора (оставьте пустым, чтобы пропустить):")
    topic_filter = simpledialog.askstring("Фильтр", "Введите тему (оставьте пустым, чтобы пропустить):")
    filtered_quotes = quotes.copy()
    if author_filter:
        filtered_quotes = [q for q in filtered_quotes if q["author"].lower() == author_filter.lower()]
    if topic_filter:
        filtered_quotes = [q for q in filtered_quotes if q["topic"].lower() == topic_filter.lower()]

# 6. Добавление новой цитаты
def add_quote():
    text = simpledialog.askstring("Добавить цитату", "Введите текст цитаты:")
    author = simpledialog.askstring("Добавить цитату", "Введите автора:")
    topic = simpledialog.askstring("Добавить цитату", "Введите тему:")
    if not text or not author or not topic:
        messagebox.showwarning("Ошибка", "Все поля должны быть заполнены")
        return
    new_q = {"text": text, "author": author, "topic": topic}
    quotes.append(new_q)
    messagebox.showinfo("Успех", "Цитата добавлена!")

# Инициализация
load_history()

# Создание GUI
root = tk.Tk()
root.title("Random Quote Generator")

quote_text = tk.StringVar()

label = tk.Label(root, textvariable=quote_text, wraplength=400, justify='center')
label.pack(pady=10)

btn_generate = tk.Button(root, text="Сгенерировать цитату", command=generate_quote)
btn_generate.pack(pady=5)

btn_history = tk.Button(root, text="Показать историю", command=show_history)
btn_history.pack(pady=5)

btn_filter = tk.Button(root, text="Фильтр", command=filter_quotes)
btn_filter.pack(pady=5)

btn_add = tk.Button(root, text="Добавить цитату", command=add_quote)
btn_add.pack(pady=5)

root.mainloop()