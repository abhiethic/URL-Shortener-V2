from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """Hi there {} 👋😃

Welcome to [BrieflyUrl Bot](t.me/BrieflyUrl_Help) - Your Personal URL Shortener Bot. 🌐

Just send me a link, and I'll work my magic to shorten it for you. Plus, I'll keep track of your earnings! 💰💼

/base_site brieflyurl.com
/shortener_api - Connect API
/me - Your profile setting
/help - Advanced setting

New User ? Then just sign up on BrieflyUrl.com and Get Highest Upto 8$ CPM rate & 10% Refer Earning Lifetime.
"""

HELP_MESSAGE = """Hey there! My name is {firstname} and I'm a link convertor and shortener bot here to make your work easier and help you earn more 💰.

I have a ton of handy features to help you out, such as:

•  Setup Header - /header 
•  Setup Footer - /footer 
•  Setup Username - /username 
•  Setup Banner Img - /banner_image 
•  Setup Include Domains - /include_domain  
•  Setup Exclude Domains - /exclude_domain 

Useful commands:

•  /start Go Back to Home.
•  /shortener_api - Setup or Change API 
•  /me - Your profile Settings 

Contact Help Support - @BrieflyUrl_Help
"""

ABOUT_TEXT = """
**Bot Details:**

`🤖 Name:` ** {} ** 
`📝 Language:` [Python 3](https://www.python.org/)
`👨‍💻 Developer:` [Dev](t.me/BrieflyUrl)
`📢 Support:` [Support Talk](https://t.me/BrieflyUrl_Help)
"""

USER_ABOUT_MESSAGE = """
<b>Current Setting Of Your Bot is Here:</b>

•  🌐 Shortener website: BrieflyUrl.com
•  🔌 BrieflyUrl API: {shortener_api}
•  📎 Username: @{username}
•  📝 Header text:
{header_text}
•  📝 Footer text:
{footer_text}
•  🎨 Banner image: {banner_image}
•  ⚖️ Method: shortener
"""

SHORTENER_API_MESSAGE = """<b>How To Connect API ?</b>

• First Visit BrieflyUrl.com/member/tools/api
• Copy the API Token & Comeback to the Bot.
• Put /shortener_api [api] Replace With Your API
• Done! Now Bot is Successfully Connected With Your BrieflyUrl Account

To add or update your Shortener Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api 6LZq851sXofffPHugiKQq`

Current Shortener API: `{shortener_api}`"""
