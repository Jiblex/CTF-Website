# CTF Website

## Overview

This is some work intended for the Northeatern CTF Club, where some of these challenges have already been used and others await their time (whenever this is being read this may not be the case however). This repo contains a website, as per its name, which contains mutiple web challenges and can be used as a template to create challenges in the future. Other challenges made in this batch that were not challenges that made their way onto the website, will be included as well. They will live in the _system_ directory. 

When working on the website, all of the required packages and libraries lived in a venv, however the directory containing all of these files grew rather large, and due to trouble uploading it all onto github I decided to omit the venv. All required packages and libraries have been placed in the _requirements.txt_ file (ctf_web/requirements.txt), this way no unnecessary installations need be made. The requirements file can be used with pip (_pip install -r requirements.txt_), or may also be ran in a Dockerfile. An example Dockerfile has been provided (ctf_web/Dockerfile). 

Below I will paste the complete README.md file I used for documentation throughout the challenge creation process. It contains every challenge, along with its description, solution and flag. It also includes some commands which can be used at the top to run the website, however if downloading, these commands may not work without setup.

If _flask run_ does not work, you can alternatively run _python run.py_, however to setup flask run simply use the command _export FLASK_APP=run.py_. Now _flask run_ should work. 

Libmagic may also cause some problems, to fix this issue refer to <a href="https://hatchjs.com/failed-to-find-libmagic-check-your-installation/"> this page  </a> to properly install it, as it is not a pip installatoin. 

For making a virtualenv, refer to documentation. You do not need one in order to run the website. 


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

<br>
<br>
<br>
CHALLENGES:

<br>
<br>
<br>

**SUPER EASY**

<br>
1. (MISC) In Plain Sight <br>
a. You will find the flag on the home page (/home). It's right there, can't you see it?<br>
b. The flag is hidden in the home page. Search the HTML code, the flag is in the id field of an h1 tag.<br>
c. CTF{1m_riGHt_hEre;)}<br>
*Website*<br>



2. (Routing) tErmINAt0r<br>
a. My search engine crawler gave me a weird looking URL for the CTF website... I wonder why it looks like that?<br>
b. Navigate to the robots.txt file. The route is simply "/robots.txt". <br>
HINT: "robots"
c. CTF{sh0Wing_mE_1s_AlLowed}<br>
*Website*<br>



3. (System) Kernel Quest<br>
a. What's the kernel release of this machine?<br>
b. Use command $uname -r.<br>
HINT: uname<br>
*NOTE* should probs check to make sure, I've had 2 dif answers when running container from host and virtual machine. <br>
c. CTF{6.6.16-linuxkit}<br>
*Docker*<br>



4. (System) Crunch Time<br>
a. What is the command set to run every 15 minutes on this machine as soon as it boots up (use an _ where there is a spcace when you submit the flag)? <br>
b. Use command "$crontab -e". You will see that the command "$run-parts /etc/periodic/15min". <br>
HINT: crontab<br>
c. CTF{run-parts_/etc/periodic/15min}<br>
*Docker*<br>



5. (MISC) Unravelling the Layers <br>
a. I can't read the file! Decompress it for me. <br>
b. Use "$tar -xvf flag.txt.gz.tgz.tgz" twice to get rid of the two .tgz, then "$gzip -d flag.txt.gz" to decompress the file to flag.txt. The flag is now readable. <br>
c. CTF{d3comPe55ion_KING}<br>
Dependencies: flag.txt.gz.tgz.tgz<br>




6. (MISC) C01D_sT0R4Ge <br>
a. Head over to the about page (/about). The flag is on the server's storage. <br>
b. Use the inspector tool, go to storage, local storage. The flag is right there. <br>
c. CTF{fR0z3N_D4t4_1s_tH3_b3st}<br>
*Website*<br>



7. (Routing) URLpass<br>
a. Go to the URLpass challenge (/URLpass/param=wKD7yf0). The flag is hidden on a page who's URL parameter is a famous wordlist. <br>
b. The worldist is rockyou. The flag is hidden on the link '/URLpass/param=rockyou'.<br>
c. CTF{c0RreCT_p4R4m_1Nt3rC3PTed}<br>
*Website*
<br>


