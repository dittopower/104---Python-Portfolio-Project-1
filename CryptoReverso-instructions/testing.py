def encrypt(text,block):
    if len(text) == 0:
        return ''
# Spaces to X
    spaces = [0]
    for _ in range (text.count(' ')):			#Replaces spaces with ‘x’ and save their positions as 
        spaces.append(text.find(' '))			#those are normally word ends were blocks may form
        text = text.replace(' ', 'X',1)
 #   print 'spaces', spaces
#Making the blocks
    totblock = float(len(spaces))/block		#Finds total number of blocks to be made
    from math import ceil                       #ceil rounds up to next whole number
    totblock = int(ceil(totblock))              # for 4 spaces/word in blocks of 3
    if totblock == 0:                           # 4/3 is 1.333 or 1 as far as python is concerned
        totblock = 1                            #ceil fixes this it makes it 2 blocks
    elif len(spaces) == 1:
        totblock = 1

    #print 'totblock', totblock
    blocks = []
    for runs in range(totblock):
         startpoint = spaces[block*runs]
       #  print 'run', runs
         if (runs+1) >= totblock:
             blocks.append (text[startpoint:len(text)])
             break
         endpoint = spaces[block*(runs+1)]
         blocks.append (text[startpoint:endpoint])
     #    print blocks
  #  print 'blocks', blocks
  #reversing the blocks
    crypttext = ''
    total = 0
    while total+1 <= totblock:
        crypttext = crypttext + 'X' + blocks[total][::-1]           # Reversing blocks [::-1]
        total = total + 1
    crypttext = crypttext.replace('XX','X')
    if crypttext[len(crypttext)-1] == 'X':
        crypttext = crypttext[:len(crypttext)-1]
    if crypttext[0] == 'X':
        crypttext = crypttext[1:]
    return crypttext

