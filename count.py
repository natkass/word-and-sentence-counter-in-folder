import os
import csv
directory = 'files'
di="./"

for filename in os.scandir(di):
    if filename.is_file():
        f=filename
        path_to_txt = os.path.abspath(os.path.join("./", f)) 
        with open(path_to_txt, "r", encoding="utf8") as stream:
            text = stream.read()
            words = text.split()
            wrd= len(words)
            print("-" * 80)
            uniqwords = sorted(set(words))
            uniq=len(uniqwords)
            print("-" * 80)
            sentences=text.split("፡፡")
            sen=len(sentences)
            print("-" * 80)
            fi = open("count.csv", "a", newline='')
            row = (path_to_txt,wrd,uniq,sen)
            writer=csv.writer ("Path","Word count","Uniqe word count","Sentences count")
            writer=csv.writer (fi)
            writer.writerow (row)
            fi.close() 
