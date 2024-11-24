class NegativeTitlesError(Exception):
  """Erro para valores negativos no campo 'titles'."""
  def __init__(self, message="titles cannot be negative"):
    self.message = message
    super().__init__(self.message)
    
    
class InvalidYearCupError(Exception):
  """Erro para anos inválidos na chave 'first_cup'."""
  def __init__(self, message="there was no world cup this year"):
    self.message = message
    super().__init__(self.message)


class ImpossibleTitlesError(Exception):
  """Erro para casos em que o número de títulos excede o número de Copas disputadas."""
  def __init__(self, message="impossible to have more titles than disputed cups"):
      self.message = message
      super().__init__(self.message)
