from PIL import Image, ImageDraw, ImageFont

import os

pgmTargets = ["font0.pgm", "font1.pgm", "font2.pgm", "font3.pgm"]
pgmSzie = [(12, 12), (12, 12), (8, 12), (12, 12)]

workPalceFolder = "my"


def pgm_to_png(pgm_path, png_path):
    # 打开 PGM 文件
    img = Image.open(pgm_path)

    # 将 PGM 文件保存为 PNG 文件
    img.save(png_path, "PNG")
    print(f"转换完成: {png_path}")


def split_image(image_path, output_folder, charWidth, charHeight):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    # 打开图像
    img = Image.open(image_path)
    _, img_height = img.size

    # 计算块数
    num_blocks = img_height // charHeight

    for i in range(num_blocks):
        # 计算每个小块的起始坐标
        top = i * charHeight

        # 高度固定为12
        bottom = top + charHeight
        # 裁剪出小块并保存
        char_img = img.crop((0, top, charWidth, bottom))
        char_img.save(f"{output_folder}/{i}.png")


def merge_images(input_folder, output_path):
    # 获取文件夹内的所有图片文件，并按文件名排序
    image_files = sorted(
        [f for f in os.listdir(input_folder) if f.endswith(".png")],
        key=lambda x: int(os.path.splitext(x)[0].split("_")[-1]),
    )

    # 图像参数
    img_width = 12
    img_height = 12
    total_height = img_height * len(image_files)

    # 创建一个新的空白图像，用于存放合并后的图像
    merged_img = Image.new("RGB", (img_width, total_height))

    # 逐个粘贴字符图片到合并图像中
    y_offset = 0
    for img_file in image_files:
        img_path = os.path.join(input_folder, img_file)
        char_img = Image.open(img_path)

        # 将每张图片粘贴到新的图像的正确位置
        merged_img.paste(char_img, (0, y_offset))
        y_offset += img_height

    # 保存合并后的图像
    merged_img.save(output_path)
    print(f"合并完成: {output_path}")


def drawChar(char, font, charImgWidth, charImgHeight, drawOffsetX, drawOffsetY):
    image = Image.new(mode="RGB", size=(charImgWidth, charImgHeight), color="#00000000")
    drawTable = ImageDraw.Draw(im=image)
    drawTable.text(
        xy=(drawOffsetX, drawOffsetY), text=char, fill="#FFFFFFFF", font=font
    )
    return image


def getCharsFolderOfPgm(pngName):
    return "chars_{}".format(pngName.replace(".pgm", ""))
