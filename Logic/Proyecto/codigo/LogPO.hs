
module LogPO where

import Data.List

-- Términos
data Term = Var String | Fun String [Term] deriving Eq

-- Fórmulas
data Form  = Top | Bot | Pred String [Term] | Eq Term Term | Neg Form | Or Form Form | And Form Form
            | Impl Form Form | Syss Form Form | Forall String Form | Exists String Form deriving Eq

instance Show Term where
      show t = case t of
               Var x -> x
               Fun a [] -> a
               Fun f (t:ts) -> f++"("++show t++ponComas ts++")" where
                              ponComas [] = []
                              ponComas (t:ts) = ","++show t++ponComas ts
  
instance Show Form where 
      show f = case f of
                  --Atómicas
                  Top -> "⊤"               
                  Bot -> "⊥"
                  Pred p (t:ts) -> p++"("++show t++ponComas ts++")" where 
                                 ponComas [] = []
                                 ponComas (t:ts) = ","++show t++ponComas ts
                  --Igualdad               
                  Eq t1 t2 -> show t1++" = "++show t2 
                  --Negación
                  Neg Top -> "¬⊤"
                  Neg Bot -> "¬⊥"
                  Neg q@(Pred p ts) -> "¬"++show q
                  Neg f1@(Neg f2) -> "¬"++show f1
                  Neg g -> "¬("++show g++")"   
                  --Conjunción
                  And Top Top -> "⊤ ∧ ⊤"
                  And Top Bot -> "⊤ ∧ ⊥"
                  And Bot Top -> "⊥ ∧ ⊤"
                  And Bot Bot -> "⊥ ∧ ⊥"
                  And p1@(Pred p ts) p2@(Pred q ss) -> show p1++" ∧ "++show p2   
                  And f1 p2@(Pred q ss) -> case f1 of
                                           Neg g -> show f1++" ∧ "++show p2
                                           _ -> "("++show f1++") ∧ "++show p2
                  And p1@(Pred p ts) f2 -> case f2 of
                                           Neg g -> show p1++" ∧ "++show f2 
                                           _ -> show p1++" ∧ ("++show f2++")"    
                  And n1@(Neg f1) n2@(Neg f2) -> show n1++" ∧ "++show n2
                  And f1 n2@(Neg f2) -> "("++show f1++") ∧ "++show n2
                  And n1@(Neg f1) f2 -> show n1++" ∧ ("++show f2++")"                                              
                  And f1 f2 -> "("++show f1++") ∧ ("++show f2++")"
                  --Disyunción
                  Or Top Top -> "⊤ ∨ ⊤"
                  Or Top Bot -> "⊤ ∨ ⊥"
                  Or Bot Top -> "⊥ ∨ ⊤"
                  Or Bot Bot -> "⊥ ∨ ⊥"
                  Or p1@(Pred p ts) p2@(Pred q ss) -> show p1++" ∨ "++show p2   
                  Or f1 p2@(Pred q ss) -> case f1 of
                                           Neg g -> show f1++" ∨ "++show p2
                                           _ -> "("++show f1++") ∨ "++show p2
                  Or p1@(Pred p ts) f2 -> case f2 of
                                           Neg g -> show p1++" ∨ "++show f2 
                                           _ -> show p1++" ∨ ("++show f2++")"    
                  Or n1@(Neg f1) n2@(Neg f2) -> show n1++" ∨ "++show n2
                  Or f1 n2@(Neg f2) -> "("++show f1++") ∨ "++show n2
                  Or n1@(Neg f1) f2 -> show n1++" ∨ ("++show f2++")"                                              
                  Or f1 f2 -> "("++show f1++") ∨ ("++show f2++")"
                  --Implicación
                  Impl Top Top -> "⊤ → ⊤"
                  Impl Top Bot -> "⊤ → ⊥"
                  Impl Bot Top -> "⊥ → ⊤"
                  Impl Bot Bot -> "⊥ → ⊥"
                  Impl p1@(Pred p ts) p2@(Pred q ss) -> show p1++" → "++show p2   
                  Impl f1 p2@(Pred q ss) -> case f1 of
                                           Neg g -> show f1++" → "++show p2
                                           _ -> "("++show f1++") → "++show p2
                  Impl p1@(Pred p ts) f2 -> case f2 of
                                           Neg g -> show p1++" → "++show f2 
                                           _ -> show p1++" → ("++show f2++")"    
                  Impl n1@(Neg f1) n2@(Neg f2) -> show n1++" → "++show n2
                  Impl f1 n2@(Neg f2) -> "("++show f1++") → "++show n2
                  Impl n1@(Neg f1) f2 -> show n1++" → ("++show f2++")"
                  Impl f1 f2 -> "("++show f1++") → ("++show f2++")"
                  --Doble implicación
                  Syss Top Top -> "⊤ ⇔ ⊤"
                  Syss Top Bot -> "⊤ ⇔ ⊥"
                  Syss Bot Top -> "⊥ ⇔ ⊤"
                  Syss Bot Bot -> "⊥ ⇔ ⊥"
                  Syss p1@(Pred p ts) p2@(Pred q ss) -> show p1++" ⇔ "++show p2   
                  Syss f1 p2@(Pred q ss) -> case f1 of
                                           Neg g -> show f1++" ⇔ "++show p2
                                           _ -> "("++show f1++") ⇔ "++show p2
                  Syss p1@(Pred p ts) f2 -> case f2 of
                                           Neg g -> show p1++" ⇔ "++show f2 
                                           _ -> show p1++" ⇔ ("++show f2++")"    
                  Syss n1@(Neg f1) n2@(Neg f2) -> show n1++" ⇔ "++show n2
                  Syss f1 n2@(Neg f2) -> "("++show f1++") ⇔ "++show n2
                  Syss n1@(Neg f1) f2 -> show n1++" ⇔ ("++show f2++")"
                  Syss f1 f2 -> "("++show f1++") ⇔ ("++show f2++")"     
                  --Para todo...
                  Forall x p1@(Pred p ts) -> "∀"++x++(show p1)
                  Forall x n1@(Neg f) -> "∀"++x++(show n1)
                  Forall x fa@(Forall y f) -> "∀"++x++(show fa)
                  Forall x ex@(Exists y f) -> "∀"++x++(show ex)
                  Forall x f -> "∀"++x++"["++show f++"]"
                  --existe...
                  Exists x p1@(Pred p ts) -> "∃"++x++(show p1)
                  Exists x n1@(Neg f) -> "∃"++x++(show n1)
                  Exists x fa@(Forall y f) -> "∃"++x++(show fa)
                  Exists x ex@(Exists y f) -> "∃"++x++(show ex)
                  Exists x f -> "∃"++x++"["++show f++"]"


