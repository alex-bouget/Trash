from PIL import Image, ImageFont, ImageDraw
import os


def Card_Model(card_name, card_data, rarity_data, bdd_folder, lang_use):
    """
    Load Card_model in Pillow Image with rarity layers, card head, name with lang and price

    :param card_name:
    :param card_data:
    :param rarity_data:
    :param bdd_folder:
    :param lang_use:
    :return card:
    """
    name = card_data["name"][lang_use]
    desc = card_data["description"][lang_use]
    price = card_data["price"]
    data = []
    for img in rarity_data:  # Get rarity layers and found head layers
        if img == "head":
            data.append("head")
        else:
            data.append(Image.open(os.path.join(bdd_folder, "rarity", img)).convert("RGBA"))
    head_index = data.index("head")  # get index of head layers
    if os.path.isfile(os.path.join(bdd_folder, "head", card_name + ".png")):  # load card head or error head
        head = Image.open(os.path.join(bdd_folder, "head", card_name + ".png")).convert("RGBA")
    else:
        head = Image.open(os.path.join(bdd_folder, "head", "error.png")).convert("RGBA")

    data[head_index] = Image.new("RGBA", data[0].size)
    if head.size == data[head_index].size:
        data[head_index].paste(head, (0, 0), head)
    else:
        data[head_index].paste(head, (100, 104), head)
    card = Image.new("RGBA", data[0].size)
    for layer in data:
        card.paste(layer, (0, 0), layer)
    draw = ImageDraw.Draw(card)  # draw name, description and price
    draw.text((600, 52), name, (0, 0, 0), anchor="mm",
              font=ImageFont.truetype(os.path.join(bdd_folder, "font.ttf"), 75))
    draw.text((600, 1187), "\n".join(desc.split("=_=")), (0, 0, 0), anchor="mm",
              font=ImageFont.truetype(os.path.join(bdd_folder, "font.ttf"), 75))
    draw.text((600, 1529), price + "E", (0, 0, 0), anchor="mm",
              font=ImageFont.truetype(os.path.join(bdd_folder, "font.ttf"), 60))
    return card
