from flask import Flask, render_template, request
from CurExchgRate import CurExchRate
import datetime
import pandas as pd
import os 


app = Flask(__name__)
#app.config.update(SERVER_NAME='10.5.6.140:5000')
@app.route('/')
def  form():
   return render_template('currency_input.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      if 'Base Currency' in result.keys():
        CurExchRt = CurExchRate(result['Base Currency'])
      if result['startdate']:
        startdate = datetime.datetime.strptime(result['startdate'],'%Y-%m-%d').date()
      if result['enddate']:
        enddate = datetime.datetime.strptime(result['enddate'],'%Y-%m-%d').date()
      historical_result = CurExchRt.historical_rates(startdate,enddate,result['Base Currency'])
      curexrate = pd.DataFrame()
      histdf    = pd.DataFrame(index=[0])
      ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      for i in historical_result.keys():
        tmp={}
        tmp['date'] =i 
        tmp['base'] = historical_result[i]['base']  
        for j in historical_result[i]['rates'].keys():
          tmp['curr']  = j
          tmp['rates'] = historical_result[i]['rates'][j]
          tmpdf  = pd.DataFrame(tmp, index=[0])
          histdf = histdf.append(tmpdf)
          if datetime.datetime.strptime(i,'%Y-%m-%d').date() == enddate:
          	curexrate=curexrate.append(tmpdf)
      curexrate=curexrate.dropna()
      aggdf = histdf.groupby(['curr','base'])['rates'].agg(['min','max','mean'])
      curexrate.to_html('templates/curexchg_' + ts + '.html',index=False)
      aggdf.to_html('templates/agg_' +ts + '.html')
      finalres = open('templates/final_' + ts + '.html','w')
      finalres.write("<html><h3> Aggregate Report </h3></html> <br>")
      finalres.close()
      os.system('cat ' + 'templates/agg_' +ts + '.html >> templates/final_' + ts + '.html')
      finalres = open('templates/final_' + ts + '.html','a')
      finalres.write("<br><html><h3> Current Day's Currency Exchange Data </h3></html> <br>")
      finalres.close()
      os.system('cat templates/curexchg_' + ts + '.html >> templates/final_' + ts + '.html' )
      return render_template('final_' + ts + '.html')

if __name__ == '__main__':
   app.run(debug = True)
