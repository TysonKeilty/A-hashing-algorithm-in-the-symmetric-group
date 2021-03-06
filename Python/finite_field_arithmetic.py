#################################################################################
# Modular arithmetic in the multiplicative group Z_p*
################################################################################# 

class field:

    def __init__(self,p):
        self.p=p

    # returns inverse of g modulo p (use Fermat's little theorem)
    def inverse(self,g):
        return field.fast_powering_algorithm(self,g,self.p-2)

    # Fast powering algorithm to compute g^n (mod p)
    def fast_powering_algorithm(self,g,n):
        bits=format(n,'0b')
        cont=len(bits)
        L=[]
        
        for bit in bits:
            cont=cont-1
            
            if bit=='1':               
                k=g
                
                for i in range(cont):
                    k=k**2%self.p
                    
                L.append(k)
        result=1
        
        for factor in L:
            result=result*factor%self.p
            
        return result
