import schedule
import time
from tasks import get_indicadores_bamx
from ImagesService.indicadores_bancomx import get_services

print('Response from the server: ', get_services())

schedule.every().friday.at("15:00").do(get_indicadores_bamx)

while True:
    schedule.run_pending()
    time.sleep(1)
