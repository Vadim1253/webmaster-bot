from yandex_webmaster import YandexWebmaster
from datetime import datetime, timedelta
import telebot
import sqlite3
from telebot import types
from telebot.types import ReplyKeyboardRemove
from time import sleep
import threading
# from time import sleep

bot=telebot.TeleBot("5958086903:AAE1Th8DsgCthbxwkbaaDoOvsZkn8fxKzFg")
client = YandexWebmaster('')
mass=""

@bot.message_handler(commands=['stop_alko_com_diagnostic'])
def res(message):
    global mass
    # d = datetime.today()
    # d=d.strftime('%H:%M')
    i=1
    debagstat=0
    while 1:
        sleep(55)
        # now = datetime.now()
        # now = str(now.time())
        # if "12:56" in now:
        if str(datetime.now().strftime("%H:%M")) == "08:33" or str(datetime.now().strftime("%H:%M")) == "08:34":
            
    # now = datetime.now()
    # now = now.time()
            # print(str(now))
            result = client.diagnostic_site(host_id='https:stop-alko.com:443')
            result=result['problems']
            # FATAL
            CONNECT_FAILEd=f'Роботы не смогли посетить сайт. Ошибка может быть связана, например, с настройками сервера или высокой нагрузкой. (CONNECT_FAILED). Тип ошибки: ({str(result["CONNECT_FAILED"]["severity"])})'
            DISALLOWED_IN_ROBOTs=f'Сайт закрыт от индексирования в файле robots.txt. (DISALLOWED_IN_ROBOTS). Тип ошибки: ({str(result["DISALLOWED_IN_ROBOTS"]["severity"])})'
            DNS_ERROr=f'Не удалось подключиться к серверу из-за ошибки DNS. (DNS_ERROR). Тип ошибки: ({str(result["DNS_ERROR"]["severity"])})'
            MAIN_PAGE_ERROr=f'Главная страница сайта возвращает ошибку. (MAIN_PAGE_ERROR). Тип ошибки: ({str(result["MAIN_PAGE_ERROR"]["severity"])})'
            THREATs=f'Обнаружены нарушения или проблемы с безопасностью. (THREATS). Тип ошибки: ({str(result["THREATS"]["severity"])})'
            TURBO_FEED_BAn=f'Источник Турбо-страниц не соответствует требованиям: контент Турбо-страниц должен совпадать с контентом оригинальных страниц. Турбо-страницы пропадут из поиска в течение трех дней. Вместо них будут отображаться оригинальные версии страниц.. Тип ошибки: ({str(result["TURBO_FEED_BAN"]["severity"])}).\nПодробнее: https://yandex.ru/dev/turbo/doc/rss/requirements.html'
            # CRITICAL
            INSIGNIFICANT_CGI_PARAMETEr=f'На вашем сайте некоторые страницы с GET-параметрами в URL дублируют содержимое других страниц (без GET-параметров). (INSIGNIFICANT_CGI_PARAMETER). Тип ошибки: ({str(result["INSIGNIFICANT_CGI_PARAMETER"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/robot-workings/double.html'
            SLOW_AVG_RESPONSE_TIMe=f'Долгий ответ сервера. (SLOW_AVG_RESPONSE_TIME). Тип ошибки: ({str(result["SLOW_AVG_RESPONSE_TIME"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/diagnosis/critical.html#diagnostics-critical__request'
            SSL_CERTIFICATE_ERROr=f'Некорректная настройка SSL-сертификата. (SSL_CERTIFICATE_ERROR). Тип ошибки: ({str(result["SSL_CERTIFICATE_ERROR"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/diagnosis/critical.html#diagnostics-critical__ssl'
            TURBO_HOST_BAn=f'Турбо-страницы сайта не соответствуют требованиям: контент Турбо-страниц должен совпадать с контентом оригинальных страниц. (TURBO_HOST_BAN). Тип ошибки: ({str(result["TURBO_HOST_BAN"]["severity"])}). Подробнее: https://yandex.ru/dev/turbo/doc/rss/requirements.html'
            # TURBO_INVALID_CART_URl=f'Переход с Турбо-страниц в корзину отключен, так как на сайте в настройках добавления товара в корзину обнаружена ошибка. (TURBO_INVALID_CART_URL). Тип ошибки: ({str(result["TURBO_INVALID_CART_URL"]["severity"])})'
            TURBO_RSS_ERROr=f'В вашем RSS-канале, используемом для формирования Турбо-страниц, обнаружены ошибки, которые мешают обновлению. Для формирования Турбо-страниц будет использоваться предыдущая версия канала. (TURBO_RSS_ERROR). Тип ошибки: ({str(result["TURBO_RSS_ERROR"]["severity"])})'
            TURBO_URL_ERRORs=f'Турбо-страницы вашего сайта не попали в поиск. Чтобы страницы смогли участвовать в поиске, исправьте ошибки. Подробно см. Часто встречающиеся ошибки. (TURBO_URL_ERRORS). Тип ошибки: ({str(result["TURBO_URL_ERRORS"]["severity"])}). Подробнее: https://yandex.ru/dev/turbo/doc/rss/requirements.html#turbo-mistakes'
            TURBO_YML_ERROr=f'В вашем YML-файле, используемом для формирования Турбо-страниц, обнаружены ошибки, которые мешают обновлению. Для формирования Турбо-страниц будет использоваться предыдущая версия файла. (TURBO_YML_ERROR). Тип ошибки: ({str(result["TURBO_YML_ERROR"]["severity"])})'
            URL_ALERT_4Xx=f'Некоторые страницы сайта отвечают роботу HTTP-кодом 4xx в течение часа. Подробно см. Коды 4xx (ошибка клиента). (URL_ALERT_4XX). Тип ошибки: ({str(result["URL_ALERT_4XX"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/error-dictionary/http-codes.html#client-4xx'
            URL_ALERT_5Xx=f'Некоторые страницы сайта отвечают роботу HTTP-кодом 5xx в течение часа. Подробно см. Коды 5xx (ошибка сервера). (URL_ALERT_5XX). Тип ошибки: ({str(result["URL_ALERT_5XX"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/error-dictionary/http-codes.html#server-5xx'
            # POSSIBLE_PROBLEM
            DISALLOWED_URLS_ALERt=f'Найдены полезные страницы, закрытые от индексирования. (DISALLOWED_URLS_ALERT). Тип ошибки: ({str(result["DISALLOWED_URLS_ALERT"]["severity"])})'
            DOCUMENTS_MISSING_DESCRIPTIOn=f'На многих страницах отсутствует метатег Description. (DOCUMENTS_MISSING_DESCRIPTION). Тип ошибки: ({str(result["DOCUMENTS_MISSING_DESCRIPTION"]["severity"])})'
            DOCUMENTS_MISSING_TITLe=f'На многих страницах отсутствует элемент title. (DOCUMENTS_MISSING_TITLE). Тип ошибки: ({str(result["DOCUMENTS_MISSING_TITLE"]["severity"])})'
            DUPLICATE_CONTENT_ATTRs=f'На некоторых страницах вашего сайта указаны одинаковые title и Description. (DUPLICATE_CONTENT_ATTRS). Тип ошибки: ({str(result["DUPLICATE_CONTENT_ATTRS"]["severity"])})'
            DUPLICATE_PAGEs=f'Некоторые страницы вашего сайта содержат одинаковый контент. (DUPLICATE_PAGES). Тип ошибки: ({str(result["DUPLICATE_PAGES"]["severity"])})'
            ERROR_IN_ROBOTS_TXt=f'Ошибки в файле robots.txt. (ERROR_IN_ROBOTS_TXT). Тип ошибки: ({str(result["ERROR_IN_ROBOTS_TXT"]["severity"])})'
            ERRORS_IN_SITEMAPs=f'Обнаружены ошибки в файлах Sitemap. (ERRORS_IN_SITEMAPS). Тип ошибки: ({str(result["ERRORS_IN_SITEMAPS"]["severity"])})'
            FAVICON_ERROr=f'На сайте недоступен файл favicon. (FAVICON_ERROR). Тип ошибки: ({str(result["FAVICON_ERROR"]["severity"])})'
            MAIN_MIRROR_IS_NOT_HTTPs=f'Главное зеркало сайта не использует HTTPS-протокол. Рекомендуем использовать протокол HTTPS. (MAIN_MIRROR_IS_NOT_HTTPS). Тип ошибки: ({str(result["MAIN_MIRROR_IS_NOT_HTTPS"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/yandex-indexing/https-migration.html'
            MAIN_PAGE_REDIRECTs=f'Главная страница перенаправляет на другой сайт. (MAIN_PAGE_REDIRECTS). Тип ошибки: ({str(result["MAIN_PAGE_REDIRECTS"]["severity"])})'
            NO_METRIKA_COUNTER_BINDINg=f'К сайту не привязан счётчик Яндекс Метрики. (NO_METRIKA_COUNTER_BINDING). Тип ошибки: ({str(result["NO_METRIKA_COUNTER_BINDING"]["severity"])})'
            NO_METRIKA_COUNTER_CRAWL_ENABLEd=f'Не включен обход по счетчикам Яндекс Метрики. (NO_METRIKA_COUNTER_CRAWL_ENABLED). Тип ошибки: ({str(result["NO_METRIKA_COUNTER_CRAWL_ENABLED"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/indexing-options/link-metrica.html'
            NO_ROBOTS_TXt=f'Не найден файл robots.txt. (NO_ROBOTS_TXT). Тип ошибки: ({str(result["NO_ROBOTS_TXT"]["severity"])})'
            NO_SITEMAPs=f'Нет используемых роботом файлов Sitemap. (NO_SITEMAPS). Тип ошибки: ({str(result["NO_SITEMAPS"]["severity"])})'
            NO_SITEMAP_MODIFICATIONs=f'Файлы Sitemap давно не обновлялись. (NO_SITEMAP_MODIFICATIONS). Тип ошибки: ({str(result["NO_SITEMAP_MODIFICATIONS"]["severity"])})'
            # NON_WORKING_VIDEo=f'Робот не смог проиндексировать видео, размеченные на сайте. (NON_WORKING_VIDEO). Тип ошибки: ({str(result["NON_WORKING_VIDEO"]["severity"])})'
            SOFt_404=f'Некорректно настроено отображение несуществующих файлов и страниц. (SOFT_404). Тип ошибки: ({str(result["SOFT_404"]["severity"])})'
            TOO_MANY_DOMAINS_ON_SEARCh=f'В результатах поиска найдены поддомены сайта. (TOO_MANY_DOMAINS_ON_SEARCH). Тип ошибки: ({str(result["TOO_MANY_DOMAINS_ON_SEARCH"]["severity"])})'
            TURBO_HOST_BAN_INFo=f'Турбо-страницы и оригинальные страницы сайта должны быть максимально близки по контенту. (TURBO_HOST_BAN_INFO). Тип ошибки: ({str(result["TURBO_HOST_BAN_INFO"]["severity"])})'
            TURBO_LISTING_ERROr=f'На сайте возникли ошибки при формировании листингов для Турбо-страниц. (TURBO_LISTING_ERROR). Тип ошибки: ({str(result["TURBO_LISTING_ERROR"]["severity"])})'
            TURBO_RSS_WARNINg=f'В RSS-канале, используемом для создания Турбо-страниц, были найдены ошибки. Это может привести к неполному отображению Турбо-страниц в результатах поиска. (TURBO_RSS_WARNING). Тип ошибки: ({str(result["TURBO_RSS_WARNING"]["severity"])})'
            TURBO_YML_WARNINg=f'В YML-файле, используемом для создания Турбо-страниц, были найдены ошибки. Это может привести к неполному отображению Турбо-страниц в результатах поиска. (TURBO_YML_WARNING). Тип ошибки: ({str(result["TURBO_YML_WARNING"]["severity"])})'
            VIDEOHOST_OFFER_FAILEd=f'Добавленное в Вебмастер пользовательское соглашение для отображения видео отклонено. (VIDEOHOST_OFFER_FAILED). Тип ошибки: ({str(result["VIDEOHOST_OFFER_FAILED"]["severity"])}). Подробнее: https://yandex.ru/support/video/partners/join.html#agreement'
            VIDEOHOST_OFFER_IS_NEEDEd=f'Для сайта отсутствует пользовательское соглашение для отображения видео. (VIDEOHOST_OFFER_IS_NEEDED). Тип ошибки: ({str(result["VIDEOHOST_OFFER_IS_NEEDED"]["severity"])}). Подробнее: https://yandex.ru/support/video/partners/join.html#agreement'
            VIDEOHOST_OFFER_NEED_PAPEr=f'Для сайта необходимо заключить специальное соглашение для сотрудничества с Яндексом. (VIDEOHOST_OFFER_NEED_PAPER). Тип ошибки: ({str(result["VIDEOHOST_OFFER_NEED_PAPER"]["severity"])}). Подробнее: https://yandex.ru/support/video/partners/join.html#agreement'
            # RECOMMENDATION
            BIG_FAVICON_ABSENt=f'Добавьте на сайт файл favicon в формате SVG или размером 120 × 120 пикселей. В таком формате логотип вашего сайта станет четче и заметнее на сервисах Яндекса, в том числе, в результатах поиска. (BIG_FAVICON_ABSENT). Тип ошибки: ({str(result["BIG_FAVICON_ABSENT"]["severity"])})'
            FAVICON_PROBLEm=f'Файл favicon не найден. Робот не смог загрузить файл с изображением, которое должно отображаться во вкладке браузера и может быть показано возле названия сайта в поиске. (FAVICON_PROBLEM). Тип ошибки: ({str(result["FAVICON_PROBLEM"]["severity"])}). Подробнее: https://yandex.ru/support/webmaster/search-results/favicon.html'
            NO_METRIKA_COUNTEr=f'Ошибка счетчика Яндекс Метрики. (NO_METRIKA_COUNTER). Тип ошибки: ({str(result["NO_METRIKA_COUNTER"]["severity"])})'
            NO_REGIONs=f'Не задана региональная принадлежность сайта. (NO_REGIONS). Тип ошибки: ({str(result["NO_REGIONS"]["severity"])})'
            NOT_IN_SPRAv=f'Сайт не зарегистрирован в Яндекс Справочнике. (NOT_IN_SPRAV). Тип ошибки: ({str(result["NOT_IN_SPRAV"]["severity"])})'
            NOT_MOBILE_FRIENDLy=f'Сайт не оптимизирован для мобильных устройств. (NOT_MOBILE_FRIENDLY). Тип ошибки: ({str(result["NOT_MOBILE_FRIENDLY"]["severity"])})'
            SPRAV_COMPANY_PROFILE_CREATEd=f'Алгоритмы Яндекс Бизнеса посчитали, что ваш сайт очень похож на сайт компании, поэтому создали на его основе карточку организации. Проверьте, что данные заполнены корректно. После подтверждения данных карточка будет размещена в результатах поиска и на Яндекс Картах. (SPRAV_COMPANY_PROFILE_CREATED). Тип ошибки: ({str(result["SPRAV_COMPANY_PROFILE_CREATED"]["severity"])}). Подробнее: https://yandex.ru/support/business-priority/index.html'
            if result["CONNECT_FAILED"]['state']=="PRESENT":
                mass=mass+"❗️"+CONNECT_FAILEd+"\n"
                debagstat=debagstat+1
            elif result["CONNECT_FAILED"]['state']=="UNDEFINED":
                mass=mass+"❓ (CONNECT_FAILED) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["DISALLOWED_IN_ROBOTS"]['state']=="PRESENT":
                mass=mass+"❗️"+DISALLOWED_IN_ROBOTs+"\n"
                debagstat=debagstat+1
            elif result["DISALLOWED_IN_ROBOTS"]['state']=="UNDEFINED":
                mass=mass+"❓ (DISALLOWED_IN_ROBOTS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["DNS_ERROR"]['state']=="PRESENT":
                mass=mass+"❗️"+DNS_ERROr+"\n"
                debagstat=debagstat+1
            elif result["DNS_ERROR"]['state']=="UNDEFINED":
                mass=mass+"❓ (DNS_ERROR) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["MAIN_PAGE_ERROR"]['state']=="PRESENT":
                mass=mass+"❗️"+MAIN_PAGE_ERROr+"\n"
                debagstat=debagstat+1
            elif result["MAIN_PAGE_ERROR"]['state']=="UNDEFINED":
                mass=mass+"❓ (MAIN_PAGE_ERROR) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["THREATS"]['state']=="PRESENT":
                mass=mass+"❗️"+THREATs+"\n"
                debagstat=debagstat+1
            elif result["THREATS"]['state']=="UNDEFINED":
                mass=mass+"❓ (THREATS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_FEED_BAN"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_FEED_BAn+"\n"
                debagstat=debagstat+1
            elif result["TURBO_FEED_BAN"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_FEED_BAN) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["INSIGNIFICANT_CGI_PARAMETER"]['state']=="PRESENT":
                mass=mass+"❗️"+INSIGNIFICANT_CGI_PARAMETEr+"\n"
                debagstat=debagstat+1
            elif result["INSIGNIFICANT_CGI_PARAMETER"]['state']=="UNDEFINED":
                mass=mass+"❓ (INSIGNIFICANT_CGI_PARAMETER) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["SLOW_AVG_RESPONSE_TIME"]['state']=="PRESENT":
                mass=mass+"❗️"+SLOW_AVG_RESPONSE_TIMe+"\n"
                debagstat=debagstat+1
            elif result["SLOW_AVG_RESPONSE_TIME"]['state']=="UNDEFINED":
                mass=mass+"❓ (SLOW_AVG_RESPONSE_TIME) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["SSL_CERTIFICATE_ERROR"]['state']=="PRESENT":
                mass=mass+"❗️"+SSL_CERTIFICATE_ERROr+"\n"
                debagstat=debagstat+1
            elif result["SSL_CERTIFICATE_ERROR"]['state']=="UNDEFINED":
                mass=mass+"❓ (SSL_CERTIFICATE_ERROR) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_HOST_BAN"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_HOST_BAn+"\n"
                debagstat=debagstat+1
            elif result["TURBO_HOST_BAN"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_HOST_BAN) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            # if result["TURBO_INVALID_CART_URL"]['state']=="PRESENT":
            #     mass=mass+"❗️"+TURBO_INVALID_CART_URl+"\n"
            #     debagstat=debagstat+1
            # elif result["TURBO_INVALID_CART_URL"]['state']=="UNDEFINED":
            #     mass=mass+"❓ (TURBO_INVALID_CART_URL) Недостаточно данных для определения наличия проблем.\n"
            #     debagstat=debagstat+1
            if result["TURBO_RSS_ERROR"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_RSS_ERROr+"\n"
                debagstat=debagstat+1
            elif result["TURBO_RSS_ERROR"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_RSS_ERROR) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_URL_ERRORS"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_URL_ERRORs+"\n"
                debagstat=debagstat+1
            elif result["TURBO_URL_ERRORS"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_URL_ERRORS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_YML_ERROR"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_YML_ERROr+"\n"
                debagstat=debagstat+1
            elif result["TURBO_YML_ERROR"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_YML_ERROR) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["URL_ALERT_4XX"]['state']=="PRESENT":
                mass=mass+"❗️"+URL_ALERT_4Xx+"\n"
                debagstat=debagstat+1
            elif result["URL_ALERT_4XX"]['state']=="UNDEFINED":
                mass=mass+"❓ (URL_ALERT_4XX) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["URL_ALERT_5XX"]['state']=="PRESENT":
                mass=mass+"❗️"+URL_ALERT_5Xx+"\n"
                debagstat=debagstat+1
            elif result["URL_ALERT_5XX"]['state']=="UNDEFINED":
                mass=mass+"❓ (URL_ALERT_5XX) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["DISALLOWED_URLS_ALERT"]['state']=="PRESENT":
                mass=mass+"❗️"+DISALLOWED_URLS_ALERt+"\n"
                debagstat=debagstat+1
            elif result["DISALLOWED_URLS_ALERT"]['state']=="UNDEFINED":
                mass=mass+"❓ (DISALLOWED_URLS_ALERT) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["DOCUMENTS_MISSING_DESCRIPTION"]['state']=="PRESENT":
                mass=mass+"❗️"+DOCUMENTS_MISSING_DESCRIPTIOn+"\n"
                debagstat=debagstat+1
            elif result["DOCUMENTS_MISSING_DESCRIPTION"]['state']=="UNDEFINED":
                mass=mass+"❓ (DOCUMENTS_MISSING_DESCRIPTION) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["DOCUMENTS_MISSING_TITLE"]['state']=="PRESENT":
                mass=mass+"❗️"+DOCUMENTS_MISSING_TITLe+"\n"
                debagstat=debagstat+1
            elif result["DOCUMENTS_MISSING_TITLE"]['state']=="UNDEFINED":
                mass=mass+"❓ (DOCUMENTS_MISSING_TITLE) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["DUPLICATE_CONTENT_ATTRS"]['state']=="PRESENT":
                mass=mass+"❗️"+DUPLICATE_CONTENT_ATTRs+"\n"
                debagstat=debagstat+1
            elif result["DUPLICATE_CONTENT_ATTRS"]['state']=="UNDEFINED":
                mass=mass+"❓ (DUPLICATE_CONTENT_ATTRS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["DUPLICATE_PAGES"]['state']=="PRESENT":
                mass=mass+"❗️"+DUPLICATE_PAGEs+"\n"
                debagstat=debagstat+1
            elif result["DUPLICATE_PAGES"]['state']=="UNDEFINED":
                mass=mass+"❓ (DUPLICATE_PAGES) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["ERROR_IN_ROBOTS_TXT"]['state']=="PRESENT":
                mass=mass+"❗️"+ERROR_IN_ROBOTS_TXt+"\n"
                debagstat=debagstat+1
            elif result["ERROR_IN_ROBOTS_TXT"]['state']=="UNDEFINED":
                mass=mass+"❓ (ERROR_IN_ROBOTS_TXT) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["ERRORS_IN_SITEMAPS"]['state']=="PRESENT":
                mass=mass+"❗️"+ERRORS_IN_SITEMAPs+"\n"
                debagstat=debagstat+1
            elif result["ERRORS_IN_SITEMAPS"]['state']=="UNDEFINED":
                mass=mass+"❓ (ERRORS_IN_SITEMAPS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["FAVICON_ERROR"]['state']=="PRESENT":
                mass=mass+"❗️"+FAVICON_ERROr+"\n"
                debagstat=debagstat+1
            elif result["FAVICON_ERROR"]['state']=="UNDEFINED":
                mass=mass+"❓ (FAVICON_ERROR) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["MAIN_MIRROR_IS_NOT_HTTPS"]['state']=="PRESENT":
                mass=mass+"❗️"+MAIN_MIRROR_IS_NOT_HTTPs+"\n"
                debagstat=debagstat+1
            elif result["MAIN_MIRROR_IS_NOT_HTTPS"]['state']=="UNDEFINED":
                mass=mass+"❓ (MAIN_MIRROR_IS_NOT_HTTPS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["MAIN_PAGE_REDIRECTS"]['state']=="PRESENT":
                mass=mass+"❗️"+MAIN_PAGE_REDIRECTs+"\n"
                debagstat=debagstat+1
            elif result["MAIN_PAGE_REDIRECTS"]['state']=="UNDEFINED":
                mass=mass+"❓ (MAIN_PAGE_REDIRECTS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NO_METRIKA_COUNTER_BINDING"]['state']=="PRESENT":
                mass=mass+"❗️"+NO_METRIKA_COUNTER_BINDINg+"\n"
                debagstat=debagstat+1
            elif result["NO_METRIKA_COUNTER_BINDING"]['state']=="UNDEFINED":
                mass=mass+"❓ (NO_METRIKA_COUNTER_BINDING) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NO_METRIKA_COUNTER_CRAWL_ENABLED"]['state']=="PRESENT":
                mass=mass+"❗️"+NO_METRIKA_COUNTER_CRAWL_ENABLEd+"\n"
                debagstat=debagstat+1
            elif result["NO_METRIKA_COUNTER_CRAWL_ENABLED"]['state']=="UNDEFINED":
                mass=mass+"❓ (NO_METRIKA_COUNTER_CRAWL_ENABLED) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NO_ROBOTS_TXT"]['state']=="PRESENT":
                mass=mass+"❗️"+NO_ROBOTS_TXt+"\n"
                debagstat=debagstat+1
            elif result["NO_ROBOTS_TXT"]['state']=="UNDEFINED":
                mass=mass+"❓ (NO_ROBOTS_TXT) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NO_SITEMAPS"]['state']=="PRESENT":
                mass=mass+"❗️"+NO_SITEMAPs+"\n"
                debagstat=debagstat+1
            elif result["NO_SITEMAPS"]['state']=="UNDEFINED":
                mass=mass+"❓ (NO_SITEMAPS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NO_SITEMAP_MODIFICATIONS"]['state']=="PRESENT":
                mass=mass+"❗️"+NO_SITEMAP_MODIFICATIONs+"\n"
                debagstat=debagstat+1
            elif result["NO_SITEMAP_MODIFICATIONS"]['state']=="UNDEFINED":
                mass=mass+"❓ (NO_SITEMAP_MODIFICATIONS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            # if result["NON_WORKING_VIDEO"]['state']=="PRESENT":
            #     mass=mass+NON_WORKING_VIDEo+"\n"
                # debagstat=debagstat+1
            # elif result["NON_WORKING_VIDEO"]['state']=="UNDEFINED":
            #     mass=mass+"❓ (CONNECT_FAILED) Недостаточно данных для определения наличия проблем.\n"
                # debagstat=debagstat+1
            if result["SOFT_404"]['state']=="PRESENT":
                mass=mass+"❗️"+SOFt_404+"\n"
                debagstat=debagstat+1
            elif result["SOFT_404"]['state']=="UNDEFINED":
                mass=mass+"❓ (SOFT_404) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TOO_MANY_DOMAINS_ON_SEARCH"]['state']=="PRESENT":
                mass=mass+"❗️"+TOO_MANY_DOMAINS_ON_SEARCh+"\n"
                debagstat=debagstat+1
            elif result["TOO_MANY_DOMAINS_ON_SEARCH"]['state']=="UNDEFINED":
                mass=mass+"❓ (TOO_MANY_DOMAINS_ON_SEARCH) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_HOST_BAN_INFO"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_HOST_BAN_INFo+"\n"
                debagstat=debagstat+1
            elif result["TURBO_HOST_BAN_INFO"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_HOST_BAN_INFO) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_LISTING_ERROR"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_LISTING_ERROr+"\n"
                debagstat=debagstat+1
            elif result["TURBO_LISTING_ERROR"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_LISTING_ERROR) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_RSS_WARNING"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_RSS_WARNINg+"\n"
                debagstat=debagstat+1
            elif result["TURBO_RSS_WARNING"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_RSS_WARNING) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["TURBO_YML_WARNING"]['state']=="PRESENT":
                mass=mass+"❗️"+TURBO_YML_WARNINg+"\n"
                debagstat=debagstat+1
            elif result["TURBO_YML_WARNING"]['state']=="UNDEFINED":
                mass=mass+"❓ (TURBO_YML_WARNING) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["VIDEOHOST_OFFER_FAILED"]['state']=="PRESENT":
                mass=mass+"❗️"+VIDEOHOST_OFFER_FAILEd+"\n"
                debagstat=debagstat+1
            elif result["VIDEOHOST_OFFER_FAILED"]['state']=="UNDEFINED":
                mass=mass+"❓ (VIDEOHOST_OFFER_FAILED) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["VIDEOHOST_OFFER_IS_NEEDED"]['state']=="PRESENT":
                mass=mass+"❗️"+VIDEOHOST_OFFER_IS_NEEDEd+"\n"
                debagstat=debagstat+1
            elif result["VIDEOHOST_OFFER_IS_NEEDED"]['state']=="UNDEFINED":
                mass=mass+"❓ (VIDEOHOST_OFFER_IS_NEEDED) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["VIDEOHOST_OFFER_NEED_PAPER"]['state']=="PRESENT":
                mass=mass+"❗️"+VIDEOHOST_OFFER_NEED_PAPEr+"\n"
                debagstat=debagstat+1
            elif result["VIDEOHOST_OFFER_NEED_PAPER"]['state']=="UNDEFINED":
                mass=mass+"❓ (VIDEOHOST_OFFER_NEED_PAPER) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["BIG_FAVICON_ABSENT"]['state']=="PRESENT":
                mass=mass+"❗️"+BIG_FAVICON_ABSENt+"\n"
                debagstat=debagstat+1
            elif result["BIG_FAVICON_ABSENT"]['state']=="UNDEFINED":
                mass=mass+"❓ (BIG_FAVICON_ABSENT) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["FAVICON_PROBLEM"]['state']=="PRESENT":
                mass=mass+"❗️"+FAVICON_PROBLEm+"\n"
                debagstat=debagstat+1
            elif result["FAVICON_PROBLEM"]['state']=="UNDEFINED":
                mass=mass+"❓ (FAVICON_PROBLEM) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NO_METRIKA_COUNTER"]['state']=="PRESENT":
                mass=mass+"❗️"+NO_METRIKA_COUNTEr+"\n"
                debagstat=debagstat+1
            elif result["NO_METRIKA_COUNTER"]['state']=="UNDEFINED":
                mass=mass+"❓ (NO_METRIKA_COUNTER) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NO_REGIONS"]['state']=="PRESENT":
                mass=mass+"❗️"+NO_REGIONs+"\n"
                debagstat=debagstat+1
            elif result["NO_REGIONS"]['state']=="UNDEFINED":
                mass=mass+"❓ (NO_REGIONS) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NOT_IN_SPRAV"]['state']=="PRESENT":
                mass=mass+"❗️"+NOT_IN_SPRAv+"\n"
                debagstat=debagstat+1
            elif result["NOT_IN_SPRAV"]['state']=="UNDEFINED":
                mass=mass+"❓ (NOT_IN_SPRAV) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["NOT_MOBILE_FRIENDLY"]['state']=="PRESENT":
                mass=mass+"❗️"+NOT_MOBILE_FRIENDLy+"\n"
                debagstat=debagstat+1
            elif result["NOT_MOBILE_FRIENDLY"]['state']=="UNDEFINED":
                mass=mass+"❓ (NOT_MOBILE_FRIENDLY) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            if result["SPRAV_COMPANY_PROFILE_CREATED"]['state']=="PRESENT":
                mass=mass+"❗️"+SPRAV_COMPANY_PROFILE_CREATEd+"\n"
                debagstat=debagstat+1
            elif result["SPRAV_COMPANY_PROFILE_CREATED"]['state']=="UNDEFINED":
                mass=mass+"❓ (SPRAV_COMPANY_PROFILE_CREATED) Недостаточно данных для определения наличия проблем.\n"
                debagstat=debagstat+1
            
                
            elif mass!="":
                if debagstat!=dd:
                    
                    bot.send_message(message.chat.id, mass)
                    mass=""
            dd=debagstat
            # sleep(30)
            
# def asss():     
#     print("ghghg")
    
# def asss1():     
#     print("ghghg1")     
    # while i<1000:
    #     sleep(3)
    #     print(i)
    #     i=i+1            
# @bot.message_handler(commands=['stop_alko_com_diagnostic'])
# def st(message):
#     x1 = threading.Thread(target=asss())
#     x2 = threading.Thread(target=asss1())
#     x = threading.Thread(target=res(message))
#     x2.start()
#     x1.start()
#     x1.start()
#     x.start()
    
    i=0
    # while i<1000:
    #     sleep(3)
    #     print(i)
    #     i=i+1
        
bot.polling(none_stop=True)