# Here some discord bots and commands written with discord.py

1. CallOfDutyMobileBot.
    - notification when bot online => on_ready().
    - handle every message sent => on_message(message).
    - send embed message with reactions => reaction(ctx).
    - send member a private message => dm_join(member: discord.Member = None) / dm_leave(member: discord.Member = None).
    - do something when reaction pressed on message => on_raw_reaction_add(payload).
    - do something when reaction removeed from message => on_raw_reaction_remove(payload).
2. commandsExamples.
    - notification when bot online => on_ready().
    - tag user (spam) only spespecific roles have access => tag(ctx, user: discord.Member).
    - send member a private message with given content => dm(ctx, member: discord.Member = None, *, message).
    - spam user in private message => spam(ctx, member: discord.Member = None, *, message).
    - delete given amount of messages => clear(ctx, amount=1).
3. CounterBot is a bot for fun, you can count with him how long you want :)
