# importing the requests library 
import requests 

class worker():
    def __init__(self):
        # api-endpoint 
        self.URL = "http://maps.googleapis.com/maps/api/geocode/json"
        
        # location given here 
        self.location = "delhi technological university"
  
        # defining a params dict for the parameters to be sent to the API 
        self.PARAMS = {'address':self.location} 
  
    def pull_data(self):
        # sending get request and saving the response as response object 
        r = requests.get(url = self.URL, params = self.PARAMS) 
        
        # extracting data in json format 
        data = r.json() 
  
        # extracting latitude, longitude and formatted address  
        # of the first matching location 
        latitude = data['results'][0]['geometry']['location']['lat'] 
        longitude = data['results'][0]['geometry']['location']['lng'] 
        formatted_address = data['results'][0]['formatted_address'] 


        # send th data to ML model to do the categorization/prediction
        