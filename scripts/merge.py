import os
import argparse

def combine_md_files(directory, output_file='combined.md'):
    separator = '------------------\n'
    md_files = []
    
    # Рекурсивный поиск .md файлов
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    # Сортировка файлов по алфавиту
    md_files.sort()
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, md_file in enumerate(md_files):
            # Записываем имя файла
            outfile.write(os.path.basename(md_file) + '\n')
            outfile.write(separator)
            
            # Читаем и записываем содержимое
            with open(md_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            
            outfile.write('\n' + separator + '\n')
    
    print(f'Объединено {len(md_files)} файлов в {output_file}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Объединение Markdown файлов')
    parser.add_argument('directory', help='Путь к директории с .md файлами')
    parser.add_argument('-o', '--output', default='combined.md', help='Имя выходного файла')
    args = parser.parse_args()
    
    combine_md_files(args.directory, args.output)
