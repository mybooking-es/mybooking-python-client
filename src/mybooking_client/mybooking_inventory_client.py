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
  def inventory(self, page_size=100, page=0):

  	# Build the URL
    url = '/api/booking-items?page={page}&page_size={page_size}'.format(page=page,
                                                                        page_size=page_size)


    # Build the URL with the prefix
    the_url = self.credentials.url
    the_url += url
    
    # Build the signature 
    signature = self.credentials.calculate_get_signature(url)
    authorization = self.credentials.authorization_header(signature)

  	# Call the API
    response = requests.get(the_url, headers = { 'Authorization': authorization })
    # check response.status_code
    if response.status_code == 200:
      return response.json()
    else:  
      return response