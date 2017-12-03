
from flask import Flask,request
from tinydb import TinyDB, Query
import re
import datetime



db = TinyDB('db.json')

app = Flask(__name__, static_url_path = "")


@app.route("/get_form",  methods = ['POST'])

def get_post_body():
        
    data = request.data.decode().split('&')

    print(data)

    data_dict = {k:v for k,v in (x.split('=') for x in data) }
    
    db_all = db.all()

    data_set = set(data_dict.keys())

    match = max(db_all, key=lambda item: len(data_set & set(item.keys())))
    
    max_index = db_all.index(match)

    if max_index ==0:
        return validate(data_dict)

    return str(db_all[max_index]['form_name'])+'\n'


def validate(val):
    answer = {}

    for k,v in val.items():

        if  valiDate(v):
            answer [k]='date'

        elif  re.match(r"[+][7][' ']\d{3}[' ']\d{3}[' ']\d{2}[' ']\d{2}$", v):
            answer [k]='tel'

        elif re.match(r"[^@]+@[^@]+\.[^@]+", v):
            answer [k]='mail'

        else:
            answer [k]='text'

    return str(answer)
 

def valiDate(val):
    formats = ['%d.%m.%Y', '%Y-%m-%d'] 
    for frmat in formats:
        try:
            datetime.datetime.strptime(val, frmat) 
            return True
        except:
            pass


if __name__ == '__main__':
    app.run(debug = True)
