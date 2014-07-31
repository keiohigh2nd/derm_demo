# coding: utf-8
import dropbox
import os
import serve, time

def authentification():
  #First time
  app_key = 'hm12h64j3x6zq57'
  app_secret = '0ovah3hqt0lhi6r'
  flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

  authorize_url = flow.start()
  print '1. Go to: '+ authorize_url
  print '2. Click "Allow" (you might have to log in first)'
  print '3. Copy the authorization code.'
  code = raw_input("Enter the authorization code here: ").strip()

  access_token, user_id = flow.finish(code)
  print access_token
  client = dropbox.client.DropboxClient(access_token)
  print'linked account: ', client.account_info()
  print '----connected succesfully ---------'
  return client

def download_image(client, img_path):
  f, metadata = client.get_file_and_metadata(img_path)
  out= open('new.jpg','w')
  out.write(f.read())
  out.close()
  print f

def upload_image(client):
  f = open('../build/img/res_new.jpg','r')
  response = client.put_file('/res_new.jpg', f)
  print'uploaded: ', response

def list_folders(client):
  folder_metadata = client.metadata('/')
  print folder_metadata

def check_new_img(client):
  folder_metadata = client.metadata('/')
  files = folder_metadata['contents']
  return len(files) 

def get_new_img(client):
  folder_metadata = client.metadata('/')
  files = folder_metadata['contents']
  return files[-1]['path']
  
if __name__ == "__main__":
  import sys
  argvs = sys.argv
  client = authentification()

  #upload_image(client)
  #download_image(client)
  #list_folders(client)

  for i in range(1000000):
    img_num = check_new_img(client)
    time.sleep(5)
    current_img_num = check_new_img(client)
    if int(img_num) != int(current_img_num):
      new_img  = get_new_img(client)
      print 'Analyzing = ', new_img
      download_image(client, new_img)
      serve.classify()
      upload_image(client)
