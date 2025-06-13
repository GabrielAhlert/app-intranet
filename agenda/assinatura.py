from PIL import Image, ImageDraw, ImageFont

class Assinatura:
    def __init__(self, image, name, funcao, ramal, unidade, email, telefone):
        self.image = image
        address = ""
        contactRow = ""
        
        if len(name) > 26:
            parts = name.split()
            if len(parts) >= 2:
                name = f"{parts[0]} {parts[-1]}"

        draw = ImageDraw.Draw(self.image)
        fontName = ImageFont.truetype("./agenda/media_assinatura/fonts/Barlow-Bold.ttf", 25)
        positionName = (64, 15)

        fontFunction = ImageFont.truetype("./agenda/media_assinatura/fonts/Barlow-Bold.ttf", 13)
        positionFunction = (64, 42)

        if unidade == "Tapera":
            address = "Sede Administrativa - Tapera/RS"
            contactRow += "(54) 3385-3000"
        elif (unidade == "Posto Tapera"):
            address = "Posto de Combustível - Posto Tapera/RS"
            contactRow += "(54) 3385-3000"
        elif (unidade == "Ibirubá"):
            address = "Unidade Regional - Ibirubá/RS"
            contactRow += "(54) 3324-9200"
        elif (unidade == "Arroio Grande"):
            address = "Unidade Regional - Arroio Grande/RS"
            contactRow += "(54) 3385-3059"
        elif (unidade == "Victor Graeff"):
            address = "Unidade Regional - Victor Graeff/RS"
            contactRow += "(54) 3385-3012"
        elif (unidade == "Posto Victor Graeff"):
            address = "Posto de Combustível - Posto Victor Graeff/RS"
            contactRow += "(54) 3385-3025"
        elif (unidade == "Trevo Selbach" or unidade == "Selbach"):
            address = "Unidade Regional - Selbach/RS"
            contactRow += "(54) 3387-1256"
        elif (unidade == "Santa Clara do Ingaí"):
            address = f"Unidade Regional - Santa Clara do Ingaí"
            contactRow += "(54) 3324-9270"
        elif (unidade == "XV de Novembro"):
            address = f"Unidade Regional - XV de Novembro"
            contactRow += "(54) 3324-9260"
        elif (unidade == "Esq. São José"):
            address = f"Unidade Regional - Esquina São José"
            contactRow += "(54) 3324-9250"
        elif (unidade == "Jóia"):
            address = f"Unidade Regional - Jóia"
            contactRow += "(54) 3324-9280"
        elif (unidade == "Posto 43"):
            address = f"Posto de Combustível - Posto Arroio Grande, Selbach/RS"
            contactRow += "(54) 3385-3059"
        elif (unidade == "Linha Floresta"):
            address = f"Unidade Regional - Linha Floresta"
            contactRow += "(54) 3387-1235"

        if ramal != '':
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
