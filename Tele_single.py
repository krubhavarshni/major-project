from Adafruit_IO import Client,Feed,Data
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import requests
import os

# a=ADAFRUIT_IO_USERNAME
# b=ADAFRUIT_IO_KEY
a = os.getenv('a')
b = os.getenv('b')
T_T = os.getenv('T_T')

def Lets_go(bot, update):
    bot.send_message(chat_id = update.effective_chat.id, text="YOKOSOO !!")
    bot.send_message(chat_id = update.effective_chat.id, text=" Type 'Turn on the light' if you want to turn on the light or type 'Turn off the light' if you want to turn off the light")
    
def err_msg(bot, update):
    bot.send_message(chat_id=update.effective_chat.id, text="Oops! I couldn't recognize.Please try again!!")

def send_data_to_adafruit(value1):
    value=Data(value=value1)
    value_send=aio.create_data('light control',value)
    
def Lights_on(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning on the light")
  bot.send_photo(chat_id, photo='https://www.pinclipart.com/picdir/big/348-3486135_png-file-svg-turn-off-lights-icon-clipart.png')
  send_data_to_adafruit(1)
  
def Lights_off(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Turning off the light")
  bot.send_photo(chat_id=update.effective_chat.id,photo='https://cdn4.iconfinder.com/data/icons/ui-controls-miscellaneous/32/interface-controls-light-bulb-off-512.png')
  send_data_to_adafruit(0)
  
def text_given(bot, update):
  text = update.message.text
  if text == 'Start':
   Lets_go(bot,update)
  elif text == 'Turn on the light':
    Lights_on(bot,update)
  elif text == 'Turn off the light':
    Lights_off(bot,update)
  else:
    err_msg(bot,update)
    
aio = Client(a,b)  
u = Updater(T_T)
dp = u.dispatcher
dp.add_handler(CommandHandler('turnonthelight',Lights_on))
dp.add_handler(CommandHandler('turnonthelight',Lights_off))
dp.add_handler(CommandHandler('start', Lets_go))
dp.add_handler(MessageHandler(Filters.command, err_msg))
dp.add_handler(MessageHandler(Filters.text, text_given))

u.start_polling()
u.idle()

