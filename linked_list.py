class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
      return str(self.value)

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
      current = self.head
      if self.head:
          while current.next:
              current = current.next
          current.next = new_element
      else:
          self.head = new_element

    def get_position(self, position):
      """Escolha um elemento de uma posição específica.
      Suponha que a primeira posição seja "1".
      Retorne "None" (Nenhum) caso a posição não esteja na lista."""
      return None


    def insert(self, new_element, position):
      """Acrescente um novo node na posição determinada.
      Suponha que a primeira posição seja "1".
      Inserir na posição 3 significa estar localizado entre o 2º e 3º elementos."""
      pass


    def delete(self, value):
      """Exclua o primeiro node que contenha um valor determinado."""
      pass


if __name__ == '__main__':
  elements = [Element(1), Element(2), Element(3)]

  if len(elements) >= 1:
    ll = LinkedList(elements.pop(0))
    for idx in range (0, len(elements)):
      ll.append(elements.pop(0))
  else:
    print("No values")

  print(ll.head.next.next.value)