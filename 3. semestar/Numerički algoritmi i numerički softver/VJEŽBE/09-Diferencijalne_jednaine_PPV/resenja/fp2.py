def fp2(t, sT, dsT):

    #  t - vreme proteklo od po?etka putovanja
    #  sT - pre?eni put
    #  dsT - trenutna brzina vozila
    v = dsT

    #  ogranicenje brzine
    speedLimit = 60*1000/3600 # 60km/h
    if sT > 10*1000: # nakon 10km
        speedLimit = 120*1000/3600 #  120km/h

    acc = 5 # 5m/(s^2)
    dec = -10 # -10m/(s^2)
    if t > 5*60 and t < 10*60: # pauza izmedju 5. i 10. min.
        if v >= 0: # usporavati sve dok vozilo ne stane
            a = dec
        else: # ako vozilo "krene u nazad" usled negativnog ubrzanja, ubrzati ponovo do 0
            a = acc
    else:
        if v <= speedLimit: # ubrzavati ako je brzina ispod ograni?enja
            a = acc
        else:
            a = dec # usporiti ako je brzina preko ograni?enja
    ddsT = a
    return ddsT
