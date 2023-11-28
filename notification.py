import random

class Notification:
    def __init__(self, user_contact, security_company_contact, alarm):
        self.user_contact = user_contact
        self.security_company_contact = security_company_contact
        self.alarm = alarm

    def send_user_notification(self, face_identified):
        # Simulate sending a notification to the user
        print(f"Notification sent to user: Do you recognize this face? {face_identified}")
        return input("User response (yes/no): ").strip().lower()

    def alert_security_company(self, face_identified):
        # Simulate sending an alert to the security company
        print(f"Alert sent to security company: Unrecognized face detected! {face_identified}")
        self.alarm.trigger_alarm()

    def handle_security_response(self):
        # This method can be called periodically to check if security has responded
        # This is a placeholder for how the security company might respond
        # In a real-world scenario, this would be replaced with actual communication logic
        if self.alarm.waiting_for_security:
            security_response = random.choice(['yes', 'no'])  # Simulating a random response
            if security_response == 'yes':
                self.alarm.security_check_done()
