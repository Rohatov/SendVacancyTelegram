from telethon import TelegramClient, events
import asyncio, os
from dotenv import load_dotenv

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
channel_username = 'UzDeveloperJobs'

client = TelegramClient('session_name', api_id, api_hash)
my_skills = ['python', 'django', 'drf', 'django rest framework']

@client.on(events.NewMessage(chats=channel_username))
async def handler(event):
    if event.message.text.startswith('**Xodim kerak:**'):
        tech_line = event.message.text.split('\n')[3]
        tech_text = tech_line.split('**')[1:-1]
        tech_text = tech_text[0].split(',')
        technology = set(t.strip().lower() for t in tech_text)
        found = False

        for skill in my_skills:
            if skill in set(technology):
                found = True
                break

        if found:
            await client.send_message('Rohatov1', event.message.text)
            print("Vakansiya muvaffaqiyatli yuborildi!", event.message.id)
        
client.start()
client.run_until_disconnected()

