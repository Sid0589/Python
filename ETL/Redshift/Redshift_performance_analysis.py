import os
import pyodbc
import sys
import datetime
from datetime import datetime
sys.path.insert(0, '/home/etl/common')
import send_email
import HTML

os.environ["LD_LIBRARY_PATH"]="/usr/local/lib"
os.environ["ODBCINI"]="/etc/odbc.ini"
os.environ["ODBCSYSINI"]="/etc/"
os.environ["AMAZONREDSHIFTODBCINI"]="/etc/amazon.redshiftodbc.ini"


htmlcode = "<h2 align=\"center\"><u> WEEKLY REPORT - REDSHIFT QUERY PERFORMANCE ANALYSIS </u></h2> <h3 align=\"center\"><u> List of Queries - Run More Than 5 Minutes </u> </h3>"

cnxn = pyodbc.connect("DRIVER={Amazon Redshift}; SERVER=server;DATABASE=bigblueguess;UID=uname;PASSWORD=pwd;PORT=5439;")
crsr = cnxn.cursor()
crsr.execute("set search_path  to '$user', 'bjn_dwh_tables'")
crsr.execute("set query_group to 'superuser'")
crsr.execute("select last_week_start_date,last_week_end_date from dim_date where calendar_date = current_date")
from_date,to_date = crsr.fetchall()[0]

subject = 'Weekly Redshift Performance Report On ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' For The Period - ' + str(from_date) + '_' + str(to_date) 

crsr.execute("select query,user_id,user_name,substring(querytext_1,1,150) as querytext,substring(alert_event_list,1,70) as alert_events,substring(alert_solution_list,1,70) as alert_probable_solutions,start_time,end_time,total_exec_time::text,total_queue_time::text,run_time::text from audit_redshift_query_history a join dim_date b on a.start_time::date between last_week_start_date and last_week_end_date and calendar_date = sysdate::date and type = 'Users' and user_id not in (102,103) and run_time > 300 and final_state ='Completed'  order by run_time desc limit 30")
result = crsr.fetchall()
exp_query_list=[]
exp_query_list = [[ i[0].upper() for i in crsr.description]]

for i in result:
  exp_query_list.append(list(i))

crsr.execute('''select count(query)::text as total_executed_queries,min(run_time)::text as min_run_time_sec,avg(run_time)::text as avg_run_time_sec,max(run_time)::text as max_run_time_sec
from audit_redshift_query_history a
 join dim_date b on a.start_time::date between last_week_start_date and last_week_end_date 
 and calendar_date = current_date
 and type = 'Users' 
 and user_id not in (102,103,104) 
 and final_state ='Completed'
''')

result = crsr.fetchall()
rt_query_info = []
rt_query_info = [[ i[0].upper() for i in crsr.description]]

for i in result:
  rt_query_info.append(list(i))

crsr.execute('''select count(case when total_queue_time > 0 then query end)::text as total_Queued_Queries,min(total_queue_time)::text as min_total_queue_time_sec,avg(total_queue_time)::text as avg_total_queue_time_sec,max(total_queue_time)::text as max_total_queue_time_sec
from audit_redshift_query_history a
 join dim_date b on a.start_time::date between last_week_start_date and last_week_end_date 
 and calendar_date = current_date
 and type = 'Users' 
 and user_id not in (102,103,104) 
 and final_state ='Completed'
''')

result = crsr.fetchall()
q_query_info = []
q_query_info = [[ i[0].upper() for i in crsr.description]]

for i in result:
  q_query_info.append(list(i))

