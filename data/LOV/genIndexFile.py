with open('ycb_adv.txt', 'w') as f:
    for scene_id in range(1, 41):
        for setting in ['B', 'D', 'D1', 'D2', 'O1', 'O2', 'O3']:
            f.write('exp{:0>3d}_{}/001\n'.format(scene_id, setting))
