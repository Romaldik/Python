import unittest
from Lab4_1 import *

class TestTextAnalyzer(unittest.TestCase):
    def test_extract_dates(self):
        self.assertEqual(extract_dates("Дата судового засідання 12.05.2023."), ["12.05.2023"])
        
    def test_extract_names(self):
        self.assertEqual(extract_names("Документ підписав Іван Петров."), ["Іван Петров"])
    
    def test_extract_case_numbers(self):
        self.assertEqual(extract_case_numbers("Номер справи №12345/6789"), ["№12345/6789"])

    def test_split_text(self):
        self.assertEqual(split_text("Hello, world!", ", "), ["Hello", "world!"])
    
    def test_format_string_f(self):
        self.assertEqual(format_string_f("Alice", 30), "Мене звати Alice і мені 30 років.")
    
    def test_format_string_method(self):
        self.assertEqual(format_string_method("Bob", 25), "Мене звати Bob і мені 25 років.")
    
    def test_extract_emails(self):
        self.assertEqual(extract_emails("Зв'яжіться з нами: info@example.com"), ["info@example.com"])
    
    def test_validate_phone_number(self):
        self.assertTrue(validate_phone_number("+380123456789"))
        self.assertFalse(validate_phone_number("12345"))
    
    def test_count_words(self):
        self.assertEqual(count_words("Це тестовий текст."), 3)
    
    def test_count_sentences(self):
        self.assertEqual(count_sentences("Це одне речення. Це друге! Це третє?"), 3)
    
    def test_word_frequency(self):
        self.assertEqual(word_frequency("Це тест. Це лише тест."), {"це": 2, "тест": 2, "лише": 1})

if __name__ == '__main__':
    import unittest
    from io import StringIO

    suite = unittest.TestLoader().loadTestsFromTestCase(TestTextAnalyzer)
    output = StringIO()
    runner = unittest.TextTestRunner(stream=output, verbosity=2)
    result = runner.run(suite)

    print(output.getvalue())
    print(f"\nУспішних тестів: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Невдалих тестів: {len(result.failures)}")
    print(f"Помилок: {len(result.errors)}")

    if result.failures or result.errors:
        print("\nДетальна інформація про невдалі тести та помилки:")
        for test, error in result.failures + result.errors:
            print(f"\n{test}")
            print(error)