#!/usr/bin/env python3

import subprocess

# Compile the .dylib
subprocess.run(['make'], check=True)

# Convert the .dylib to a JS array literal
payload = open('stage2.dylib', 'rb').read()

js = 'var stage2 = new Uint8Array(['
js += ','.join(map(str, payload))
js += ']);\n'

with open('stage2.js', 'w') as f:
    f.write(js)
