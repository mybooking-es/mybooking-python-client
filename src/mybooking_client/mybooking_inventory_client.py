import requests;
import json;

class MybookingInventoryClient:
  
  #
  # Constructor
  #	
  def __init__(self, api_credentials):
  	self.credentials = api_credentials


  # 
  # Get inventory
  #
  def inventory(self, limit=100, offset=0):
    # Prepare the pagination args
    page = offset * limit
    page_size = limit
    #args = {"search_filter":"all"}

  	# Build the URL
    url = '/api/booking-items'
    body = '' #json.dumps(args)

    # Build the URL with the prefix
    the_url = self.credentials.url
    the_url += url
    # 
    signature = self.credentials.calculate_post_signature(url, body)
    authorization = self.credentials.authorization_header(signature)
    print(authorization)
  	# Call the API
    response = requests.post(the_url, headers = { 'Authorization': authorization })
    # check response.status_code
    if response.status_code == 200:
      return response.json()
    else:  
      return response