import schedule
from tasks import get_indicadores_bamx

schedule.every().friday.at("15:00").do(get_indicadores_bamx)

schedule.run_pending()
