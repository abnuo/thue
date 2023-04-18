import sys

def get(arr,i):
  try:
    return arr[i]
  except:
    return ""

newlines = ["\n","\r","\r\n"]
thue = ["<>::="]
modes = ["words","chars"]
try:
  fn = sys.argv[1]
except:
  print("USAGE: text2thue.py <infile> <outfile> <max> <mode> <print>")
  sys.exit()
try:
  out = sys.argv[2]
except:
  out = "thue.txt"
try:
  maxwords = int(sys.argv[3])
except:
  maxwords = 0
try:
  mode = sys.argv[4]
except:
  mode = "chars"
try:
  if sys.argv[4] == "true":
    yesprint = True
  else:
    yesprint = False
except:
  yesprint = False
if not mode in modes:
  print("Mode",mode,"is not a valid mode.")
  sys.exit()
with open(fn,"r",encoding="utf-8") as f:
  corpus = f.read()
print(corpus[:100])
sep = ","
if mode == "words":
  words = corpus.split()
if mode == "chars":
  words = [i for i in list(corpus) if not i in newlines]
  sep = ""
if maxwords != 0:
  words = words[:maxwords]
no_duplicates = list(dict.fromkeys(words))
def get_next_words(word):
  return [get(words,x+1) for x,v in enumerate(words) if v == word]
print(no_duplicates[:10])
for i in no_duplicates:
  thue.append(f"<{i}>::=")
for i in no_duplicates:
  next_words = [get(words,x+1) for x,v in enumerate(words) if v == i]
  if yesprint == True:
    print(i,next_words[:2])
  for x in next_words:
    thue.append(f"<{i}>::={i}{sep}<{x}>")
    #thue.append(f" {i}::= {x}")
for i in no_duplicates:
  thue.append(f"@markov::=<{i}>")
thue.append(",::= ")
thue.append("::=")
thue.append("@markov")
with open(out,"w",encoding="utf-8") as f:
  f.write("\n".join(thue))
