# Mybooking Python Client

## Reservations

```
# Import the classes
from mybooking_api_credentials import MybookingApiCredentials
from mybooking_reservation_client import MybookingReservationClient

# Build the credentials
credentials = MybookingApiCredentials('MYBOOKING-ACCOUNT-URL','{API-KEY}','{SECRET-KEY}')

# Create an instance of Mybooking reservation client
api_client = MybookingReservationClient(credentials)

# Get the first 5 reservations
data = api_client.reservations(5, 0)

# Get the total reservations
total = data['total']

# Paginate to the next 
data = api_client.reservations(5, 5)
```