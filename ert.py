meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek/Sinirlenmek"}
            
while True:            
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")   
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Hiç bir fikrim yok")
