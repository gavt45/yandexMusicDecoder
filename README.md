# Yandex music decoder
Android cached yandex music decoder.

Usually music files are stored in `/sdcard/Android/data/ru.yandex.music/files/<...>`

## WARNING!!! Use only for educational purposes. Do not publish decoded tracks! This actions are violating the license agreement!!! 



curl 'https://music.yandex.ru/api/v2.1/handlers/tracks?tracks=631623:69842&external-domain=music.yandex.ru&overembed=no' -H 'Connection: keep-alive' -H 'Accept: application/json; q=1.0, text/*; q=0.8, */*; q=0.1' -H 'X-Requested-With: XMLHttpRequest' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0' -H 'X-Retpath-Y: https%3A%2F%2Fmusic.yandex.ru%2F'
-H 'Referer: https://music.yandex.ru/album/1337/track/1337' -H 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' 
-H 'Sec-Fetch-Mode: cors' 
 -H 'Sec-Fetch-Site: same-origin'
-H 'Sec-Fetch-Dest: empty'


-H 'Cookie: yandexuid=4164165061589644315; yuidss=4164165061589644315; ymex=1906723743.yrts.1591363743; _ym_uid=1591363743826884788; _ym_d=1591363743; mda=0; my=YwA=; cycada=J03AlwvwiyNnf88v7ZCSDq659zLl0+bYz7pB/qpmnRE=; yabs-frequency=/5/200002CPxbu00000/; L=RUBFU0QEfVxGSFoNYWVgBABOD0h9UgdyASdTBVo=.1592841566.14273.373340.b24d4f8de758a1ee237344d220c3a23a; device_id="b2c073114152541047c870afb5d826b14102abac3"; i=6kL/UorEFi7lU7m5hdAtUEsfn4aC9bANVTcaiGwFJhRGB5XwOCf/ktVZn4Me4pOGCPlwMReY34d0V59DkPkb1W46R2I=; yp=1907767074.sad.1592407074%3A1592407074%3A1#1908201631.multib.1#1593673188.szm.2%3A1680x1050%3A1680x844#1593673464.zlgn_smrt.1#1593324950.ln_tp.01; ys=wprid.1593238547506492-1748814652654577490100303-production-app-host-vla-web-yp-350; active-browser-timestamp=1593238777545'