8. (MISC) H0tD0g<br>
a. Click on the right hot dog. Even if all is 404, check the URL.<br>
b. Click the "Hot Dogs" part of the essay title. This will lead you to a 404 error page. Flag is in the URL. <br>
c. CTF{tH3_secreT_HOT_D0G}<br>
*Website*
<br>


**EASY**
<br><br>


1. (SQL Injection) In the Data<br>
a. I forgot my username, but I made a bet that I know my username and my friend doesn't and as usual I forgot it... my friend said the login page (/login) had some sort of weakness and that he got it from there. I can't lose this bet!<br>
b. The flag is in the database. SQL injection: "SELECT * FROM users". <br>
HINT: The flag is the users table. <br>
c. CTF{iDk_mY_usrName}<br>
*Website*<br>



2. (Crypto) $YouxWill_Know&My#Feelings<br>
a. I have a message. $2b$12$pGN/fxQLP4n6UkhYF9nccuo7pl4HX0scaaM1V.FDCfAjQ3YuofaMy<br>
b. The hashing algorithm is bcrypt blowfish. Use hashcat (or any other password cracking tools) to decrypt via dictionary attack. Command I used: <br>
$hashcat -m 3200 -a 0 hash.txt wordlist.txt<br>
This will give back the message, make it CTF format by putting in into CTF{}.<br>
***NOTE*** I made sure to use a password that can be found earlier (so it doesn't take a week) in rockyou.txt, as this is probably the wordlist most will try using. <br>
HINT: Use rockyou (josuamarcelc)... and remember to be patient.<br>
c. CTF{friendsforever}<br>
Dependencies: feelings.txt<br>



3. (OSINT) ExpCert<br>
a. Find out what the expiration date of the https://www.northeastern.edu/ server certificate is. Submit the flag in the form CTF{Month Day Hour:Minute:Second Year TimeZone}. <br>
b. Mutiple ways to do this. I did "$curl -v https://www.northeastern.edu/". The expiration date can be found in the "Server certificate" towards the top of the output, right under the TLS handshake. <br>
c. CTF{May 17 23:59:59 2024 GMT}<br>



4. (Routing) Phantom Pathfind<br>
a. The flag is hidden on a secret route. Go to /phantom for some help. Gobust some invisible routes! <br>
b. Use gobuster along with the provided wordlist. "$gobuster dir -u URL/IP -w wordlist.txt".f This gives list of found routes. The flag is on the /rockyou route. <br>
HINT: gobuster<br>
c. CTF{r0UT3_bU5T3r5}<br>
*Website*<br>



5. (Recon) Rdar <br>
a. What is the version of OpenSSH running on scanme.nmap.org?<br>
b. Use command "$nmap -sV scanme.nmap.org", this will give OpenSSH version. <br>
***NOTE*** Should make sure that the version hasn't changed before running challenge. <br>
c. CTF{6.6.1p1}<br>



6. (MISC) Packet Prowl <br>
a. What is the MAC address of the Apple device?<br>
b. Apple device has IP 192.168.1.151, look for its MAC address in the Ethernet II section after clicking on the packet. <br>
c. CTF{f0:2f:4b:09:7e:3c}<br>
Dependencies: crash.pcap<br>



**MEDIUM**
<br>

1. (Reverse Engineering) fork<br>
a. Woah I think I might have dropped my knife on the wrong button when encoding the flag!<br>
b. Need to use spoon decoder to in order to get the flag. <br>
HINT: spoon<br>
c. CTF{3s0T3r1c_l4ng5_3XiST}<br>
Dependencies: 01.txt<br>



2. (API) Access Abyss<br>
a. Stare into the abyss and the abyss will not send you a post. Anyway I need to login through the /abyss page, but there's no place for me to input my credentials... what to do?<br>
b. Use any technique to find the 'usrname' and 'passwd' that are hidden in the black text (ctrl+f, grep...). Then use a curl POST request on the /abyss page with these credentials. This will return the flag in your terminal. <br>
Username: 'FatherChristmas', Password:'d1dUctrlF?'. <br>
$curl -X POST -F "username=FatherChristmas" -F "password=d1dUctrlF" http://127.0.0.1:5000/abyss<br>
HINT: Send a POST request<br>
HINT: cURL<br>
c. CTF{the4Byss_sT4r3es_RIGhtB4ck}<br>
*Website*<br>



3. (API) Agent 007: User Agent Undercover<br>
a. Go the challenge tab or navigate to "/user_agent". Use cURL.<br>
b. Use "$curl -X POST http://127.0.0.1:5000/user_agent", you will be told you have the incorrect user agent and to go to /user_agent/help. Navigate to the page. The injection needs to look similar to this: /user_agent/help?injection={{secret_ua}}<br>
Using secret User-Agent agH8dGG7, send curl request and get the flag:<br>
"$curl -A SECRET http://127.0.0.1:5000/user_agent" or "$curl -H "User-Agent: SECRET" http://127.0.0.1:5000/user_agent".<br>
c. CTF{B3rRy_5TR4Wberry}<br>
*Website*<br>



4. (Forensics) Seen Through The Sea<br>
a. You can only see the flag in the panes of sea and blood. <br>
b. Using any stenography (I used StegOnline to make and solve the challenge), look at the image in bit planes 1 and 2 in the colors red and blue respectively. Put the two parts of the flag together. Looking at the text you will find that it ends in an = sign, which is how base32 and base64 encodings end. Decode the string using base32 results in the flag.<br>
c. CTF{500n_maY_tH3_w311erman_cOME}<br>
Dependencies: flag.png<br>



**HARD**
<br>

1. (Reverse Engineering) To Code or Not To Code<br>
a. What is Hamlet? What is Juliet? Give the flag in the form CTF{Hamlet.Juliet}. Here's a free clue: 10111511111610111410599<br>
b. The free clue is the ASCII representation of "esoteric". <br>
Change Hamlet.txt to Hamlet.spl. This makes it a Shakespeare Programming Language file (an esoteric programming language). Note that you must install shakespearelang via pip. Then run "$shakespeare debug Hamlet.spl", once in debug mode run "state" at first pause. This will return the values of both Hamlet and Juliet. <br>
HINT: Esoteric Programming Language<br>
HINT: Shakespeare<br>
c. CTF{72.-15}<br>
Dependencies: Hamlet.txt<br>



2. (Cut it 0FF)<br>
a. My friend challenged me to submit a txt file on the /submit_me webpage... but it only accepts PDFs. Could you help me out?<br>
b. Use null byte expressions (%00) to submit a txt (file.pdf%00.txt) file. This will return the flag. Note that \x00 does not work, %00 is the one that is used.<br>
HINT: Trick the page into thinking it's taking a pfd, but the file is a .txt. <br>
HINT: Null<br>
c. CTF{1f_0nLY_1T_r34D_th3_NU11bYte}<br>
*Website*<br>



4. (Pixel Mosaic Mystery)<br>
a. Someone tampered with my image! How should I get it back... HELP! All that was left with it... is a bunch of pixels? Now that I look at them, these pixels don't seem so random. <br>
b. Make a python script using cv2 which can perform bitwise addition and subtraction on images. Perform: placehold_key + key to get a partial_flag. You will know it is the partial_flag as when added to the key you get the partial_flag again. Then, perform partial_flag - flag to get the full flag. solution.py is an example of a script that can be used. <br>
The idea here is that in the middle of placehold_key you can vaguely make out some text. Once you strip all the surrounding pixels by adding it with the key, you get some extra pixels of the flag, but on a white font instead of the black font of the flag image. Once you subtract them (if you add the black font to the white you will once again pixelize the entire image) you will combine the pixels into the full flag. <br>
**Note** The scripts for flag and key generation are in the devs folder. You will find the partial_flag provided in devs folder as well. It is entirely possible that players come up with a different solution, there is a lot of possible combinations that would take a lot of time to test ;).  <br>
HINT: Pixel Arithmetic<br>
c. CTF{B1T5_4dd3D} <br>
Dependencies: key.png, flag.png, placehold_key.png<br>
