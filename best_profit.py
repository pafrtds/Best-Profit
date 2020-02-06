from presentation import text

class Investments():
    """
    Responsible for creating the array
    
    """
    def create_invest(self,qty):
        """
        Parameters
        ----------
        qty : int
        Function responsible for creating the array with the investment values
        according to the number of days to compare
        """
        vet = []
        i=0
        while i < qty:
            try:
                vet.append(float(input(("Digite o Valor do Dia {}: ".format(str(i+1)) ))))
                i+=1                
            except ValueError:
                print("Por gentileza Digitar um Valor valido, caso for decimal utilizar '.' como separador, ex:\n 2.2")
                            
        b = Compare(vet)
        b.profit()
        

    
class Compare():
    def __init__(self,vet):
        """
        Parameters
        ----------
        vet : (list) --> float
            Receive the list with the values to be compared.

        """
        self.vet = vet
        
    def profit(self):
        """
        Compares the values one by one in the list 
        creating a new list only with the values that give profits so that it is
        compared and the best option returned
        """
        ret = []
        for i in range(len(self.vet)):
            current_value = self.vet[i]
            highest_value = max(self.vet[i:])
            if current_value < highest_value:
                buy = i
                sale = self.vet.index(highest_value,i)
                profit_temp = highest_value - current_value
                ret.append([buy,sale,profit_temp])
        if not ret:
            print('Sem Lucro!')
            False
        else:
            resp = self.best_profit(ret)
            print("Compra no dia {}\n Venda no dia {}\n Lucro de R$ {}".format(str(resp[0]+1),str(resp[1]+1),str(resp[2])))
            

        
    def best_profit(self,L):
        """
        Parameters
        ----------
        (list) --> float, float, float
        Function that takes a matrix as parameter and returns
        the most valuable element (profit) in the matrix and the position 
        purchase and sale (buy_day, dia_venda_ret)
        """
        highest_profit = 0 
        buy_day = 0
        sale_day = 0
        for i in range(len(L)):
            if L[i][2] > highest_profit:
                highest_profit = L[i][2]
                buy_day = L[i][0]
                sale_day = L[i][1]
        return buy_day, sale_day, highest_profit


print(text)
comp = Investments()
while True:
    try:
        days = int(input("Digite a quantidade de dias que deseja comparar: "))
        comp.create_invest(days)
        break
    except ValueError:
        print("Digite um número inteiro!\n\n\n")
    except KeyboardInterrupt:
        print("\n\n Até a Proxima! :) ")
        break
        
    
    
    
