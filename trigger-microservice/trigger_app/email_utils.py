import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.conf import settings

REMETENTE = settings.REMETENTE
PASSWORD = settings.PASSWORD

def enviar_email(destinatario, assunto, mensagem):

    try:
        # Configuração do servidor SMTP do Outlook
        servidor = "smtp.office365.com"
        porta = 587
        
        # Configurando a mensagem
        msg = MIMEMultipart()
        msg['From'] = REMETENTE
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))
        
        # Conectando ao servidor
        with smtplib.SMTP(servidor, porta) as servidor_smtp:
            servidor_smtp.starttls()  
            servidor_smtp.login(REMETENTE, PASSWORD)  
            servidor_smtp.sendmail(REMETENTE, destinatario, msg.as_string()) 
        print("E-mail enviado com sucesso!")
    
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")