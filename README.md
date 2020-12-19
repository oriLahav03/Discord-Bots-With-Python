# Here some discord bots and commands written with discord.py

1. ___CallOfDutyMobileBot.
     **The bot handle the verify and staff tags in my server.
    - Notification when bot online => on_ready().
    - Handle every message sent => on_message(message).
    - Send embed message with reactions => reaction(ctx).
    - Send member a private message => dm_join(member: discord.Member = None) / dm_leave(member: discord.Member = None).
    - Do something when reaction pressed on message => on_raw_reaction_add(payload).
    - Do something when reaction removeed from message => on_raw_reaction_remove(payload).
2. ___CommandsExamples.
    **There is some code examples you can use.
    - Notification when bot online => on_ready().
    - Tag user (spam) only spespecific roles have access => tag(ctx, user: discord.Member).
    - Send member a private message with given content => dm(ctx, member: discord.Member = None, *, message).
    - Spam user in private message => spam(ctx, member: discord.Member = None, *, message).
    - Delete given amount of messages => clear(ctx, amount=1).
3. ___CounterBot.
    **This bot use for counter rooms, when user send message its will check if its a valid number in the raw
    **of the previous numbers and send the nex number.
    - Notification when bot online => on_ready().
    - Handle every message sent => on_message(message).
