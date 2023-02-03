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
  def reservations(self, page_size=100, page=0, opts={}):

    # Define valid options
    valid_options = ['search_type', 'date_filter', 'from', 'to']

    # Create a dictionary with the args
    url_args_values = dict(page= page,
                           page_size= page_size)

    # Process the options
    for key in opts:
      if key in valid_options:
        url_args_values[key] = opts[key]

    # Build URL query string
    url_args = []
    for key in url_args_values:
      if isinstance(url_args_values[key], int):
        url_args.append(key+'='+str(url_args_values[key]))
      else:
        url_args.append(key+'='+url_args_values[key])  

  	# Build the URL
    url = '/api/booking/reservation-report?'
    url += "&".join(url_args)
    
    # Format the URL
    url = url.format(**url_args_values)
    
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