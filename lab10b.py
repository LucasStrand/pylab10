import re
# htmltxt = """ bla bla bla
# <h1> My Rubric </h1>
# bla bla bla. """
# print(re.findall(r"<h1>\s*(.*)\s*</h1>", htmltxt))

f = open("tabla.html", encoding="utf-8")
txt = f.read()
txt

simpsons = re.findall(r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>', txt )

print (simpsons)