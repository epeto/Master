
-- Gramática para cálculo lambda puro

import Data.List

data Term = Var String |  Abs String Term | App Term Term deriving Eq

instance Show Term where
    show (Var x) = x
    show (Abs x e) = "λ"++x++"."++show e
    show (App (Var x) (Var y)) = x++" "++y
    show (App (Var x) e2) = x++" ("++show e2++")"
    show (App e1 (Var y)) = "("++show e1++") "++y
    show (App t1 t2) = "("++show t1++") "++"("++show t2++")"


expr1 = Abs "x" (Var "x")
expr2 = Abs "y" (Var "y")

