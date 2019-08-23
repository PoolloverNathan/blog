from __future__ import with_statement
from __future__ import print_function

from flask import *

app = Flask(__name__)

@app.route('/style-<str:sheet>.css')
def stylesheet(sheet: str = ''):
  """Gets a style sheet by name."""
  print('Requested stylesheet '+sheet+'.css.')
  try:
    with open('styles/'+sheet+'.css', 'rt') as f:
      data = f.read(), 200, {'Content-Type': 'text/css'}
  except Exception as e:
    return 'Could not read stylesheet: '+e.__name__+'('+e.args+')', 500, 
  else:
    return data
@app.route('/')
@app.route('/index.html')
@app.route('/all/')
