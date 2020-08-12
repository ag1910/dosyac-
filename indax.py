d = input("Dosya oluşturmak için(1) / Dosya silmek için(2) :")
if d == "1":
    o = input("Dosyanın adını yazın :")
    y = input("Dosyanın uzantısını yazın :")
    f = open(o+"."+y, "x")
    ob = input("Dosyanın içeriğini yazın :")
    k = open(o+"."+y, "w")
    k.write(ob)
    if y == "py":
        g = input("Python dosyasının adını yazın :")
        from subprocess import Popen
        Popen('python '+g) 
if d == "2":
    e = input("Silmek istediğiniz dosyanın adını yazın :")
    r = input("Silmek istediğiniz dosyanın uzantısını yazın :")
    import os
    os.remove(e+"."+r)