import logging

format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="teste.log", level= logging.DEBUG, filemode="w", format=format )


logging.info("Mensagem de informação")
logging.debug("Mensagen de depuração")