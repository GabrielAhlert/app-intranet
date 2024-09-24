from PIL import Image, ImageDraw, ImageFont

class Assinatura:
    def __init__(self, image, name, funcao, ramal, unidade, email, telefone):
        self.image = image
        address = ""
        contactRow = ""

        draw = ImageDraw.Draw(self.image)
        fontName = ImageFont.truetype("./agenda/media_assinatura/fonts/Barlow-Bold.ttf", 25)
        positionName = (64, 15)

        fontFunction = ImageFont.truetype("./agenda/media_assinatura/fonts/Barlow-Bold.ttf", 13)
        positionFunction = (64, 42)

        if unidade == "Tapera":
            address = "Sede Administrativa - Tapera/RS"
            contactRow += "(54) 3385-3000"
        elif (unidade == "Ibirubá"):
            address = "Unidade Regional - Ibirubá/RS"
            contactRow += "(54) 3324-9200"
        elif (unidade == "Arroio Grande"):
            address = "Unidade Regional - Arroio Grande/RS"
            contactRow += "(54) 3385-3059"
        elif (unidade == "Posto Victor Graeff"):
            address = "Posto de Combustível - Posto Victor Graeff/RS"
            contactRow += "(54) 3385-3012"
        elif (unidade == "Trevo Selbach" or unidade == "Selbach"):
            address = "Unidade Regional - Selbach/RS"
            contactRow += "(54) 3387-1256"

        contactRow += " - Ramal " + ramal

        fontAddress = ImageFont.truetype("./agenda/media_assinatura/fonts/Barlow-Bold.ttf", 12)
        positionAddress = (92, 68)

        fontPhone = ImageFont.truetype("./agenda/media_assinatura/fonts/Barlow-Regular.ttf", 12)
        positionPhone = (92, 81)

        fontMail = ImageFont.truetype("./agenda/media_assinatura/fonts/Barlow-Regular.ttf", 12)
        positionMail = (92, 101)

        draw.text(positionName, name, font=fontName, fill="black")
        draw.text(positionFunction, funcao, font=fontFunction, fill="#1DB439")
        draw.text(positionAddress, address, font=fontAddress, fill="#1DB439")

        if telefone != "-":
            contactRow += "  |  " + telefone

        draw.text(positionPhone, contactRow, font=fontPhone, fill="black")
        draw.text(positionMail, email, font=fontMail, fill="black")

    def save_file(self, path):
        self.image.save(path, format='PNG')