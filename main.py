import hashlib
s='omegacloud'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
