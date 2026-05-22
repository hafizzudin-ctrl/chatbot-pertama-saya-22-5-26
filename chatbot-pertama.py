def jawab (soalan):
  soalan = soalan.lower()
  if "hai" in soalan:
    return "hai, saya chatbot anda"
  elif "nama" in soalan:
    return "Saya pelajar Ai baru"
  elif "umur" in soalan:
    return "Umur saya 27 tahun"
  elif "Hobi" in soalan:
    return "Hobi saya buat grab"
  elif "buat" in soalan:
    return "sedang belajar Ai"
  else:
    return "Maaf saya tidak faham"

print("Chatbot sedia. Taip 'keluar' untuk berhenti")
print("-" * 60)

while True:
  user = input("Anda: ")
  if "keluar" in user.lower():
     print("Bot jumpa lagi")
     break
  print("Bot:", jawab(user))

