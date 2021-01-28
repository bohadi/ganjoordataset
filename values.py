#
#
# values.py
# 77 nevisandeha

# why do we hardcode the urls
# more than a few navigation links are misplaced on ganjoor
# this is rather exhaustive

# TODO after scrapping
# collate consecutive collections e.g.
#   'https://ganjoor.net/jami/7ourang/7-1/sd1/'                     :       177,
#   'https://ganjoor.net/jami/7ourang/7-1/sd12/'                    :        32,
#   'https://ganjoor.net/jami/7ourang/7-1/sd2/'                     :        77,
#   'https://ganjoor.net/jami/7ourang/7-1/sd3/'                     :        51,
#   'https://ganjoor.net/jami/7ourang/7-2/'                         :        76,
#   'https://ganjoor.net/jami/7ourang/7-3/'                         :        62,
#   'https://ganjoor.net/jami/7ourang/7-4/'                         :       130,
#   'https://ganjoor.net/jami/7ourang/7-5-yusof-zoleykha/'          :        75,
#   'https://ganjoor.net/jami/7ourang/7-6-leyli-majnoon/'           :        58,
#   'https://ganjoor.net/jami/7ourang/7-7/'                         :        78,

#   'https://ganjoor.net/jami/7ourang/kh7/kh7-1/'                   :        26,
#   'https://ganjoor.net/jami/7ourang/kh7/kh7-2/'                   :        25,
#   'https://ganjoor.net/jami/7ourang/kh7/kh7-3/'                   :        18,
#   'https://ganjoor.net/jami/7ourang/kh7/kh7-4/'                   :        31,
#   'https://ganjoor.net/jami/7ourang/kh7/kh7-5/'                   :        45,
#   'https://ganjoor.net/jami/7ourang/kh7/kh7-6/'                   :        22,
#   'https://ganjoor.net/jami/7ourang/kh7/kh7-7/'                   :        21,

#   'https://ganjoor.net/jami/baharestan/dibache/'                  :         0,
#   'https://ganjoor.net/jami/baharestan/rowze1/'                   :        35,
#   'https://ganjoor.net/jami/baharestan/rowze2/'                   :        18,
#   'https://ganjoor.net/jami/baharestan/rowze3/'                   :        20,
#   'https://ganjoor.net/jami/baharestan/rowze4/'                   :        15,
#   'https://ganjoor.net/jami/baharestan/rowze5/'                   :        13,
#   'https://ganjoor.net/jami/baharestan/rowze6/'                   :        49,
#   'https://ganjoor.net/jami/baharestan/rowze7/'                   :        32,
#   'https://ganjoor.net/jami/baharestan/rowze8/'                   :        22,
#    'https://ganjoor.net/jami/baharestan/khateme/'                  :        0,

#   'https://ganjoor.net/khayyam/tarane/tkh1/'                      :        15,
#   'https://ganjoor.net/khayyam/tarane/tkh2/'                      :        10,
#   'https://ganjoor.net/khayyam/tarane/tkh3/'                      :         9,
#   'https://ganjoor.net/khayyam/tarane/tkh4/'                      :        22,
#   'https://ganjoor.net/khayyam/tarane/tkh5/'                      :        17,
#   'https://ganjoor.net/khayyam/tarane/tkh6/'                      :        27,
#   'https://ganjoor.net/khayyam/tarane/tkh7/'                      :         7,
#   'https://ganjoor.net/khayyam/tarane/tkh8/'                      :        36,


