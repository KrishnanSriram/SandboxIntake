class USBApp:
    def __init__(self, data):
        self.app_id = data['AppID']
        self.app_full_name = data['AppFullName']
        self.app_short_name = data['AppShortName']
        self.primary_owner_id = data['PrimaryOwnerId']
        self.secondary_owner_id = data['SecondaryOwnerId']
        self.cost_center = data['CostCenter']
        self.primary_owner_email = data['PrimaryOwnerEmail']
        self.secondary_owner_email = data['SecondaryOwnerEmail']
        self.gitlab_project_id = data['GitLabProjectId']

    def __repr__(self):
        return f"Application({self.app_id}, {self.app_full_name}, {self.app_short_name})"

    def to_dict(self):
        return {
            'app_id': self.app_id,
            'app_full_name': self.app_full_name,
            'app_short_name': self.app_short_name,
            'primary_owner_id':self.primary_owner_id,
            'secondary_owner_id': self.secondary_owner_id,
            'cost_center': self.cost_center,
            'primary_owner_email': self.primary_owner_email,
            'secondary_owner_email': self.secondary_owner_email,
            'gitlab_project_id': self.gitlab_project_id

        }