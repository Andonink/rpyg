import random

class Monster():
    def stats(self,lvl):
	if lvl == 1:
	    self.hp = 20 + random.randint(1,10)
	    self.exp = random.randint(1, 10)
	    self.strg = random.randint(1,3) * random.randint(2,6)
	    self.defs = self.strg * (random.randint(lvl*2,lvl*5) / 2)
	elif lvl == 2:
	    self.hp == 25 + random.randint(10,20)
	    self.exp = random.randint(1,15)
	    self.strg = random.randint(6,10)
	    self.defs = self.strg * random.randint(1,4)
	else:
	    self.hp = 30 + (lvl * 2) + (random.randint(10,20) * lvl)
	    self.exp = random.randint(10,lvl*random.randint(4,8))
	    self.strg = random.randint(lvl,lvl*5)
	    self.defs = self.strg * random.randint(1,4)
	return self.hp, self.exp, self.strg, self.defs

    def debug(self):
	print 'Hp = %d Exp = %d Strg = %d Defs = %d' % \
				(self.hp,self.exp,self.strg,self.defs)

class Player:
    def stats(self,lvl):
	    self.hp = random.randint(lvl*3,lvl*6) * 8
	    self.exp = random.randint(lvl*2, lvl*5) + \
					    random.randint(self.hp/4,self.hp)
	    self.strg = random.randint(lvl,lvl*3) + \
					    (random.randint(lvl*3,lvl*5) * lvl)
	    self.defs = (self.strg * random.randint(lvl,lvl*4)) / 2
	    return self.hp, self.exp, self.strg, self.defs

    def debug(self):
	print 'Hp = %d Exp = %d Strg = %d Defs = %d' % \
				(self.hp,self.exp,self.strg,self.defs)

def menu():
    print '''
           .----------------------------.  
	   |1) Attack    2)Defend       |  
	   |3) Potions   4)Stats        |  
	   |____________________________|  '''

ply = Player()
for i in range(1,10):
    php, pexp, pstrg, pdefs = ply.stats(i)
    print 'level %d, hp %d exp %d strg %d def %d' % (i,php,pexp,pstrg,pdefs)

#mns = Monster()
#for i in range (1,10):
#    mhp, mexp, mstrg, mdefs = mns.stats(i)
#    print 'leve', i,'hp:', mhp,'exp', mexp,'strg', mstrg,'defs', mdefs

