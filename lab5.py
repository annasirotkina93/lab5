import re
import csv


#задание 1
with open("task1-en.txt") as file:
    text = file.read()

words_with_a_hyphen = re.findall(r"\b\w+-\w+\b", text)
print("Слова с дефисами:", words_with_a_hyphen)

information_in_brackets = re.findall(r"\((.*?)\)", text)
print("Информация в круглых скобках:", information_in_brackets)


#задание 2
with open("task2.html", "r", encoding="utf-8") as file:
    html_content = file.read()

links_com = re.findall(r"https?://(?:www\.)?\S+\.com(?:/\S*)?", html_content)
print("Ссылки в домене .com:", links_com)


#задание 3
with open("task3.txt", "r", encoding="utf-8") as file:
    data = file.read()

id = re.findall(r"\b\d+\b", data)
name = re.findall(r"\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b", data)
email = re.findall(r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}", data)
date = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", data)
website = re.findall(r"https?://(?:www\.)?\S+", data)

records = zip(id, name, email, date, website)
with open("result.csv", "w", encoding="utf-8", newline="") as csvfile: #заполнение таблицы
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Name", "Email", "Date", "Website"])
    writer.writerows(records)