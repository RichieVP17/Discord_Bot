import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('Head!')
    if num == 2:
        await ctx.send('Tail!')

