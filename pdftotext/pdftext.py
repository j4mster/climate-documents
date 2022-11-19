import os
import pdftotext

# dir = r'/Users/jxc/PycharmProjects/internship/Orig_CAP_5_pdf'
# newdir = r'/Users/jxc/PycharmProjects/internship/pdftotext/CAP_5_txt'
path = input('What is the path to the folder with the original documents? ')
fin = input('What is the path to the folder that you want the final documents in? ')

# dir = path
# dir = r'Users/jxc/PycharmProjects/internship/Orig_CAP_5_pdf'
# newdir = r'/Users/jxc/PycharmProjects/internship/pdftotext/CAP_5_txt'
print(os.getcwd())
for x in os.scandir(path):
    if x.is_file():
        # print(x.path)
        filename = os.path.basename(x.path)
        # print(filename)   
        if 'pdf' not in filename:
            continue
        with open(x.path, "rb") as f:
            pdf = pdftotext.PDF(f)
        newpath = fin + '/' + filename[0:len(filename) - 4] + '.txt'
        with open(newpath, 'w') as f:
            f.write("\n\n".join(pdf))

# # Load your PDF
# with open("pdf file name", "rb") as f:
#     pdf = pdftotext.PDF(f)
#
# # Save all text to a txt file.
# with open('txt file name', 'w') as f:
#     f.write("\n\n".join(pdf))
