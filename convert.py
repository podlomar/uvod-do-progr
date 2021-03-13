import os
import html2text

root_directory_list = ("prvni-krucky", )

for root_directory in root_directory_list:
    for directory in os.listdir(root_directory):
        is_directory = os.path.isdir(os.path.join(root_directory, directory))
        if is_directory:
            subdirectory = os.path.join(root_directory, directory)
            for filename in os.listdir(subdirectory):
                if filename.endswith(".mako"): 
                    filename = os.path.join(subdirectory, filename)
                    f = open(filename, "r", encoding="utf-8")
                    text = html2text.html2text(f.read())
                    target_fileaname = os.path.splitext(filename)[0]+'.md'
                    f.close()
                    f = open(target_fileaname, "w", encoding="utf-8")
                    f.write(text)
                    f.close()
