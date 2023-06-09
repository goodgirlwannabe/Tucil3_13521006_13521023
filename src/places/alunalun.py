x = -6.917921152550039
y = 107.60374055640584
zoom = 17

listKoordinat = [(-6.914763482418373, 107.59806082445583),      # Paskal [0]
                 (-6.916314446905801, 107.59819713067857),      # Parapan Kebon Jati [1]
                 (-6.920102574626576, 107.59838782222505),      # Sudirman [2]
                 (-6.915782319451493, 107.60449944984325),      # Stasiun Bandung [3]
                 (-6.92139789132258, 107.5983944107498),        # Cibadak [4]
                 (-6.9268349273287075, 107.59985715600061),     # Astana Anyar [5]
                 (-6.927243471429872, 107.60362566069243),      # Pasir Koja [6]
                 (-6.920815316114, 107.6041037562899),          # Norsefiicden [7]
                 (-6.92208984114456, 107.60400910131901),       # Otto Iskandar Dinata [8]
                 (-6.927390546790986, 107.60592904774549),     # Pungkur [9]
                 (-6.915389760946487, 107.60744118231969),      # Patung Tentara Pelajar [10]
                 (-6.916239625489668, 107.60891830680069),      # Braga Citywalk [11]
                 (-6.919708211715332, 107.609905698286),        # Braga [12]
                 (-6.919735443811863, 107.60889424224001),      # Air Mancur Asia Afrika [13]
                 (-6.918880823058204, 107.6067069791089),       # Jalan ABC [14]
                 (-6.921441946335599, 107.60979549903513),      # Asia Afrika [15]
                 (-6.92131144369633, 107.60874097849286),       # Mural Asia Afrika [16]
                 (-6.922782395509796, 107.60977084474239),      # Jalan Homan [17]
                 (-6.921225265358179, 107.60762122080159),      # Alun-Alun Bandung [18]
                 (-6.922512286325299, 107.60742554184935),      # Pendopo Kota Bandung [19]
                 (-6.918295574544841, 107.60431298317197)]      # Pasar Baru [20]

listNodeName = ["Paskal",                           # [0] x
                "Parapan Kebon Jati",               # [1] x
                "Sudirman",                         # [2] x
                "Stasiun Bandung",                  # [3] x
                "Cibadak",                          # [4] x
                "Astana Anyar",                     # [5] x
                "Pasir Koja",                       # [6] x
                "Norsefiicden",                     # [7] x
                "Otto Iskandar Dinata",             # [8] x
                "Pungkur",                          # [9] x
                "Patung Tentara Pelajar",           # [10] x
                "Braga Citywalk",                   # [11] x
                "Braga",                            # [12] x
                "Air Mancur Asia Afrika",           # [13] x
                "Jalan ABC",                        # [14] x
                "Asia Afrika",                      # [15] x
                "Mural Asia Afrika",                # [16] x
                "Jalan Homan",                      # [17] x
                "Alun-Alun Bandung",                # [18] x
                "Pendopo Kota Bandung",             # [19] x
                "Pasar Baru"]                       # [20] x

#            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
matriks = [ [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],   
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
           ]