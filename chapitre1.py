import random

def sujet():
  s = open("lexique_sujets.txt")
  sujet = s.readlines()
  s.close()
  last = 50
  rnd = random.randint(0, last)
  print(sujet[rnd], end='', flush=True)
  
def verbe():
  v = open("lexique_verbes.txt")
  verbe = v.readlines()
  v.close()
  last = 50
  rnd = random.randint(0, last)
  print(verbe[rnd], end='', flush=True)
 
def complement():
  c = open("lexique_complements.txt")
  complement = c.readlines()
  c.close()
  last = 50
  rnd = random.randint(0, last)
  print(complement[rnd], end='', flush=True)

def phrase():
  print(' ', sujet(), verbe(), complement(), '.', end='', flush=True)

def chapitre():
 for _ in range(1250):
    phrase()

sujet()
chapitre()
