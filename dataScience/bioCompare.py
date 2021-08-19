humanInput = open("dataScience/human.fasta").read()
humanInput = humanInput.replace("\n","")

humanOutput = open("dataScience/human.html","w")
count = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count[i+j] = 0


for k in range(len(humanInput)-1):
    par = humanInput[k]+humanInput[k+1]
    if par in count:
        count[par] += 1

#html
humanOutput.write("<style>* { box-sizing: border-box; }")
humanOutput.write(".column {color:white; float: left; border:1px solid #111; width: 25%;  padding: 10px;  height: 100px;}")
humanOutput.write(".row:after { content: ""; display: table; clear: both;}")
humanOutput.write("</style>")
humanOutput.write("<div class='row'>")

maxValues = max(count.values())
for k in count:
    opacity = count[k]/maxValues
    humanOutput.write("<div class='column' style='background-color:rgba(0,0,0,"+str(opacity)+")'>"+str(k)+"</div>")
humanOutput.write("</div>")    
humanOutput.close()





bacteriaInput = open("dataScience/bacteria.fasta").read()
bacteriaInput = bacteriaInput.replace("\n","")

bacteriaOutput = open("dataScience/bacteria.html","w")
count = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count[i+j] = 0


for k in range(len(bacteriaInput)-1):
    par = bacteriaInput[k]+bacteriaInput[k+1]
    if par in count:
        count[par] += 1

#html
bacteriaOutput.write("<style>* { box-sizing: border-box; }")
bacteriaOutput.write(".column {color:white; float: left; border:1px solid #111; width: 25%;  padding: 10px;  height: 100px;}")
bacteriaOutput.write(".row:after { content: ""; display: table; clear: both;}")
bacteriaOutput.write("</style>")
bacteriaOutput.write("<div class='row'>")

maxValues = max(count.values())
for k in count:
    opacity = count[k]/maxValues
    bacteriaOutput.write("<div class='column' style='background-color:rgba(0,0,0,"+str(opacity)+")'>"+str(k)+"</div>")
bacteriaOutput.write("</div>")    
bacteriaOutput.close()


