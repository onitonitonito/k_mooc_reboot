"""
# WebHook Setup page using Flask App
# Given Token: {TELEGRAM_TOKEN_HERE}
# A very simple Flask Hello World app for you to get started with...
"""
import telepot
import urllib3

from nltk.chat.eliza import eliza_chatbot
from flask import (Flask,
                    request,
                    render_template,
                    redirect,
                    url_for,
                    session,
                    send_from_directory)


proxy_url = "http://proxy.server:3128"

telepot.api._pools = {
    'default': urllib3.ProxyManager(
        proxy_url=proxy_url,
        num_pools=3,
        maxsize=10,
        retries=False,
        timeout=30
        ),
}

telepot.api._onetime_pool_spec = (
    urllib3.ProxyManager,
    dict(
        proxy_url=proxy_url,
        num_pools=1,
        maxsize=1,
        retries=False,
        timeout=30,
        )
    )
