from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from theards_start import thread_login
from main import start

from config import TOKEN
from main import unauthorized, authorized, sub_list, ip_list

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

accs = []


def template(message):
    separated = message.split()
    for i in separated:
        accs.append(i)


@dp.message_handler()
async def echo_message(msg: types.Message):
    # print(0/0)
    accs.clear()
    template(msg.text)
    for accont in accs:
        authorized.clear()
        unauthorized.clear()
        acc = accont.split(':')
        sub_list.clear()
        ip_list.clear()
        await bot.send_message(msg.from_user.id, f'Привет, {msg.from_user.username.upper()}.\n Началось выполнение.')
        start(acc[0], acc[1], f'bob0', str(0))
        # print(thread_login(accs, 3, start))
        for account_mail in unauthorized:
            await bot.send_message(msg.from_user.id, f'Аккаунт, {account_mail}. Ошибка авторизации.')
        unauthorized.clear()
        for account_mail in authorized:
            await bot.send_message(msg.from_user.id, f'Аккаунт, {account_mail}. Выполнено успешно.\n Создано {len(ip_list)}')
        authorized.clear()
        ip_list.clear()
if __name__ == '__main__':
    executor.start_polling(dp)
