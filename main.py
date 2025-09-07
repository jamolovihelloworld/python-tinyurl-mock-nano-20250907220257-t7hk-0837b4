import hashlib
s='nanoalpha'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
