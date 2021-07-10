# Message Forwarding Telegram Bot
Forward messages to multiple Telegram groups easily | Hack-X-Tronics 2021 FCRIT

### The bot program is not well written due to the time constraints of Hack-X-Tronics event but the bot works well!
> Telegram token removed for security reasons
---
<img src="https://github.com/ashvnv/Message-Forwarding-Telegram-Bot/blob/main/pics/sending%20msg%20pics/photo_2021-07-09_21-22-53.jpg?raw=true" width=250>

Salent features:
- Now no need to manually send messages to different class groups!
- Using robust Telegram Bot Framework
- Send multiple texts,documents,photos
- Delete a sent message without any hassle

### How to use the bot
1. Send a message/ messages to the bot
2. Then click on the inline buttons given by the bot (I made this bot for my engineering college)
3. When you click on any button (say All 1st year), the message will be sent to that respective group/groups (for All 1st year it will be all the 1st year groups of all the departments)
4. You can then click on other buttons and forward the same message to other groups too.
5. Once done sending, click on 'Done' button and the message/messages will be cleared. Now you can send new set of messages which can be forwarded using the buttons.
6. Bot can even send images or other documents as well.
7. There is a 'delete send msg' button sent whenever a message is sent to the bot. Clicking on that button will delete that sent message from the database.


Send something to bot  |  Tell the bot where to forward   | Bot forwarded the message | Clearing the messages
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/ashvnv/Message-Forwarding-Telegram-Bot/blob/main/pics/sending%20msg%20pics/photo_2021-07-09_21-22-56.jpg?raw=true" width=220> | <img src="https://github.com/ashvnv/Message-Forwarding-Telegram-Bot/blob/main/pics/sending%20msg%20pics/photo_2021-07-09_21-23-00.jpg?raw=true" width=220> | <img src="https://github.com/ashvnv/Message-Forwarding-Telegram-Bot/blob/main/pics/sending%20msg%20pics/photo_2021-07-09_21-23-02.jpg?raw=true" width=220> | <img src="https://github.com/ashvnv/Message-Forwarding-Telegram-Bot/blob/main/pics/sending%20msg%20pics/photo_2021-07-09_21-23-04.jpg?raw=true" width=220>
</br>
Delete a sent message</br>Can be done for files as well!</br>
<img src="https://github.com/ashvnv/Message-Forwarding-Telegram-Bot/blob/main/pics/sending%20msg%20pics/photo_2021-07-09_21-35-12.jpg?raw=true" width=220>

---

## Database management
- The messages sent by admins are stored in 'Admin/<chat_id_of_admin>/' folder. '<chat_id_of_admin>/' folder stores admininfo.txt and chat.txt along with files (like .png, .pdf etc).
- chat.txt file stores the messages sent by that admin in JSON format. Messages are saved with message_id as 'key' and text sent as 'value'.
> {"1825": "hello"}
- All the messages are concatenated and stored. Once 'Done' command is sent all the chat.txt is cleared and all the files are deleted
- admininfo.txt stored Admin's information in JSON format
> {"id": 123456789, "is_bot": false, "first_name": "Ashwin", "username": "abcd", "language_code": "en"}

## group.txt
- This file contants the group chat ID stored in JSON format.
- 'Key' is the groups and 'value' is the group's chat ID. I have used Regex in the program for reading the values easily without using if-else, so according 'key' is named. Refer the regex added inside the program.
- To get group chat ID, add the bot to the group and send a command to the bot. The bot does not allow commands from a group so it replies with 'Not allowed!' followed by group's chat ID and Group's name
<img src="https://github.com/ashvnv/Message-Forwarding-Telegram-Bot/blob/main/pics/sending%20msg%20pics/photo_2021-07-09_22-13-02.jpg?raw=true" width=220>
