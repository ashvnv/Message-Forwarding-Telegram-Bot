"""
MIT License
Copyright (c) 2021 Ashwin Vallaban
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#Messaging Bot
#This project was mode for FCRIT HACK-X-TRONICS 2021
#6 July 2021
#
#This program is not ready for production use
#
#Telegram Bot Token was removed for security reasons
#Admin Authorization not added



import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import json
import re
import os
import requests

#Telegram Bot Token-------------------------------------
TOKEN = "<>"  #Token removed
#-------------------------------------------------------
    

EXTC_MENU = 'EXTC'
COMP_MENU = 'COMPUTER'
IT_MENU = 'IT'
MECH_MENU = 'MECHANICAL'

ALL_1 = 'All 1st year'
ALL_2 = 'All 2nd year'
ALL_3 = 'All 3rd year'
ALL_4 = 'All 4th year'
ALL_YR = 'Send to everyone'

ALL_1_DEPT = '1st year '
ALL_2_DEPT = '2nd year '
ALL_3_DEPT = '3rd year '
ALL_4_DEPT = '4th year '
ALL_YR_DEPT = 'Send to all years '

BACK_TO_MAINMENU = 'Back to main menu'

DONE_SENDING = 'Done'

#============ Regex =================
ALL_DEPT_RX = '.+'

ALL_DEPT_1ST_RX = '1.+'
ALL_DEPT_2ND_RX = '2.+'
ALL_DEPT_3RD_RX = '3.+'
ALL_DEPT_4TH_RX = '4.+'

ALL_YEAR_EXTC = '[1-4]EXTC'
ALL_YEAR_COMP = '[1-4]COMP'
ALL_YEAR_IT = '[1-4]IT'
ALL_YEAR_MECH = '[1-4]MECH'

EXTC_DEPT_RX = 'EXTC'
MECH_DEPT_RX = 'MECH'
IT_DEPT_RX = 'IT'
COMP_DEPT_RX = 'COMP'

#====================================


#func reads the txt file and returns it's contents
#filename should be with extension
def file_read(filename, filemode):
    print('file_read()')
    # Open a file: file
    file = open(filename,mode=filemode)
 
    # read all lines at once
    itemdata = file.read()
 
    # close the file
    file.close()

    print('File Read')

    return itemdata


#=============================================== Main Menu ==========================================================
def main_menu(chat_id,done):
    print('main_menu()')
    temp_exec_cmd = """bot.sendMessage(chat_id, 'Main Menu',
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=["""
    done_btn = """[KeyboardButton(text=DONE_SENDING)],"""
    temp_exec_cmd2 = """[KeyboardButton(text=EXTC_MENU),KeyboardButton(text=COMP_MENU)],
                            [KeyboardButton(text=IT_MENU),KeyboardButton(text=MECH_MENU)],
                            [KeyboardButton(text=ALL_1),KeyboardButton(text=ALL_2),KeyboardButton(text=ALL_3),KeyboardButton(text=ALL_4)],
                            [KeyboardButton(text=ALL_YR)]
                            ]
                        )
                    )"""

    if done == 0:
        exec(temp_exec_cmd + temp_exec_cmd2)
    else:
        exec(temp_exec_cmd + done_btn + temp_exec_cmd2)
        
    print('Executed custom keyboard')
    

#=============================================== Sub-main Menu ==========================================================
def sub_main_menu(chat_id,DEPT_NAME,done):
    print('sub_main_menu()')
    
    temp_exec_cmd = """bot.sendMessage(chat_id, 'Sub-Main Menu',
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=["""
    done_btn = """[KeyboardButton(text=DONE_SENDING + ' ' + DEPT_NAME)],"""
    temp_exec_cmd2 = """[KeyboardButton(text=ALL_1_DEPT + DEPT_NAME),KeyboardButton(text=ALL_2_DEPT + DEPT_NAME),KeyboardButton(text=ALL_3_DEPT + DEPT_NAME),KeyboardButton(text=ALL_4_DEPT + DEPT_NAME)],
                            [KeyboardButton(text=ALL_YR_DEPT + '[' + DEPT_NAME + ']')],
                            [KeyboardButton(text=BACK_TO_MAINMENU)]
                            ]
                        )
                    )"""
    if done == 0:
        exec(temp_exec_cmd + temp_exec_cmd2)
    else:
        exec(temp_exec_cmd + done_btn + temp_exec_cmd2)
    
    print('Executed custom keyboard')


#############################
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    #call delete func!
    try:
        inline_delete(re.findall(" .+", msg['data'])[0].strip(),from_id)
        bot.sendMessage(from_id, 'deleted message!')
    except:
        bot.sendMessage(from_id, 'Message Not Found')
    
def inline_key_send(key_msg,callback_msg,chat_id):
    from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=key_msg, callback_data=callback_msg)],
        ])
    bot.sendMessage(chat_id, '_', reply_markup=keyboard)


#############################
#this func deletes the item
def db_clear(chat_id, done):
    
    print('db_clear()')
    
    itemdata = file_read('Admin/' + str(chat_id) + '/chat.txt','r')

    json_dictionary = json.loads(itemdata)

    v = ''

    for k,v in json_dictionary.items():
        if re.search("^#.+",v):
            #delete files from local folder
            print('deleting file: ' + re.findall("[A-z0-9].+", v)[0].strip())
            os.remove('Admin/' + str(chat_id) + '/' + re.findall("[A-z0-9].+", v)[0].strip())
            print('files deleted')
        
    # Open a file: file
    with open('Admin/' + str(chat_id) + '/chat.txt','w') as file:
        file.write('{}') #clear chat db
 
    # close the file
    file.close()

    bot.sendMessage(chat_id, 'Done! Cleared all messages!')

    print('db cleared')

    if done == 'Done':
        main_menu(chat_id,0)
    else:
        sub_main_menu(chat_id,done,0)

    print('menu updated')

    return

#for deleting messages from inline keyboard
def inline_delete(message_id,chat_id):
    print('inline_delete()')
    
    itemdata = file_read('Admin/' + str(chat_id) + '/chat.txt','r')

    json_dictionary = json.loads(itemdata)

    if re.search("^#.+",json_dictionary[message_id]):
        os.remove('Admin/' + str(chat_id) + '/' + re.findall("[A-z0-9].+", json_dictionary[message_id])[0].strip())
        print('File deleted')
        
    else:
        print('Not a file')
    del json_dictionary[message_id]
    print('deleted')

    with open('Admin/' + str(chat_id) + '/chat.txt','w') as file:
        file.write(json.dumps(json_dictionary)) #update db
 
    # close the file
    file.close()
        

def chk_if_send_cmd(msg,chat_id):
    if msg == ALL_1:
        print('True')
        send_messages(ALL_DEPT_1ST_RX,chat_id)
        return True
    elif msg == ALL_2:
        print('True')
        send_messages(ALL_DEPT_2ND_RX,chat_id)
        return True
    elif msg == ALL_3:
        print('True')
        send_messages(ALL_DEPT_3RD_RX,chat_id)
        return True
    elif msg == ALL_4:
        print('True')
        send_messages(ALL_DEPT_4TH_RX,chat_id)
        return True
    elif msg == ALL_YR:
        print('True')
        send_messages(ALL_DEPT_RX,chat_id)
        return True

    elif re.search(ALL_YR_DEPT + '\[(EXTC|MECH|IT|COMP)\]$',msg):
        send_messages('[1-4]' + re.findall("\[(EXTC|MECH|IT|COMP)\]$", msg)[0].strip(), chat_id)
        return True

    elif re.search('[1-4].+year ' + '(EXTC|MECH|IT|COMP)$',msg):
        print('True')
        send_messages(re.findall("^[1-4]", msg)[0].strip() + re.findall("(EXTC|MECH|IT|COMP)$", msg)[0].strip(), chat_id)
        return True

    return False

#======================================== Send message ==========================================

def send_messages(rx,chat_id):
    bot.sendMessage(chat_id, 'Sending messages please wait.....')

    print('send_messages()')
    print('regex: ' + rx)

    filedata = file_read('Admin/' + str(chat_id) + '/chat.txt','r')
    if filedata == '{}':
        print('Nothing to send!')
        bot.sendMessage(chat_id, 'Nothing to send!')
        return

    grpdata = file_read('groups.txt','r')
    json_dictionary_grp = json.loads(grpdata)

    for k,v in json_dictionary_grp.items():
        if re.search(rx,k):

            if v == 'NA':
                print('Chat id not found skipped')
                bot.sendMessage(chat_id, 'Group not made!')
            else:
                #send message
                print(k + ' :' + v)

                json_dictionary = json.loads(filedata)

                for i,j in json_dictionary.items():
                    if re.search('^#.+',j):
                        if re.search('.+.png$',j):
                            print('photo in db')
                            bot.sendPhoto(v, photo=open('Admin/' + str(chat_id) + '/' + re.findall('[0-9]+',j)[0].strip() + '.png', 'rb'))
                            print('photo sent')
                        else:
                            print('file in db')
                            bot.sendDocument(v, document=open('Admin/' + str(chat_id) + '/' + re.findall('[A-z0-9].+',j)[0].strip()))
                            print('file sent')
                    else:
                        bot.sendMessage(v,j)
                        print('message sent')

    bot.sendMessage(chat_id, 'Sent!')

    if re.search('[1-4]\.\+',rx) or re.search('\.\+',rx):
        main_menu(chat_id,1)
    else:
        sub_main_menu(chat_id,re.findall("[A-Za-z].+", rx)[0].strip(),1)

            

############################################# Root #######################################################

def add_chat_to_db(chat_id, msg, file_sent, content_type):
    #check if files are available
    #create file and folder if not available
    
    filedata = ''
    
    try:
        filedata = file_read('Admin/' + str(chat_id) + '/chat.txt','r')
        print('File available!')
        
    except:
        try:
            os.mkdir('Admin/' + str(chat_id))
            with open('Admin/' + str(chat_id) + '/chat.txt','w') as file:
                file.write('{}')
            file.close()
            print('chat.txt file created successfully!')
            filedata = '{}'
        except:
            print('Error creating file!')
            file.close()
#------------------------------------------------------------------------

    json_dictionary = json.loads(filedata)
    
    if file_sent == False:
        json_dictionary.update({msg['message_id']: msg['text']})
    else:
        if content_type == 'photo':
            json_dictionary.update({msg['message_id']: '#' + str(msg['message_id']) + '.png'})
        else:
            json_dictionary.update({msg['message_id']: '#' + msg['document']['file_name']})

    #--------------------- Add chat to DB ----------------------------------------
    try:
        with open('Admin/' + str(chat_id) + '/chat.txt','w') as file:
            file.write(json.dumps(json_dictionary))
            print('Chat added to DB')
        file.close()
    except:
        print('Error updating the DB')
        file.close()

    ############################
    inline_key_send('delete sent msg', '#delete ' + str(msg['message_id']), chat_id)
    ############################

    #---------------------Update Admin info txt file------------------------------
    try:
        with open('Admin/' + str(chat_id) + '/admininfo.txt','w') as file:
            file.write(json.dumps(msg['from']))
        file.close()
    except:
        print('Error updating the DB')
        file.close()


def on_chat_message(msg):
    print('\non_chat_message() msg received')
    
    content_type, chat_type, chat_id = telepot.glance(msg)

    if msg['chat']['type'] == 'group':
        print('Message received from group. Chat ID: ' + str(chat_id) + '\nGroup name: ' + msg['chat']['title'])
        bot.sendMessage(chat_id, 'Not Allowed! ' + str(chat_id) + '\nGroup name: ' + msg['chat']['title'])
        return

    if content_type == 'text':

        #add auth here

        #--------Check if done button should be added or not--------------
        add_done_btn = 0
        try:
            if (file_read('Admin/' + str(chat_id) + '/chat.txt','r') == '{}') == False:
                add_done_btn = 1
                print('add done button')
            else:
                print('not adding done')
        except:
            print('not adding done button! chat.txt not found')
        
        if msg['text'] == '/start':
            main_menu(chat_id,add_done_btn)
            print('show main menu')
        
        #========================================
        #Dept-wise sub menu
        elif msg['text'] == EXTC_MENU:
            sub_main_menu(chat_id,'EXTC',add_done_btn)
            print('show sub main menu EXTC')
        elif msg['text'] == COMP_MENU:
            sub_main_menu(chat_id,'COMP',add_done_btn)
            print('show sub main menu COMP')
        elif msg['text'] == IT_MENU:
            sub_main_menu(chat_id,'IT',add_done_btn)
            print('show sub main menu IT')
        elif msg['text'] == MECH_MENU:
            sub_main_menu(chat_id,'MECH',add_done_btn)
            print('show sub main menu MECH')            
        elif msg['text'] == BACK_TO_MAINMENU:
            main_menu(chat_id,add_done_btn)
            print('show main menu')
        #========================================

        elif re.search("^Done (EXTC|IT|COMP|MECH)", msg['text']):
            #delete chat db and documents
            db_clear(chat_id,re.findall("(EXTC|IT|COMP|MECH)$", msg['text'])[0].strip())

        elif msg['text'] == 'Done':
            db_clear(chat_id, 'Done')

        #============ Regex =====================
        elif re.search('[1-4AS].+',msg['text']) and chk_if_send_cmd(msg['text'],chat_id):
            pass

        else:
            add_chat_to_db(chat_id, msg, False, content_type)

    # media file sent!
    else:
        print('File sent!')
        add_chat_to_db(chat_id, msg, True, content_type)
        #------------- Download the file ---------------------
        if content_type == 'photo':
            bot.download_file(msg['photo'][-1]['file_id'], 'Admin/' + str(chat_id) + '/' + str(msg['message_id']) + '.png')
        else:
            bot.download_file(msg['document']['file_id'], 'Admin/' + str(chat_id) + '/' + msg['document']['file_name'])
        #-----------------------------------------------------
        
           

##############################################################
bot = telepot.Bot(TOKEN)
print('Listening ...')
bot.message_loop({'chat': on_chat_message,
                  'callback_query': on_callback_query}, run_forever=True)
