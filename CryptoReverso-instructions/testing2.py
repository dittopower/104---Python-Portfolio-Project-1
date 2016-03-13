'''
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

'''




def decrypt (msg,block):
    if len(msg) == 0:
        return ''
# X's to spaces
    spaces = [0]
    for _ in range (msg.count('X')):			 
        spaces.append(msg.find('X'))			
        msg = msg.replace('X', ' ',1)
 #   print 'spaces', spaces
#Making the blocks
    totblock = float(len(spaces))/block		#Finds total number of blocks to be made
    from math import ceil                       #ceil rounds up to next whole number
    totblock = int(ceil(totblock))              # for 4 spaces/word in blocks of 3
    if totblock == 0:                           # 4/3 is 1.333 or 1 as far as python is concerned
        totblock = 1
#blocks
    blocks =  []
    for runs in range(totblock):
         startpoint = spaces[block*runs]
       #  print 'run', runs
         if (runs+1) >= totblock:
             blocks.append (msg[startpoint:len(msg)])
             break
         endpoint = spaces[block*(runs+1)]
         blocks.append (msg[startpoint:endpoint])
#decrypt
    text = ''
    total = 0
    while total+1 <= totblock:
        text = text + ' ' + blocks[total][::-1]           # Reversing blocks [::-1]
        total = total + 1
    text = text.replace('  ',' ')
    if text[len(text)-1] == ' ':
        text = text[:len(text)-1]
    if text[0] == ' ':
        text = text[1:]
    return text
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
