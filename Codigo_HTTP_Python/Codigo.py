# -*- coding: utf-8 -*-
"""
@author: Sabrina Hablocher
"""

import web
import json
import http.client
import pymssql

urls = (
    '/', 'padrao',
    '/health', 'health',
    '/mail/validation/v1', 'validacaov1',
    '/mail/validation/v3', 'validacaov3'
)

app = web.application(urls, globals())

class padrao:        
    def GET(self):
        return json.dumps({
            'status': 'OK',
            'code': 200,
            'results': []
            })

class health:        
    def GET(self):
        return json.dumps({'status':"OK",
                          'code': 200,
                          'results': [{"message": "Servidor executando na porta 8080"}]
                          })

class validacaov1:        
    def POST(self):
        jsonbody = json.loads(web.data())
        emailsvalidados = []
        for email in jsonbody['emails']:
            emailvalidado = json.loads(validaremail(email))
            inseriremailvalidadov1(emailvalidado)
            emailsvalidados.append(emailvalidado)
        return json.dumps({
            'status': 'OK',
            'code': 200,
            'results': emailsvalidados})

class validacaov3:
    def POST(self):
        jsonbody = json.loads(web.data())
        conn = http.client.HTTPSConnection("api.eva.pingutil.com")
        payload = ''
        headers = {}
        emailsvalidados = []
        for email in jsonbody['emails']:
            emailvalidado3 = json.loads(validaremail(email))
            emailsvalidados.append(emailvalidado3)
            email_address = str(email['email_address'])
            conn.request("GET", "/email?email=" + email_address,
                         payload,
                         headers)
            res = json.loads(conn.getresponse().read())
            emailsvalidados.append({'data': res['data']})
            inseriremailvalidadov3(email['email_address'], res['data'])
        return json.dumps({
            'status': 'OK',
            'code': 200,
            'results': emailsvalidados})
   
def inseriremailvalidadov1(email):
    conn = pymssql.connect(server='localhost', user='sa', password='password', database='Residuall')  
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ValidacaoV1 (email_address, domain, valid_syntax) VALUES (%s, %s, %s)",
        (email['email_address'], email['domain'], email['valid_syntax']))
    conn.commit()
    cursor.close()
    conn.close()

def inseriremailvalidadov3(emailaddress, data):
    conn = pymssql.connect(server='localhost', user='sa', password='password', database='Residuall')  
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ValidacaoV3 (email_address, domain, valid_syntax, disposable, webmail, deliverable, catch_all, gibberish) VALUES (%s, %s, %s, %s, %s, %s, %s, %s )",
        (emailaddress,
         'email',
         data['valid_syntax'],
         data['disposable'],
         data['webmail'],
         data['deliverable'],
         data['catch_all'],
         data['gibberish']))
    conn.commit()
    cursor.close()
    conn.close()    

def validaremail(email):
    email_address = str(email['email_address'])
    valido = False
    if (email_address.endswith(".com.br")):
        valido = True
    elif (email_address.endswith(".com")):
        valido = True
    elif (email_address.endswith(".gov.br")):
        valido = True
    elif (email_address.endswith(".org")):
        valido = True
    return json.dumps({
            'email_address' : email_address,
            'domain' : "email",
            'valid_syntax' : valido
            })

if __name__ == "__main__":
    app.run()

