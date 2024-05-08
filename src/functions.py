from params import credentials
import requests

def get_data(target, start = '2020-09-07', end='2024-01-01'):
    if target == 'asteroids':
        link = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start}&end_date={end}&api_key={credentials['key']}"
        response = requests.get(link)
        if response.status_code == 200:
            data = response.json()
            return data
    elif target == 'exoplanets':
        link = f'https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI'
        params = {
            'table': 'exoplanets',
            'format': 'ipac',
            'where': 'pl_kepflag=1'
        }
        response = requests.get(link,params=params)
        # Check if the request was successful
        if response.status_code == 200:
            # Get the response as plain text
            data = response.text
            
            # Split the data into lines
            lines = data.split('\n')
            start_of_data_index = next(i for i, line in enumerate(lines) if line.startswith('\----')) + 1
    
            # Extract column names (assuming they are in the line immediately before the separator)
            column_names = lines[start_of_data_index - 2].split()
            
            # Process each data line
            for line in lines[start_of_data_index:]:
                if line.strip():  # Skip empty lines
                    # Split the line into data fields
                    data_fields = line.split()
                    # Now you can process each data field using the column_names for reference
                    
                    # Example: Print the data fields
                    print(data_fields)
        else:
            print(f"Failed to retrieve data: {response.status_code}")
        
    else: 
        return f'Error: {response.status_code}, {response.text}'