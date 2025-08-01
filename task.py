# write a programmm to insert a record in sql table via Api
# write a programm to update a record
# write a programmm to delete a record
# write a programm to fetch a record
# Do the same in Mongo_DB

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://maniyarabu:AbuAneeza@cluster0.ufr0quv.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
import mysql.connector
db = client['new']


cnx = mysql.connector.connect(user='root', password='AbuAneeza@123')
cursor = cnx.cursor()
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    cursor.execute('use assignments')
    return render_template('fortask.html')

@app.route('/addrecord', methods=['POST','GET'])
def add():
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = int(request.form['c'])
    cursor.execute('use assignments')
    cursor.execute(f'insert into calls value({a},{b},{c})')
    #print(f'insert into calls value({a},{b},{c})')
    cnx.commit()
    
    
    coll = db['collection1']
    coll.insert_one({'caller_id':f'{a}', 'callee' : f'{b}', 'duration': f'{c}'})
    return 'Value added'

@app.route('/update', methods=['POST'])
def update():
    id = int(request.form['id'])
    duration =  int(request.form['dur'])
    cursor.execute(f'update calls set duration = {duration} where caller_id = {id}')
    cnx.commit()
    
    coll = db['collection1']
    coll.update_many({'caller_id': str(id)}, {"$set":{'duration': str(duration) }})
    
    return f"Duration for caller id {id} has been updated to {duration}"
 
 
@app.route('/delete', methods=['POST'] )
def delete():
    id = int(request.form['a'])
    cursor.execute(f'delete from calls where caller_id = {id};')
    cnx.commit()
    return f'entry with id {id} has been deleted'
 
@app.route('/fetch')
def fetch():
    cursor.execute('select * from calls;') 
    records = cursor.fetchall()
    return records
    
    
if __name__ == '__main__':
    app.run(debug=True) 