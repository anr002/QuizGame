import re
import json

text = """
T Achilles Default IconTransparent God Icon
Achilles
T Agni Default IconTransparent God Icon
Agni
T AhMuzenCab Default IconTransparent God Icon
Ah Muzen Cab
T AhPuch Default IconTransparent God Icon
Ah Puch
T Amaterasu Default IconTransparent God Icon
Amaterasu
T Anhur Default IconTransparent God Icon
Anhur
T Anubis Default IconTransparent God Icon
Anubis
T AoKuang Default IconTransparent God Icon
Ao Kuang
T Aphrodite Default IconTransparent God Icon
Aphrodite
T Apollo Default IconTransparent God Icon
Apollo
T Arachne Default IconTransparent God Icon
Arachne
T Ares Default IconTransparent God Icon
Ares
T Artemis Default IconTransparent God Icon
Artemis
T Artio Default IconTransparent God Icon
Artio
T Athena Default IconTransparent God Icon
Athena
T Atlas Default IconTransparent God Icon
Atlas
T Awilix Default IconTransparent God Icon
Awilix
T BabaYaga Default IconTransparent God Icon
Baba Yaga
T Bacchus Default IconTransparent God Icon
Bacchus
T Bakasura Default IconTransparent God Icon
Bakasura
T BakeKujira Default IconTransparent God Icon
Bake Kujira
T BaronSamedi Default IconTransparent God Icon
Baron Samedi
T Bastet Default IconTransparent God Icon
Bastet
T Bellona Default IconTransparent God Icon
Bellona
T Cabrakan Default IconTransparent God Icon
Cabrakan
T Camazotz Default IconTransparent God Icon
Camazotz
T Cerberus Default IconTransparent God Icon
Cerberus
T Cernunnos Default IconTransparent God Icon
Cernunnos
T Chaac Default IconTransparent God Icon
Chaac
T Chang'e Default IconTransparent God Icon
Chang'e
T Charon Default IconTransparent God Icon
Charon
T Charybdis Default IconTransparent God Icon
Charybdis
T Chernobog Default IconTransparent God Icon
Chernobog
T Chiron Default IconTransparent God Icon
Chiron
T Chronos Default IconTransparent God Icon
Chronos
T Cliodhna Default IconTransparent God Icon
Cliodhna
T Cthulhu Default IconTransparent God Icon
Cthulhu
T CuChulainn Default IconTransparent God Icon
Cu Chulainn
T Cupid Default IconTransparent God Icon
Cupid
T DaJi Default IconTransparent God Icon
Da Ji
T Danzaburou Default IconTransparent God Icon
Danzaburou
T Discordia Default IconTransparent God Icon
Discordia
T ErlangShen Default IconTransparent God Icon
Erlang Shen
T Eset Default IconTransparent God Icon
Eset
T Fafnir Default IconTransparent God Icon
Fafnir
T Fenrir Default IconTransparent God Icon
Fenrir
T Freya Default IconTransparent God Icon
Freya
T Ganesha Default IconTransparent God Icon
Ganesha
T Geb Default IconTransparent God Icon
Geb
T Gilgamesh Default IconTransparent God Icon
Gilgamesh
T GuanYu Default IconTransparent God Icon
Guan Yu
T Hachiman Default IconTransparent God Icon
Hachiman
T Hades Default IconTransparent God Icon
Hades
T HeBo Default IconTransparent God Icon
He Bo
T Heimdallr Default IconTransparent God Icon
Heimdallr
T Hel Default IconTransparent God Icon
Hel
T Hera Default IconTransparent God Icon
Hera
T Hercules Default IconTransparent God Icon
Hercules
T Horus Default IconTransparent God Icon
Horus
T HouYi Default IconTransparent God Icon
Hou Yi
T HunBatz Default IconTransparent God Icon
Hun Batz
T Ishtar Default IconTransparent God Icon
Ishtar
T IxChel Default IconTransparent God Icon
Ix Chel
T Izanami Default IconTransparent God Icon
Izanami
T Janus Default IconTransparent God Icon
Janus
T JingWei Default IconTransparent God Icon
Jing Wei
T Jormungandr Default IconTransparent God Icon
Jormungandr
T Kali Default IconTransparent God Icon
Kali
T Khepri Default IconTransparent God Icon
Khepri
T KingArthur Default IconTransparent God Icon
King Arthur
T Kukulkan Default IconTransparent God Icon
Kukulkan
T Kumbhakarna Default IconTransparent God Icon
Kumbhakarna
T Kuzenbo Default IconTransparent God Icon
Kuzenbo
T Lancelot Default IconTransparent God Icon
Lancelot
T Loki Default IconTransparent God Icon
Loki
T MamanBrigitte Default IconTransparent God Icon
Maman Brigitte
T Martichoras Default IconTransparent God Icon
Martichoras
T Maui Default IconTransparent God Icon
Maui
T Medusa Default IconTransparent God Icon
Medusa
T Mercury Default IconTransparent God Icon
Mercury
T Merlin Default IconTransparent God Icon
Merlin
T MorganLeFay Default IconTransparent God Icon
Morgan Le Fay
T Mulan Default IconTransparent God Icon
Mulan
T NeZha Default IconTransparent God Icon
Ne Zha
T Neith Default IconTransparent God Icon
Neith
T Nemesis Default IconTransparent God Icon
Nemesis
T Nike Default IconTransparent God Icon
Nike
T Nox Default IconTransparent God Icon
Nox
T NuWa Default IconTransparent God Icon
Nu Wa
T Odin Default IconTransparent God Icon
Odin
T Olorun Default IconTransparent God Icon
Olorun
T Osiris Default IconTransparent God Icon
Osiris
T Pele Default IconTransparent God Icon
Pele
T Persephone Default IconTransparent God Icon
Persephone
T Poseidon Default IconTransparent God Icon
Poseidon
T Ra Default IconTransparent God Icon
Ra
T Raijin Default IconTransparent God Icon
Raijin
T Rama Default IconTransparent God Icon
Rama
T Ratatoskr Default IconTransparent God Icon
Ratatoskr
T Ravana Default IconTransparent God Icon
Ravana
T Scylla Default IconTransparent God Icon
Scylla
T Serqet Default IconTransparent God Icon
Serqet
T Set Default IconTransparent God Icon
Set
T Shiva Default IconTransparent God Icon
Shiva
T Skadi Default IconTransparent God Icon
Skadi
T Sobek Default IconTransparent God Icon
Sobek
T Sol Default IconTransparent God Icon
Sol
T SunWukong Default IconTransparent God Icon
Sun Wukong
T Surtr Default IconTransparent God Icon
Surtr
T Susano Default IconTransparent God Icon
Susano
T Sylvanus Default IconTransparent God Icon
Sylvanus
T Terra Default IconTransparent God Icon
Terra
T Thanatos Default IconTransparent God Icon
Thanatos
T TheMorrigan Default IconTransparent God Icon
The Morrigan
T Thor Default IconTransparent God Icon
Thor
T Thoth Default IconTransparent God Icon
Thoth
T Tiamat Default IconTransparent God Icon
Tiamat
T Tsukuyomi Default IconTransparent God Icon
Tsukuyomi
T Tyr Default IconTransparent God Icon
Tyr
T Ullr Default IconTransparent God Icon
Ullr
T Vamana Default IconTransparent God Icon
Vamana
T Vulcan Default IconTransparent God Icon
Vulcan
T Xbalanque Default IconTransparent God Icon
Xbalanque
T XingTian Default IconTransparent God Icon
Xing Tian
T Yemoja Default IconTransparent God Icon
Yemoja
T Ymir Default IconTransparent God Icon
Ymir
T YuHuang Default IconTransparent God Icon
Yu Huang
T Zeus Default IconTransparent God Icon
Zeus
T ZhongKui Default IconTransparent God Icon
Zhong Kui
"""

# Split the text into lines
lines = text.split("\n")

# Use a regular expression to filter out lines that don't represent god names
god_names = [line for line in lines if not re.match(r"T .* IconTransparent God Icon", line)]

# Now god_names contains only the names of the gods

# Create a list of dictionaries, each containing a god name and a placeholder for the icon URL
gods = [{"name": name, "icon": "placeholder_icon_url"} for name in god_names if name]

# Convert the list to a JSON array
json_array = json.dumps(gods)

print(json_array)