def mayorlista(lista=[100,250,43]):
  return(max(i for i in lista))

def primolist(lista=[3,4,8,5,5,22,13]):
    def isprime(n):
        return  all(n%i!=0 for i in range (2,n-1))
    return(list(filter(isprime,lista)))
    
if __name__ == "__main__":
    print(mayorlista())
    print(primolist())

