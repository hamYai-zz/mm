elif pil.lower() == 'irk':
                    if dat['grant'] == 'Vip':
                        clear()
                        print(warna('[00ffff]', '=================== Istant King Rank'))
                        contoh = {'t_distance': '10000', 'time': '30000', 'speed_banner': '1000', 'gifts': '100', 'treasure': '100', 'cars': '137', 'race_win': '1000', 'levels': '82', 'drift': '1000', 'run': '500', 'police': '1000', 'block_post': '1000', 'real_estate': '12', 'fuel': '10000', 'car_trade': '100', 'car_exchange': '100', 'burnt_tire': '100', 'car_fix': '100', 'car_wash': '100', 'offroad': '1000', 'passanger_distance': '1000', 'reactions': '2000', 'drift_max': '1000', 'taxi': '1000', 'delivery': '1000', 'cargo': '1000', 'push_ups': '957', 'slicer_cut': '1', 'car_collided': '1', 'new_type': '0'}
                        isidata = {'RatingData': contoh}
                        if SetUserRatingCall(isidata) == True:
                            print(f"{warna('[00ff00]', 'Success')}")
                        else:
                            print(f"{warna('[ff0000]', 'Failed')}")
                    else:
                        print(warna('[FF0000]', 'Regist your Email into VIP First'))
