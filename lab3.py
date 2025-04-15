import re


#Завдання 1
def delete_bukv_zifr_vyraz(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def find_word_with_liter(text, n):
    return re.findall(rf'\b\w*{n}\w*\b', text)

def find_lim_world(text, n):
    return re.findall(r'\b\w{' + str(n) + r'}\b', text)

def find_words_start_ab_end_s(text):
    return re.findall(r'\b[ab]\w*s\b', text)

#Завдання 2
def extract_and_sum_money(text):
    amounts = re.findall(r'\$\d+', text)  
    floats = [float(amount[1:]) for amount in amounts]  
    return floats, sum(floats)

#Завдання 3
def cleanup_python_code(code):
    code = re.sub(r'#.*', '', code)  
    code = re.sub(r'[\r\n]+', '\n', code)  
    return code

#Завдання 4
def convert_date_format(date_str):
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_str)
    if match:
        year, month, day = match.groups()
        return f'{day}-{month}-{year}'
    return None

# Виконання завдання 1 
print(delete_bukv_zifr_vyraz("fa, -0--, asf"))
print(find_word_with_liter('ghdy a slk', n='s'))
print(find_lim_world('lakal asd', 5)) 
print(find_words_start_ab_end_s("abs bus cats dogs"))  

#Виконання завдання 2
text = "kapusta prise is $123, ogirok is $400, sum is $50"
amounts, total_sum = extract_and_sum_money(text)
print(f"Суми: {amounts}, Загальна сума: {total_sum}")

#Виконання завдання 3
python_code = """
# Це коментар
print("Hello, world!")

# Ще один коментар

print("Another line")

"""
cleaned_code = cleanup_python_code(python_code)
print(cleaned_code)

#Виконання завдання 4
converted_date = convert_date_format("2025-02-01")
print(converted_date)