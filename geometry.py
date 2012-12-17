#!/usr/bin/env python
#-*-coding:utf-8-*-

"""
    Screens feometry variants
"""


def vports_recall(scr_w, scr_h, btb=5, blr=10):
    return dict(
                #  x                y               width           height
        vt01_01 = [blr,           btb,           scr_w*1/1-blr, scr_h*1/1-btb],
        vt04_01 = [blr,           btb,           scr_w*1/2-blr, scr_h*1/2-btb],
        vt04_02 = [scr_w*1/2+blr, btb,           scr_w*1/2-blr, scr_h*1/2-btb],
        vt04_03 = [blr,           scr_h*1/2+btb, scr_w*1/2-blr, scr_h*1/2-btb],
        vt04_04 = [scr_w*1/2+blr, scr_h*1/2+btb, scr_w*1/2-blr, scr_h*1/2-btb],
        vt06_01 = [blr,           btb,           scr_w*2/3-blr, scr_h*2/3-btb],
        vt06_02 = [scr_w*2/3+blr, btb,           scr_w*1/3-blr, scr_h*1/3-btb],
        vt06_03 = [scr_w*2/3+blr, scr_h*1/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt06_04 = [blr,           scr_h*2/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt06_05 = [scr_w*1/3+blr, scr_h*2/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt06_06 = [scr_w*2/3+blr, scr_h*2/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt07_01 = [blr,           btb,           scr_w*1/2-blr, scr_h*1/2-btb],
        vt07_02 = [scr_w*1/2+blr, btb,           scr_w*1/2-blr, scr_h*1/2-btb],
        vt07_03 = [blr,           scr_h*1/2+btb, scr_w*1/2-blr, scr_h*1/2-btb],
        vt07_04 = [scr_w*1/2+blr, scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt07_05 = [scr_w*3/4+blr, scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt07_06 = [scr_w*1/2+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt07_07 = [scr_w*3/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt08_01 = [blr,           btb,           scr_w*3/4-blr, scr_h*3/4-btb],
        vt08_02 = [scr_w*3/4+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt08_03 = [scr_w*3/4+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt08_04 = [scr_w*3/4+blr, scr_h*2/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt08_05 = [blr,           scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt08_06 = [scr_w*1/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt08_07 = [scr_w*2/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt08_08 = [scr_w*3/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt09_01 = [blr,           btb,           scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_02 = [scr_w*1/3+blr, btb,           scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_03 = [scr_w*2/3+blr, btb,           scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_04 = [blr,           scr_h*1/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_05 = [scr_w*1/3+blr, scr_h*1/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_06 = [scr_w*2/3+blr, scr_h*1/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_07 = [blr,           scr_h*2/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_08 = [scr_w*1/3+blr, scr_h*2/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt09_09 = [scr_w*2/3+blr, scr_h*2/3+btb, scr_w*1/3-blr, scr_h*1/3-btb],
        vt10_01 = [blr,           btb,           scr_w*1/2-blr, scr_h*1/2-btb],
        vt10_02 = [scr_w*1/2+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt10_03 = [scr_w*3/4+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt10_04 = [scr_w*1/2+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt10_05 = [scr_w*3/4+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt10_06 = [blr,           scr_h*1/2+btb, scr_w*1/2-blr, scr_h*1/2-btb],
        vt10_07 = [scr_w*1/2+blr, scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt10_08 = [scr_w*3/4+blr, scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt10_09 = [scr_w*1/2+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt10_10 = [scr_w*3/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_01 = [blr,           btb,           scr_w*1/2-blr, scr_h*1/2-btb],
        vt13_02 = [scr_w*1/2+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_03 = [scr_w*3/4+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_04 = [scr_w*1/2+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_05 = [scr_w*3/4+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_06 = [blr,           scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_07 = [scr_w*1/4+blr, scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_08 = [scr_w*2/4+blr, scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_09 = [scr_w*3/4+blr, scr_h*1/2+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_10 = [blr,           scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_11 = [scr_w*1/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_12 = [scr_w*2/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt13_13 = [scr_w*3/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_01 = [blr,           btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_02 = [scr_w*1/4+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_03 = [scr_w*2/4+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_04 = [scr_w*3/4+blr, btb,           scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_05 = [blr,           scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_06 = [scr_w*1/4+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_07 = [scr_w*2/4+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_08 = [scr_w*3/4+blr, scr_h*1/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_09 = [blr,           scr_h*2/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_10 = [scr_w*1/4+blr, scr_h*2/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_11 = [scr_w*2/4+blr, scr_h*2/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_12 = [scr_w*3/4+blr, scr_h*2/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_13 = [blr,           scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_14 = [scr_w*1/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_15 = [scr_w*2/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
        vt16_16 = [scr_w*3/4+blr, scr_h*3/4+btb, scr_w*1/4-blr, scr_h*1/4-btb],
    )
