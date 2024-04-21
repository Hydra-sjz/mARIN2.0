from telethon import Button, events

from Mikobot import tbot, ubot2

# Constants
MAX_BUTTONS = 5
CHANNEL_ID = -1001709507082
CHANNEL_USERNAME = "Anime_State"


@tbot.on(events.NewMessage(incoming=True, pattern=r"^[!/]search|^[!/]download ?(.*)"))
async def mangastash(event):
    try:
        # Extract the query from the message
        _, query = event.message.text.split(" ", 1)
    except ValueError:
        await event.reply(
            "𝗜𝗳 𝗬𝗼𝘂 𝘄𝗮𝗻𝘁 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗔𝗻𝘆 𝗔𝗻𝗶𝗺𝗲 𝗝𝘂𝘀𝘁 𝗨𝘀𝗲 /download {anime name} 𝗶𝘁 𝘄𝗶𝗹𝗹 𝗴𝗶𝘃𝗲 𝘆𝗼𝘂 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗟𝗶𝗻𝗸\n\nexample: `/download one piece`"
        )
        return

    # Get the user's name
    user = f"[{event.sender.first_name}](tg://user?id={event.sender_id})"

    # Search for messages in the specified channel
    btns = []
    async for message in ubot2.iter_messages(CHANNEL_ID, search=query):
        if len(btns) >= MAX_BUTTONS:
            break

        text = message.raw_text
        msg_id = message.id
        link = f"https://t.me/{CHANNEL_USERNAME}/{str(msg_id)}"
        btns.append([Button.url(text=f"{text[:20]}", url=link)])

    if not btns:
        await event.reply("Not found!")
    else:
        # Construct the reply message with buttons
        message_text = f"""👤 Hey {user},
 
🔎 Found some results.."""
        await event.reply(message_text, buttons=btns)
