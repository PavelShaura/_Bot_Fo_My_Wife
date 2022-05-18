import asyncio

import python_weather
import telebot

bot = telebot.TeleBot("5269200934:AAFTpKdXVFmqlL12IsfK2ZAVuHi65KCxp-k")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    async def getweather():

        global answer

        client = python_weather.Client(format=python_weather.METRIC)
        '''Определяем город'''

        weather = await client.find("Tuapse")

        answer = f'Температура воздуха в \nпгт. НОВОМИХАЙЛОВСКОМ на данный момент...\n   \n'
        answer += f'   {weather.current.temperature}°C         ⬅\n\n'

        if int(weather.current.temperature) <= 15:
            answer += f'Еще не лето, в шортах будет холодно...😩\n\n'
        elif int(weather.current.temperature) > 25:
            answer += f'Фух...Ужасная жара, никуда не идите😤\n\n'
        else:
            answer += f'Класс!!! Отличный денек погулять с Анютой 👶\n\n'

        answer += f'💚 ПОГОДА НА БЛИЖАЙШИЕ 5 ДНЕЙ: \n\n'

        for forecast in weather.forecasts:
            answer += f'{forecast.temperature} °C   '
            mood = forecast.sky_text
            for i in mood:
                if mood == "Clear":
                    answer += f'Солнечно    🌞\n\n'
                    break
                elif mood == "Cloudy":
                    answer += f'    🌤\n\n'
                    break
                elif mood == "Partly Sunny":
                    answer += f'    🌥\n\n'
                    break
                elif mood == "Mostly Cloudy":
                    answer += f'     ☁\n\n'
                    break
                elif mood == "Mostly Sunny":
                    answer += f'     🌥\n\n'
                    break
                elif mood == "Light Rain":
                    answer += f'     ⛈\n\n'
                    break
                elif mood == "Rain":
                    answer += f'    ⛈\n\n'
                    break
                elif mood == "Havy Rain":
                    answer += f'     ⛈\n\n'
                    break
                elif mood == "Partly Cloudy":
                    answer += f'     🌤\n\n'
                    break

        await client.close()

        bot.send_message(message.chat.id, answer)

    if __name__ == "__main__":
        loop = asyncio.new_event_loop()
        loop.run_until_complete(getweather())


bot.infinity_polling()
