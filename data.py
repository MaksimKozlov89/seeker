class MyScreen:
    num_of_belts = 17
    belts = {x: (400, 232 + (x - 1) * 21) for x in range(1, num_of_belts)}
    spot = 400, 590

    stop = (915, 973)
    update_scan = (1880, 220)
    lock = (1715, 323)
    orbit = (1652, 321)

    change_over_for_loot = (1751, 416)
    change_over_for_combat = (1633, 416)
    loot = (1652, 328)
    loot_all = (1368, 353)

    frequency_beep = 2500
    duration_beep = 1000

    pixel_for_can_warp = (985, 985)


class HotKeys:
    f1_cloacking = 'f1'
    f2_afterburner = 'f2'
    f3_hardener = 'f3'
    launch_drones = ('shift', 'f')
    scoop_drones = ('shift', 'r')
    attack = 'F'