#########
# 1 ⇒ 233
RAZI = {
    'https://ganjoor.net/razi/saghiname/'                           :         0,
    'https://ganjoor.net/razi/sougandname/'                         :         0,
    'https://ganjoor.net/razi/gouhar-e-eshgh/'                      :         0,
    'https://ganjoor.net/razi/tarjee-band/'                         :         0,
    'https://ganjoor.net/razi/ghazalar/'                            :        94,
    'https://ganjoor.net/razi/ghasidear/'                           :         6,
    'https://ganjoor.net/razi/robaeear/'                            :       100,
    'https://ganjoor.net/razi/ghatghaz/'                            :        20,
    'https://ganjoor.net/razi/mofrar/'                              :         9,
}
# 2 ⇒ 281
EBNEHESAM = {
    'https://ganjoor.net/ebnehesam/ghazalebn/'                      :       178,
    'https://ganjoor.net/ebnehesam/robaeebn/'                       :       100,
    'https://ganjoor.net/ebnehesam/tarebn/'                         :         2,
    'https://ganjoor.net/ebnehesam/tarjeebnh/'                      :         1,
}
# 3 ⇒ 786
ABUSAEED = {
    'https://ganjoor.net/abusaeed/robaee-aa/'                       :       724,
    'https://ganjoor.net/abusaeed/abyat-aa/'                        :        62,
}
# 4 ⇒ 144
ASADI = {
    'https://ganjoor.net/asadi/garshaspname/'                       :       144,
}
# 5 ⇒ 113
ASAD = {
    'https://ganjoor.net/asad/veysoramin/'                          :       113,
}
# 6 ⇒ 183
AZRAGHI = {
    'https://ganjoor.net/azraghi/aghas/'                            :        66,
    'https://ganjoor.net/azraghi/amogh/'                            :         9,
    'https://ganjoor.net/azraghi/arob/'                             :       108,
}
# 7 ⇒ 973
IQBAL = {
    'https://ganjoor.net/iqbal/asrar-khodi/'                        :        20,
    'https://ganjoor.net/iqbal/romooz-bikhodi/'                     :        32,
    'https://ganjoor.net/iqbal/payam-mashregh/'                     :       300,
    'https://ganjoor.net/iqbal/zaboor-ajam/'                        :       142,
    'https://ganjoor.net/iqbal/javidname/'                          :        62,
    'https://ganjoor.net/iqbal/pas-che-bayad-kard/'                 :        24,
    'https://ganjoor.net/iqbal/armaghan-hejaz/'                     :       393,
}
# 8 ⇒ 2819
KHOSRO = {
    'https://ganjoor.net/khosro/gozide/ghazal-khosro/'              :       626,
    'https://ganjoor.net/khosro/gozide/ghaside-khosro/'             :         6,
    'https://ganjoor.net/khosro/gozide/masnaviatkh/'                :       100,
    'https://ganjoor.net/khosro/gozide/matlaolanvar/'               :        14,
    'https://ganjoor.net/khosro/gozide/khosro-shirin2/'             :        39,
    'https://ganjoor.net/khosro/gozide/majnoon-leyli/'              :        31,
    'https://ganjoor.net/khosro/gozide/ayeene-sekandari/'           :         5,
    'https://ganjoor.net/khosro/gozide/8behesht/'                   :         2,
    'https://ganjoor.net/khosro/gozide/ghazalamkh/'                 :      1996,
}
# 9 ⇒ 742
AMIR = {
    'https://ganjoor.net/amir/ghasa/'                               :       466,
    'https://ganjoor.net/amir/taram/'                               :         3,
    'https://ganjoor.net/amir/tarjam/'                              :         3,
    'https://ganjoor.net/amir/ghazam/'                              :        61,
    'https://ganjoor.net/amir/ghatam/'                              :        34,
    'https://ganjoor.net/amir/robam/'                               :       174,
    'https://ganjoor.net/amir/mosammat'                             :         0,
}


