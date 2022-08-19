import smtplib
import csv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#VAI COLOCAR O NOME DO ARQUIVO CSV QUE FARA O LOOP
def send():
    with open('Clientes.csv', encoding='utf-8') as list:
        new_list = csv.reader(list, delimiter=';')
        for i in new_list:
            #A ORDEM DOS CAMPOS QUE ESTA NO CSV
            nome = i[0]
            contato = i[1]
            status = i[2]
            if status != 'Enviado':
                body = """
                    <p>Olá</p>
                    <p>Segue em anexo o boleto conforme solicitado.</p>
                    """
                #VAI COLOCAR O EMAIL DO QUAL SERÁ ENVIADO OS ARQUIVOS(SEU EMAIL)    
                sender = 'XXXXXXX'
                #VAI COLOCAR A SENHA QUE VOCÊ GERA PELAS CONFIGURAÇÕES DO GOOGLE, REFERENTE A 'SENHAS DE APP'
                password = 'XXXXXXXX'
                receiver = f'{contato}'
                
                #informações de envio
                message = MIMEMultipart()
                message['From'] = sender
                message['To'] = receiver
                message['Subject'] = 'Assunto do email'
                
                message.attach(MIMEText(body, 'html'))
                #NA PARTE ONDE TA ESCRITO 'BOLETO', VOCÊ VAI COLOCAR A PASTA QUE TA COLOCANDO O ARQUIVO, DEVE SER A MESMA DOS ARQUIVOS EM PDF
                #pdfname = away + '\\Boleto\\' + f'{Nome}.pdf'
                pdfname = f'{nome}.pdf'
                # abrir o arquivo em modo binario
                binary_pdf = open(pdfname, 'rb')
                
                payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                payload.set_payload((binary_pdf).read())
                
                # Passar para a base64
                encoders.encode_base64(payload)
                
                # abrir o header com o arquivo pdf
                payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                message.attach(payload)
                
                #porta do gmail
                session = smtplib.SMTP('smtp.gmail.com', 587)
                
                #habilitar segurança
                session.starttls()
                
                #login com a senha
                session.login(sender, password)
                
                text = message.as_string()
                session.sendmail(sender, receiver, text)
                session.quit()
                print('Email Enviado!')
send()            