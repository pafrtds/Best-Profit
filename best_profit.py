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
        values_investment = []
        i=0
        while i < qty:
            try:
                values_investment.append(float(input(("Digite o Valor do Dia {}: ".format(str(i+1)) ))))
                i+=1                
            except ValueError:
                print("Por gentileza Digitar um Valor valido, caso for decimal utilizar '.' como separador, ex:\n 2.2")
                            
        b = Compare(values_investment)
        b.profit()
        

    
class Compare():
    def __init__(self,values_investment):
        """
        Parameters
        ----------
        values_investment : (list) --> float
            Receive the list with the values to be compared.

        """
        self.values_investment = values_investment
        
    def profit(self):
        """
        Compares the values one by one in the list 
        creating a new list only with the values that give profits so that it is
        compared and the best option returned
        """
        general_profits = [] # variable that stores the values that give profits in matrix form [buy day, sell day, profit]
        for i in range(len(self.values_investment)):
            current_value = self.values_investment[i]
            highest_value = max(self.values_investment[i:])
            if current_value < highest_value:
                buy = i
                sale = self.values_investment.index(highest_value,i)
                profit_temp = highest_value - current_value
                general_profits.append([buy,sale,profit_temp])
        if not general_profits:
            print('Sem Lucro!')
            False
        else:
            resp = self.best_profit(general_profits)
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
        
    
    
    
