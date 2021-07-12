# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%

def search_property_details():
    import requests
    import json
    import questionary
     
    #property_link = 'https://www.zillow.com/homedetails/2815-W-Avenue-K12-APT-172-Lancaster-CA-93536/20282227_zpid/'
    property_link = questionary.text("What's the property url?").ask()
    loan_to_value = questionary.text("What's the requested loan to value (LTV)%?").ask()

    url = "https://zillow-com1.p.rapidapi.com/property"

    querystring = {"property_url":property_link}

    headers = {
        'x-rapidapi-key': "9e1cff16cfmsh4ae959b5f19f74cp15a657jsn43681ebd7350",
        'x-rapidapi-host': "zillow-com1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
    
    #load data into json dictionary
    data = json.loads(response.text)

    #print(type(data))

    #save zestimate
    zestimate = int(data['zestimate']/1000)
    #loan_amount  = zestimate * (loan_to_value/100)

    #print(f"Your zestimate is ${zestimate:.02f}")
    #print(f"Your loan amount is ${loan_amount:.02f}")

    #return response.text
    return zestimate, loan_to_value


# %%



