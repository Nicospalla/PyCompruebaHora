import datetime

import comprueba.comprobador

horaActual = datetime.datetime.now()

comprueba.comprobador.comprodarorHora(horaActual.hour,horaActual.minute)
