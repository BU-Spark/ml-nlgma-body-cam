import zipfile
import smtplib
import ssl
from email.message import EmailMessage

def all_funcs(openai_key, zip_path, yolo_weights, email, pr = gr.Progress(track_tqdm = True)):

  sentences = {}
  batons = {}
  count = 1
  
  with zipfile.ZipFile(zip_path, "r") as zip_ref:
    for filename in zip_ref.namelist():
        # Inn 2 lines mein error aa sakta hai
        
        zip_ref.extract(filename)
        video_path = filename[0].split('/')[-1]

        yolo_weights = yolo_weights[0].split('/')[-1]
        transcript = video_transcription(video_path)
        video_name = "Video " + str(count)
        sentences[video_name] = action_detection(transcript, openai_key)
        batons[video_name] = process_video(video_path, yolo_weights)
        count+=1

  email_sender = 'bodycam1211@gmail.com'
  email_password = 'evmt luaz mgoi iapl'
  email_receiver = email

  # Set the subject and body of the email
  subject = 'Timestamps Detection Complete'

  result = ""
  for i in sentences.keys():
     result = result + i + "\n"
     result = result + sentences[i] + "\n"
     result = result + batons[i] + "\n\n"
  
  body = "Here are the results of your detected timestamps:\n" + result

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email_receiver
  em['Subject'] = subject
  em.set_content(body)

  # Add SSL (layer of security)
  context = ssl.create_default_context()

  # Log in and send the email
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())
  
  print("ALL FUNC Executed without errors")

  return sentences, batons