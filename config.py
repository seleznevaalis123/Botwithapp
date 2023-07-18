import os

bot_token = '6387861262:AAE7RZRfmEW5lVq79-U4teJIW0EqmD5ypcM'
provider_token = '1744374395:TEST:456f5c5404655212fde1'
admin_id = 1120855801
ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))


ip=localhhost
PGUSER=postgres
PGPASSWORD=F8K-sRH-hR9-ASS
DATABASE=test

POSTGRES_URI = f'posgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'