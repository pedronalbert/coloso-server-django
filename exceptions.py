class NotFoundException(Exception):
  def __init__(self, message = 'NotFoundException'):
    self.message = message

class RiotServerError(Exception):
  def __init__(self, message = 'Error al conectar a los servidores de RiotGames'):
    self.message = message