crsr.execute('''select coalesce(max(case when bucket = 'No of Queries-Run_Time <= 5 minutes' then "No of Executed Queries" end),0)::text "No of Queries-Run_Time <= 5 minutes"
,coalesce(max(case when bucket = 'No of Queries-Run_Time Between 5 and 15 minutes' then "No of Executed Queries"  end),0)::text "No of Queries-Run_Time Between 5 and 15 minutes"
,coalesce(max(case when bucket = 'No of Queries-Run_Time Between 15 and 30 minutes' then "No of Executed Queries"  end),0)::text "No of Queries-Run_Time Between 15 and 30 minutes"
,coalesce(max(case when bucket = 'No of Queries-Run_Time Between 30 and 60 minutes' then "No of Executed Queries"  end),0)::text "No of Queries-Run_Time Between 30 and 60 minutes"
,coalesce(max(case when bucket = 'No of Queries-Run_Time More Then 1 hour' then "No of Executed Queries"  end),0)::text "No of Queries-Run_Time More Then 1 hour"
from
(
select case when run_time >= 0.000 and run_time < 300.000 then 'No of Queries-Run_Time <= 5 minutes'
      when run_time >= 300.000 and run_time < 900.000 then 'No of Queries-Run_Time Between 5 and 15 minutes'
      when run_time >= 900.000 and run_time < 1800.000 then 'No of Queries-Run_Time Between 15 and 30 minutes'
      when run_time >= 1800.000 and run_time < 3600.000 then 'No of Queries-Run_Time Between 30 and 60 minutes'
      when run_time > 3600.00 then 'No of Queries-Run_Time More Then 1 hour'
    end  as "Bucket"
    ,count(query) as "No of Executed Queries"
from audit_redshift_query_history a
 join dim_date b on a.start_time::date between last_week_start_date and last_week_end_date 
 and calendar_date = current_date
 and type = 'Users' 
 and user_id not in (102,103,104) 
 and final_state ='Completed'
 group by 1
 )''')

result = crsr.fetchall()
bucket_list = []
bucket_list = [[ i[0].upper() for i in crsr.description]]
for i in result:
  bucket_list.append(list(i))

crsr.execute('''select  user_id,user_name,count(query) as "No of Executed Queries",avg(run_time) as avg_run_time_sec
from audit_redshift_query_history a
 join dim_date b on a.start_time::date between last_week_start_date and last_week_end_date 
 and calendar_date = current_date
 and type = 'Users' 
 and user_id not in (102,103,104) 
 and final_state ='Completed'
 group by 1,2
 having count(query) > 1
 order by 3 desc,4 desc
limit 5''')

result = crsr.fetchall()
top_5_users = []
top_5_users = [[ i[0].upper() for i in crsr.description]]
for i in result:
  top_5_users.append(list(i))

cnxn.close()

htmlcode = htmlcode + str(HTML.table(exp_query_list[1:],header_row=HTML.TableRow(exp_query_list[0],bgcolor='#D8D8D8',header=True),style="border: 1px solid #000000; border-collapse:collapse; font-size: 12px",attribs={"align":"center","table-layout":"fixed","width":"60%"}))
htmlcode = htmlcode + "<h3 align=\"center\"><u> Query Run Time Analysis </u> </h3>"
htmlcode = htmlcode + str(HTML.table(rt_query_info[1:],header_row=HTML.TableRow(rt_query_info[0],bgcolor='#D8D8D8',header=True),style="border: 1px solid #000000; border-collapse:collapse; font-size: 12px",attribs={"align":"center","table-layout":"fixed","width":"60%"}))
htmlcode = htmlcode + "<h3 align=\"center\"><u> Query Queue Time Analysis </u> </h3>"
htmlcode = htmlcode + str(HTML.table(q_query_info[1:],header_row=HTML.TableRow(q_query_info[0],bgcolor='#D8D8D8',header=True),style="border: 1px solid #000000; border-collapse: collapse; font-size: 12px",attribs={"align":"center","table-layout":"fixed","width":"60%"}))
htmlcode = htmlcode + "<h3 align=\"center\"><u> Query Run Time - Bucket Analysis </u> </h3>"
htmlcode = htmlcode + str(HTML.table(bucket_list[1:],header_row=HTML.TableRow(bucket_list[0],bgcolor='#D8D8D8',header=True),style="border: 1px solid #000000; border-collapse: collapse; font-size: 12px",attribs={"align":"center","table-layout":"fixed","width":"60%"}))
htmlcode = htmlcode + "<h3 align=\"center\"><u> Weekly Top 5 Users - By Number of Queries </u> </h3>"
htmlcode = htmlcode + str(HTML.table(top_5_users[1:],header_row=HTML.TableRow(top_5_users[0],bgcolor='#D8D8D8',header=True),style="border: 1px solid #000000; border-collapse: collapse; font-size: 12px",attribs={"align":"center","table-layout":"fixed","width":"60%"}))

send_email.send_email(subject,str(htmlcode),[],'soupam@bluejeansnet.com',['soupam@bluejeansnet.com'])


