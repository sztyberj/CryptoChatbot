from coinapi_rest_v1.restapi import CoinAPIv1
import pandas as pd
import datetime
import ChatbotServer.Database.db_operations as op

top_crypto = ['BTC', 'ETH', 'BNB', 'ADA', 'SOL', 'XRP', 'LUNA', 'DOT', 'AVAX', 'DOGE', 'SHIB', 'MATIC' ]

def money_format(amount):
    currency = "{:,.2f}".format(amount)
    return currency

def download_prices():
    test_key = '1DAF11D7-FB1A-442E-9F5D-1357BF1A22D1'

    api = CoinAPIv1(test_key)
    exchanges = api.metadata_list_exchanges()

    assets = api.metadata_list_assets()

    cp = open('../Files/current_prices.txt', 'w')
    for asset in assets:
        if asset['type_is_crypto'] == 1 and asset['asset_id'] in top_crypto:
            data = [(asset['name'], asset['asset_id'], money_format(asset['price_usd']), asset['data_quote_end'][:10])]
            op.insert_prices('Cryptocurrency', data)
            cp.write((asset['name'] + f"({asset['asset_id']}):  {money_format(asset['price_usd'])} USD \n"))


    cp.close()


if op.select_newest_date() != datetime.date.today():
    download_prices()





