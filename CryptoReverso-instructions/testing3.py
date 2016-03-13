"""
---------------------- Encrypt function tests ------------------------

Empty message
>>> encrypt('', 4) # Test 1
''

Encryption that changes nothing
>>> encrypt('MADAM', 2) # Test 2
'MADAM'

A message with one word, no spaces, and block size one
>>> encrypt ('CRYPTOGRAPHY', 1) # Test 3
'YHPARGOTPYRC'

A message that exactly fills two blocks
>>> encrypt('WHO WATCHES THE WATCHERS', 2) # Test 4
'SEHCTAWXOHWXSREHCTAWXEHT'

A message with one word in the final block
>>> encrypt('PARANOIA IS OUR PROFESSION', 3) # Test 5
'RUOXSIXAIONARAPXNOISSEFORP'

A message that needs padding at both ends
>>> encrypt('THE PRICE OF FREEDOM IS ETERNAL VIGILENCE', 4) # Test 6
'MODEERFXFOXECIRPXEHTXECNELIGIVXLANRETEXSI'

The same message but a different block size
>>> encrypt('THE PRICE OF FREEDOM IS ETERNAL VIGILENCE', 5) # Test 7
'SIXMODEERFXFOXECIRPXEHTXECNELIGIVXLANRETE'

Extreme case - blocks of size one
>>> encrypt('BIG BROTHER IS WATCHING', 1) # Test 8
'GIBXREHTORBXSIXGNIHCTAW'

---------------------- Decrypt function tests ------------------------

Decrypting nothing
>>> decrypt('', 8) # Test 9
''

Decrypting a single word
>>> decrypt('NOITPYRCNE', 3) # Test 10
'ENCRYPTION'

Decrypting some ciphertext with the block size used to encrypt it
>>> decrypt('TONXSIXYTIRUCESXTUBXTCUDORPXAXSSECORPXA', 3) # Test 11
'SECURITY IS NOT A PRODUCT BUT A PROCESS'

Decrypting the same ciphertext but with the wrong block size
>>> decrypt('TONXSIXYTIRUCESXTUBXTCUDORPXAXSSECORPXA', 4) # Test 12
'BUT SECURITY IS NOT A PROCESS A PRODUCT'

Decrypting some long ciphertext
>>> decrypt('EVIHCRAXTONXODXOHWXESOHTXOTX' + \
            'DENMEDNOCXERAXTSAPXEHTXTIXEPYTER', 5) # Test 13
'THOSE WHO DO NOT ARCHIVE THE PAST ARE CONDEMNED TO RETYPE IT'

---------------- Encryption and decryption tests ---------------------

Encrypting and decrypting a short phrase
>>> decrypt(encrypt('PRIVACY IS NOT FOR THE PASSIVE', 3), 3) # Test 14
'PRIVACY IS NOT FOR THE PASSIVE'

And a final test for good measure
>>> decrypt(encrypt('EVEN A PARANOID CAN HAVE ENEMIES', 5), 5) # Test 15
'EVEN A PARANOID CAN HAVE ENEMIES'

"""
#
#--------------------------------------------------------------------#


#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.


##### PUT YOUR encrypt AND decrypt FUNCTIONS HERE

def crypt(text,block,gap,holder):
    message = ''
    if len(text) == 0:
        return message
# Spaces to X
    spaces = [0]
    for _ in range (text.count(gap)):			#Replaces spaces with ‘x’ and save their positions as 
        spaces.append(text.find(gap))			#those are normally word ends were blocks may form
        text = text.replace(gap, holder,1)
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
    total = 0
    while total+1 <= totblock:
        message = message + holder + blocks[total][::-1]           # Reversing blocks [::-1]
        total = total + 1
    message = message.replace(holder+holder,holder)
    if message[len(message)-1] == holder:
        message = message[:len(message)-1]
    if message[0] == holder:
        message = message[1:]
    return message

def encrypt(text,block):
    return crypt(text,block,' ','X')
def decrypt(text,block):
    return crypt(text,block,'X',' ')
#--------------------------------------------------------------------#


#-----Automatic Testing----------------------------------------------#
#
#  The following code will automatically run the acceptance tests
#  when the program is "run".  If you want to prevent the tests
#  from running, and test your functions manually, comment out the
#  code below.
#
if __name__ == '__main__':
    from doctest import testmod
    testmod(verbose=True)
#
#--------------------------------------------------------------------#
