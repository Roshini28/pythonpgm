class depart:
  def __init__(self):
    self.branch =[]
  def push(self,branch):
    self.branch.append(branch)
  def pop(self):
    return self.branch.pop()
d = depart();
d.push("mba")
d.push("mca")
d.push("csc")
d.push("it")
print(d.branch)
print(d.pop())
print(d.branch)
d.branch.remove("mba")
print(d.branch)


