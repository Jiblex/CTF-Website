# CTF Website

## Overview

This is some work intended for the Northeatern CTF Club, where some of these challenges have already been used and others await their time (whenever this is being read this may not be the case however). This repo contains a website, as per its name, which contains mutiple web challenges and can be used as a template to create challenges in the future. Other challenges made in this batch that were not challenges that made their way onto the website, will be included as well. They will live in the _system_ directory. 

When working on the website, all of the required packages and libraries lived in a venv, however the directory containing all of these files grew rather large, and due to trouble uploading it all onto github I decided to omit the venv. All required packages and libraries have been placed in the _requirements.txt_ file (ctf_web/requirements.txt), this way no unnecessary installations need be made. The requirements file can be used with pip (_pip install -r requirements.txt_), or may also be ran in a Dockerfile. An example Dockerfile has been provided (ctf_web/Dockerfile). 

Below I will paste the complete README.md file I used for documentation throughout the challenge creation process. It contains every challenge, along with its description, solution and flag. It also includes some commands which can be used at the top to run the website, however if downloading, these commands may not work without setup. Refer to venv and Flask documentation for the _source_ and _flask run_ commands and how to setup these up. It also contains some user credentials. 

<br>
<br>
<br>
<br>


Running virtualenv:
$ source CTF_web/bin/activate 
$ deactivate

Run flask app:
$ flask run
or 
$ python app.py 

Debug mode:
$ export FLASK_DEBUG=1
*When running the website turn debug mode off*

Users:
billy@gmail.com: password
Bencat@gmail.com: qwertyBAD
prestige@gmail.com: not_weak_password


Flag users:
username@gmail.com(this account has flag as username for E1): passwordisnotpassword

--- This user does not exist in the database. These credentials only work on the /abyss page. ---
FatherChristmas: d1dUctrlF


Challenge Write up format:

x. (Type) Name
a. Description:

b. Walkthrough:
***NOTE*** if need be
HINT (if there's a hint): 

c. FLAG:
	CTF{...}
*Docker* - needs container
*Website* - on website

CHALLENGES:


**SUPER EASY**


1. (MISC) In Plain Sight
a. You will find the flag on the home page (/home). It's right there, can't you see it?
b. The flag is hidden in the home page. Search the HTML code, the flag is in the id field of an h1 tag.
c. CTF{1m_riGHt_hEre;)}
*Website*



2. (Routing) tErmINAt0r
a. My search engine crawler gave me a weird looking URL for the CTF website... I wonder why it looks like that?
b. Navigate to the robots.txt file. The route is simply "/robots.txt". 
HINT: "robots"
c. CTF{sh0Wing_mE_1s_AlLowed}
*Website*



3. (System) Kernel Quest
a. What's the kernel release of this machine?
b. Use command $uname -r.
HINT: uname
*NOTE* should probs check to make sure, I've had 2 dif answers when running container from host and virtual machine. 
c. CTF{6.6.16-linuxkit}
*Docker*



4. (System) Crunch Time
a. What is the command set to run every 15 minutes on this machine as soon as it boots up (use an _ where there is a spcace when you submit the flag)? 
b. Use command "$crontab -e". You will see that the command "$run-parts /etc/periodic/15min". 
HINT: crontab
c. CTF{run-parts_/etc/periodic/15min}
*Docker*



5. (MISC) Unravelling the Layers 
a. I can't read the file! Decompress it for me. 
b. Use "$tar -xvf flag.txt.gz.tgz.tgz" twice to get rid of the two .tgz, then "$gzip -d flag.txt.gz" to decompress the file to flag.txt. The flag is now readable. 
c. CTF{d3comPe55ion_KING}

Dependencies: flag.txt.gz.tgz.tgz




6. (MISC) C01D_sT0R4Ge 
a. Head over to the about page (/about). The flag is on the server's storage. 
b. Use the inspector tool, go to storage, local storage. The flag is right there. 
c. CTF{fR0z3N_D4t4_1s_tH3_b3st}
*Website*



