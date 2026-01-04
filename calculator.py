import sys
sys.set_int_max_str_digits(1000000)#python limit integer string values up to 43300 digit,,to increase the system limit
class AdvancedCalculator:

    def main(self):
        
        print("Welcome to the Advance Calculator")
        
        while True:
            try: 
                choice=int(input("Please select an operation:\n1:Add\n2:Substract\n3:Multiply\n4:Divide\n5:Find Root\n6:Find Factorial\n7:Find Power\n8:Simple Interest\n9:Compounded Interest\n10:Find the nth root\n11:find log base a of b\n12:calulate sine\n13:Exit\nEnter choice(1-13) :"))
                if choice==13:
                    print("Bye!!!")
                    break
                if 0>choice<5:
                    a , b = int(input("Enter first number : ")),int(input("Enter second number : "))
                    if choice==1:
                        print(f"Result: {self.add(a,b)}\n---")
                    elif choice==2:
                        print(f"Result: {self.substract(a,b)}\n---")
                    elif choice==3:
                        print(f"Result: {self.multiply(a,b)}\n---")
                    elif choice==4:
                        print(f"Result: {self.divide(a,b)}\n---")
                else:
                    if choice==5:
                        n=int(input("Enter the Number: "))
                        print(f"√{n}={self.find_square_root(n):.4f}")
                    elif choice==6:
                        n=int(input("Enter the Number: "))
                        print(f"{n}!={self.find_factorial(n)}")
                    elif choice==7:
                        base,exponent=int(input("Enter the Base: ")),int(input("Enter the exponent"))
                        print(f"{base}^{exponent}= {self.find_power(base,exponent)}")
                    elif choice==8:
                        principal, rate, time=int(input("Enter the Principal amount: ")),int(input("Enter the Rate of interest: ")),int(input("Enter the Number of years: "))
                        print(f"Simple Interest= {self.calculate_simple_interest(principal,rate,time)}")
                    elif choice==9:
                        principal, rate, time, periods =int(input("Enter the Principal amount: ")),int(input("Enter the Rate of interest: ")),int(input("Enter the Number of years: ")),int(input("Enter the Number of times interest is compounded per year: "))
                        print(f"Compounded Interest= {self.calculate_compound_interest(principal,rate,time,periods)}")
                    elif choice==10:
                        n,a=int(input("Enter nth  Number: ")),int(input("Enter the number: "))
                        print(f"{n}√{a}={self.find_n_th_root(n,a)}")
                    elif choice==11:
                        x,n=int(input("Enter the 'a' Number: ")),int(input("Enter the 'b' Number: "))
                        print(f"√{n}={self.compute_log_base_a_of_b(a,b)}")
                    elif choice==12:
                        n=int(input("Enter the degree: "))
                        print(f"{n}!={self.calculate_sine(n)}")
            except ValueError:
                print("Error: Enter a number,try again")
                    
    def add(self,a,b):
        return f"{a} + {b}={a+b}"
    
    def substract(self,a,b):
        return f"{a}-{b}={a-b}"
    def multiply(self,a,b):
        return f"{a}*{b}={a*b}"
    def divide(self,a,b):
        if b==0:
           print("Error: Cannot divide by zero, please try again")
        else:
            return f"{a}/{b}={a/b}"
        
    def find_square_root(self,n):
        precision=0.00001
        guess=n/2.0
        while abs(guess*guess-n) >precision:
            new_guess=(guess+(n/guess))/2.0
            guess=new_guess
        return guess
   
    def find_factorial(self,n):
        a,b=1,1
        for i in range(n-1):
            c=a+b
            a=b
            b=c
        return b
    
    def find_power(self,base,exponent): 
        power=1 
        if exponent>0:
            for i in range(exponent-1):
                power*=base
        elif exponent==0:
            return 1
        else:
            for i in range(-(exponent)):
                power *= base
            power=1/power
        return power
    def calculate_simple_interest(self,principal, rate, time):
        simple_interest=principal*(1+(rate/100)*time)
        print(simple_interest)
        return simple_interest
    def calculate_compound_interest(self,principal, rate, time, periods):
        power_value=self.find_power((1+(rate/100)/periods),periods*time)
        return round(principal*power_value-principal)
    
    def find_n_th_root(self,n,a):
        
        if a<0 and n%2==0:
            raise ValueError("ERROR: Enter a number with real roots, please try again")
        tol=1e-12
        if abs(a)<1:
            guess=1.0
        else:
            guess=a/n
        if a==0:
            return 0 
        if a==1:
            return 1
        if n == 1:
            return a
        
        return guess
""" def compute_log_base_a_of_b(a, b): 
    
    
    def calculate_sine(degrees):
    """
calculator=AdvancedCalculator() 
result=calculator.main()
