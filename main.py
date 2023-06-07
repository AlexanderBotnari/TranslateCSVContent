import csv
import os
from translate import Translator


def translatePhrase(phrase):
    translator = Translator(from_lang='ru', to_lang='ro')
    result = translator.translate(phrase)
    return result


original_file = 'ru-front.csv'
target_file = 'ro-front.csv'

if os.path.isfile(original_file):
    with open(original_file, 'r', newline='', encoding='utf-8') as file_csv:
        reader_csv = csv.reader(file_csv)
        lines = list(reader_csv)
        table_head = lines[0]
        table_head.clear()
        table_head.append('RO')

        for line in lines[1:]:
            original_phrase = line[0]
            translated_phrase = translatePhrase(original_phrase)
            line[0] = translated_phrase
            print(original_phrase + ' -> ' + translated_phrase)

    with open(target_file, 'w', newline='', encoding='utf-8') as file_csv:
        writer_csv = csv.writer(file_csv)
        writer_csv.writerows(lines)
else:
    print("Original file does not exist or failed to open!")
