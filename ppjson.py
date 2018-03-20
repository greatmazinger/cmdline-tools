import sys
import json

parsed = json.load( sys.stdin )
print json.dumps( parsed,
                  indent = 2,
                  sort_keys = True )
