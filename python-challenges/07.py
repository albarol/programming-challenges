import urllib
import png

PIXEL_SIZE = 28


reader = png.Reader(file=urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png'))
pixels = reader.read_flat()[2]

def get_letter(pixels, index):
    return pixels[index] if pixels[index] == pixels[index + 1] and pixels[index] == pixels[index + 2] else 0

message = ['']

index = 0
while index < len(pixels):
    letter = get_letter(pixels, i)
    if letter > 0:
        message.append(chr(letter))
    index = index + PIXEL_SIZE

print "".join(message)

# message: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

next_message = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print  "".join(map(chr, next_message))

# next url: http://www.pythonchallenge.com/pc/def/integrity.html