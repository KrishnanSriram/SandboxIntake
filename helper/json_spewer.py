import json

def sanboxapp_to_json(sandbox_applications):
    for app in sandbox_applications:
        app_dict = app.to_dict()
        #    persist/append into a file
        with open(app.app_short_name + ".json", "w") as file:
            json.dump(app_dict, file)