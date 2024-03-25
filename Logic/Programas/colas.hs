
data Cola = Empty | A Cola | E Cola | I Cola | O Cola | U Cola | Dequeue Cola | Head Cola deriving Show

-- La función A¹ pega al final de una cadena al caracter 'a'. Análogamente con las demás funciones (E, I, O, U)

interp::Cola->[Char]
interp Empty = []
interp (A q) = (interp q)++['a']
interp (E q) = (interp q)++['e']
interp (I q) = (interp q)++['i']
interp (O q) = (interp q)++['o']
interp (U q) = (interp q)++['u']
interp (Dequeue q) = tail (interp q)
interp (Head q) = [head (interp q)]

cola1a = O $ I $ E $ Empty
cola2a = O $ I $ I $ Empty
cola2aPrima = Dequeue cola2a
cola1c = U $ E $ A $ Empty
cola1cPrima = Head $ Dequeue cola1c
cola2c = A $ O $ I $ U $ Empty
cola2cPrima = Head $ Dequeue $ Dequeue cola2c

