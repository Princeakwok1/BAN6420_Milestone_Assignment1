
class Policyholder:
    def __init__(self, name, policy_id, status="Active"):
        self.name = name
        self.policy_id = policy_id
        self.status = status

    def suspend(self):
        self.status = "Suspended"

    def reactivate(self):
        self.status = "Active"

    def get_details(self):
        return f"Policyholder: {self.name}, ID: {self.policy_id}, Status: {self.status}"
