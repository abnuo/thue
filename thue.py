import random
import sys

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

if __name__ == "__main__":
  try:
    fn = sys.argv[1]
  except:
    print("USAGE: thue.py <file>")
    sys.exit()
  with open(fn,"r",encoding="utf-8") as f:
    c = f.read()
  vm = VM(c)
  out = vm.run()
  print(out)
