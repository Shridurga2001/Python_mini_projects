from email.message import EmailMessage
from emailpass import password
import ssl
import smtplib # Logining in and send email

email_sender = 'shrimadhuuday2001@gmail.com'
email_password = password
email_receiver = 'nebulathanos29@gmail.com'

subject = "I'm an Enthusiastic Fresher Seeking Employment Opportunity at ABC company"
body = """ 
I am eager to contribute my skills, creativity, and passion for technology to support ABC's mission and drive business success. 
As a quick learner and a proactive team player, I am confident in my ability to adapt to new challenges and contribute positively to the development team.
I have attached my resume to this email, which provides a detailed overview of my education, projects, and relevant experiences. I would be grateful for the opportunity to discuss how my qualifications and potential align with ABC's requirements during an interview.  
Thank you for considering my application. I am excited about the possibility of becoming a part of ABC's dynamic team and contributing to the company's success. 
Please find my contact information below, and I look forward to the opportunity to speak with you further.   
Sincerely, 
Shridurga U
"""
# creating instance for emailmessage
mail = EmailMessage()
mail['From'] = email_sender
mail['To'] = email_receiver
mail['subject'] = subject
mail.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
   smtp.login(email_sender, email_password)
   smtp.sendmail(email_sender, email_receiver, mail.as_string())