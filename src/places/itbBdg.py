x = -6.89132022515749
y = 107.61061618283757
zoom = 17

listKoordinat = [(-6.8931357321569795, 107.61043417848474),     # Gerbang Utama [0]
                 (-6.8926481246340465, 107.60876860281701),     # Gedung Sipil [1]
                 (-6.891045439979195, 107.60868333225132),      # Gedung CIBE [2]
                 (-6.89102682287638, 107.60971545320055),       # CC Barat [3]
                 (-6.891019098250985, 107.6110472483217),       # CC Timur [4]
                 (-6.891911273407023, 107.61039174777933),      # Lapangan Cinta [5]
                 (-6.891357415665471, 107.61104060119305),      # Gedung SAPPK [6]
                 (-6.892441432391727, 107.61184871738482),      # Gedung SR [7]
                 (-6.891324641487534, 107.6121777135574),       # Sekretariat IMG  [8]
                 (-6.8909780544008346, 107.61154244628963),     # Gedung Lingkungan [9]
                 (-6.89013568927372, 107.60904936987745),       # GKU Barat [10]
                 (-6.889858493408902, 107.61152535852719),      # Labtek VII [11]
                 (-6.888703707464329, 107.60912116012126),      # Labtek III [12]
                 (-6.889445935319975, 107.61153615159377),      # Gedung Kimia [13]
                 (-6.889100770793402, 107.61153640188064),      # Gedung FTTM [14]
                 (-6.888696387683714, 107.61151220623402),      # Gedung FITB [15]
                 (-6.8881713215082385, 107.61148441227157),     # Gedung CAS [16]
                 (-6.887865079092212, 107.61144904859228),      # Gedung CRCS [17]
                 (-6.887843022137563, 107.61049315714548),      # Perpustakaan [18]
                 (-6.887996245289205, 107.60920683118938),      # Gedung SBM [19]
                 (-6.888680340973249, 107.61035240783394),      # Sunken Court [20]
                 (-6.88989395284103, 107.61035124543669),       # Pusat Gema [21]
                 (-6.891022084739352, 107.6103473815715),       # Plaza Widya [22]
                 (-6.892600770578635, 107.61042090218989)]      # Aula Barat-Timur [23]

listNodeName = ['Gerbang Utama',        # 0 x
                'Gedung Sipil',         # 1 x
                'Gedung CIBE',          # 2 x
                'CC Barat',             # 3 x
                'CC Timur',             # 4 x
                'Lapangan Cinta',       # 5 x
                'Gedung SAPPK',         # 6 x
                'Gedung SR',            # 7 x
                'Sekretariat IMG',      # 8 x
                'Gedung Lingkungan',    # 9 x
                'GKU Barat',            # 10 x
                'Labtek VII',           # 11 x
                'Labtek III',           # 12 x
                'Gedung Kimia',         # 13 x
                'Gedung FTTM',          # 14 x
                'Gedung FITB',          # 15 x
                'Gedung CAS',           # 16 x
                'Gedung CRCS',          # 17 x
                'Perpustakaan',         # 18 x
                'Gedung SBM',           # 19 x
                'Sunken Court',         # 20 x
                'Pusat Gema',           # 21 x
                'Plaza Widya',          # 22
                'Aula Barat-Timur']     # 23

#            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3
matriks = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]