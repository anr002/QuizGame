import requests
import shutil

gods = [
{"name": "Achilles", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/5a/T_Achilles_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20180227153129"}, {"name": "Agni", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/90/T_Agni_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140305171831"}, {"name": "AMC", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/99/T_AMC_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131107140006"}, {"name": "AhPuch", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/8b/T_AhPuch_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150428141250"}, {"name": "Amaterasu", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/9b/T_Amaterasu_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160107232457"}, {"name": "Anhur", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/db/T_Anhur_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131002124558"}, {"name": "Anubis", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/13/T_Anubis_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150512105740"}, {"name": "AoKuang", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/33/T_AoKuang_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20141011061602"}, {"name": "Aphrodite", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/16/T_Aphrodite_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20141115065255"}, {"name": "Apollo", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/dc/T_Apollo_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20220201022344"}, {"name": "Arachne", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/f/f9/T_Arachne_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160426085330"}, {"name": "Ares", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/35/T_Ares_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20200715231638"}, {"name": "Artemis", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/41/T_Artemis_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20230516192533"}, {"name": "Artio", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/9f/T_Artio_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170801121012"}, {"name": "Athena", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/80/T_Athena_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20210518144418"}, {"name": "Atlas", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/15/T_Atlas_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20211128200121"}, {"name": "Awilix", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/30/T_Awilix_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20141213035001"}, {"name": "BabaYaga", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/15/T_BabaYaga_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20200403194247"}, {"name": "Bacchus", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/f/ff/T_Bacchus_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170606043914"}, {"name": "Bakasura", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/51/T_Bakasura_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20141011061659"}, {"name": "BakeKujira", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/da/T_BakeKujira_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20231207083409"}, {"name": "BaronSamedi", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/ef/T_BaronSamedi_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20180616064642"}, {"name": "Bastet", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/ee/T_Bastet_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140402111043"}, {"name": "Bellona", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/4d/T_Bellona_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150206030947"}, {"name": "Cabrakan", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/4a/T_Cabrakan_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140816080241"}, {"name": "Camazotz", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/50/T_Camazotz_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160923201754"}, {"name": "Cerberus", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/44/T_Cerberus_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20180109193501"}, {"name": "Cernunnos", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/5f/T_Cernunnos_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170309023249"}, {"name": "Chaac", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/20/T_Chaac_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150324011705"}, {"name": "ChangE", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/9d/T_ChangE_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131218155336"}, {"name": "Charon", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/ee/T_Charon_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20230711192207"}, {"name": "Charybdis", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/d7/T_Charybdis_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20210824201522"}, {"name": "Chernobog", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/e3/T_Chernobog_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20180515160022"}, {"name": "Chiron", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/a/a6/T_Chiron_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20151111224639"}, {"name": "Chronos", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/88/T_Chronos_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20130710101705"}, {"name": "Cliodhna", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/d4/T_Cliodhna_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20211019210353"}, {"name": "Cthulhu", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/90/T_Cthulhu_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20200530233848"}, {"name": "CuChulainn", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/3d/T_CuChulainn_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170615153314"}, {"name": "Cupid", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/5d/T_Cupid_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20130828111033"}, {"name": "DaJi", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/41/T_DaJi_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170518015424"}, {"name": "Danzaburou", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/7/77/T_Danzaburou_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20201123110649"}, {"name": "Discordia", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/8a/T_Discordia_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20171106222609"}, {"name": "ErLangShen", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/9d/T_ErLangShen_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160630032018"}, {"name": "Eset", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/d8/T_Eset_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20191112174755"}, {"name": "Fafnir", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/6/6d/T_Fafnir_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160602154711"}, {"name": "Fenrir", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/93/T_Fenrir_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140108151348"}, {"name": "Freya", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/29/T_Freya_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160719100447"}, {"name": "Ganesha", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/8b/T_Ganesha_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170420083454"}, {"name": "Geb", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/b/be/T_Geb_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140116122829"}, {"name": "Gilgamesh", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/58/T_Gilgamesh_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20210406205038"}, {"name": "GuanYu", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/e7/T_GuanYu_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20130828111229"}, {"name": "Hachiman", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/2b/T_Hachiman_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170913151851"}, {"name": "Hades", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/83/T_Hades_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20130918202732"}, {"name": "HeBo", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/0/01/T_HeBo_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131113162558"}, {"name": "Heimdallr", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/59/T_Heimdallr_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20191211174152"}, {"name": "Hel", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/c/c6/T_Hel_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131009101308"}, {"name": "Hera", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/f/fa/T_Hera_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20181006021330"}, {"name": "Hercules", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/f/f0/T_Hercules_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140611104249"}, {"name": "Horus", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/5b/T_Horus_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20190725150726"}, {"name": "HouYi", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/7/77/T_HouYi_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150109061556"}, {"name": "HunBatz", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/20/T_HunBatz_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20130620102421"}, {"name": "Ishtar", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/b/bc/T_Ishtar_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20220823041512"}, {"name": "IxChel", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/99/T_IxChel_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20230416212712"}, {"name": "Izanami", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/6/6f/T_Izanami_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160827073027"}, {"name": "Janus", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/33/T_Janus_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140523094912"}, {"name": "JingWei", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/e9/T_JingWei_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160407050420"}, {"name": "Jormungandr", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/2a/T_Jormungandr_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20190725150728"}, {"name": "Kali", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/15/T_Kali_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131211111749"}, {"name": "Khepri", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/24/T_Khepri_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150804123805"}, {"name": "KingArthur", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/8a/T_KingArthur_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20181222025858"}, {"name": "Kukulkan", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/7/76/T_Kukulkan_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140907045704"}, {"name": "Kumbhakarna", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/6/67/T_Kumbhakarna_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140413085852"}, {"name": "Kuzenbo", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/2c/T_Kuzenbo_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170210055446"}, {"name": "Lancelot", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/43/T_Lancelot_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20220611002111"}, {"name": "Loki", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/c/c6/T_Loki_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150721140839"}, {"name": "MamanBrigitte", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/0/0d/T_MamanBrigitte_Default_Icon.png/revision/latest/scale-to-width-down/50?cb=20230918193118"}, {"name": "Martichoras", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/dd/T_Martichoras_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20230213175101"}, {"name": "Maui", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/b/bd/T_Maui_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20221018195205"}, {"name": "Medusa", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/d/d6/T_Medusa_Dragonshifter_Icon.png/revision/latest/scale-to-width-down/50?cb=20230825160751"}, {"name": "Mercury", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/6/6a/T_Mercury_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131002124832"}, {"name": "Merlin", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/0/0b/T_Merlin_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20190123200830"}, {"name": "MorganLeFay", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/2/2c/T_MorganLeFay_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20210529122823"}, {"name": "Mulan", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/37/T_Mulan_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20200226000013"}, {"name": "NeZha", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/91/T_NeZha_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20151214152142"}, {"name": "Neith", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/f/fc/T_Neith_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150324011722"}, {"name": "Nemesis", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/0/03/T_Nemesis_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140206130112"}, {"name": "Nike", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/17/T_Nike_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20161201002949"}, {"name": "Nox", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/95/T_Nox_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20141025053437"}, {"name": "NuWa", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/88/T_NuWa_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140802122240"}, {"name": "Odin", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/36/T_Odin_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140108151641"}, {"name": "Olorun", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/8a/T_Olorun_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20190725150734"}, {"name": "Osiris", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/39/T_Osiris_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140503031024"}, {"name": "Pele", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/c/c8/T_Pele_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20180728014558"}, {"name": "Persephone", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/6/61/T_Persephone_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20190809070856"}, {"name": "Poseidon", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/a/a9/T_Poseidon_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170327235107"}, {"name": "Ra", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/49/T_Ra_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150206031107"}, {"name": "Raijin", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/92/T_Raijin_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160211044638"}, {"name": "Rama", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/eb/T_Ram_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140621052437"}, {"name": "Ratatoskr", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/e4/T_Ratatoskr_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150602174529"}, {"name": "Ravana", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/3/3d/T_Ravana_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150630143930"}, {"name": "Scylla", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/c/c3/T_Scylla_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140305171820"}, {"name": "Serqet", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/c/c0/T_Serqet_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140712121145"}, {"name": "Set", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/e0/T_Set_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20190725150739"}, {"name": "Shiva", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/53/T_Shiva_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20220206020947"}, {"name": "Skadi", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/85/T_Skadi_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160310035911"}, {"name": "Sobek", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/b/b1/T_Sobek_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20210323080301"}, {"name": "Sol", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/9b/T_Sol_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20151001001754"}, {"name": "SunWukong", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/17/T_SunWukong_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140319115339"}, {"name": "Surtr", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/43/T_Surtr_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20230120213053"}, 
        {"name": "Susano", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/8f/T_Susano_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160504234521"}, 
        {"name": "Sylvanus", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/1e/T_Sylvanus_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140927154431"}, 
        {"name": "Terra", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/8/87/T_Terra_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20160728140202"}, 
        {"name": "Thanatos", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/c/cd/T_Thanatos_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20130918203013"}, 
        {"name": "TheMorrigan", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/a/a4/T_TheMorrigan_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170106025216"}, 
        {"name": "Thor", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/6/60/T_Thor_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20130918212445"}, 
        {"name": "Thoth", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/0/05/T_Thoth_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20161103071335"}, 
        {"name": "Tiamat", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/6/61/T_Tiamat_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20210206005516"}, 
        {"name": "Tsukuyomi", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/b/b8/T_Tsukuyomi_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20200725213152"}, 
        {"name": "Tyr", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/56/T_Tyr_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20141126183939"}, 
        {"name": "Ullr", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/4/41/T_Ullr_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140319115351"}, 
        {"name": "Vamana", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/c/cb/T_Vamana_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20170125131004"}, 
        {"name": "Vulcan", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/a/a6/T_Vulcan_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20131120115058"}, 
        {"name": "Xbalanque", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/5b/T_Xbalanque_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150206031135"}, 
        {"name": "XingTian", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/1/1a/T_XingTian_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150827233834"}, 
        {"name": "Yemoja", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/e/ec/T_Yemoja_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20191015181619"}, 
        {"name": "Ymir", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/f/f4/T_Ymir_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150219021054"}, 
        {"name": "YuHuang", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/7/79/T_YuHuang_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20220416031228"}, 
        {"name": "Zeus", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/9/96/T_Zeus_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20140802122401"},
        {"name": "ZhongKui", "icon": "https://static.wikia.nocookie.net/smite_gamepedia/images/5/59/T_ZhongKui_Default_Icon.png/revision/latest/scale-to-width-down/96?cb=20150311043555"}
]

for god in gods:
    response = requests.get(god['icon'], stream=True)
    response.raise_for_status()

    with open(f"{god['name']}.png", 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)