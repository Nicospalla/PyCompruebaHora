def comprodarorHora(hora,minuto):
    if hora < 10:
        print("Todavia puedes descansar")
    elif hora >= 19:
        print('Hora de ir a casa')
    else:
        h1 = 22 - (hora+1)
        m1 = 60 - minuto
        print('Debes trabajar por ' + str(h1) + ' horas, ' + str(m1) + ' minutos más')
