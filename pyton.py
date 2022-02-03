#!/usr/bin/env python
# coding: utf-8

# In[9]:


from random import choice

words = [
    choice(["Büyüleyici", "Muhteşem", "Renkli", "Keyifli", "Hassas"]),
    choice(["vizyonlar", "mesafe", "vicdan", "süreç", "kaos"]),
    choice(["batıl", "zıt", "zarif", "davetkar", "çelişkili", "ezici"]),
    choice(["doğru", "karanlık", "soğuk", "sıcak", "harika"]),
    choice(["manzara","mevsim", "renkler","ışıklar","İlkbahar","Kış","Yaz","Sonbahar"]),
    choice(["inkar edilemez", "güzel", "yeri doldurulamaz", "inanılmaz", "geri alınamaz"]),
    choice(["ilham", "hayal gücü", "bilgelik", "düşünceler"])
]

print(("-" * 30) + "\nHaiku Oluşturucu\n" + ("-" * 30))
print("{} {},\n{} {} {},\n{} {}.".format(*words))


# In[ ]:





# In[ ]:




