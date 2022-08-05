from flask import Flask, render_template, request, Response, url_for
from mrz.generator.td1 import TD1CodeGenerator

app = Flask(__name__) 



@app.route('/')
def index():
  return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
  document_number = request.form.get('document-number', '')
  birth_date = request.form.get('birth-date', '')
  gender = request.form.get('gender', '')
  expiry_date = request.form.get('expiry-date', '')
  nationality = request.form.get('nationality', '')
  surname = request.form.get('surname', '')
  gnames = request.form.get('gnames', '')
  country = "CACAN"
  result = TD1CodeGenerator("I",               # Document type   Normally 'I' or 'ID' for id cards
                       country,             # Country         3 letters code or country name
                       document_number,        # Document number"9D001187"
                       birth_date,          # Birth date      YYMMDD"850401"
                       gender,               # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                       expiry_date,          # Expiry date     YYMMDD"260302"
                       nationality,             # Nationality"CAN"
                       surname,        # Surname         Special characters will be transliterated
                       gnames,
                       "00185978",
                       " 210302") # Given name(s)   Special characters will be transliterated
  result2 = str(result)
  n = 30
  split_string = [result2[i:i+n] for i in range(0, len(result2), n)]
  print(split_string)
  new = ''.join(split_string)
  new2 = new.strip()
  new3 = ','.join(new2[i:i+31] for i in range(0, len(new2), 31))
  new4 = new3.split(',')
  print(new4[0])
  
  return render_template('index2.html', new4=new4)

# print(str(result))
  
# from examples.functions.functions import open_image
