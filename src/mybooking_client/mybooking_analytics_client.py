import requests;
import json;

class MybookingAnalyticsClient:
  
  #
  # Constructor
  #	
  def __init__(self, api_credentials):
  	self.credentials = api_credentials


  # 
  # Get expenses
  #
  def expenses(self, year, page_size=100, page=0):

  	# Build the URL
    url = '/api/booking/booking-item/expenses'\
          '?year={year}&page={page}&page_size={page_size}'
    
    url = url.format(year=year,
                     page=page,
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
    return response.json()