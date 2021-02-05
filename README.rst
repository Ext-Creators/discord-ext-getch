|Analyse Status|
|Build Status|
|Lint Status|

.. |Analyse Status| image:: https://github.com/Ext-Creators/discord-ext-getch/workflows/Analyze/badge.svg?event=push
   :target: https://github.com/Ext-Creators/discord-ext-getch/actions?query=workflow%3AAnalyze+event%3Apush


.. |Build Status| image:: https://github.com/Ext-Creators/discord-ext-getch/workflows/Build/badge.svg?event=push
   :target: https://github.com/Ext-Creators/discord-ext-getch/actions?query=workflow%3ABuild+event%3Apush


.. |Lint Status| image:: https://github.com/Ext-Creators/discord-ext-getch/workflows/Lint/badge.svg?event=push
   :target: https://github.com/Ext-Creators/discord-ext-getch/actions?query=workflow%3ALint+event%3Apush

----------

discord-ext-getch
-----------------

A discord.py extension that allows simplification of getting and fetching objects.


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
