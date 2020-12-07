import re
# htmltxt = """ bla bla bla
# <h1> My Rubric </h1>
# bla bla bla. """
# print(re.findall(r"<h1>\s*(.*)\s*</h1>", htmltxt))

f = open("tabla.html", encoding="utf-8")
txt = f.read()
txt

simpsons = re.findall(r"""<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>\s*<div class="svtJsStopPropagation">\s*<div class="svtTablaTitleInfo svtHide-Js">\s*<div class="svtTablaContent-Description">\s*<p class="svtXMargin-Bottom-10px">\s*Amerikansk animerad komediserie från\s*\d+(?:\-*\d+)*. Säsong\s*(\d+)\.\s*Del\s*(\d+)\s*\w+\s*(\d+)\.\s*(.+?) Simpsons bor i Springfield.""", txt)
    #print(result)
    #print(len(result))
for i in range(len(simpsons)):

    print("Tid: ", simpsons[i][0])
    print("Säsong: ", simpsons[i][1])
    print("Avsnitt: ", simpsons[i][2],"/",simpsons[i][3])
    print("Handling: ", simpsons[i][4])
    print("---------------")