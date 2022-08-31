import textwrap
import os

file = "id.txt"
sample_text = "Ti-tidak sopan! Ini buku asli Magic Girl TeRiRi yang sudah memenangkan pertempuran yang tak terhitung jumlahnya! "

result_text = ""



def breakline(text=""):
    return  textwrap.wrap(text,width=85,break_long_words= True)
# for i in range(0,len(linebreak)):
#     print(linebreak[i])

def creatfile(file):
    with open(file,"r",encoding = "utf-8") as f,open("断行版"+file, "w", encoding="utf-8") as f2:
        for line in f:
            if len(line)>85:
                sample_text = line
                result_text = breakline(sample_text)
                # line = line.replace(line,result_text[0]+'\n'+result_text[1])
                for i in range(0,len(result_text)):
                    line = result_text[i]
                    f2.write(line)
                    print(line)
                    f2.write("\n")
                continue
            f2.write(line)
    for file in os.listdir("."):
        if file.split('.')[0][0:3] == "断行版":
            os.rename(file, file[:-3] + "srt")
        # os.rename("%s.bak" % file,file+"_改")


for file in os.listdir("."):
    if file.split('.')[-1] == "srt":
        os.rename(file,file[:-3]+"txt")
        creatfile(file[:-3]+"txt")
        os.rename(file[:-3] + "txt",file)

print("断行完成", end = " ")




    # for name in files:
    #     if name.split('.')[-1] == 'txt':
    #         print(name)
            # creatfile(name)


