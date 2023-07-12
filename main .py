api_hash = 
api_id = 
token = 
import datetime
import asyncio
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
free = mm + "/" + dd + "/" + yyyy

admin=1920601678
admin_change="null"
# Start 
admin_or_no ="""
Admin -> 🖥️

برای وارد شدن به پنل ادمین دستور :

/adminpanel 💾

پنل عادی:
/panel 🪪
"""

admin_welcome =  """
Admin -> 🖥️


سلام خوش آمدید


برای دیدن تمامی کاربران دستور زیر :

/allusers 📑

برای دیدن افرادی که سکه خریداری کردن دستور زیر :

/alluserbuycoin 🤑

برای ارسال اخبار دستور زیر :
/news 🗞️

برای دیدن سکه تمامی یوزر ها دستور زیر:

/allcoin 💰

برای اضافه کردن سکه به یوزر دستور زیر :

/addcoin 🏦

برای استعلام از یک نفر دستور زیر :

/chekuser 👁️‍🗨️

برای ایجاد کد سکه رایگان دستور زیر :

/addfreecoin 💵

تغییر مقدار سکه :

/changecoin ⚠️
"""






import sqlite3
conn = sqlite3.connect("bot.db")
act = conn.cursor()
def ex(conn,act,ex):
     act.execute(ex)
     conn.commit()
     
def get(conn,act,ex):
     act.execute(ex)
     data = act.fetchall()
     conn.commit()
     
     return data
     




from pyrogram import Client, filters

bot = Client(name="DG",api_id=api_id,api_hash=api_hash,bot_token=token)




@bot.on_message(filters.text)
async def test_bot(client, message,admin=admin,admin_or_no=admin_or_no,admin_welcome=admin_welcome,admin_change=admin_change):



     print(message.from_user.id)

     redirct = "@"+message.from_user.username + " 👉 "+message.text

     if message.from_user.id != admin :

          await bot.send_message(admin , redirct)
     else:
          pass
     print(message)

     if message.text=="/start" :
          try:

               id__=int(message.from_user.id)
               user__=str(message.from_user.username)
               money__=5
               send= f"INSERT INTO Users VALUES({money__}, '{user__}', {id__})"
               rec=ex(conn=conn,act=act,ex=send)
          except:
               pass


          


     if message.text=="/start" and message.from_user.id == admin and admin_change == "null":
          await bot.send_message(admin , admin_or_no)
          print(admin_change)

     if message.text == "/adminpanel" and message.from_user.id == admin and admin_change == "null":
          admin_change = "admin"

     if message.text == "/panel" and message.from_user.id == admin and admin_change == "null":
          admin_change = "user"

     if message.text=="/adminpanel" and message.from_user.id == admin and admin_change == "admin":
          print(admin_change)
          await bot.send_message(admin , admin_welcome)

     mess = message.text
     id_ = message.from_user.id 

     
     if mess=="/allusers" and id_ == admin:
          send= "SELECT username FROM Users"
          rec=get(conn=conn,act=act,ex=send)
         
          global sen
          sen=""
          for i in rec:
               
               i = i[0]
               
               sen = sen+f"@{i} \n"

          await bot.send_message(admin ,sen )
     try:

          pl=str(mess).split("*")
     except:
          pass
     print(pl)
     if mess=="/changecoin" and id_ == admin:
    
          i = message.text
          await bot.send_message(admin , "example /changecoin*ali*23*password")
               


          
                    

     if len(pl)>1 and pl[0]=="/changecoin" and id_ == admin and pl[3]=="ahoora@1386":
          money=int(pl[2])
          username=pl[1]
          send= f"UPDATE Users SET money = {money} WHERE username = '{username}'"
          rec=ex(conn=conn,act=act,ex=send)

     if mess=="/chekuser" and id_ == admin:
          await bot.send_message(admin , "example /chekuser*ali")
     if len(pl)>1 and id_ == admin:
          username=pl[1]
          send= f"SELECT * FROM Users Where username = '{username}'"
          rec=get(conn=conn,act=act,ex=send)
          await bot.send_message(admin , rec)

     if len(pl)>1 and pl[0]=="/addcoin" and id_ == admin:
          
          username=pl[1]
          send= f"SELECT money FROM Users Where username = '{username}'"
          rec=get(conn=conn,act=act,ex=send)
          
          
          
          money=int(pl[2])+int(rec[0][0])
         
          send= f"UPDATE Users SET money = {money} WHERE username = '{username}'"
          rec=ex(conn=conn,act=act,ex=send)

     if  mess=="/allcoin" and id_ == admin:
          send= f"SELECT username, money FROM Users"
          rec=get(conn=conn,act=act,ex=send)
          global sens
          sens=""
          print(rec)
          for i in rec:
              
               

               
               sens = sens+f"@{i} \n \n"

          await bot.send_message(admin ,sens )       

     if len(pl)==1 and pl[0]=="/news" and id_ == admin:
          await bot.send_message(admin , "for example /news | hello ...")
     n = str(mess).split("|")
     if len(n)>1 and n[0]=="/news" and id_ == admin:

          send= "SELECT id FROM Users"
          rec=get(conn=conn,act=act,ex=send)  
          #try:

          print(rec)
                   
          #except:
          #     pass
          













          





bot.run()
