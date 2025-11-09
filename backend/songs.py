# songs.py

# backend/songs.py

mood_data = {
    "moods": [
        {"id": "happy", "name": "Happy", "emoji": "😊", "description": "Upbeat and cheerful tunes"},
        {"id": "sad", "name": "Sad", "emoji": "😢", "description": "Melancholic and soothing"},
        {"id": "energetic", "name": "Energetic", "emoji": "⚡", "description": "High-energy and dynamic"},
        {"id": "calm", "name": "Calm", "emoji": "🧘", "description": "Peaceful and relaxing"},
        {"id": "romantic", "name": "Romantic", "emoji": "💕", "description": "Love and passion"},
        {"id": "glamorous", "name": "Glamorous", "emoji": "✨", "description": "Concentration music for productivity"}
    ],
    "recommendedSongs": {
    "happy": [
            {
                "title": "On & On (feat. Daniel Levi)",
                "artist": "Cartoon, Jéja",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1751994456/Cartoon_Daniel_Levi_J%C3%A9ja_-_On_On_feat._Daniel_Levi_NCS_Release_qev555.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/onandon",
                "ncsLink": "http://ncs.io/onandon",
                "ncsWatch": "http://youtu.be/K4DyBUG242c"
            },
            {
                "title": "Energy",
                "artist": "Elektronomia",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1751999840/Elektronomia_-_Energy_NCS_Release_myjsqp.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/energy",
                "ncsLink": "http://ncs.io/energy",
                "ncsWatch": "http://youtu.be/fzNMd3Tu1Zw"
            },
            {
                "title": "Blank VIP (feat. Tara Louise)",
                "artist": "Disfigure",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1751999527/Disfigure_Tara_Louise_-_Blank_VIP_NCS_Release_kdlps2.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/blankvip",
                "ncsLink": "http://ncs.io/blankvip",
                "ncsWatch": "http://youtu.be/j5DCb1ycXyA"
            },
            {
                "title": "Invincible",
                "artist": "DEAF KEV",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1751999421/DEAF_KEV_-_Invincible_NCS_Release_peqpec.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/invincible",
                "ncsLink": "http://ncs.io/invincible",
                "ncsWatch": "http://youtu.be/J2X5mJ3HDYE"
            },
            {
                "title": "Limitless",
                "artist": "Elektronomia",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1751999855/Elektronomia_-_Limitless_NCS_Release_sevf9z.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Limitless",
                "ncsLink": "http://ncs.io/Limitless",
                "ncsWatch": "http://youtu.be/cNcy3J4x62M"
            },
            {
                "title": "So Happy",
                "artist": "Raven & Kreyn",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752000150/Raven_Kreyn_-_So_Happy_NCS_Release_dtn5va.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/SoHappy",
                "ncsLink": "http://ncs.io/SoHappy",
                "ncsWatch": "http://youtu.be/cmVdgWL5548"
            },
            {
                "title": "Feel Good",
                "artist": "Syn Cole",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752000157/Syn_Cole_-_Feel_Good_NCS_Release_khbnb1.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/feelgood",
                "ncsLink": "http://ncs.io/feelgood",
                "ncsWatch": "http://youtu.be/q1ULJ92aldE"
            },
            {
                "title": "Superhero (feat. Chris Linton)",
                "artist": "Unknown Brain, Chris Linton",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752000143/Unknown_Brain_Chris_Linton_-_Superhero_feat._Chris_Linton_NCS_Release_ambxhb.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/superhero",
                "ncsLink": "http://ncs.io/superhero",
                "ncsWatch": "http://youtu.be/LHvYrn3FAgI"
            },
            {
                "title": "Symbolism",
                "artist": "Electro-Light",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1751999814/Electro-Light_-_Symbolism_NCS_Release_kufa75.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/symbolism",
                "ncsLink": "http://ncs.io/symbolism",
                "ncsWatch": "http://youtu.be/__CRWE-L45k"
            },
            {
                "title": "My Heart",
                "artist": "Different Heaven, EH!DE",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1751999461/Different_Heaven_EH_DE_-_My_Heart_NCS_Release_znbpk7.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/myheart",
                "ncsLink": "http://ncs.io/myheart",
                "ncsWatch": "http://youtu.be/jK2aIUmmdP4"
            }
    ],
    "sad": [
            {
                "title": "Fearless (Slowed)",
                "artist": "Lost Sky",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003664/Lost_Sky_-_Fearless_Slowed_NCS_Release_ol4mai.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Fearless",
                "ncsLink": "http://ncs.io/Fearless",
                "ncsWatch": "http://youtu.be/ScSn235gQx0"
            },
            {
                "title": "AWOL",
                "artist": "Papa Khan",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003889/Papa_Khan_-_AWOL_NCS_Release_ga6mky.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/AWOL",
                "ncsLink": "http://NCS.io/AWOL",
                "ncsWatch": "http://youtu.be/8xlDwukxjnA"
            },
            {
                "title": "Darkness",
                "artist": "Lost Sky, She Is Jules",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003877/She_Is_Jules_Lost_Sky_-_Darkness_NCS_Release_fqj8j6.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/Darkness",
                "ncsLink": "http://NCS.io/Darkness",
                "ncsWatch": "http://youtu.be/ScSn235gQx0"
            },
            {
                "title": "Nobody",
                "artist": "Zack Merci, CRVN",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752004222/Zack_Merci_CRVN_-_Nobody_NCS_Release_z3vaoo.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/ZMCNobody",
                "ncsLink": "http://NCS.io/ZMCNobody",
                "ncsWatch": "http://youtu.be/8xlDwukxjnA"
            },
            {
                "title": "Freedom",
                "artist": "Goodknight.",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003309/Goodknight._-_Freedom_NCS_Release_fs1pgy.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/GFreedom",
                "ncsLink": "http://NCS.io/GFreedom",
                "ncsWatch": "http://youtu.be/zvrMzRVtj1s"
            },
            {
                "title": "Mr. Bully",
                "artist": "CHENDA",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752002197/CHENDA_-_Mr._Bully_NCS_Release_tjxftg.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/MrBully",
                "ncsLink": "http://NCS.io/MrBully",
                "ncsWatch": "http://youtu.be/vGf8pXk3HJs"
            },
            {
                "title": "Ruined My Life",
                "artist": "Shiah Maisel, EBEN, Coopex",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003876/Shiah_Maisel_EBEN_Coopex_-_Ruined_My_Life_NCS_Release_t36euk.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/RuinedMyLife",
                "ncsLink": "http://ncs.io/RuinedMyLife",
                "ncsWatch": "http://youtu.be/pB8ZNnNHWyU"
            },
            {
                "title": "Father",
                "artist": "Diamond Eyes",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003483/Diamond_Eyes_-_Father_NCS_Release_z3k7jg.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/iFather",
                "ncsLink": "http://ncs.io/iFather",
                "ncsWatch": "http://youtu.be/5NTvXKUXEX4"
            },
            {
                "title": "Whispered Promises",
                "artist": "DJ Frog, Nito-Onna, Coopex",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003320/DJ_Frog_Nito-Onna_Coopex_-_Whispered_Promises_NCS_Release_cxtge3.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/WhisperedPromises",
                "ncsLink": "http://NCS.io/WhisperedPromises",
                "ncsWatch": "http://youtu.be/xwcwExC4t7w"
            },
            {
                "title": "Finally Healing",
                "artist": "Abandoned, Shiah Maisel, InfiNoise",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752001962/Abandoned_Shiah_Maisel_InfiNoise_-_Finally_Healing_NCS_Release_r0zobm.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/FinallyHealing",
                "ncsLink": "http://NCS.io/FinallyHealing",
                "ncsWatch": "http://youtu.be/hkas1m6m9AQ"
            },
            {
                "title": "Pray That You'll Be Dead To Me",
                "artist": "Barren Gates, Jon Becker",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752002061/Barren_Gates_Jon_Becker_-_Pray_That_You_ll_Be_Dead_To_Me_NCS_Release_bqs1cm.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/PTYBDTM",
                "ncsLink": "http://ncs.io/PTYBDTM",
                "ncsWatch": "http://youtu.be/XDNSPfIEX2o"
            },
            {
                "title": "Oh Darling",
                "artist": "Unknown Brain",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003857/Unknown_Brain_-_Oh_Darling_NCS_Release_i0zgke.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/OhDarling",
                "ncsLink": "http://ncs.io/OhDarling",
                "ncsWatch": "http://youtu.be/gdnzYaTcypw"
            },
            {
                "title": "Let You Go (ft. NotEvenTanner)",
                "artist": "Unknown Brain, NotEvenTanner",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752004213/Unknown_Brain_NotEvenTanner_-_Let_You_Go_NCS_Release_mavyaa.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/UBLetYouGo",
                "ncsLink": "http://ncs.io/UBLetYouGo",
                "ncsWatch": "http://youtu.be/gdnzYaTcypw"
            },
            {
                "title": "Pain (feat. Mia Vaile)",
                "artist": "Ship Wrek, Mia Vaile",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752003886/Ship_Wrek_Mia_Vaile_-_Pain_feat._Mia_Vaile_NCS_Release_uxdffw.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/pain",
                "ncsLink": "http://ncs.io/pain",
                "ncsWatch": "http://youtu.be/UDEpRK8WL_I"
            }
    ],
    "energetic": [
            {
                "title": "Royalty",
                "artist": "Maestro Chives, Egzod, Neoni",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753512746/Maestro_Chives_Egzod_Neoni_-_Royalty_NCS_Release_znjgbe.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Royalty",
                "ncsLink": "http://ncs.io/Royalty",
                "ncsWatch": "http://ncs.lnk.to/RoyaltyAT/youtube"
            },
            {
                "title": "Ark",
                "artist": "Ship Wrek, Zookeepers",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752004900/Ship_Wrek_-_Ark_NCS_Release_n7estd.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/ark",
                "ncsLink": "http://ncs.io/ark",
                "ncsWatch": "http://youtu.be/8xlDwukxjnA"
            },
            {
                "title": "Nekozilla",
                "artist": "Different Heaven",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752004877/Different_Heaven_-_Nekozilla_NCS_Release_wbfroz.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/nekozilla",
                "ncsLink": "http://ncs.io/nekozilla",
                "ncsWatch": "http://youtu.be/6FNHe3kf8_s"
            },
            {
                "title": "Cradles",
                "artist": "Sub Urban",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752006216/Sub_Urban_-_Cradles_NCS_Release_p6trkk.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Cradles",
                "ncsLink": "http://ncs.io/Cradles",
                "ncsWatch": "http://youtu.be/Hn4sfC2PbhI"
            },
            {
                "title": "Invisible",
                "artist": "Julius Dreisig, Zeus X Crona",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752006219/Zeus_X_Crona_-_Invisible_NCS_Release_jbgkwb.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Invisible",
                "ncsLink": "http://ncs.io/Invisible",
                "ncsWatch": "http://youtu.be/QglaLzo_aPk"
            },
            {
                "title": "Shine (Neddie Flip)",
                "artist": "Spektrem, Neddie",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752006224/Neddie_Spektrem_-_Shine_Neddie_Flip_NCS_Release_vgnxzf.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Shine_NF",
                "ncsLink": "http://ncs.io/Shine_NF",
                "ncsWatch": "http://ncs.lnk.to/Shine_NFAT/youtube"
            },
            {
                "title": "Why We Lose (feat. Coleman Trapp)",
                "artist": "Cartoon, Jéja, Coleman Trapp",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752004890/Cartoon_Coleman_Trapp_J%C3%A9ja_-_Why_We_Lose_feat._Coleman_Trapp_NCS_Release_ytcmjz.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/whywelose",
                "ncsLink": "http://ncs.io/whywelose",
                "ncsWatch": "http://youtu.be/zyXmsVwZqX4"
            },
            {
                "title": "Sky High",
                "artist": "Elektronomia",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752006220/Elektronomia_-_Sky_High_NCS_Release_nwiyyn.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/skyhigh",
                "ncsLink": "http://ncs.io/skyhigh",
                "ncsWatch": "http://youtu.be/TW9d8vYrVFQ"
            },
            {
                "title": "Mortals (feat. Laura Brehm)",
                "artist": "Warriyo, Laura Brehm",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752006210/Warriyo_Laura_Brehm_-_Mortals_feat._Laura_Brehm_NCS_Release_grwxgm.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/mortals",
                "ncsLink": "http://ncs.io/mortals",
                "ncsWatch": "http://youtu.be/yJg-Y5byMMw"
            },
            {
                "title": "Heroes Tonight (feat. Johnning)",
                "artist": "Janji, Johnning",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752004972/Janji_Johnning_-_Heroes_Tonight_feat._Johnning_NCS_Release_geoo8v.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/ht",
                "ncsLink": "http://ncs.io/ht",
                "ncsWatch": "http://youtu.be/3nQNiWdeH2Q"
            }
    ],
    "calm": [
            {
                "title": "Cruising",
                "artist": "Dosi & Aisake",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752040699/Aisake_Dosi_-_Cruising_NCS_Release_sbcgbj.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Cruising",
                "ncsLink": "http://ncs.io/Cruising",
                "ncsWatch": "http://ncs.lnk.to/CruisingAT/youtube"
            },
            {
                "title": "Moon Farewell",   
                "artist": "Wiguez",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041748/Wiguez_Alltair_Josh_Levoid_P-One_-_Moon_Farewell_NCS_Release_tufqam.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.lnk.to/MoonFarewell",
                "ncsLink": "http://NCS.lnk.to/MoonFarewell",
                "ncsWatch": "http://NCS.lnk.to/MoonFarewellAT/youtube"
            },
            {
                "title": "Love U",
                "artist": "intouch",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041781/intouch_-_Love_U_NCS_Release_oy8og7.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.lnk.to/it-LoveU",
                "ncsLink": "http://ncs.lnk.to/it-LoveU",
                "ncsWatch": "http://ncs.lnk.to/it-LoveUAT/youtube"
            },
            {
                "title": "I Like It",
                "artist": "Defx x P for Parker x Fame Sounds",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041597/Fame_Sounds_P_for_Parker_Defx_-_I_Like_It_NCS_Release_gmjhnj.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/ILikeIt",
                "ncsLink": "http://ncs.io/ILikeIt",
                "ncsWatch": "http://ncs.io/ILikeItAT/youtube"
            },
            {
                "title": "Alright",
                "artist": "Avi Snow, Sync",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041616/Sync_Avi_Snow_Marky_Style_-_Alright_NCS_Release_dftkqh.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Alright",
                "ncsLink": "http://ncs.io/Alright",
                "ncsWatch": "http://ncs.lnk.to/AlrightAT/youtube"
            },
            {
                "title": "GO ₊˚✩⋆｡°",
                "artist": "Sam Day",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041501/Sam_Day_-_GO_NCS_Release_vzokr7.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/SD_GO",
                "ncsLink": "http://ncs.io/SD_GO",
                "ncsWatch": "http://ncs.lnk.toAT/youtube"
            },
            {
                "title": "For You (ft. Snnr)",
                "artist": "T & Sugah",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752040559/T_Sugah_Snnr_-_For_You_ft._Snnr_NCS_Release_r6l8sa.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream:",
                "ncsLink": "",
                "ncsWatch": ""
            },
            {
                "title": "Heart My Heart",
                "artist": "intouch",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041421/intouch_-_Heart_My_Heart_NCS_Release_usrjii.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/heartmyheart",
                "ncsLink": "http://ncs.io/heartmyheart",
                "ncsWatch": "http://ncs.io/heartmyheartAT/youtube"
            },
            {
                "title": "Reason (feat. Remy Night)",
                "artist": "MANIA",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041353/MANIA_Remy_Night_-_Reason_ft._Remy_Night_NCS_Release_axtpcx.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Reason",
                "ncsLink": "http://ncs.io/Reason",
                "ncsWatch": "AT/youtube"
            },
            {
                "title": "No Way (with Avi Snow)",
                "artist": "BIMINI",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041506/BIMINI_Avi_Snow_-_No_Way_with_Avi_Snow_NCS_Release_i5btpu.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/noway",
                "ncsLink": "http://ncs.io/noway",
                "ncsWatch": "AT/youtube"
            },
            {
                "title": "Baby Sweet",
                "artist": "intouch",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041287/intouch_-_Baby_Sweet_NCS_Release_mjjcbt.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/babysweet",
                "ncsLink": "http://ncs.io/babysweet",
                "ncsWatch": "http://ncs.lnk.to/babysweetAT/youtube"
            },
            {
                "title": "Are You With Me",
                "artist": "PLVTO",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041443/PLVTO_-_Are_You_With_Me_NCS_Release_kplgce.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/AYMW",
                "ncsLink": "http://ncs.io/AYMW",
                "ncsWatch": "http://ncs.lnk.to/AYMWAT/youtube"
            },
            {
                "title": "BABY",
                "artist": "Sam Day",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041304/Sam_Day_-_BABY_NCS_Release_fg9obs.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/baby",
                "ncsLink": "http://ncs.io/baby",
                "ncsWatch": "http://ncs.lnk.to/babyAT/youtube"
            },
            {
                "title": "NEBRASKA (WITH YOU)",
                "artist": "Sam Day",
                "file": "",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/NEBRASKA_WY",
                "ncsLink": "http://ncs.io/NEBRASKA_WY",
                "ncsWatch": "http://ncs.lnk.to/NEBRASKA_WYAT/youtube"
            },
            {
                "title": "Hold You",
                "artist": "Low Mileage",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041913/Low_Mileage_-_Hold_You_NCS_Release_cjdhoj.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/holdyou",
                "ncsLink": "http://ncs.io/holdyou",
                "ncsWatch": "http://ncs.lnk.to/holdyouAT/youtube"
            },
            {
                "title": "Tidal Wave",
                "artist": "KHEMIS, Coopex, ZANA",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041792/ZANA_Coopex_KHEMIS_-_Tidal_Wave_NCS_Release_bloymq.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/TIdalWave",
                "ncsLink": "http://ncs.io/TIdalWave",
                "ncsWatch": "http://ncs.lnk.to/TIdalWaveAT/youtube"
            },
            {
                "title": "More",
                "artist": "Asketa & Natan Chaim",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041876/Natan_Chaim_Asketa_-_More_NCS_Release_w44rw0.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/more",
                "ncsLink": "http://ncs.io/more",
                "ncsWatch": "http://ncs.lnk.to/moreAT/youtube"
            },
            {
                "title": "Follow (feat. Vikki Gilmore)",
                "artist": "T-Mass & Rain Main",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041859/T-Mass_Rain_Man_Vikki_Gilmore_-_Follow_NCS_Release_ueg9ry.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Follow",
                "ncsLink": "http://ncs.io/Follow",
                "ncsWatch": "http://youtu.be/ScSn235gQx0"
            },
            {
                "title": "Need Ya",
                "artist": "Syn Cole",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752041806/Syn_Cole_-_Need_Ya_NCS_Release_as9rzg.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/NeedYa",
                "ncsLink": "http://NCS.io/NeedYa",
                "ncsWatch": "http://youtu.be/ScSn235gQx0"
            },
            {
                "title": "Me Times Two (Ft. Moav)",
                "artist": "Raptures",
                "file": "http://res.cloudinary.com/dfudjyqrj/video/upload/v1752040553/Moav_Raptures._-_Me_Times_Two_Ft._Moav_NCS_Release_trjxg5.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://NCS.io/RMMeTimesTwo",
                "ncsLink": "http://NCS.io/RMMeTimesTwo",
                "ncsWatch": "http://youtu.be/ScSn235gQx0"
            }
    ],
    "romantic": [
            {
                "title": "Dreams pt. II (feat. Sara Skinner)",
                "artist": "Lost Sky, Sara Skinner",
                "file": "/static/romantic/Lost Sky, Sara Skinner - Dreams pt. II (feat. Sara Skinner) [NCS Release].mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Dreams2",
                "ncsLink": "http://ncs.io/Dreams2",
                "ncsWatch": "http://youtu.be/L7kF4MXXCoA"
            },
            {
                "title": "Light It Up (feat. Jex)",
                "artist": "Robin Hustin, Tobimorrow",
                "file": "/static/romantic/Robin Hustin, Tobimorrow - Light It Up [NCS Release].mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/LightItUp",
                "ncsLink": "http://ncs.io/LightItUp",
                "ncsWatch": "http://youtu.be/bdE_SyHad90"
            },
            {
                "title": "ghost",
                "artist": "youth",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144235/youth_-_ghost_NCS_Release_ro3ybu.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/youthghost",
                "ncsLink": "http://ncs.io/youthghost",
                "ncsWatch": "http://ncs.lnk.to/AT/youtube"
            },
            {
                "title": "X2",
                "artist": "mupp",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144259/MUPP_-_X2_NCS_Release_e3ihtp.mp3",
                "copyright": "Music provided by NoCopyrig   htSounds. Free Download/Stream: http://ncs.io/MUPPX2",
                "ncsLink": "http://ncs.io/MUPPX2",
                "ncsWatch": "http://ncs.lnk.to/MUPPX2AT/youtube"
            },
            {
                "title": "Around Us (ft. Pasha & Carlos Ukareda)",
                "artist": "Cartoon, NCT",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144241/Pasha_Carlos_Ukareda_VALLO_NCT_Cartoon_-_Around_Us_ft._Pasha_Carlos_Ukareda_NCS_Release_pgggt0.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/AroundUs",
                "ncsLink": "http://ncs.io/AroundUs",
                "ncsWatch": "http://ncs.lnk.to/AroundUsAT/youtube"
            },
            {
                "title": "Call My Name",
                "artist": "Janji, Robbie Hutton",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144273/Robbie_Hutton_Janji_-_Call_My_Name_NCS_Release_aaocbl.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/CallMyName",
                "ncsLink": "http://ncs.io/CallMyName",
                "ncsWatch": "http://ncs.lnk.to/CallMyNameAT/youtube"
            },
            {
                "title": "From The Top",
                "artist": "Ariis",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143829/Ariis_-_From_The_Top_NCS_Release_q4a9xe.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/FromTheTop",
                "ncsLink": "http://ncs.io/FromTheTop",
                "ncsWatch": "http://ncs.lnk.to/FromTheTopAT/youtube"
            },
            {
                "title": "Baby Sweet (Tails Remix)",
                "artist": "intouch",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143838/Tails_intouch_-_Baby_Sweet_Tails_Remix_NCS_Release_rswb8u.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/BS_Tails",
                "ncsLink": "http://ncs.io/BS_Tails",
                "ncsWatch": "http://ncs.lnk.to/BS_TailsAT/youtube"
            },
            {
                "title": "Magnetic",
                "artist": "springs!",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143723/springs_-_Magnetic_NCS_Release_fisfcw.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Magnetic",
                "ncsLink": "http://ncs.io/Magnetic",
                "ncsWatch": "http://ncs.lnk.to/MagneticAT/youtube"
            },
            {
                "title": "Look No Further (ft Grace Luisa)",
                "artist": "Madison Mars",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143603/Grace_Luisa_Madison_Mars_-_Look_No_Further_ft_Grace_Luisa_NCS_Release_plhpid.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/LookNoFurther",
                "ncsLink": "http://ncs.io/LookNoFurther",
                "ncsWatch": "http://ncs.lnk.to/LookNoFurtherAT/youtube"
            },
            {
                "title": "Win & Lose",
                "artist": "Chime",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144389/Chime_-_Win_Lose_NCS_Release_ycljfw.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/WinAndLose",
                "ncsLink": "http://ncs.io/WinAndLose",
                "ncsWatch": "http://ncs.lnk.to/WinAndLoseAT/youtube"
            },
            {
                "title": "Always Be",
                "artist": "Netrum",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143603/Netrum_-_Always_Be_NCS_Release_ic9gsh.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/AlwaysBe",
                "ncsLink": "http://ncs.io/AlwaysBe",
                "ncsWatch": "http://ncs.lnk.to/AlwaysBeAT/youtube"
            },
            {
                "title": "Jealous",
                "artist": "The Trinity",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143646/The_Trinity_-_jealous_NCS_Release_fyhvid.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Jealous",
                "ncsLink": "http://ncs.io/Jealous",
                "ncsWatch": "http://ncs.lnk.to/JealousAT/youtube"
            },
            {
                "title": "Nostalgia",
                "artist": "Janji & Johnning",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143789/Johnning_Janji_-_Nostalgia_NCS_Release_gb4jzl.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/JJ_Nostalgia",
                "ncsLink": "http://ncs.io/JJ_Nostalgia",
                "ncsWatch": "http://ncs.lnk.to/JJ_NostalgiaAT/youtube"
            },
            {
                "title": "Underrated (Feat. Sunny Lukas)",
                "artist": "Zushi & Vanko",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143724/Sunny_Lukas_Zushi_Vanko_-_Underrated_Feat._Sunny_Lukas_NCS_Release_wcoq1y.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Underrated",
                "ncsLink": "http://ncs.io/Underrated",
                "ncsWatch": "http://ncs.lnk.to/UnderratedAT/youtube"
            },
            {
                "title": "Red Lights",
                "artist": "Cafe Disko & Ella Rosa",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752143649/Ella_Rosa_Cafe_Disko_-_Red_Lights_NCS_Release_uitnno.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/RedLights",
                "ncsLink": "http://ncs.io/RedLights",
                "ncsWatch": "http://ncs.lnk.to/RedLightsAT/youtube"
            },
            {
                "title": "Purpose",
                "artist": "Aeden & Sketchez",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144291/Sketchez_Aeden_-_Purpose_NCS_Release_ac1evq.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Purpose",
                "ncsLink": "http://ncs.io/Purpose",
                "ncsWatch": "http://ncs.lnk.to/PurposeAT/youtube"
            },
            {
                "title": "Donna (feat. maria kallastu)",
                "artist": "Soundy x Sander Mölder",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144309/maria_kallastu_Sander_M%C3%B6lder_Soundy_-_Donna_NCS_Release_vg1wg0.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Donna",
                "ncsLink": "http://ncs.io/Donna",
                "ncsWatch": "http://ncs.lnk.to/DonnaAT/youtube"
            },
            {
                "title": "Vibe",
                "artist": "Spicyverse",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144242/Spicyverse_-_Vibe_NCS_Release_ofzcl1.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/SV_Vibe",
                "ncsLink": "http://ncs.io/SV_Vibe",
                "ncsWatch": "http://ncs.lnk.to/SV_VibeAT/youtube"
            },
            {
                "title": "Stars in the Sky",
                "artist": "BEKSY.",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1752144271/BEKSY._-_Stars_in_the_Sky_NCS_Release_ggvzlh.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/SITS",
                "ncsLink": "http://ncs.io/SITS",
                "ncsWatch": "http://ncs.lnk.to/SITSAT/youtube"
            }
    ],
    "glamorous": [
            {
                "title": "Seasons (feat. Harley Bird)",
                "artist": "Rival x Cadmium",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753512032/Rival_Cadmium_Harley_Bird_-_Seasons_feat._Harley_Bird_NCS_Release_fljlbv.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Seasons",
                "ncsLink": "http://ncs.io/Seasons",
                "ncsWatch": "http://youtu.be/Nl_4MWNh08I"
            },
            {
                "title": "Too Far Gone",
                "artist": "Inukshuk",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753511787/Inukshuk_-_Too_Far_Gone_NCS_Release_gazxs9.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/TooFarGone",
                "ncsLink": "http://ncs.io/TooFarGone",
                "ncsWatch": "http://youtu.be/60XUgHQo71Q"
            },
            {
                "title": "Why So Serious",
                "artist": "Sync, Roby Fayer, Eytan Peled",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753511763/Eytan_Peled_Roby_Fayer_Sync_-_Why_So_Serious_NCS_Release_xrfx6f.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/WSS",
                "ncsLink": "http://ncs.io/WSS",
                "ncsWatch": "http://ncs.lnk.to/WSSAT/youtube"
            },
            {
                "title": "Wonder (ft. Rarin & Bri Tolani)",
                "artist": "Unknown Brain",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753425740/Rarin_Bri_Tolani_Unknown_Brain_-_Wonder_ft._Rarin_Bri_Tolani_NCS_Release_ads6ns.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/Wonder",
                "ncsLink": "http://ncs.io/Wonder",
                "ncsWatch": "http://ncs.lnk.to/WonderAT/youtube"
            },
            {
                "title": "AIN'T MISS A CALL",
                "artist": "Guy Arthur",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753511787/Guy_Arthur_-_AIN_T_MISS_A_CALL_NCS_Release_iphhuo.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/AMAC",
                "ncsLink": "http://ncs.io/AMAC",
                "ncsWatch": "http://ncs.lnk.to/AMACAT/youtube"
            },
            {
                "title": "Follow Back",
                "artist": "LXNGVX",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753425276/LXNGVX_-_Follow_Back_NCS_Release_kxkbzi.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/FollowBack",
                "ncsLink": "http://ncs.io/FollowBack",
                "ncsWatch": "http://ncs.lnk.to/FollowBackAT/youtube"
            },
            {
                "title": "My Heart Is Broken",
                "artist": "NEYVO",
                "file": "https://res.cloudinary.com/dfudjyqrj/video/upload/v1753511767/NEYVO_-_My_Heart_Is_Broken_NCS_Release_gjs9ws.mp3",
                "copyright": "Music provided by NoCopyrightSounds. Free Download/Stream: http://ncs.io/MHIB",
                "ncsLink": "http://ncs.io/MHIB",
                "ncsWatch": "http://ncs.lnk.to/MHIBAT/youtube"
            }
    ]
  }
}
