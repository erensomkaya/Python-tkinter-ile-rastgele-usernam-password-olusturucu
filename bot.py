import random
import tkinter as tk
# Eğer kullanıcı adı kısmı anlamlı olmasını istiyorsanız belirli kullanıcı adları yazıp rastgele gelmesini belirleyebilirsiniz.
def generate_kullanici(length):
    kullanici = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    return ''.join(random.choice(kullanici) for i in range(length))

def generate_parola(length):
    parola = 'abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return ''.join(random.choice(parola) for i in range(length))

def generate_credentials():
    kullanici = generate_kullanici(8)
    parola = generate_parola(12)

    with open('bilgiler.txt', 'w') as f:
        f.write(f"Kullanıcı Adı: {kullanici}\n")
        f.write(f"Şifre: {parola}")

    kullanici_label.config(text=f"Kullanıcı Adı: {kullanici}")
    parola_label.config(text=f"Şifre: {parola}")

root = tk.Tk()
root.title("Kullanıcı Adı ve Şifre Oluşturucu")

kullanici_label = tk.Label(root, text="Kullanıcı Adı:")
kullanici_label.pack()

parola_label = tk.Label(root, text="Şifre:")
parola_label.pack()

generate_button = tk.Button(root, text="Oluştur", command=generate_credentials)
generate_button.pack()

root.mainloop()