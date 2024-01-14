import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Add this line to enable message content intent

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command(name='embed')
async def send_embed(ctx):
    # Ask in which channel to send the embed
    await ctx.send("In which channel do you want to send the embed? Mention the channel or type its name.")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Wait for a response from the same user and channel
        response = await bot.wait_for('message', check=check, timeout=30)

        # Try to get the channel from the mentioned channel or by name
        channel = response.channel_mentions[0] if response.channel_mentions else discord.utils.get(ctx.guild.channels, name=response.content)

        if channel:
            # Ask for the color of the embed
            await ctx.send("What color should be set to the embed? Provide a hex color code (e.g., #8B1BB5).")

            # Wait for a response for the color
            color_response = await bot.wait_for('message', check=check, timeout=30)
            color = discord.Color(int(color_response.content, 16))  # Convert hex to decimal

            # Ask for the title of the embed
            await ctx.send("What should be the title of the embed?")

            # Wait for a response for the title
            title_response = await bot.wait_for('message', check=check, timeout=30)
            title = title_response.content

            # Ask for the message of the embed
            await ctx.send("What should be the message of the embed?")

            # Wait for a response for the message
            message_response = await bot.wait_for('message', check=check, timeout=30)
            message = message_response.content

            # Ask for the thumbnail URL
            await ctx.send("What should be the thumbnail URL of the embed?")

            # Wait for a response for the thumbnail URL
            thumbnail_response = await bot.wait_for('message', check=check, timeout=30)
            thumbnail_url = thumbnail_response.content

            # Ask for the image URL at the bottom of the embed
            await ctx.send("What should be the image URL at the bottom of the embed?")

            # Wait for a response for the image URL
            image_response = await bot.wait_for('message', check=check, timeout=30)
            image_url = image_response.content

            # Create an embed with the provided title, message, color, thumbnail, and image
            embed = discord.Embed(
                title=title,
                description=message,
                color=color
            )

            # Set the thumbnail
            embed.set_thumbnail(url=thumbnail_url)

            # Add an image at the bottom of the embed
            embed.set_image(url=image_url)

            # Set the footer
            embed.set_footer(text='Embed Footer')

            # Send the embed to the specified channel
            await channel.send(embed=embed)

        else:
            await ctx.send("Channel not found. Embed creation canceled.")

    except TimeoutError:
        await ctx.send("Embed creation timed out. Please run the command again.")



bot.run('MTE5NTM0NDM5ODMxODMxMzU0Mg.Gd-kg3.1rso1h8k1s9M42QWpcfQdo69XfOJSBER97JNk0')