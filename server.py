from flask import Flask,render_template,request,send_file
from werkzeug.utils import secure_filename, send_file
import pandas as pd
import os

app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/files'



@app.route('/', methods=['GET','POST'])
def success():  
    if request.method == 'POST':  
          text = request.files['text']
          textname = secure_filename(text.filename)
          text.save(os.path.join(app.config['UPLOAD_FOLDER'], textname))

          csvf = request.files['csv']
          csvname = secure_filename(csvf.filename)
          text.save(os.path.join(app.config['UPLOAD_FOLDER'], csvname))

          opentext='static/files/'+textname
          opencsv='static/files/'+csvname
          print(type(opencsv))

          file=open(opentext)

          i=0
          data=[]
          name=[]
          hello={}
          key=0
          value=0

          for lines in file.readlines():
              a=len(lines)
    
              if(i%2!=0):
                  for j in range(a):
                      if(lines[j]=='2'):
                         key=(lines[j:j+9])
                         hello[key]=value.upper() 
                         break

              if(i%2==0):
                  for j in range(a):      
                      if(lines[j]=='1'):
                          value=lines[0:j]
                          break   
              
              i=i+1 

          df = pd.read_csv(csvf)
    
          y=len(data)

          df['Attendance']='0'

          for lines in hello:
              h=int(lines)
              student=df.loc[df['RollNo.']==h]


              if((student.loc[student['Name']==hello[lines]]).empty):
                  print(student['Name'])

              else:    
                 df.loc[df["RollNo."] == h, 'Attendance'] = '1'

          df.to_csv(opencsv, index=False)


          return render_template('index.html')  


    else:
       return render_template('index.html')     
 

app.run(debug=True)
