import requests
import wave
import struct
import random

def get_quota():
    quota_url = 'https://www.random.org/quota/?format=plain'
    rq = requests.get(url=quota_url)
    # TODO errors
    return int(rq.text)

def get_random(count):
    url = ('https://www.random.org/integers/?num={num}&min=1'
           '&max=50&col=1&base=10&format=plain&rnd=new').format(num=count)

    r = requests.get(url=url)
    # TODO: errors
    print r.text
    print type(r.text)
    return [int(line) for line in r.text.split('\n') if line]

def generate(filepath='sound.wav', values_to_receive=None):
    sampleRate = 8000.0
    duration = 3.0

    if values_to_receive is None:
        needed = int(duration * sampleRate)
        quota = int(get_quota() / 64 / 10)
        values_to_receive = min(needed, quota)
        print values_to_receive

    # values = get_random(values_to_receive)
    values = range(10)
    print('len', len(values))

    wavef = wave.open(filepath, 'w')
    wavef.setnchannels(1)  # mono
    wavef.setsampwidth(2)
    wavef.setframerate(sampleRate)

    for i in range(int(duration * sampleRate)):
        index = random.randint(0, len(values)-1)
        value = values[index] * 600
        data = struct.pack('<h', value)
        wavef.writeframesraw(data)

    wavef.writeframes('')
    wavef.close()
    print 'Done'

if __name__ == '__main__':
    generate()
