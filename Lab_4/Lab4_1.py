# 1. Обробка юридичних документів: витяг дат, імен, номерів справ.
# 2. Телефонні номери (наприклад, +3000-555-NEO-TERRA).
import re 
from collections import Counter

def find_substring(text, substring):
    """Пошук підрядка в тексті"""
    return text.find(substring)

def replace_substring(text, old, new):
    """Заміна підрядка в тексті"""
    return text.replace(old, new)

def split_text(text, delimiter=' '):
    """Розділення тексту за роздільником."""
    return text.split(delimiter)

def format_string_f(name, age):
    """Форматування рядка з використанням f-string."""
    return f"Мене звати {name} і мені {age} років."

def format_string_method(name, age):
    """Форматування рядка з використанням методу .format()."""
    return "Мене звати {} і мені {} років.".format(name, age)

def extract_dates(text):
    """Витягує дати з тексту у форматі дд.мм.рррр"""
    pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b'
    return re.findall(pattern, text)

def extract_names(text):
    """Витягує імена у форматі Ім'я Прізвище з тексту."""
    pattern = r'\b[A-ZА-ЯЁЇІЄ][a-zа-яёїіє]+(?:\s[A-ZА-ЯЁЇІЄ][a-zа-яёїіє]+)+\b' 
    return re.findall(pattern, text)

    
def extract_emails(text):
    """Витяг email адресу з тексту"""
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def validate_phone_number(number):
    """Валідація телефонного номера."""
    pattern = r'^\+?3?8?(0\d{9})$'
    return bool(re.match(pattern, number))
    
def extract_case_numbers(text):
    """Витяг номер справ"""
    case_number_pattern = r'№\s?\d+/\d+'
    case_numbers = re.findall(case_number_pattern, text)
    return case_numbers
            
def count_words(text):
    """Підрахунок кількості слів у тексті"""
    return len(re.findall(r'\w+', text))
    
def count_sentences(text):
    """Підрахунок кількості речень у тексті"""
    return len(re.findall(r'[.!?]', text))

def word_frequency(text):
    """Підрахунок частоти слів у тексті."""
    words = (re.findall(r'\w+', text.lower()))
    return Counter(words)

def analyze_text(text):
    """Аналіз тексту"""
    results = {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'freq': word_frequency(text),
        'emails': extract_emails(text),
        'case_numbers': extract_case_numbers(text),
        'dates': extract_dates(text),
        'names': extract_names(text)
    }
    return results

def format_analysis_results(results):
    """Форматування результатів аналізу"""
    output = "Результат аналізу тексту:\n\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n\n"
    
    output += "Топ-5 найчастіших слів:\n"
    for word, count in results['freq'].most_common(5):
        output += f"{word}: {count}\n" 
        
    output += f"\nЗнайдені email адреси: {', '.join(results['emails'])}\n"
    output += f"\nЗнайдені номери справ: {', '.join(results['case_numbers'])}\n"
    output += f"\nЗнайдені імена: {', '.join(results['names'])}\n"
    output += f"\nЗнайдені дати: {', '.join(results['dates'])}\n"
    
    return output

def main():
    print("Ласкаво просимо до аналізатора тексту!")
    while True:
        try:
            choice = input("\nОберіть опцію:\n1. Аналіз тексту\n2. Валідація телефону\n3. Вихід\nВаш вибір: ")
            if choice == '1':
                text = input('Введіть текст для аналізу:')
                results = analyze_text(text)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input('Введіть номер телефону для валідації:')
                if validate_phone_number(phone):
                    print('Номер телефону валідований.')
                else:
                    print('Номер телефону невалідний')
            
            elif choice == '3':
                print('Дякуємо за використання аналізатору!')
                break
            
            else:
                print('Невірний вибір. Спробуйте ще раз.')
                                
        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    main()
