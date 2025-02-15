import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("directory", help="Directory in log files")
parser.add_argument("-t","--text", help="text for search in logs file")
parser.add_argument("-f", "--full", help="Full search", action="store_true")

args = parser.parse_args()

def find_text_in_log_file(directory, text_in_logs_file, full_logs_in_file):
    list_all_files = [f for f in os.listdir(directory) if f.endswith('.log')]
    for log_file in list_all_files:
        log_dir_path = os.path.join(directory, log_file)
        try:
            with open(log_dir_path, 'r', encoding='utf-8') as logs_file:
                number_line = 0
                for line in logs_file:
                    number_line += 1
                    if text_in_logs_file in line:
                        print('Текст найден в: ', log_file, number_line)
                        line_split = line.split()
                        index_text = line_split.index(text_in_logs_file)
                        start = max(0, index_text - 5)
                        finish = index_text + len(text_in_logs_file) + 5
                        print({" ".join(line_split[start:finish])})
                        if full_logs_in_file is False:
                            return

        except FileNotFoundError:
            print(f'Файл {log_file} не найден')


find_text_in_log_file(args.directory, args.text, args.full)
