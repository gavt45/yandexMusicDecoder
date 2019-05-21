import os,sys

def main(files_path):
    for f in os.listdir(files_path):
        print("Processing {}...".format(f), end='')
        fle = open(files_path+"/"+f, 'rb')
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
            fileStream2 = open(files_path+"/{}.m4a".format(f), 'ab')
        else:
            fileStream2 = open(files_path+"/{}.mp3".format(f), 'ab')
        fle.seek(0)
        array2 = fle.read(16384)
        while len(array2) > 0:
            fileStream2.write(bytes([e^b for e in array2]))
            array2 = fle.read(16384)
        print('done!')
if len(sys.argv) < 2:
    print("Usage: "+sys.argv[0]+" <dir with encoded files>")
    exit(1)
else:
    main(sys.argv[1])
