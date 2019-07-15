# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:30:21 2019

@author: VEN01335
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import base64
import array
import objectpath

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify','https://mail.google.com/']
jsonstring=''
def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    bodymail=''
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            path='D:\saurabh\workflow\09072019\PDCMS_LOAD\credentials.json'
            flow = InstalledAppFlow.from_client_secrets_file(
                path, SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])
    

    if not labels:
        print('No labels found.')
    else:
        print('')
        for label in labels:
            print('')
        results = service.users().messages().list(userId='me', maxResults=1).execute()
        for result in results:
            print(result)
        message_id = results['messages'][0]['id']
        message = service.users().messages().get(userId='me', id=message_id).execute()
        datasets=message["payload"]["parts"]
        """for  dataset in datasets:
             mailbody=str(base64.b64decode(dataset['body']['data']))"""
        encodestr=(datasets[len(datasets)-1]['body']['data'])
        print(encodestr)
        """if(mailbody.find('Ted')>-1):
            print("")"""
        senders=message["payload"]["headers"]
        for sender in senders:
            if(sender["name"]=="From"):
                print(sender["name"])
        messagenew=service.users().messages().get(userId='me',id='16be5c8b6950a4eb').execute()
        """print(messagenew)"""
        response = service.users().messages().list(userId='me', q="PDCMS_LOAD").execute()
        """print(results)"""
        response = service.users().messages().list(userId='me',labelIds='UNREAD').execute()
        """print(response)"""
        response = service.users().messages().list(userId='me',
                                               labelIds='UNREAD').execute()
        messages = []
        print('')
        if 'messages' in response: 
            senders=message["payload"]["headers"]               
            w = response['messages']
            for x in range(len(w)):
                print(w[x]['id'])
                messagebyid = service.users().messages().get(userId='me', id=w[x]['id']).execute()
                print(messagebyid['payload']['headers'])
                for sender in senders:
                    if(sender["name"]=="From"):
                        print(sender["value"])
                for  dataset in datasets:
                    lens=len(dataset['body']['data'])
                    print(lens)
                messagemod=service.users().messages().modify(userId='me',id=(w[x]['id']),body='READ').execute()
                """mailbody=base64.b64decode(lens+'=' *(-len(str(lens)%4))"""
                """print(mailbody)"""
                    
                       
                    
if __name__ == '__main__':
    main()

    