7. (Routing) URLpass
a. Go to the URLpass challenge (/URLpass/param=wKD7yf0). The flag is hidden on a page who's URL parameter is a famous wordlist. 
b. The worldist is rockyou. The flag is hidden on the link '/URLpass/param=rockyou'.
c. CTF{c0RreCT_p4R4m_1Nt3rC3PTed}
*Website*



8. (MISC) H0tD0g
a. Click on the right hot dog. Even if all is 404, check the URL.
b. Click the "Hot Dogs" part of the essay title. This will lead you to a 404 error page. Flag is in the URL. 
c. CTF{tH3_secreT_HOT_D0G}
*Website*



**EASY**



1. (SQL Injection) In the Data
a. I forgot my username, but I made a bet that I know my username and my friend doesn't and as usual I forgot it... my friend said the login page (/login) had some sort of weakness and that he got it from there. I can't lose this bet!
b. The flag is in the database. SQL injection: "SELECT * FROM users". 
HINT: The flag is the users table. 
c. CTF{iDk_mY_usrName}
*Website*



2. (Crypto) $YouxWill_Know&My#Feelings
a. I have a message. $2b$12$pGN/fxQLP4n6UkhYF9nccuo7pl4HX0scaaM1V.FDCfAjQ3YuofaMy
b. The hashing algorithm is bcrypt blowfish. Use hashcat (or any other password cracking tools) to decrypt via dictionary attack. Command I used: 
$hashcat -m 3200 -a 0 hash.txt wordlist.txt
This will give back the message, make it CTF format by putting in into CTF{}.

