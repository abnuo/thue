def get(arr,i):
  try:
    return arr[i]
  except:
    return ""

newlines = ["\n","\r","\r\n"]
thue = ["<>::="]
fn = "corpus.txt"
with open(fn,"r",encoding="utf-8") as f:
  corpus = f.read()
print(corpus[:10])
mode = "chars"
sep = ","
if mode == "words":
  words = corpus.split()
if mode == "chars":
  words = [i for i in list(corpus) if not i in newlines]
  sep = ""
words = words[:500]
no_duplicates = list(dict.fromkeys(words))
def get_next_words(word):
  return [get(words,x+1) for x,v in enumerate(words) if v == word]
print(no_duplicates[:10])
for i in no_duplicates:
  thue.append(f"<{i}>::=")
for i in no_duplicates:
  next_words = [get(words,x+1) for x,v in enumerate(words) if v == i]
  print(i,next_words[:2])
  for x in next_words:
    thue.append(f"<{i}>::={i}{sep}<{x}>")
    #thue.append(f" {i}::= {x}")
for i in no_duplicates:
  thue.append(f"markov::=<{i}>")
thue.append(",::= ")
thue.append("::=")
thue.append("markov")
with open("thue.txt","w",encoding="utf-8") as f:
  f.write("\n".join(thue))
