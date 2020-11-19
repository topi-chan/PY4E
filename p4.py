astr = 'Bob'
try:
    instr = int(astr)
except:
    instr = -1
print'First', instr
astr = '123'
try:
    instr = int(astr)
except:
     instr = -1
print'First', instr
astr = 'Bob'
try:
    print'Hello'
    instr = int(astr)
    print'There'
except:
    instr = -1
print'Done', instr
