import json, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--inputfile")
parser.add_argument("-o", "--outputfile")
args = parser.parse_args()

inputfile = args.inputfile
outputfile = args.outputfile

i = open(inputfile, "r")
o = open(outputfile, "w")

j = json.loads(i.read())

for wfh in j:
    wfid=wfh["execution"]["workflowId"]
    runid=wfh["execution"]["runId"]
    o.writelines()

o.close()

