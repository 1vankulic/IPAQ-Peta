# Unesi jedan troznamenkasti broj i zbroji njegove znamenke

x = int(input("Unesi troznamenkasi broj"))

stotice = x // 100
print(stotice)

desetice = int((x-stotice*100) / 10)
print(desetice)

jedinice = int((x-stotice*100) % 10)
print(jedinice)

zbroj = (stotice + desetice + jedinice)

print(zbroj)