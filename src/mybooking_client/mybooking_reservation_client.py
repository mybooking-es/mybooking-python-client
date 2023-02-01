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
  def reservations(self, limit=100, offset=0):
    # Prepare the pagination args
    page = offset * limit
    page_size = limit
  	# Build the URL
    url = '/api/booking/reservation-report?page={page}&page_size={page_size}'.format(page=page,
                                                                                     page_size=page_size)
    # Build the URL with the prefix
    the_url = self.credentials.url
    the_url += url
    # 
    signature = self.credentials.calculate_get_signature(url)
    authorization = self.credentials.authorization_header(signature)
  	# Call the API
    response = requests.get(the_url, headers = { 'Authorization': authorization })
    return response.json()