class Notification:
    def __init__(self, user_contact, security_company_contact):
        self.user_contact = user_contact
        self.security_company_contact = security_company_contact

    def send_user_notification(self, face_identified):
        # Simulate sending a notification to the user
        print(f"Notification sent to user: Do you recognize this face? {face_identified}")
        return input("User response (yes/no): ").strip().lower()

    def alert_security_company(self, face_identified):
        # Simulate sending an alert to the security company
        print(f"Alert sent to security company: Unrecognized face detected! {face_identified}")
