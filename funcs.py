import pyautogui as pg
import time
import winsound
from data import MyScreen, HotKeys


def warp(x_, y_):
    pg.moveTo(x_, y_, 1)
    pg.rightClick()
    pg.moveRel(25, 10, 1)
    pg.click()
    time.sleep(10)


def signal():
    print('Signal')
    winsound.Beep(MyScreen.frequency_beep, MyScreen.duration_beep)


def can_warp():
    warp_ = pg.pixel(MyScreen.pixel_for_can_warp[0], MyScreen.pixel_for_can_warp[1])

    if 140 < sum(warp_) // 3 < 160:
        return True


def cloaking():
    print('Cloacking')
    pg.press(HotKeys.f1_cloacking)


def hardener():
    print('Hardener')
    pg.press(HotKeys.f3_hardener)


def stop():
    print('Stop')
    pg.moveTo(MyScreen.stop[0], MyScreen.stop[1])
    pg.click()
    time.sleep(7)


def afterburner():
    print('Afterburner')
    pg.press(HotKeys.f2_afterburner)


def update_d_scan():
    print('Update SCAN')
    x, y = MyScreen.update_scan
    pg.moveTo(MyScreen.update_scan[0], MyScreen.update_scan[1])
    pg.click()


def out_drones():
    print('Launch drones')
    pg.keyDown(HotKeys.launch_drones[0])
    pg.keyDown(HotKeys.launch_drones[1])
    pg.keyUp(HotKeys.launch_drones[0])
    pg.keyUp(HotKeys.launch_drones[1])


def scoop_drones():
    print('Scoop drones')
    pg.keyDown(HotKeys.scoop_drones[0])
    pg.keyDown(HotKeys.scoop_drones[1])
    pg.keyUp(HotKeys.scoop_drones[0])
    pg.keyUp(HotKeys.scoop_drones[1])


def see_clone():
    if pg.locateOnScreen('png/clone.png', confidence=.8):
        return True


def lock():
    print('Lock')
    pg.moveTo(MyScreen.lock[0], MyScreen.lock[1], 1)
    pg.click()
    time.sleep(3)


def orbit():
    print('Orbit')
    pg.moveTo(MyScreen.orbit[0], MyScreen.orbit[1], 1)
    pg.click()
    time.sleep(3)


def attacking_clone():
    print('Serpentis Clone Soldier attacked!')
    position = pg.locateOnScreen('clone.png', confidence=.8)
    pg.moveTo(position[0] + 10, position[1] + 10, 1)
    pg.click()
    lock()

    orbit()
    out_drones()
    time.sleep(3)
    pg.press(HotKeys.attack)
    afterburner()
    while see_clone():
        update_d_scan()
        time.sleep(10)
    scoop_drones()
    time.sleep(3)


def loot_clone():
    print('Looting')
    pg.moveTo(MyScreen.change_over_for_loot, 1)
    pg.click()
    time.sleep(2)
    pos_wreck = pg.locateOnScreen('clone_.png', confidence=.8)
    pg.moveTo(pos_wreck[0] + 10, pos_wreck[1] + 10, 1)
    pg.click()
    pg.moveTo(MyScreen.loot[0], MyScreen.loot[1], 1)
    pg.click()
    time.sleep(50)
    pg.moveTo(MyScreen.loot_all[0], MyScreen.loot_all[0],  1)
    pg.click()
    time.sleep(3)
    afterburner()
    pg.moveTo(MyScreen.change_over_for_combat[0], MyScreen.change_over_for_combat[1], 1)
    pg.click()


def start():
    time.sleep(3)
    cloaking()
    time.sleep(3)
    hardener()
    for belt in MyScreen.belts.keys():
        warp(MyScreen.belts[belt][0], MyScreen.belts[belt][1])
        print('Warping!!! Target: belt N: {}'.format(belt))

        while not can_warp():
            print('Waiting...')
            update_d_scan()
            time.sleep(7)
        if see_clone():
            print('Serpentis Clone Soldier discovered')
            signal()
            attacking_clone()
            loot_clone()
            stop()

    warp(MyScreen.spot[0], MyScreen.spot[1])
    time.sleep(35)
    cloaking()