#########
# 10 ⇒ 1464
ANVARI = {
    'https://ganjoor.net/anvari/divan-anvari/ghazala/'              :       321,
    'https://ganjoor.net/anvari/divan-anvari/ghaside-anvari/'       :       208,
    'https://ganjoor.net/anvari/divan-anvari/ghetea/'               :       491,
    'https://ganjoor.net/anvari/divan-anvari/robaeea/'              :       444,
}
# 11 ⇒ 1326
OUHADI = {
    'https://ganjoor.net/ouhadi/divano/ghasideo/'                   :        42,
    'https://ganjoor.net/ouhadi/divano/tarkibato/'                  :         2,
    'https://ganjoor.net/ouhadi/divano/robaeeo/'                    :       184,
    'https://ganjoor.net/ouhadi/divano/ghazalo/'                    :       887,
    'https://ganjoor.net/ouhadi/divano/tarjeeato/'                  :         2,
    'https://ganjoor.net/ouhadi/mantegholoshagh/'                   :        77,
    'https://ganjoor.net/ouhadi/jaamejam/'                          :       131,
    'https://ganjoor.net/ouhadi/divano/morabba/'                    :         0,
}
# 12 ⇒ 199
BABAAFZAL = {
    'https://ganjoor.net/babaafzal/robba/'                          :       192,
    'https://ganjoor.net/babaafzal/ghazalba/'                       :         7,
  # 'https://ganjoor.net/babaafzal/ghasba/'                         #   'به زودی اضافه خواهد شد'
}
# 13 ⇒ 368
BABATAHER = {
    'https://ganjoor.net/babataher/2beytiha/'                       :       366,
    'https://ganjoor.net/babataher/ghazal/'                         :         0,
    'https://ganjoor.net/babataher/ghaside/'                        :         0,
}
# 14 ⇒ 1047
BAHAR = {
    'https://ganjoor.net/bahar/ghasidebk/'                          :       276,
    'https://ganjoor.net/bahar/ghazalbk/'                           :       101,
    'https://ganjoor.net/bahar/ghetebk/'                            :       191,
    'https://ganjoor.net/bahar/masnavibk/'                          :        84,
    'https://ganjoor.net/bahar/mosammatbk/'                         :        22,
    'https://ganjoor.net/bahar/tarkibbk/'                           :        13,
    'https://ganjoor.net/bahar/tarjeebk/'                           :         9,
    'https://ganjoor.net/bahar/mostazadbk/'                         :         9,
    'https://ganjoor.net/bahar/4parebk/'                            :         6,
    'https://ganjoor.net/bahar/robaeebk/'                           :        71,
    'https://ganjoor.net/bahar/manzoomebk/ayeene-ebrat/'            :         3,
    'https://ganjoor.net/bahar/manzoomebk/karnamez/'                :        88,
    'https://ganjoor.net/bahar/manzoomebk/4khatabe/'                :         4,
    'https://ganjoor.net/bahar/manzoomebk/magas/'                   :         3,
    'https://ganjoor.net/bahar/manzoomebk/madarbk/'                 :         8,
    'https://ganjoor.net/bahar/manzoomebk/tbad/'                    :        10,
    'https://ganjoor.net/bahar/manzoomebk/armaghanbk/'              :       118,
    'https://ganjoor.net/bahar/mahalibk/'                           :         9,
    'https://ganjoor.net/bahar/tasnifbk/'                           :        18,
    'https://ganjoor.net/bahar/divanb/ghete/'                       :         0,
    'https://ganjoor.net/bahar/divanb/4pare/'                       :         0,
    'https://ganjoor.net/bahar/divanb/mostazad/'                    :         0,
    'https://ganjoor.net/bahar/divanb/tasneef/'                     :         0,
}
# 15 ⇒ 2828
BIDEL = {
    'https://ganjoor.net/bidel/ghazalbi/'                           :      2827,
    'https://ganjoor.net/bidel/tarjee-band/'                        :         0,
}
# 16 ⇒ 223
PARVIN = {
    'https://ganjoor.net/parvin/divanp/ghasidep/'                   :        42,
    'https://ganjoor.net/parvin/divanp/mtm/'                        :       181,
}
# 17 ⇒ 3539
JAMI = {
    'https://ganjoor.net/jami/7ourang/7-1/sd1/'                     :       177,
    'https://ganjoor.net/jami/7ourang/7-1/sd12/'                    :        32,
    'https://ganjoor.net/jami/7ourang/7-1/sd2/'                     :        77,
    'https://ganjoor.net/jami/7ourang/7-1/sd3/'                     :        51,
    'https://ganjoor.net/jami/7ourang/7-2/'                         :        76,
    'https://ganjoor.net/jami/7ourang/7-3/'                         :        62,
    'https://ganjoor.net/jami/7ourang/7-4/'                         :       130,
    'https://ganjoor.net/jami/7ourang/7-5-yusof-zoleykha/'          :        75,
    'https://ganjoor.net/jami/7ourang/7-6-leyli-majnoon/'           :        58,
    'https://ganjoor.net/jami/7ourang/7-7/'                         :        78,
    'https://ganjoor.net/jami/7ourang/kh7/kh7-1/'                   :        26,
    'https://ganjoor.net/jami/7ourang/kh7/kh7-2/'                   :        25,
    'https://ganjoor.net/jami/7ourang/kh7/kh7-3/'                   :        18,
    'https://ganjoor.net/jami/7ourang/kh7/kh7-4/'                   :        31,
    'https://ganjoor.net/jami/7ourang/kh7/kh7-5/'                   :        45,
    'https://ganjoor.net/jami/7ourang/kh7/kh7-6/'                   :        22,
    'https://ganjoor.net/jami/7ourang/kh7/kh7-7/'                   :        21,
    'https://ganjoor.net/jami/divanj/fateha-shabab/ghazal-jf/'      :      1015,
    'https://ganjoor.net/jami/divanj/fateha-shabab/ghaside-fj/'     :        22,
    'https://ganjoor.net/jami/divanj/fateha-shabab/ghete-jf/'       :        44,
    'https://ganjoor.net/jami/divanj/fateha-shabab/masnavi-jf/'     :         8,
    'https://ganjoor.net/jami/divanj/fateha-shabab/tarkib-jf/'      :         4,
    'https://ganjoor.net/jami/divanj/fateha-shabab/tarjee-jf/'      :         4,
    'https://ganjoor.net/jami/divanj/fateha-shabab/robaee-jf/'      :       154,
    'https://ganjoor.net/jami/divanj/fateha-shabab/sayer-jf/'       :         7,
    'https://ganjoor.net/jami/divanj/vaseta-eghd/'                  :         0,
    'https://ganjoor.net/jami/divanj/vaseta-eghd/ghazal-jv/'        :       493,
    'https://ganjoor.net/jami/divanj/vaseta-eghd/ghaside-vj/'       :        27,
    'https://ganjoor.net/jami/divanj/vaseta-eghd/ghete-jv/'         :        53,
    'https://ganjoor.net/jami/divanj/vaseta-eghd/robaee-jv/'        :        74,
    'https://ganjoor.net/jami/divanj/vaseta-eghd/parakande-jv/'     :        22,
    'https://ganjoor.net/jami/divanj/khatema-hayat/'                :         0,
    'https://ganjoor.net/jami/divanj/khatema-hayat/ghazal-jk/'      :       296,
    'https://ganjoor.net/jami/divanj/khatema-hayat/ghaside-kj/'     :        17,
    'https://ganjoor.net/jami/divanj/khatema-hayat/ghete-jk/'       :        38,
    'https://ganjoor.net/jami/divanj/khatema-hayat/robaee-jk/'      :        45,
    'https://ganjoor.net/jami/divanj/khatema-hayat/parakande-jk/'   :         4,
    'https://ganjoor.net/jami/baharestan/dibache/'                  :         0,
    'https://ganjoor.net/jami/baharestan/rowze1/'                   :        35,
    'https://ganjoor.net/jami/baharestan/rowze2/'                   :        18,
    'https://ganjoor.net/jami/baharestan/rowze3/'                   :        20,
    'https://ganjoor.net/jami/baharestan/rowze4/'                   :        15,
    'https://ganjoor.net/jami/baharestan/rowze5/'                   :        13,
    'https://ganjoor.net/jami/baharestan/rowze6/'                   :        49,
    'https://ganjoor.net/jami/baharestan/rowze7/'                   :        32,
    'https://ganjoor.net/jami/baharestan/rowze8/'                   :        22,
    'https://ganjoor.net/jami/baharestan/khateme/'                  :         0,
}
# 18 ⇒ 7
JABALI = {
    'https://ganjoor.net/jabali/gozidej/ghasidej/'                  :         7,
}


