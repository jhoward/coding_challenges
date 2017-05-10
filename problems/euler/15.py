rv = {}

def routes(m, n):
    
    if m == 0 or n == 0:
        return 1
    
    return routes(m - 1, n) + routes(m, n - 1)


def fastRoutes(m, n):
    
    if m == 0 or n == 0:
        return 1
        
    if not rv.has_key((m, n)):
        rv[(m, n)] = fastRoutes(m - 1, n) + fastRoutes(m, n-1)
        
    return rv[(m, n)]
    
#print routes(13, 13)
print fastRoutes(20, 20)