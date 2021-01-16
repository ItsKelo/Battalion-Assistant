#  Battalion Assistant <img src="https://user-images.githubusercontent.com/32295800/104533495-69d28c80-560a-11eb-92a0-9023d0665d68.png" height="50"/>
Discord bot to help with LOA automation and tryout blacklist checking.
This bot runs on python, so in order to run it, you'll need to install the python coding language + the required packages.
This bot's uptime is dependant on what you host it on. You can host it on your local PC if you want, but uptime will be dependant on your internet + willingness to keep your PC on. Other hosting options (e.g. web services/cloud servers) are available.

## Features
### Automated LOA System
The battalion assistant discord bot is able to automate your google sheets LOA system. It will notify individuals in your discord when their LOA has expired. Freeing you poor officers of the need to check the LOA sheet everyday.

<img src="https://user-images.githubusercontent.com/32295800/104526129-99c56400-55f9-11eb-95bd-d7254270b8f2.png" height="100" />


### Mass Blacklist checking
Allows for a battalion doing tryouts to check multiple steam ids for possible blacklisted individuals at once. Great if you hate using alt+tab. 

<img src="https://user-images.githubusercontent.com/32295800/104526068-7d292c00-55f9-11eb-920f-3cfbf6464668.png" height="200" />

---
## Setup Tutorial
These steps should be done on the device which the bot will run on. 
**Disclaimer: You will need administrator on the server you want the bot to run on to allow it to join.**

### Prerequisities
1. Download the latest version of Python 3 (if you don't have it already). Can be downloaded from https://www.python.org/downloads/
2. Now that Python is downloaded, you will need to download the code for the bot and unzip it. This can be done by clicking "Download ZIP" under the "Code" dropdown Button. Place the folder containing the code in your desired directory.
<img src="https://user-images.githubusercontent.com/32295800/104519316-291a4980-55f1-11eb-826f-716031810f63.png" height="200" />
3. You'll need to use your terminal to install the required pip packages. Pip is a package manager built for the python language. It allows for pre-packaged libraries of code to be easily downloaded through your terminal. You can do this by going to the directory with the code, and running the terminal command `pip3 install -r requirements.txt`.

### Setting up the Discord Bot
1. Head to the Discord Developer Portal, found at https://discord.com/developers/applications, and sign in using your discord account.
2. Create a 'New Application' & fill out a name
3. Go to the 'Bot' subsection and click 'Add Bot'.
4. Fill out all the required fields such as the bot's name, profile picture etc.
5. **Disable the 'Public Bot' option. You DO NOT want this bot to be added to random servers.**
6. Invite the bot to your discord server by going to the 'OAuth2' tab, clicking 'bot' in the scopes area, giving the bot the needed permissions, and copying and going to the URL provided. (You need discord admin to have the bot join).
![OAuth2URL](https://user-images.githubusercontent.com/32295800/104520624-4fd97f80-55f3-11eb-86d1-2a43664f3cb2.png)
7. Lastly, copy the Token for the bot from the bot page and paste it into the `token.txt` in the resources folder of the project. Do not share this token with anyone!

### Google Developer Console.
1. Head to Google Developers Console and create a new project. Link: https://console.developers.google.com/project
2. In the project, in the search box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.
3. Head to the 'Credentials' section of the project by clicking the dropdown menu shown. <img src="https://user-images.githubusercontent.com/32295800/104520889-cbd3c780-55f3-11eb-8149-9b58bc3188da.png" height="200" />
4. Click “Create credentials > Service account”.
5. Fill out the form
6. Click on the email of the newly created service account and "Create a Key"
7. Select “JSON” and click “Create”
8. Rename this downloaded json file to `creds.json` and move it to the resources folder of the project.
9. Take the 'client_email' email and give it editor access to your google sheet. (It's the discord bot's google account email). 

### Setting up the bot to deal with your google sheet.
1. Open `settings.json` in the resources folder.
2. Fill in the settings accordingly:
- Prefix: Prefix of bot commands. This should be either one or two characters e.g. - or s!
- Admin Ids: This is the list of bot admin discord accounts. Do not give this permission to people unless you explicitly trust them. You should enter administrators discord ids separated by a comma.
- Privileged Roles: To operate the blacklist checking functionality of the bot, a security check has to be satified, this can be done using discord server roles. You should add the role ids of the roles that you want to be able to run the blacklist checking command. Once again each role id is separated by a comma.
- loa_sheet_url: URL of your google sheet.
- loa_channel: Channel ID of the channel where you want the bot to send notifications. You can set this in discord while the bot is live using the setLOAChannel command.
- end_date_column: The integer representation of the letter where the end dates/returning dates of an LOA are kept. A=1 B=2 C=3 etc.
- first_unformatted_row: This should be the number of the first row where data is actually stored. To clarify, skip all the headers and formatting. The first slot where an entry would go should be used. e.g. 3.
- names_column: The letter of the column containing the name of the individual on LOA
- end_dates_column: The letter of the column containing the end date of an LOA
- loa_sheetname: The worksheet name for the LOA data (preferably the form). This is not the entire sheet name, just the sub worksheet.
- blacklist_sheetname: The worksheet name for the Blacklist data.

Should end up looking similar to:

<img src="https://user-images.githubusercontent.com/32295800/104526327-ff195500-55f9-11eb-933f-496f8dfa660d.png" height="200" />


## Run the bot
Open your terminal, route to the directory containing the code for the bot. Once inside, run `python3 bot.py`. If you've followed the steps correctly, the bot should boot up and start checking your LOAs.

## Extended Features?
These are just two of the features that I've put into the battalion management bots I've created for two CWRP battalions. I'm open and able to create additional functionality for your bot. Discord tag: Kelo#5800.