#########
# 19 ⇒ 630
HAFEZ = {
    'https://ganjoor.net/hafez/ghazal/'                             :       495,
    'https://ganjoor.net/hafez/masnavi/'                            :         0,
    'https://ganjoor.net/hafez/saghiname/'                          :         0,
    'https://ganjoor.net/hafez/robaee2/'                            :        42,
    'https://ganjoor.net/hafez/ghete/'                              :        34,
    'https://ganjoor.net/hafez/ghaside/'                            :         3,
    'https://ganjoor.net/hafez/montasab/'                           :        54,
}
# 20 ⇒ 1766
HAZIN = {
    'https://ganjoor.net/hazin/ghaside-hz/'                         :        51,
    'https://ganjoor.net/hazin/ghazal-hz/'                          :       912,
    'https://ganjoor.net/hazin/ghete-hz/'                           :        56,
    'https://ganjoor.net/hazin/robaee-hz/'                          :       264,
    'https://ganjoor.net/hazin/ghazal-natamam-hz/'                  :       344,
    'https://ganjoor.net/hazin/manavi-hz/chaman-o-anjoman/'         :        10,
    'https://ganjoor.net/hazin/manavi-hz/tazkerat-ol-asheghin/'     :        11,
    'https://ganjoor.net/hazin/manavi-hz/farhangname/'              :        18,
    'https://ganjoor.net/hazin/manavi-hz/safir-e-del/'              :        31,
    'https://ganjoor.net/hazin/manavi-hz/kharabat/'                 :        21,
    'https://ganjoor.net/hazin/manavi-hz/vadeeat-ol-badeea/'        :        41,
    'https://ganjoor.net/hazin/manavi-hz/matmah-ol-anzar/'          :         6,
    'https://ganjoor.net/hazin/tarkib-band-mar30ye/'                :         0,
}
# 21 ⇒ 1354
KHAGHANI = {
    'https://ganjoor.net/khaghani/divankh/ghazalkh/'                :       401,
    'https://ganjoor.net/khaghani/divankh/ghasidekh/'               :       224,
    'https://ganjoor.net/khaghani/divankh/robaeekh/'                :       352,
    'https://ganjoor.net/khaghani/divankh/ghetekh/'                 :       361,
    'https://ganjoor.net/khaghani/divankh/tarjeeatkh/'              :         7,
    'https://ganjoor.net/khaghani/divankh/tarkibatkh/'              :         9,
}
# 22 ⇒ 54
KHALILI = {
    'https://ganjoor.net/khalili/robaeekl/'                         :        54,
}
# 23 ⇒ 932
KHAJOO = {
    'https://ganjoor.net/khajoo/ghazal-khajoo/'                     :       932,
}
# 24 ⇒ 262
ABDULLAH = {
    'https://ganjoor.net/abdullah/monajat/'                         :       262,
}
# 25 ⇒ 363
KHAYYAM = {
    'https://ganjoor.net/khayyam/robaee/'                           :       178,
    'https://ganjoor.net/khayyam/tarane/tkh1/'                      :        15,
    'https://ganjoor.net/khayyam/tarane/tkh2/'                      :        10,
    'https://ganjoor.net/khayyam/tarane/tkh3/'                      :         9,
    'https://ganjoor.net/khayyam/tarane/tkh4/'                      :        22,
    'https://ganjoor.net/khayyam/tarane/tkh5/'                      :        17,
    'https://ganjoor.net/khayyam/tarane/tkh6/'                      :        27,
    'https://ganjoor.net/khayyam/tarane/tkh7/'                      :         7,
    'https://ganjoor.net/khayyam/tarane/tkh8/'                      :        36,
    'https://ganjoor.net/khayyam/nouroozname/'                      :        42,
}
# 26 ⇒ 29
RASHEH = {
    'https://ganjoor.net/hatef/divan-hatef/gar/'                    :        29,
}
# 27 ⇒ 539
ROODAKI = {
    'https://ganjoor.net/roodaki/baghimande/'                       :       129,
    'https://ganjoor.net/roodaki/robaeer/'                          :        38,
    'https://ganjoor.net/roodaki/masnaviha/kalila-sand/'            :       105,
    'https://ganjoor.net/roodaki/masnaviha/khafeef/'                :        27,
    'https://ganjoor.net/roodaki/masnaviha/motaghareb/'             :        43,
    'https://ganjoor.net/roodaki/masnaviha/hzj/'                    :        12,
    'https://ganjoor.net/roodaki/masnaviha/digar/'                  :         8,
    'https://ganjoor.net/roodaki/parakande/'                        :       177,
}


#########
# 28 ⇒
RAHI = {
    ''                                                              :       000,
}
# 29 ⇒
SAADI = {
    ''                                                              :       000,
}
# 30 ⇒
SALMAN = {
    ''                                                              :       000,
}
# 31 ⇒
SANAEE = {
    ''                                                              :       000,
}
# 32 ⇒
SEYF = {
    ''                                                              :       000,
}
# 33 ⇒
SHAHNEMATOLLAH = {
    ''                                                              :       000,
}
# 34 ⇒
SHABESTARI = {
    ''                                                              :       000,
}
# 35 ⇒
MAGHREBI = {
    ''                                                              :       000,
}
# 36 ⇒
SHAHRIAR = {
    ''                                                              :       000,
}


#########
#########


'''

#########
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}
# XX ⇒
POET = {
    ''                                                              :       000,
}

'''
