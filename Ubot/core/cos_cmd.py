# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


import os
import logging
import asyncio

from pyrogram import filters, enums, Client
from pyrogram.handlers import MessageHandler
from pyrogram.errors.exceptions.bad_request_400 import MessageIdInvalid

from Ubot.core.db import *
from .func import rm_markdown
from Ubot import cmds, app
from config import CMD_HNDLR


class naya:
    def on_cmd(self, command: str):
        naya_filter = (filters.command(command, CMD_HNDLR) & filters.me)
        return self.decorate_naya(naya_filter)

    def decorate_naya(self, naya_filter):
        def decorator(func):
            async def x_wrapper(client, message):
                self.add_handler(x_wrapper, naya_filter)
                return await func(client, message)
            return x_wrapper
        return decorator

    def on_cf(self, custom_filters):
        def decorate_naya_cf(func):
            async def x_wrapper_cf(client, message):
                self.add_handler(x_wrapper_cf, custom_filters)
                return x_wrapper_cf
            return decorate_naya_cf

    def add_handler(self, x_wrapper, naya_filter):
        app.add_handler(MessageHandler(x_wrapper, filters=naya_filter))


def nay(command: list):
    async def wrapper(func):
        user_id = client.me.id
        cmd_handler = await get_cmd_handler(user_id)
        @Client.on_message(filters.command(command, cmd_handler) & filters.me)
        async def wrapped_func(client, message):
            await func(client, message)
        return wrapped_func

    return wrapper


n = naya()










