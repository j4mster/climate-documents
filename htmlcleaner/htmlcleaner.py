import re


path = '/Users/jxc/Documents/GitHub/climate-documents/pdfhtml_test_simple/AR_2008_Action_Plan-html-washed.html'
newpath = '/Users/jxc/Documents/GitHub/climate-documents/pdfhtml_test_simple/AR_2008_Action_Plan-html-cleaned.html'
file = open(path, 'r', encoding='utf-8')
text = file.read()

# text = '  <p><img width="73" height="73" alt="image" src="AZ_2006_Action_Plan%20statepubs_3104_files/Image_004.gif"></p>'
p = re.compile('<img.*?>')
res = p.sub('', text, count = 0)
# print(res)

newfile = open(newpath, 'w')
newfile.write(res)