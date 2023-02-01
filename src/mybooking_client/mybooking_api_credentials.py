import base64
import hashlib
import hmac

class MybookingApiCredentials:
  
  #
  # Constructor
  #	
  def __init__(self, url, api_key, secret_key):
    self.url = url
    self.api_key = api_key
    self.secret_key = secret_key

  #
  # Calculate a get signature
  #
  def calculate_get_signature(self, the_url):
    hash = hmac.new(self.secret_key.encode('utf-8'), the_url.encode('utf-8'), hashlib.sha1)
    result = hash.hexdigest()
    return result

  #
  # Calculate post signature
  #    
  def calculate_post_signature(self, the_url, the_body):
    data = the_url + the_body
    hash = hmac.new(self.secret_key.encode('utf-8'), data.encode('utf-8'), hashlib.sha1)
    result = hash.hexdigest()
    return result

  #
  # Get the authorization header
  #
  def authorization_header(self, signature):
    result = ''
    result += self.api_key
    result += ":"
    result += signature
    return result