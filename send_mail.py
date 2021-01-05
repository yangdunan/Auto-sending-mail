import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart #email內容載體
from email.mime.text import MIMEText #用於製作文字內文
from email.mime.base import MIMEBase #用於承載附檔
from email import encoders #用於附檔編碼
import datetime
import ssl
#寄件者使用的Gmail帳戶資訊
gmail_user = 'juliany922@gapp.nthu.edu.tw'
gmail_password = 'maus0922'
from_address = gmail_user
  
#設定信件內容與收件人資訊
df_CH4_score = pd.read_csv('./ch4_part2/CH4_part2_score.csv')  
# df_PA3_score = pd.read_csv('./pa3/PA3_score.csv')  
df_CH4_score = df_CH4_score.dropna(axis=0,how='all')  
# df_PA3_score = df_PA3_score.dropna(axis=0,how='all')  
for index in range(len(df_CH4_score))[15:16]:
    # print (df_CH4_score["email"][index])
    to_address = "juliany922@gmail.com"  
    Subject = "計算機結構CH4_part2成績"
    contents = "\
    {} 同學好, \n \
    計算機結構CH4_part2總成績 : {} \n \
    1.1 :{}/10\n \
    1.2 :{}/10\n \
    2.1 :{}/20\n \
    2.2 :{}/30\n \
    2.3 :{}/30\n \
    如有任何問題請與助教聯繫 \n \
    謝謝\n \
    TA 楊惇安 \n \
    \n \
    Dear {} \n \
    You got {} on 'Computer Architecture CH4_part2' \n \
    1.1 :{}/10\n \
    1.2 :{}/10\n \
    2.1 :{}/20\n \
    2.2 :{}/30\n \
    2.3 :{}/30\n \
    Please contact TA if you have any question about your score. \n \
    Thank you \n \
    \n \
    TA 楊惇安 \n ".format(df_CH4_score["Name"][index],df_CH4_score["total"][index],df_CH4_score["1.1"][index],df_CH4_score["1.2"][index],df_CH4_score["2.1"][index]
    ,df_CH4_score["2.2"][index],df_CH4_score["2.3"][index],df_CH4_score["Name"][index],df_CH4_score["total"][index],df_CH4_score["1.1"][index],df_CH4_score["1.2"][index],df_CH4_score["2.1"][index]
    ,df_CH4_score["2.2"][index],df_CH4_score["2.3"][index])

 
    # #開始組合信件內容
    mail = MIMEMultipart()
    mail['From'] = from_address
    mail['To'] = to_address
    mail['Subject'] = Subject
    # #將信件內文加到email中
    mail.attach(MIMEText(contents))     
    

    # # 設定smtp伺服器並寄發信件    
    smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtpserver.ehlo()
    smtpserver.login(gmail_user, gmail_password)
    smtpserver.sendmail(from_address, to_address, mail.as_string())
    smtpserver.quit()

# Reference & Special thanks to:
# https://lcycblog.wordpress.com/2018/09/10/python-gmail-%E5%AF%84%E4%BF%A1-with-%E9%99%84%E5%8A%A0%E5%A4%9A%E5%80%8B%E6%AA%94%E6%A1%88/

