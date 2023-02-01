# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from FallenMusic import SUDOERS, app


@app.on_message(filters.command(["مطور"]) & filters.user(OWNER_ID))
async def sudoadd(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "» اعمل ريب عليه او اكتب الايدي او يوزه جنب الامر."
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) in SUDOERS:
            return await message.reply_text(f"» {user.mention} هو بالفعل مطور ف البوت.")
        try:
            SUDOERS.add(int(user.id))
            await message.reply_text(f"تم {user.mention} اضافته مطور.")
        except:
            return await message.reply_text("انا فشلت في دي كمان.")

    if message.reply_to_message.from_user.id in SUDOERS:
        return await message.reply_text(
            f"» {message.reply_to_message.from_user.mention} ɪs ᴀʟʀᴇᴀᴅʏ ᴀ sᴜᴅᴏ ᴜsᴇʀ."
        )
    try:
        SUDOERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            f"ᴀᴅᴅᴇᴅ {message.reply_to_message.from_user.mention} ɪɴ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ."
        )
    except:
        return await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴅᴅ ᴜsᴇʀ ɪɴ sᴜᴅᴏᴇʀs.")


@app.on_message(filters.command(["تك", "تنزيل مطور"]) & filters.user(OWNER_ID))
async def sudodel(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(
                "» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ ɪᴅ."
            )
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if int(user.id) not in SUDOERS:
            return await message.reply_text(
                f"» {user.mention} ɪs ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ."
            )
        try:
            SUDOERS.remove(int(user.id))
            return await message.reply_text(
                f"» ʀᴇᴍᴏᴠᴇᴅ {user.mention} ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ."
            )
        except:
            return await message.reply_text(f"ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴜsᴇʀ ғʀᴏᴍ sᴜᴅᴏᴇʀs.")
    else:
        user_id = message.reply_to_message.from_user.id
        if int(user_id) not in SUDOERS:
            return await message.reply_text(
                f"» {message.reply_to_message.from_user.mention} ɪs ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ."
            )
        try:
            SUDOERS.remove(int(user_id))
            return await message.reply_text(
                f"» ʀᴇᴍᴏᴠᴇᴅ {message.reply_to_message.from_user.mention} ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ."
            )
        except:
            return await message.reply_text(f"ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴜsᴇʀ ғʀᴏᴍ sᴜᴅᴏᴇʀs.")


@app.on_message(filters.command(["المطورين", "نادي المطورين", "المطوين"]))
async def sudoers_list(_, message: Message):
    hehe = await message.reply_text("» ɢᴇᴛᴛɪɴɢ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ...")
    text = "<u>🥀 **ᴏᴡɴᴇʀ :**</u>\n"
    count = 0
    user = await app.get_users(OWNER_ID)
    user = user.first_name if not user.mention else user.mention
    count += 1
    text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n<u>✨ **sᴜᴅᴏᴇʀs :**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("» ɴᴏ sᴜᴅᴏ ᴜsᴇʀs ғᴏᴜɴᴅ.")
    else:
        await hehe.edit_text(text)
