import random

def run(rules,init=None):
  rules = rules.strip().split("\n")
  if not init:
    init = "\n".join([i for i in rules if not "::=" in i])
  rules = [i for i in rules if "::=" in i and not i == "::="]
  shuffled = rules
  output = init
  random.shuffle(shuffled)
  print(shuffled)
  for i in shuffled:
    lhs = i.split("::=")[0]
    rhs = i.split("::=")[1]
    print(lhs,rhs)
    if rhs.startswith("~"):
      output = lhs
      rhs = rhs[1:]
    output = output.replace(lhs,run("\n".join(rules+["::="]+init.split("\n")),rhs))
  return output

class VM:
  def __init__(self,rules,init=None):
    rules = rules.strip().split("\n")
    if not init:
      self.init = "\n".join([i for i in rules if not "::=" in i])
    self.rules = [i for i in rules if "::=" in i and not i == "::="]
  def replace(self,s,main=False):
    shuffled = self.rules
    random.shuffle(shuffled)
    output = s
    for i in shuffled:
      lhs = i.split("::=")[0]
      rhs = i.split("::=")[1]
      if rhs.startswith("~"):
        output = lhs
        rhs = rhs[1:]
      if rhs == ":::":
        rhs = input("Gimme a string!")
      if not main:
        output = output.replace(lhs,rhs)
      else:
        output = self.replace(output)
    return output
  def run(self):
    shuffled = self.rules
    random.shuffle(shuffled)
    output = self.init
    for i in shuffled:
      lhs = i.split("::=")[0]
      rhs = i.split("::=")[1]
      if rhs.startswith("~"):
        output = lhs
        rhs = rhs[1:]
      if rhs == ":::":
        rhs = input("Gimme a string!")
      output = self.replace(output)
    return output
  def run2(self):
    output = self.init
    output = self.replace(output,True)
