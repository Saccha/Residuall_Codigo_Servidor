# -*- coding: utf-8 -*-
"""
@author: Sabrina Hablocher
"""

import web
import json

urls = (
    '/', 'padrao',
    '/health', 'health',
    '/mail/validation/v1', 'validacao'
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
        return json.dumps({
            'status': "OK",
            'code': 200,
            'results':[{"message": "Servidor executando na porta 8080"}]'
        })

class validacao:        
    def POST(self):
        jsonbody = json.loads(web.data())
        emailsvalidados = []
        for email in jsonbody['emails']:
            emailsvalidados.append(json.loads(validaremail(email)))
        return json.dumps({
            'status': 'OK',
            'code': 200,
            'results': emailsvalidados})

def validaremail(email):
    email_address = str(email['email_address'])
    valido = False
    if (email_address.endswith(".com")):
        valido = True
    elif (email_address.endswith(".com.br")):
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
