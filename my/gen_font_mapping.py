
from sympy import ImageSet

from my.common import drawChar, merge_images


chars = """
多么寂寞的背影啊...
你是失去了什么重要的东西吗？
……
这样啊…不是失去，而是找回了…记忆
人啊，活着就是为了赎罪
以前这里到了夏日祭的时候就特别热闹…
随着日子一天天的过，珍贵的东西都被遗忘了吧
到底是记住比较好、还是忘了比较好…
你还是不能下定决心呢…
是啊…我想起来了…
可是本不该存在的罪…要如何偿还呢…？
"""

maps = {}
mapsRev = []
counter = 0
for char in chars:
    if not (char in maps.keys()):
        maps[char] = counter
        mapsRev.append(char)
        print(hex(counter)[2:], end=" ")
        counter += 1
    else:
        print(hex(maps[char])[2:], end=" ")
print(maps)



inputFolderRoot = 'output_folder_font1'



# //https://github.com/TakWolf/fusion-pixel-font
fontPath = "fusion-pixel-font-12px-monospaced-ttf-v2024.11.04/fusion-pixel-12px-monospaced-zh_hans.ttf"
charSize = 12
font = ImageSet.truetype(fontPath, charSize)

index = 0
while index < counter:
    charImg = drawChar(mapsRev[index], font, 12, 12, 0, 0)
    charImg.save("output_folder_font1/char_{}.png".format(index))
    index+=1


merge_images(inputFolderRoot, "merged_image.png")

lines = chars.split('\n')
for line in lines:
    print(line)
    for char in line:
        code = maps[char]
        # print("{}".format(hex(code)[2:].zfill(2)), end=" 00 ")
        print("{}".format(code), end=",")
    print()
print()