
import datetime
from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# Connect to MongoDB
client = MongoClient('mongodb+srv://purushoth170288:Bruce17@cluster0.yfliaq8.mongodb.net/?retryWrites=true&w=majority')
db = client['test']
collection = db['animal']

def get_data_last_1_minute():
    # Get current date and time
    current_date = datetime.datetime.now()
    # Calculate date and time 1 minute ago
    start_date = current_date - datetime.timedelta(minutes=1)
    # Query data for the last 1 minute
    data = collection.find({'timestamp': {'$gte': start_date}})
    return list(data)

def generate_report(data):
    # Format data into a report
    report = "Animal Intrusion Detection Report for the Last 1 Minute:\n\n"
    for item in data:
        report += f"Timestamp: {item['timestamp']}, Angle: {item['angle']}, Area: {item['area']}, Trespasser: {item['trespasser']}\n"
    return report

def send_email(report):
    # Email configuration
    from_email = 'purushoth170288@gmail.com'
    to_email = 'vijay2110746@ssn.edu.in'
    password = 'xwzy lyhq ujun npzn'
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Animal Intrusion Detection Report'
    
    # Attach report to the email body
    msg.attach(MIMEText(report, 'plain'))
    
    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    
    # Send email
    server.send_message(msg)
    server.quit()

def main():
    total_data = []  # Initialize an empty list to store total data
    while True:
        # Get data for the last 1 minute
        data_last_1_minute = get_data_last_1_minute()
        # Append data to total_data list
        total_data.extend(data_last_1_minute)
        # Check if 3 minutes have passed
        if len(total_data) >= 1:
            # Generate report for total data
            report = generate_report(total_data)
            # Send email with report
            send_email(report)
            # Clear total data list
            total_data = []
        # Wait for 1 minute before checking again
        # time.sleep(60)

# if __name__ == '__main__':
#     main()
