import os
import re

# 修改此處為您的目錄路徑
directory_path = '.'

# 遍歷指定的目錄中的所有 .md 檔
for folder_name, subfolders, filenames in os.walk(directory_path):
    for filename in filenames:
        if filename.endswith('.md'):
            file_path = os.path.join(folder_name, filename)

            # 讀取文件內容
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.read()

            # 用正則表達式替換字符串
            updated_contents = re.sub(r'!\[\[Pasted image (.+?).png\]\]', r'![](images/\1.png)', file_contents)

            # 如果文件被更改，則寫回文件
            if updated_contents != file_contents:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_contents)
