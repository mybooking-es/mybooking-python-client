import requests;
import json;

class MybookingReservationClient:
  
  #
  # Constructor
  #	
  def __init__(self, api_credentials):
  	self.credentials = api_credentials


  # 
  # Get reservations
  #
  def reservations(self, page_size=100, page=0):

  	# Build the URL
    url = '/api/booking/reservation-report?page={page}&page_size={page_size}'.format(page=page,
                                                                                     page_size=page_size)
    # Build the URL with the prefix
    the_url = self.credentials.url
    the_url += url
    # 
    signature = self.credentials.calculate_get_signature(url)
    authorization = self.credentials.authorization_header(signature)
    #print(authorization)
  	# Call the API
    response = requests.get(the_url, headers = { 'Authorization': authorization })
    # check response.status_code
    return response.json()