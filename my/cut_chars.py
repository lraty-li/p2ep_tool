from common import (
    getCharsFolderOfPgm,
    pgmTargets,
    pgm_to_png,
    split_image,
    workPalceFolder,
    pgmSzie
)
import os

for index, pgm in enumerate(pgmTargets):
    pngName = pgm.replace(".pgm", ".png")
    pgmPath = os.path.join(workPalceFolder, pgm)
    pngPath = os.path.join(workPalceFolder, pngName)
    pngOutputPath = os.path.join(workPalceFolder, getCharsFolderOfPgm(pgm))
    pgm_to_png(pgmPath, pngPath)
    # font1, font3: 12*12
    # font2: 8*12

    split_image(pngPath, pngOutputPath, pgmSzie[index][0], pgmSzie[index][1])
