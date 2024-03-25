
data Prop = VarP Int |  Top | Bot | Neg Prop | And Prop Prop | Or Prop Prop | Imp Prop Prop | Equiv Prop Prop  deriving (Show,Eq)


p = VarP 1

q = VarP 2

r = VarP 3

s = VarP 4

t = VarP 5


-- A = ~p -> q \/ r

fa = Imp (Neg p) (Or q r)

-- B = s /\  ~(r -> t)

fb = And s (Neg (Imp r t))



vars :: Prop -> [Prop]


vars (Neg a) = vars a

vars (And a b) = vars a ++ vars b

vars (Or a b) = vars a ++ vars b

vars (Imp a b) = vars a ++ vars b

vars (Equiv a b) = vars a ++ vars b

vars (VarP n) = [VarP n]

vars _  =  []



nc :: Prop -> Int

nc (Neg a) = 1 + nc a

nc (And a b) = 1 + nc a + nc b

nc (Or a b) = 1 + nc a + nc b

nc (Imp a b) = 1 + nc a + nc b

nc (Equiv a b) = 1 + nc a + nc b

nc _  = 0


qi :: Prop -> Prop

qi (Neg a) = Neg (qi a)

qi (Imp a b) = Or (Neg (qi a)) (qi b)

qi (And a b) = And (qi a) (qi b)

qi (Or a b) = Or (qi a) (qi b)

qi (Equiv a b) = Equiv (qi a) (qi b)

qi a = a