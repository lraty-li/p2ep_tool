from my.common import pgm_to_png,pgmTargets

for target in pgmTargets:
    pgm_to_png(target, "{}.png".format(target))
