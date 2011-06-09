import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText

def send(sender, recipients, subject, message, format='plain', config={}):
  '''
  format: 'plain' or 'html'
  '''

  if not config.get('use_ssl'):
    server = smtplib.SMTP(config.get('host'), config.get('port'))
  else:
    server = smtplib.SMTP_SSL(config.get('host'), config.get('port'))
  
  if config.get('use_tls'):
    server.ehlo()
    server.starttls()
    server.ehlo()
  
  if config.get('username'):
    server.login(config.get('username'), config.get('password'))
  
  msg = MIMEText(message, format)
  msg['From'] = sender
  msg['To'] = ', '.join(recipients)
  msg['Subject'] = subject

  # server.set_debuglevel(True)
  server.sendmail(sender, recipients, msg.as_string())
  
  server.quit()
