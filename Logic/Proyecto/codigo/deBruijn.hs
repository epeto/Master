
data Term = Var Int | Abs Term | App Term Term deriving Eq

instance Show Term where
    show (Var x) = Prelude.show x
    show (Abs e) = "λ."++show e
    show (App (Var x) (Var y)) = (Prelude.show x)++" "++(Prelude.show y)
    show (App (Var x) e2) = (Prelude.show x)++" ("++show e2++")"
    show (App e1 (Var y)) = "("++show e1++") "++ (Prelude.show y)
    show (App t1 t2) = "("++show t1++") "++"("++show t2++")"

expr1 = Abs (Var 0)
expr2 = Abs (App (Abs (App (Var 0) (Var 1))) (Var 0))

