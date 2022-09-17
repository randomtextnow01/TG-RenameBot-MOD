'''
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo 
Dont kang !!!
© Mrvishal2k2
'''
import os 

class Config(object):
  APP_ID = int(os.environ.get("APP_ID", "17124006"))
  API_HASH = os.environ.get("API_HASH", "97e184dc9c07513de148002859aef2b2")
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5378478282:AAEgw2icIMpes6YuyHbobv5r9jk3ETf578I")
  AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1165699179").split())
  DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
  DB_URI = os.environ.get("DATABASE_URL", "postgres://twgxgxjk:ndkpWxP_MvorOqRpePLQBpGcIiikeMze@suleiman.db.elephantsql.com/twgxgxjk")
  # owner is for log cmd only owner can use (this can be multiple users)
  OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "1165699179").split(" ")]
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "eternalpokemontrainer")
  CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",False)
