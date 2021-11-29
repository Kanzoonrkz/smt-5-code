class Pokemon:
  def __init__(self, name, nick, hp, baseAtk, baseDef):
    self.name = name
    self.nick = nick
    self.hp = hp
    self.baseAtk = baseAtk
    self.baseDef = baseDef
    self.dmg = 0

    self.moves = []

  def stat(self):
    print(self.name, " : ", self.nick, "\nHP : ", self.hp, "\nATK : ",
      self.baseAtk, "\nDEF : ", self.baseDef, "\nMoves List : ")
    for i in range(len(self.moves)):
      print("    " , self.moves[i].name , " : " , self.moves[i].power)
    print("\n")    

  # def addMove(self, move):
  #   if len(self.moves) >= 4:
  #     self.moves.pop(0)
  #   self.moves.extend(move)

  def damageOut(self, moveindex, target):
    stat = self.moves[moveindex].power
    target.dmg = (self.baseAtk * stat/100)
    return target.dmg

  def damageIn(self):
    self.hp = int(self.hp - (self.dmg - self.baseDef/10))
    return (self.dmg - self.baseDef/10)


class Move:
  def __init__(self, name, power):
    self.name = name
    self.power = power

def attack(self, target, moveindex):
  x = self.damageOut(moveindex, target)
  y = target.damageIn()
  print(self.nick , " attacks " , target.nick , " inflicting " , str(x) , " raw damage!!\n" , target.nick , " lost " , y , " HP")
  target.stat()


#########################################################################################

def main():
  hydropump = Move("Hydro Pump", 110)
  skullbash = Move("Skull Bash", 130)
  rapidspin = Move("Rapid Spin", 50)
  tackle = Move("Tackle", 40)

  flamethrower = Move("Flamethrower", 90)
  fireblitz = Move("Fire Blitz", 120)
  slash = Move("Slash", 70)
  dragonbreath = Move("Dragon Breath", 80)

  blasty = Pokemon("Blastoise", "Blasty", 79, 83, 100)
  blasty.moves.extend([hydropump, skullbash, rapidspin, tackle])

  charmy = Pokemon("Charmender", "Charmy", 78, 84, 78)
  charmy.moves.extend([flamethrower, fireblitz, slash, dragonbreath])

  print("\n############-POKEMON BATTLE-############\n")

  blasty.stat()
  charmy.stat()

  attack(charmy, blasty, 0)

  blasty.stat()


if __name__ == "__main__":
  main()
