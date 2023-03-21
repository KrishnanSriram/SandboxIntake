#! /usr/local/bin/python3
from model.usbapp import USBApp
import re
import json

content = '''
AppID: "7697"
AppFullName: "Open Banking"
AppShortName: "openbnkg"
PrimaryOwnerId: "sknooka"
SecondaryOwnerId: "vxmadda"
CostCenter: "03000008024"
PrimaryOwnerEmail: "sunil.nooka@usbank.com"
SecondaryOwnerEmail: "ram.maddali@usbank.com"
GitLabProjectId: "2238"
--
AppID: "1234"
AppFullName: "Raja Simba Gabru"
AppShortName: "RJG"
PrimaryOwnerId: "simba"
SecondaryOwnerId: "gabru"
CostCenter: "001976"
PrimaryOwnerEmail: "simba@usbank.com"
SecondaryOwnerEmail: "gabru@usbank.com"
GitLabProjectId: "9999"
'''

def load_content_from_file():
    pass

def load_local_content():
    return content

def contents():
    return load_local_content()

def main():
    sb_applications_info = contents()
    # Separate multiple applications
    # TODO: separator constant shoudl be externalized
    applications = content.split("--")
    sandbox_applications = []
    # Parse each application separately
    for app in applications:
        if app.strip():  # Ignore empty sections
            # Extract key-value pairs from the section using regex
            pairs = re.findall(r'(\w+):\s*"([^"]*)"', app)
            # Create a dictionary from the key-value pairs
            data = dict(pairs)
            # Create an instance of the Application class using the data dictionary
            app = USBApp(data=data)
            sandbox_applications.append(app)
    # serialize them into JSON
    for app in sandbox_applications:
        app_dict = app.to_dict()
        #    persist/append into a file
        with open(app.app_short_name + ".json", "w") as file:
            json.dump(app_dict, file)

if __name__ == "__main__":
    main()