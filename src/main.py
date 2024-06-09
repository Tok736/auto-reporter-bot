import asyncio

from aiogram import Dispatcher

from bot import bot

from users.router import router as users_router


async def main() -> None:
    """ Register all routes and start polling """
    
    dp = Dispatcher()

    dp.include_routers(
        users_router
    )

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

