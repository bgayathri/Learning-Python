


datestring = 'SELECT endtime FROM ud401.vlr308_query a  WHERE a.userid=2039'
date_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H-%M-%S')
date_str = date_obj.strftime('%Y-%m-%d')
print(date_str)

userid = 'SELECT userid FROM ud401.vlr308_query a  WHERE a.userid=2039'
print(userid)

username = 'SELECT b.username from crdb.stl_userlog_hst b, ud401.vlr308_query a  WHERE a.userid=b.userid and a.userid=2039'
print(username)