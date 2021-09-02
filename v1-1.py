from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, PeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest, JoinChannelRequest
from telethon import types, utils, errors
import configparser
import sys
import csv
from csv import reader
import traceback
import time
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from colorama import init, Fore
init()

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [lg, r, w, cy, ye]


def legend_dev():
    import random
    b = [
        '    ___              __',
        '   /   |  __________/ /_  ____ ___  ____ _____ _____           _________  ____ ___',
        '  / /| | / ___/ ___/ __ \/ __ `__ \/ __ `/ __ `/ __ \         / ___/ __ \/ __ `__ \ ',
        ' / ___ |/ /  (__  ) / / / / / / / / /_/ / /_/ / / / /        / /__/ /_/ / / / / / /',
        '/_/  |_/_/  /____/_/ /_/_/ /_/ /_/\__,_/\__,_/_/ /_/   (.)   \___/\____/_/ /_/ /_/ '
        ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    print(f'==========================================Buy Software : t.me/ArshMaanChannel======{n}')
    print(f'==========================================Main Developer : t.me/Legend_dev========{n}')
    print(f'==========================================Developer Partner : t.me/Rocky_200====={n}\n')

legend_dev()

with open('memory.csv', 'r') as hash_obj:
    csv_reader = reader(hash_obj)
    list_of_rows = list(csv_reader)  
    row_number = 1
    col_number = 1
    numdel = list_of_rows[row_number - 1][col_number - 1]
    
LEGEND = int(numdel)
global nextLEGEND
nextLEGEND = LEGEND+1

with open('phone.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)    
    row_number = LEGEND
    col_number = 1
    value = list_of_rows[row_number - 1][col_number - 1]


    
api_id = int(2392599)
api_hash = str('7e14b38d250953c8c1e94fd7b2d63550')
pphone = value

config = configparser.ConfigParser()
config.read("config.ini")
to_group = config['Legend_dev']['ToGroup']


def ADDER():
    
    channel_username = to_group
    phone = utils.parse_phone(pphone)
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)
    
    client.connect()
    if not client.is_user_authorized():
        print(Style.BRIGHT + Fore.RED + 'some thing has changed')
        client.send_code_request(phone)
        client.sign_in(phone, input    (Style.BRIGHT + Fore.GREEN + 'Enter the code: '))
        
    input_file = 'data.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            user['id'] = int(row[2])
            #user['access_hash'] = int(row[3])
            user['name'] = row[3]
            users.append(user)

    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 2
        numnext = list_of_rows[row_number - 1][col_number - 1]
    
    startfrom = int(numnext)
    nextstart = startfrom+50
    
    with open('memory.csv', 'r') as hash_obj:
        csv_reader = reader(hash_obj)
        list_of_rows = list(csv_reader)  
        row_number = 1
        col_number = 3
        numend = list_of_rows[row_number - 1][col_number - 1]
    
    endto = int(numend)
    nextend = endto+50
        
    with open("memory.csv","w",encoding='UTF-8') as df:
        writer = csv.writer(df, delimiter=",", lineterminator="\n")
        writer.writerow([nextLEGEND,nextstart,nextend])

    for user in users:
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
            try:
                status = 'Legend_dev'
                if user['username'] == "":
                    print("no username, moving to next")
                    continue
                    
                client(InviteToChannelRequest(channel_username,[user['username']]))
                status = Style.BRIGHT + Fore.GREEN + 'DONE'
                
                print(Style.BRIGHT + Fore.YELLOW + "Please Wait...")
                time.sleep(random.randrange(1,5))
                
            except UserPrivacyRestrictedError:
                status = Style.BRIGHT + Fore.RED + 'PrivacyRestrictedError'
                time.sleep(random.randrange(3,5))
                            
            except UserAlreadyParticipantError:
                status = 'ALREADY'
                            
            except PeerFloodError as g:
                status = 'PeerFloodError'
                print(Style.BRIGHT + Fore.YELLOW + 'Getting FloodError........')
                time.sleep(random.randrange(60,90))
                           
            except ChatWriteForbiddenError as cwfe:
                client(JoinChannelRequest(channel_username))
                time.sleep(5)
                continue
                
            except errors.RPCError as e:
                status = e.__class__.__name__
            
            except Exception as d:
            	status = d
            	
            except:
                traceback.print_exc()
                print("Unexpected Error")
                continue
            channel_connect = client.get_entity(channel_username)
            channel_full_info = client(GetFullChannelRequest(channel=channel_connect))
            countt = int(channel_full_info.full_chat.participants_count)

            print(Style.BRIGHT + Fore.RESET + f"Group Members {(countt)}{Style. RESET_ALL} {Style.BRIGHT+Fore.CYAN}>> {user['name']} >> {status}")
        elif int(user['srno']) > int(endto):
            print(Style.BRIGHT + Fore.GREEN + "\nMembers Added Successfully !\n")
            stat = input(Style.BRIGHT + Fore.YELLOW + 'Press Enter To Exit')
            if stat == 1 :
                ADDER()
            else:
                quit()
             
ADDER()