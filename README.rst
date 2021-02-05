.. raw:: html

    <p align="center">
        <a href="https://github.com/Ext-Creators/discord-ext-getch/actions?query=workflow%3AAnalyze+event%3Apush">
            <img alt="Analyze Status"
                 src="https://github.com/Ext-Creators/discord-ext-getch/workflows/Analyze/badge.svg?event=push" />
        </a>

        <a href="https://github.com/Ext-Creators/discord-ext-getch/actions?query=workflow%3ABuild+event%3Apush">
            <img alt="Build Status"
                 src="https://github.com/Ext-Creators/discord-ext-getch/workflows/Build/badge.svg?event=push" />
        </a>

        <a href="https://github.com/Ext-Creators/discord-ext-getch/actions?query=workflow%3ALint+event%3Apush">
            <img alt="Lint Status"
                 src="https://github.com/Ext-Creators/discord-ext-getch/workflows/Lint/badge.svg?event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">discord-ext-getch</h1>
    <p align="center">A discord.py extension with additional and alternative features.</p>


Installation
------------

.. code-block:: sh

    python3 -m pip install --upgrade discord-ext-getch


Usage
-----

.. code-block:: py

    from discord.ext.getch import GetchMixin

    class Bot(commands.Bot, GetchMixin):
        ...

    bot = Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print(await bot.annel(123456789).essage(987654321).getch())
