import os,sys
from re import findall,sub,match
import requests

def get_info(idd):
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
        'X-Retpath-Y': 'https%3A%2F%2Fmusic.yandex.ru%2F',
    }

    params = (
        ('tracks', str(idd)),
        ('external-domain', 'music.yandex.ru'),
        ('overembed', 'no'),
    )

    resp = requests.get('https://music.yandex.ru/api/v2.1/handlers/tracks', headers=headers, params=params)
    json = resp.json()
    return ['{} - {}'.format(json[i]['artists'][0]['name'],json[i]['title']) for i in range(len(idd.split(',')))] 

# print(get_info('112314,18385776,61835292,24327733'))
# exit(0)

def main(files_path):
    if files_path.endswith('/'):
        files_path = files_path[:-1]
    if not os.path.exists(files_path+"-decoded"):
        os.mkdir(files_path+"-decoded")
    files = os.listdir(files_path)
    files_count = len(files)
    for i, f in enumerate(files):
        stat_msg = "\rProcessing %s%s: [%s>%s] %.2f%%" % (
                                '0'*(8-len(f)),
                                f,
                                '='*int(float(i+1)/float(files_count)*30.0),
                                '.'*int(30.0-float(i+1)/float(files_count)*30.0-1),
                                float(i+1)/float(files_count)*100.0
                            )
        fle = open(files_path+"/"+f, 'rb')
        sz = os.stat(files_path+"/"+f).st_size
        b = fle.read(1)[0]
        b2 = fle.read(1)[0]
        flag10 = False
        flag11 = b != b2
        if flag11:
            flag10 = True
            print(bin(~b))
            b = (~b & 0xFF)
        flag12 = not flag10
        if flag12:
            fileStream2 = open("{}-decoded/{}.m4a".format(files_path,f), 'ab')
        else:
            fileStream2 = open("{}-decoded/{}.mp3".format(files_path,f), 'ab')
        fle.seek(0)
        read_sz = 0
        array2 = fle.read(16384)
        while len(array2) > 0:
            read_sz += len(array2)
            print(stat_msg + " file decoding progress: [%s>%s] %.2f%%   " % ('='*int(float(read_sz)/float(sz)*30.0), '.'*int(29.0 - float(read_sz)/float(sz)*30.0), float(read_sz)/float(sz)*100.0),end='')
            fileStream2.write(bytes([e^b for e in array2]))
            array2 = fle.read(16384)
        # print('...done!',end)
def resolve(files_path):
    if files_path.endswith('/'):
        files_path = files_path[:-1]
    if not os.path.exists(files_path+"-decoded"):
        print("{}-decoded folder not found!".format(files_path))
        return
    files_path += "-decoded"
    files = os.listdir(files_path)
    files_count = len(files)
    for i in range(0,files_count,10):
        print("\rProcessing [%s>%s] %.2f%%" % (
            '='*int(float(i+1)/float(files_count)*30.0),
            '.'*int(30.0-float(i+1)/float(files_count)*30.0-1),
            float(i+1)/float(files_count)*100.0
        ), end='')
        chunk = files[i:i+10]
        _chunk = []
        for part in chunk:
            if match(r"[0-9]+\.(m4a|mp3)", part):
                _chunk.append(part)
        del chunk
        ids = ','.join([part.replace(".m4a","").replace(".mp3","") for part in _chunk])
        results = get_info(ids)
        # print(results)
        # print(chunk)
        for i,fle in enumerate(_chunk):
            new_name = sub(r"[0-9]+\.m",results[i]+".m",fle)
            # print("new name: "+new_name)
            os.rename(files_path + "/" + fle, files_path + "/" + new_name.replace('/','|').replace('\\','|'))
        # return


if len(sys.argv) < 2:
    print("Usage: "+sys.argv[0]+" <dir with encoded files>")
    exit(1)
else:
    main(sys.argv[1])
    inp = input('Start resolvment process? [Y/n]')
    if inp == 'y' or inp == 'yes' or inp == '':
        print("Starting resolvment process...")
        resolve(sys.argv[1])
