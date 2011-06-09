'''
Uses the Twilio client to send SMS messages.
'''

import twilio

def send(sender, recipient, message, config):
  '''
  Sends an SMS containing `message`, from `sender` to `recipient`.
  The dict `config` should define account_sid, auth_token.
  
  Returns the response from Twilio.
  '''

  client = _get_client(config)

  request = {'From': sender, 'To': recipient, 'Body': message}
  response = client.request(_get_api_url(config), 'POST', request)

  return response

def _get_client(config):
  return twilio.Account(config['account_sid'], config['auth_token'])

def _get_api_url(config):
  return '/%(api_version)s/Accounts/%(account_sid)s/SMS/Messages' % config