***NOTE*** I made sure to use a password that can be found earlier (so it doesn't take a week) in rockyou.txt, as this is probably the wordlist most will try using. 
HINT: Use rockyou (josuamarcelc)... and remember to be patient.
c. CTF{friendsforever}

Dependencies: feelings.txt



3. (OSINT) ExpCert
a. Find out what the expiration date of the https://www.northeastern.edu/ server certificate is. Submit the flag in the form CTF{Month Day Hour:Minute:Second Year TimeZone}. 
b. Mutiple ways to do this. I did "$curl -v https://www.northeastern.edu/". The expiration date can be found in the "Server certificate" towards the top of the output, right under the TLS handshake. 
c. CTF{May 17 23:59:59 2024 GMT}



4. (Routing) Phantom Pathfind
a. The flag is hidden on a secret route. Go to /phantom for some help. Gobust some invisible routes! 
b. Use gobuster along with the provided wordlist. "$gobuster dir -u URL/IP -w wordlist.txt".f This gives list of found routes. The flag is on the /rockyou route. 
HINT: gobuster
c. CTF{r0UT3_bU5T3r5}
*Website*



5. (Recon) Rdar 
a. What is the version of OpenSSH running on scanme.nmap.org?
b. Use command "$nmap -sV scanme.nmap.org", this will give OpenSSH version. 
***NOTE*** Should make sure that the version hasn't changed before running challenge. 
c. CTF{6.6.1p1}



6. (MISC) Packet Prowl 
a. What is the MAC address of the Apple device?
b. Apple device has IP 192.168.1.151, look for its MAC address in the Ethernet II section after clicking on the packet. 
c. CTF{f0:2f:4b:09:7e:3c}

Dependencies: crash.pcap



**MEDIUM**


1. (Reverse Engineering) fork
a. Woah I think I might have dropped my knife on the wrong button when encoding the flag!
b. Need to use spoon decoder to in order to get the flag. 
HINT: spoon
c. CTF{3s0T3r1c_l4ng5_3XiST}

Dependencies: 01.txt



2. (API) Access Abyss
a. Stare into the abyss and the abyss will not send you a post. Anyway I need to login through the /abyss page, but there's no place for me to input my credentials... what to do?
b. Use any technique to find the 'usrname' and 'passwd' that are hidden in the black text (ctrl+f, grep...). Then use a curl POST request on the /abyss page with these credentials. This will return the flag in your terminal. 
Username: 'FatherChristmas', Password:'d1dUctrlF?'. 
$curl -X POST -F "username=FatherChristmas" -F "password=d1dUctrlF" http://127.0.0.1:5000/abyss
HINT: Send a POST request
HINT: cURL
c. CTF{the4Byss_sT4r3es_RIGhtB4ck}
*Website*



3. (API) Agent 007: User Agent Undercover
a. Go the challenge tab or navigate to "/user_agent". Use cURL.
b. Use "$curl -X POST http://127.0.0.1:5000/user_agent", you will be told you have the incorrect user agent and to go to /user_agent/help. Navigate to the page. The injection needs to look similar to this: /user_agent/help?injection={{secret_ua}}
Using secret User-Agent agH8dGG7, send curl request and get the flag:
"$curl -A SECRET http://127.0.0.1:5000/user_agent" or "$curl -H "User-Agent: SECRET" http://127.0.0.1:5000/user_agent".
c. CTF{B3rRy_5TR4Wberry}
*Website*



4. (Forensics) Seen Through The Sea
a. You can only see the flag in the panes of sea and blood. 
b. Using any stenography (I used StegOnline to make and solve the challenge), look at the image in bit planes 1 and 2 in the colors red and blue respectively. Put the two parts of the flag together. Looking at the text you will find that it ends in an = sign, which is how base32 and base64 encodings end. Decode the string using base32 results in the flag.
c. CTF{500n_maY_tH3_w311erman_cOME}

Dependencies: flag.png



**HARD**


1. (Reverse Engineering) To Code or Not To Code
a. What is Hamlet? What is Juliet? Give the flag in the form CTF{Hamlet.Juliet}. Here's a free clue: 10111511111610111410599
b. The free clue is the ASCII representation of "esoteric". 
Change Hamlet.txt to Hamlet.spl. This makes it a Shakespeare Programming Language file (an esoteric programming language). Note that you must install shakespearelang via pip. Then run "$shakespeare debug Hamlet.spl", once in debug mode run "state" at first pause. This will return the values of both Hamlet and Juliet. 
HINT: Esoteric Programming Language
HINT: Shakespeare
c. CTF{72.-15}

Dependencies: Hamlet.txt



2. (Cut it 0FF)
a. My friend challenged me to submit a txt file on the /submit_me webpage... but it only accepts PDFs. Could you help me out?
b. Use null byte expressions (%00) to submit a txt (file.pdf%00.txt) file. This will return the flag. Note that \x00 does not work, %00 is the one that is used.
HINT: Trick the page into thinking it's taking a pfd, but the file is a .txt. 
HINT: Null
c. CTF{1f_0nLY_1T_r34D_th3_NU11bYte}
*Website*



3. (Pixel Mosaic Mystery)
a. Someone tampered with my image! How should I get it back... HELP! All that was left with it... is a bunch of pixels? Now that I look at them, these pixels don't seem so random. 
b. Make a python script using cv2 which can perform bitwise addition and subtraction on images. Perform: placehold_key + key to get a partial_flag. You will know it is the partial_flag as when added to the key you get the partial_flag again. Then, perform partial_flag - flag to get the full flag. solution.py is an example of a script that can be used. 

The idea here is that in the middle of placehold_key you can vaguely make out some text. Once you strip all the surrounding pixels by adding it with the key, you get some extra pixels of the flag, but on a white font instead of the black font of the flag image. Once you subtract them (if you add the black font to the white you will once again pixelize the entire image) you will combine the pixels into the full flag. 
**Note** The scripts for flag and key generation are in the devs folder. You will find the partial_flag provided in devs folder as well. It is entirely possible that players come up with a different solution, there is a lot of possible combinations that would take a lot of time to test ;).  
HINT: Pixel Arithmetic
c. CTF{B1T5_4dd3D} 

Dependencies: key.png, flag.png, placehold_key.png