-- A partir de aquí se definen las gramáticas en representación local sin nombres.

-- Términos
data TermLNR = Bvar Integer | Fvar String | FunLNR String [TermLNR] deriving Eq

-- Fórmulas
data FormLNR  = TopLNR | BotLNR | PredLNR String [TermLNR] | EqLNR TermLNR TermLNR | NegLNR FormLNR | OrLNR FormLNR FormLNR | AndLNR FormLNR FormLNR
            | ImplLNR FormLNR FormLNR | SyssLNR FormLNR FormLNR | ForallLNR FormLNR | ExistsLNR FormLNR deriving Eq

instance Show TermLNR where
      show t = case t of
               Bvar x -> show x
               Fvar x -> x
               FunLNR a [] -> a
               FunLNR f (t:ts) -> f++"("++show t++ponComas ts++")" where
                              ponComas [] = []
                              ponComas (t:ts) = ","++show t++ponComas ts

instance Show FormLNR where 
      show f = case f of
                  --Atómicas
                  TopLNR -> "⊤"               
                  BotLNR -> "⊥"
                  PredLNR p (t:ts) -> p++"("++show t++ponComas ts++")" where 
                                 ponComas [] = []
                                 ponComas (t:ts) = ","++show t++ponComas ts
                  --Igualdad               
                  EqLNR t1 t2 -> show t1++" = "++show t2 
                  --Negación
                  NegLNR TopLNR -> "¬⊤"
                  NegLNR BotLNR -> "¬⊥"
                  NegLNR q@(PredLNR p ts) -> "¬"++show q
                  NegLNR f1@(NegLNR f2) -> "¬"++show f1
                  NegLNR g -> "¬("++show g++")"   
                  --Conjunción
                  AndLNR TopLNR TopLNR -> "⊤ ∧ ⊤"
                  AndLNR TopLNR BotLNR -> "⊤ ∧ ⊥"
                  AndLNR BotLNR TopLNR -> "⊥ ∧ ⊤"
                  AndLNR BotLNR BotLNR -> "⊥ ∧ ⊥"
                  AndLNR p1@(PredLNR p ts) p2@(PredLNR q ss) -> show p1++" ∧ "++show p2   
                  AndLNR f1 p2@(PredLNR q ss) -> case f1 of
                                           NegLNR g -> show f1++" ∧ "++show p2
                                           _ -> "("++show f1++") ∧ "++show p2
                  AndLNR p1@(PredLNR p ts) f2 -> case f2 of
                                           NegLNR g -> show p1++" ∧ "++show f2 
                                           _ -> show p1++" ∧ ("++show f2++")"    
                  AndLNR n1@(NegLNR f1) n2@(NegLNR f2) -> show n1++" ∧ "++show n2
                  AndLNR f1 n2@(NegLNR f2) -> "("++show f1++") ∧ "++show n2
                  AndLNR n1@(NegLNR f1) f2 -> show n1++" ∧ ("++show f2++")"                                              
                  AndLNR f1 f2 -> "("++show f1++") ∧ ("++show f2++")"
                  --Disyunción
                  OrLNR TopLNR TopLNR -> "⊤ ∨ ⊤"
                  OrLNR TopLNR BotLNR -> "⊤ ∨ ⊥"
                  OrLNR BotLNR TopLNR -> "⊥ ∨ ⊤"
                  OrLNR BotLNR BotLNR -> "⊥ ∨ ⊥"
                  OrLNR p1@(PredLNR p ts) p2@(PredLNR q ss) -> show p1++" ∨ "++show p2   
                  OrLNR f1 p2@(PredLNR q ss) -> case f1 of
                                           NegLNR g -> show f1++" ∨ "++show p2
                                           _ -> "("++show f1++") ∨ "++show p2
                  OrLNR p1@(PredLNR p ts) f2 -> case f2 of
                                           NegLNR g -> show p1++" ∨ "++show f2 
                                           _ -> show p1++" ∨ ("++show f2++")"    
                  OrLNR n1@(NegLNR f1) n2@(NegLNR f2) -> show n1++" ∨ "++show n2
                  OrLNR f1 n2@(NegLNR f2) -> "("++show f1++") ∨ "++show n2
                  OrLNR n1@(NegLNR f1) f2 -> show n1++" ∨ ("++show f2++")"
                  OrLNR f1 f2 -> "("++show f1++") ∨ ("++show f2++")"
                  --Implicación
                  ImplLNR TopLNR TopLNR -> "⊤ → ⊤"
                  ImplLNR TopLNR BotLNR -> "⊤ → ⊥"
                  ImplLNR BotLNR TopLNR -> "⊥ → ⊤"
                  ImplLNR BotLNR BotLNR -> "⊥ → ⊥"
                  ImplLNR p1@(PredLNR p ts) p2@(PredLNR q ss) -> show p1++" → "++show p2   
                  ImplLNR f1 p2@(PredLNR q ss) -> case f1 of
                                           NegLNR g -> show f1++" → "++show p2
                                           _ -> "("++show f1++") → "++show p2
                  ImplLNR p1@(PredLNR p ts) f2 -> case f2 of
                                           NegLNR g -> show p1++" → "++show f2 
                                           _ -> show p1++" → ("++show f2++")"
                  ImplLNR n1@(NegLNR f1) n2@(NegLNR f2) -> show n1++" → "++show n2
                  ImplLNR f1 n2@(NegLNR f2) -> "("++show f1++") → "++show n2
                  ImplLNR n1@(NegLNR f1) f2 -> show n1++" → ("++show f2++")"
                  ImplLNR f1 f2 -> "("++show f1++") → ("++show f2++")"
                  --Doble implicación
                  SyssLNR TopLNR TopLNR -> "⊤ ⇔ ⊤"
                  SyssLNR TopLNR BotLNR -> "⊤ ⇔ ⊥"
                  SyssLNR BotLNR TopLNR -> "⊥ ⇔ ⊤"
                  SyssLNR BotLNR BotLNR -> "⊥ ⇔ ⊥"
                  SyssLNR p1@(PredLNR p ts) p2@(PredLNR q ss) -> show p1++" ⇔ "++show p2   
                  SyssLNR f1 p2@(PredLNR q ss) -> case f1 of
                                           NegLNR g -> show f1++" ⇔ "++show p2
                                           _ -> "("++show f1++") ⇔ "++show p2
                  SyssLNR p1@(PredLNR p ts) f2 -> case f2 of
                                           NegLNR g -> show p1++" ⇔ "++show f2 
                                           _ -> show p1++" ⇔ ("++show f2++")"    
                  SyssLNR n1@(NegLNR f1) n2@(NegLNR f2) -> show n1++" ⇔ "++show n2
                  SyssLNR f1 n2@(NegLNR f2) -> "("++show f1++") ⇔ "++show n2
                  SyssLNR n1@(NegLNR f1) f2 -> show n1++" ⇔ ("++show f2++")"
                  SyssLNR f1 f2 -> "("++show f1++") ⇔ ("++show f2++")"     
                  --Para todo...
                  ForallLNR p1@(PredLNR p ts) -> "∀"++(show p1)
                  ForallLNR n1@(NegLNR f) -> "∀"++(show n1)
                  ForallLNR fa@(ForallLNR f) -> "∀"++(show fa)
                  ForallLNR ex@(ExistsLNR f) -> "∀"++(show ex)
                  ForallLNR f -> "∀["++show f++"]"
                  --existe...
                  ExistsLNR p1@(PredLNR p ts) -> "∃"++(show p1)
                  ExistsLNR n1@(NegLNR f) -> "∃"++(show n1)
                  ExistsLNR fa@(ForallLNR f) -> "∃"++(show fa)
                  ExistsLNR ex@(ExistsLNR f) -> "∃"++(show ex)
                  ExistsLNR f -> "∃["++show f++"]"
