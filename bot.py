import interactions


import os
from dotenv import load_dotenv
from interactions import Option

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
bot = interactions.Client(token=TOKEN)


@bot.command(
    name="say_something",
    description="say something!",
    scope=1152789940040642560,
    options = [
        interactions.Option(
            name="role",
            description="Uhh test role, will be defaulted to countbanned role soon enough",
            type=interactions.OptionType.ROLE,
            required=True,
        ),
        interactions.Option(
            name="user",
            description="the person you wanna BAN >:^)",
            required=True,
            type=interactions.OptionType.USER
        )
    ],
)
async def my_first_command(ctx: interactions.CommandContext, role: interactions.api.Role, user: interactions.api.User):
    # await interactions.Guild.add_member_role(self=interactions.Guild,role=role, member_id=user.id, reason="countbanned")
    await user.add_role(role.id, ctx.guild_id)
    await ctx.send("done")

   


bot.start()