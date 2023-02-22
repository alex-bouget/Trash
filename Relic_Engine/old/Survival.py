import Relic_Engine
from PIL import Image
import json
x= 250
y= 250
seed =  5637 #91234 #5489

root = Relic_Engine.Engine("Survival", 720, 480)
pr = root.procedural_Map()
data = pr.generating_chunk_data(x,y, seed)

def colors_biomes(data):
    data_biomes = json.load(open("biome.json"))
    print(data)
    for biome in data_biomes:
        humidity = [data_biomes[biome]["data"]["humidity"]["minimum"], data_biomes[biome]["data"]["humidity"]["maximum"]]
        latitude = [data_biomes[biome]["data"]["latitude"]["minimum"], data_biomes[biome]["data"]["latitude"]["maximum"]]
        temperature = [data_biomes[biome]["data"]["temperature"]["minimum"], data_biomes[biome]["data"]["temperature"]["maximum"]]
        if data["humidity"] >= humidity[0] and data["humidity"] <= humidity[1]:
            if data["latitude"] >= latitude[0] and data["latitude"] <= latitude[1]:
                if data["temperature"] >= temperature[0] and data["temperature"] <= temperature[1]:
                    return (data_biomes[biome]["data"]["colors"]["R"], data_biomes[biome]["data"]["colors"]["G"], data_biomes[biome]["data"]["colors"]["B"])
    raise Exception



img = Image.new("RGB", (x, y))
for xa in range(x):
    for ya in range(y):
        img.putpixel((xa,ya), colors_biomes(data[xa][ya]))
img.save("g.png")