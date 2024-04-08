from CAFESFacebook.post_photo import post_photo
from ImagesService.indicadores_bancomx import get_indicadores_bamx
from constants import PAGE_ID, PAGE_TOKEN



def post_indicadores_bancomx():
    content = get_indicadores_bamx()
    photo_id = post_photo(PAGE_ID, PAGE_TOKEN, content, 'Repaso financiero semanal')
