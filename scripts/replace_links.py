import os
import re
import sys

def replace_links(content, pages_dir):
    """Заменяет ссылки [[PageName]] на содержимое файлов"""
    pattern = r'\[\[(.*?)\]\]'
    
    def replace_match(match):
        page_name = match.group(1).strip()
        file_path = os.path.join(pages_dir, f"{page_name}.md")
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                page_content = f.read().strip()
            return f"> {page_name}\n---\n{page_content}\n---"
        else:
            print(f"Предупреждение: Файл '{file_path}' не найден", file=sys.stderr)
            return match.group(0)
    
    return re.sub(pattern, replace_match, content)

def main():
    if len(sys.argv) != 3:
        print("Использование: python script.py <файл_разметки> <папка_страниц>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    pages_dir = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Ошибка: Файл '{input_file}' не найден", file=sys.stderr)
        sys.exit(1)
    
    if not os.path.isdir(pages_dir):
        print(f"Ошибка: Папка '{pages_dir}' не найдена", file=sys.stderr)
        sys.exit(1)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = replace_links(content, pages_dir)
    
    print(new_content)

if __name__ == "__main__":
    main()
