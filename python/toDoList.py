class ToDoList():
    def __init__(self):
        self.__tarefas_list = []
        pass
    
    @property 
    def tarefas_list(self): 
        return self.__tarefas_list
    
    @tarefas_list.setter
    def tarefas_list(self):
        print("nao pode alterar essa variavel")
        
    def adiciona_tarefa(self, nova_tarefa):
        self.tarefas_list.append(nova_tarefa)  
        
    def visualizar_tarefas(self):
        print(self.tarefas_list)  
        
toDoList = ToDoList()
toDoList.adiciona_tarefa("fazer fala derek")

numero = int(input("qual tabuada vc quer?"))
for i in range(1,11):
    print(f"{i} x {numero} = {i * numero}")