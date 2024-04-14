from characterai import aiocai, sendCode, authUser
import asyncio

async def main():
    email = input('YOUR EMAIL: ')

    code = sendCode(email)

    link = input('CODE IN MAIL: ')

    token = authUser(link, email)

    print(token)

    info = await aiocai.get_me(token=token)

    print(info)

asyncio.run(main())
