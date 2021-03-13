import os
import html2text
import urllib
import re
import unidecode

root_directory_list = ("prvni-krucky", )

def insert_excercise(text):
    text_lines = text.split("\n")
    new_text = []
    inside_excs = False
    excs = {}
    excs_id = None
    excs_cont = None
    for line in text_lines:
        if len(line.strip()) == 0:
            new_text.append(line)
            continue
        if line.strip() == "<h2>Cvičení</h2>":
            line = "[[[ excs Cvičení"
            inside_excs = True
            new_text.append(line)
            continue
        if line.strip() == "<h2>Bonusy</h2>":
            new_text.append("]]]")
            line = "[[[ excs Bonusy"
            new_text.append(line)
            continue
        if inside_excs:
            regex = re.compile(r"<\%self:exrc title=\"[\w ]*\">")
            if regex.match(line.strip()):
                excs_name = line.replace('<%self:exrc title="', "").replace('">', "").strip()
                excs_id = unidecode.unidecode(excs_name).replace(" ", "-").lower()
                new_text.append(f"- {excs_id}")
                excs_tile_title = "---<br/>"
                excs_tile_title += f"title: {excs_name}<br/>"
                excs_tile_title += "demand: 1<br/>"
                excs_tile_title += "---<br/>"
                excs[excs_id] = excs_tile_title
            else:
                excs[excs_id] += line
        else:
            new_text.append(line)
    new_text.append("]]]")
    return new_text, excs


for root_directory in root_directory_list:
    for directory in os.listdir(root_directory):
        is_directory = os.path.isdir(os.path.join(root_directory, directory))
        if is_directory:
            subdirectory = os.path.join(root_directory, directory)
            if not os.path.exists(os.path.join(subdirectory, "excs")):
                os.mkdir(os.path.join(subdirectory, "excs"))
            for filename in os.listdir(subdirectory):
                if filename.endswith(".mako"): 
                    filename = os.path.join(subdirectory, filename)
                    f = open(filename, "r", encoding="utf-8")
                    text = f.read()
                    new_text, excs = insert_excercise(text)
                    target_fileaname = os.path.splitext(filename)[0]+'.md'
                    f.close()
                    f = open(target_fileaname, "w", encoding="utf-8")
                    for line in new_text:
                        converted_text = html2text.html2text(line).replace("\-", "-")
                        if len(converted_text.strip()) > 0:
                            f.write(converted_text)
                    f.close()
                    for key, value in excs.items():
                        f = open(os.path.join(subdirectory, "excs", f"{key}.md"), "w", encoding="utf-8")
                        f.writelines(html2text.html2text(value).replace("\-", "-"))
                        f.close()
                    
