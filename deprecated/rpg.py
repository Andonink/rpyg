# *-* coding: utf-8 *-*
import random

def mstats(lvl):
    if lvl <= 3:
	hp = 20 + (lvl + ((lvl*3)/2))
	strg = (hp/6) + (lvl/2)
	mdef = (random.randint(1,lvl) + (hp/8))/2
	exp = hp / 3 - mdef
    elif lvl <= 6:
	hp = 25 + (lvl + ((lvl*3)/2))
	strg = (hp/8) + (lvl/2)
	mdef = (random.randint(1,lvl) + (hp/6))/2
	exp = hp / 3 
    elif lvl <= 9:
	hp = random.randint(60,80) + (lvl + ((lvl*3)/2))
	strg =  (hp/9) + (lvl/2)
	mdef = (random.randint(1,lvl) + (hp/3))/2
	exp = hp / 3 - strg
    return hp, strg, mdef, exp

def pstats(lvl=1):
    if lvl == 1:
	hp = 15
	strg = 4
	lck = random.randint(1,10)
	exp = 20
    elif lvl == 2:
	hp = 17
	strg = 6
	lck = lck + random.randint(1,10)
	exp = 40
    else:
	hp = random.randint(6,10) * lvl
	strg = hp / 4 + (hp/5)
	lck = random.randint(10,20) + lvl*random.randint(1,lvl)
	exp = 50 + (random.randint(lvl*2, lvl*3))
    pdef = hp/ 4
    return hp, strg, pdef, lck, exp

# Player stats
plvl = 4
php, pstrg, pdef, lck, pexp = pstats(plvl)
pexp = 10
ptn = 3
while php > 0:

    # Monster stats
    mlvl = random.randint(1,5)
    mhp, mstrg, mdef, mexp = mstats(mlvl)

    print '''
    -----------------------------------------------------
    |A monster appear!He is at level %d and His hp are %d|
    -----------------------------------------------------''' % (mlvl,mhp)
    while php > 0:
	action = raw_input('What are you gonna do?: ')
	if action not in ['1', '2', '3', '4']:
	    print 'Valid options are 1,2 or 3!'
	if action == '1':
	    mdam = random.randint(pstrg/2,pstrg) - (mdef/2)
	    print 'You attack! Dealing %d to the monster!' % (mdam)
	    mhp = mhp - mdam
	    if mhp < 0:
		print 'The monster is dead! Congrats hero!'
		print 'You won %d experience' % (mexp)
		pexp = pexp - mexp
		if pexp < 0:
		    plvl += 1
		    print 'You passed to level %d' % (plvl)
		    php, pstrg, pdef, lck, pexp = pstats(plvl)
	    else:
		print 'His hp are now %d' % (mhp)
		pdam = mstrg - (random.randint(pdef/5, pdef/2)/2)
		php = php - pdam
		if pdam <= 0:
		    print 'His attack miss you'
		else:
		    print 'He deals %d hp damage at you!' % (pdam)
		    print 'Your hp is now %d' % (php)
	if action == '2':
	    print 'You are now defending!'
	    pdam = mstrg - (random.randint(pdef/2, pdef)/2)
	    if pdam <= 0:
		print 'His attack got blocked'
	    else:
		print 'He deals %d hp damage at you! Your adamantine defense is a bless!' % (pdam)
		print 'Your hp is now %d' % (php)
	if action == '3':
	    print 'You have %d potions' % (ptn)
	    ans = raw_input('Do you want to drink one?: (y/n) ')
	    if ans == 'y':
		ptn -= 1
		php += 50
		print 'You drinked one potion! Now you have %d' % (ptn)
	    else:
		print 'Ok, its your call!'
	if action == '4':
	    print '''Your stats:
	    -------------------------------------------
            |HP: %d    Exp:%d   Level:%d               |
	    -------------------------------------------
	    ''' % (php, pexp, plvl)









## For Debug
#for i in range(1,10):
#    print i
#    print mstats(i)
