class Node:
    class Person:
        def __init__(self, position, name, title, contact):
            self.position = position
            self.name = name
            self.title = title
            self.contact = contact

        def __str__(self):
            return f"{self.position}: {self.name} ({self.title}), Contact: {self.contact}"

    def __init__(self, person: "Node.Person"):
        self._person = person
        self._children = []

    def add(self):
        position = input("Ingrese la posición de la persona: ")
        name = input("Ingrese el nombre de la persona: ")
        title = input("Ingrese el título de la persona: ")
        contact = input("Ingrese el contacto de la persona: ")

        new_person = Node.Person(position, name, title, contact)
        new_node = Node(new_person)

        print("\nJerarquía actual:")
        self.print_tree()

        parent_name = input("\nIngrese el nombre de la persona bajo la cual desea agregar esta nueva persona: ")

        parent_nodes = self._find_node_by_name(parent_name)

        if not parent_nodes:
            print("No se encontró la persona especificada para agregar el nuevo nodo.")
            return
        
        if len(parent_nodes) > 1:
            print(f"Se encontraron {len(parent_nodes)} coincidencias para '{parent_name}':")
            for i, node in enumerate(parent_nodes, 1):
                print(f"{i}. {node._person}")
            choice = int(input("Seleccione el número de la persona bajo la cual desea agregar: ")) - 1
            parent_node = parent_nodes[choice]
        else:
            parent_node = parent_nodes[0]

        parent_node._children.append(new_node)
        print(f"Persona {name} agregada bajo {parent_node._person.name}.")


    def _find_node_by_name(self, busqueda):
        result = []
        if self._person.name == busqueda or self._person.title == busqueda:
            result.append(self)
        
        for child in self._children:
            result += child._find_node_by_name(busqueda)
        
        return result
    
    def delete(self):
        name = input("Ingrese el nombre de la persona que desea eliminar: ")

        parent_node = self._find_parent_of_node(name)
        if parent_node:
            parent_node._children = [child for child in parent_node._children if child._person.name != name]
            print(f"Persona {name} eliminada.")
        else:
            print("No se encontró la persona especificada para eliminar.")

    def _find_parent_of_node(self, name):
        for child in self._children:
            if child._person.name == name:
                return self
            result = child._find_parent_of_node(name)
            if result:
                return result
        return None

    def print_tree(self, level=0):
        ident = " " * (level * 4)
        print(f"{ident}{self._person}")

        for child in self._children:
            child.print_tree(level + 1)

def main():
    print("Bienvenido al sistema de jerarquías.")

    print("\nPrimero, crea la persona raíz:")
    position = input("Ingrese la posición de la persona: ")
    name = input("Ingrese el nombre de la persona: ")
    title = input("Ingrese el título de la persona: ")
    contact = input("Ingrese el contacto de la persona: ")

    root_person = Node.Person(position, name, title, contact)
    root = Node(root_person)

    while True:
        print("\n¿Qué le gustaría hacer?")
        print("1. Agregar persona")
        print("2. Eliminar persona")
        print("3. Buscar persona")
        print("4. Mostrar jerarquía")
        print("5. Salir")

        option = input("Seleccione una opción (1-5): ")

        if option == "1":
            root.add()
        elif option == "2":
            root.delete()
        elif option == "3":
            bus = input("¿Qué deseas buscar (nombre o título)? ")
            bus2 = root._find_node_by_name(bus)
            
            if bus2:
                for i in bus2:
                    print(f"Encontré: {i._person}")
            else:
                print("No se encontró ninguna persona.")
        elif option == "4":
            print("\nJerarquía completa:")
            root.print_tree()
        elif option == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")

if __name__ == "__main__":
    main()