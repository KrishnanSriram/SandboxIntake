import re

from model.usbapp import USBApp


def parse_intake_file(intake_file):
    sandbox_applications = []
    with open(intake_file, "r") as file:
        content = file.read()
        applications = content.split("--")
        # TODO: Check to see if there are applications before you parse it
        # Parse each application separately
        for app in applications:
            if app.strip():  # Ignore empty sections
                # Extract key-value pairs from the section using regex
                pairs = re.findall(r'(\w+):\s*"([^"]*)"', app)
                # Create a dictionary from the key-value pairs
                data = dict(pairs)
                # TODO: Validate if this data is a valid USBApplication. If not error and continue
                # Create an instance of the Application class using the data dictionary
                app = USBApp(data=data)
                sandbox_applications.append(app)

    return sandbox_applications