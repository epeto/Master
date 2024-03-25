
-- Locally Named Representation

data Term = Bvar String | Fvar String | Abs String Term | App Term Term deriving Eq

instance Show Term where
    show (Bvar x) = x
    show (Fvar x) = x
    show (Abs x e) = "λ"++x++"."++show e
    show (App (Bvar x) (Bvar y)) = x++" "++y
    show (App (Fvar x) (Bvar y)) = x++" "++y
    show (App (Bvar x) (Fvar y)) = x++" "++y
    show (App (Fvar x) (Fvar y)) = x++" "++y
    show (App (Bvar x) e2) = x++" ("++show e2++")"
    show (App (Fvar x) e2) = x++" ("++show e2++")"
    show (App e1 (Bvar y)) = "("++show e1++") "++y
    show (App e1 (Fvar y)) = "("++show e1++") "++y
    show (App t1 t2) = "("++show t1++") "++"("++show t2++")"


expr1 = Abs "x" (App (Bvar "x") (Fvar "y"))

