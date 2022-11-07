import json
import tracery
from tracery.modifiers import base_english

rules = {"origin": ""}
fn = "thue_1.txt"
code = """
*::=Hello World
::=
*
"""
if fn:
  with open(fn,"r",encoding="utf-8") as f:
    code = f.read()
code = code.strip()
code = [i for i in code.split("\n") if not i == "::="]
init = "\n".join([i for i in code if not "::=" in i])
finds = list(set([i[:i.index("::=")] for i in code if "::=" in i]))
def tracify(text):
  for i in finds:
    text = text.replace(i,f"#{i}_step#")
  return text
for i in finds:
  rules[f"{i}_step"] = []
for i in code:
  if "::=" in i:
    find = i[:i.index("::=")]
    replace = tracify(i[i.index("::=")+3:])
    if replace.startswith("~"):
      replace = replace[1:]
    rules[f"{find}_step"].append(replace)
rules["origin"] = init
rules["origin"] = tracify(rules["origin"])
body = []
for i in rules:
    body.append(" "*8+json.dumps(i)+": "+json.dumps(rules[i]))
with open("tracery.json","w",encoding="utf-8") as f:
  f.write("{\n")
  f.write(",\n".join(body))
  f.write("\n}")
grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print(grammar.flatten("#origin#"))
