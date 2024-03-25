-- Lógica Computacional 2023-1
-- Maestría en Ciencia e Ingeniería de la Computación UNAM
-- Dr. Favio E. Miranda Perea
-- Algoritmo de unificación de Martelli-Montanari

-- Tarea de Emmanuel Peto Gutiérrez

module Unificacion where

import Data.List

-- Los identificadores son cadenas
type Ident = String

-- Un término es una variable o un símbolo de función seguido de una
-- lista de términos. No hay constantes explícitas.

data Termino = V Ident
             | T Ident [Termino]
             deriving Eq

-- Instancia show para terminos 

instance Show Termino where
  show (V ident)    = ident
  show (T ident []) = ident
  show (T ident ts) = ident ++ concat [show ts]

-- Tipo de variabls como alias de términos. 

type Variable = Termino

-- Una sustitución es una lista de pares formados por una variable y un término.

type Sustitucion = [(Variable, Termino)]

-- Función que nos dice si un un termino es una variable.

esVariable :: Termino -> Bool
esVariable (V _) = True
esVariable _     = False

-- Función que dado un término, regresa su lista de variables.

variables :: Termino -> [Variable]
variables (V v)    = [V v]
variables (T n ts) = variablesEnLista ts

-- Función que regresa la lista de variables, sin duplicados, dada una lista de términos.

variablesEnLista :: [Termino] -> [Variable]
variablesEnLista = nub . concat . map variables

-- Función que representa a la sustitución identidad

idSust:: Sustitucion
idSust = []

-- Función que dada una sustitución, obtiene su dominio.

dominio :: Sustitucion -> [Variable]
dominio = map fst

-- Función que dada una sustitución y una variable, regresa la
-- aplicación de la sustitución a la variable.

aplicaVar :: Sustitucion -> Variable -> Termino
aplicaVar []         (V y) = V y
aplicaVar ((x,t):xs) (V y)
  | x == (V y) = t
  | otherwise = aplicaVar xs (V y)

-- Función que dada una sustitución y un término, regresa la
-- aplicación de la sustitución al término.

aplicaT :: Sustitucion -> Termino -> Termino
aplicaT s (V x)    = aplicaVar s (V x)
aplicaT s (T f ts) = T f [aplicaT s t | t <- ts]

-- Función que elimina los pares
-- cuyos elementos son iguales en una sustitucion.

reduce :: Sustitucion -> Sustitucion
reduce s = [(x, t) | (x, t) <- s, x /= t]

-- Función que dadas dos sustituciones, regresa su composición.
composicion :: Sustitucion -> Sustitucion -> Sustitucion
composicion xs ys =
  (reduce [ (y, aplicaT ys t) | (y, t) <- xs])
  ++
  [(x,t) | (x,t) <- ys, x `notElem` (dominio xs)]

-- Funcion que compone todas las sustituciones en una lista.

complista :: [Sustitucion] -> Sustitucion
complista = foldl composicion idSust 

complistaR :: [Sustitucion] -> Sustitucion
complistaR = foldr composicion idSust 

-- Una ecuacion es un par de terminos
type EqTerm = (Termino,Termino)

-- Aplicación de una sustitución a una equación
apSustEq :: Sustitucion -> EqTerm -> EqTerm
apSustEq s (t1,t2)  = (aplicaT s t1, aplicaT s t2)

-- Función que implementa el algoritmo de Martelli-Montanari
unifmm :: [EqTerm] -> [Sustitucion] -> Sustitucion
unifmm [] subs =  complista (reverse subs)
unifmm ((V x,t2):eqs) subs -- x=t
 | V x == t2                 = unifmm eqs subs
 | elem (V x) (variables t2) = error ("La ecuacion " ++ show (V x) ++ " = " ++
                                       show t2 ++ " no es unificable")  
 | otherwise                 = unifmm (reduce (map (apSustEq [(V x, t2)]) eqs))
                                      ([(V x, t2)]:subs)
unifmm ((t1,V x):eqs) subs -- t=x
 | not (esVariable t1) = unifmm ((V x,t1):eqs) subs
unifmm ((T f1 l1,T f2 l2):eqs) subs = if f1 == f2 then -- s=t
    unifmm (eqs++(zip l1 l2)) subs
    else error ("La ecuación "++ show (T f1 l1) ++ "=" ++ show (T f2 l2)++" no es unificable")

-- Función que unifica una ecuación
unif :: EqTerm -> Sustitucion
unif eq = unifmm [eq] []

-- Función que unifica una lista de términos
unifL :: [Termino] -> Sustitucion
unifL [] = []
unifL [t] = []
unifL (t1:(t2:ts)) = let s1_2 = unif (t1,t2)
                     in composicion s1_2 (unifL (map (aplicaT s1_2) (t2:ts)))

--- Ejemplos

-- Símbolos de constante
a = T "a" []
b = T "b" []
c = T "c" []

-- Variables
x = V "x"
y = V "y"
z = V "z"
u = V "u"
w = V "w"

-- Símbolos de función
f = T "f" 
g = T "g"
h = T "h"
p = T "P"
q = T "Q"
r = T "R"

-- Términos
t1 = f [x,y,x]
t2 = f [y, g [x],x]
t3 = f [g [x], h [x,u]]
t4 = f [z, h [f [y,y],z]]
t5 = h [g [z]]
t6 = h [f [a], g [x]]
t7 = h [z,z]
t8 = h [y,z]
t9 = h [x, g [a]]
t10 = h [g [z],z]

-- Sustituciones
s1 = [(x, a), (z, f [x, y])]
s2 = [(x, z), (y, u)]
s3 = [(z, x), (x, b), (u, c)]
s4 = [(u, f [x]), (y, a)]
s5 = [(x, h [z]), (y, g [b])]
s6 = [(z, g [x])]
s7 = [(x, f [y,y])]
s8 = [(u, g [f [y,y]])]

-- Ejemplos de las notas
ejemplo51 = [f [g [x], h [x, u]], f [z, h [f [y, y], z]]]
ejemplo52 = [f [x, y, x], f [y, g [x], x]]
la = [h [f [a], g [x]], h [z, z]]
lb = [f [w, f [x, h [z]]], f [g [x], f [x, y]], f [g [x], f [a, b]]]
lc = [f [x, g [f [a, y], z]], f [b, g [f [a, g [x, c]], f [y, x]]]]
le = [q [x, f [x, y]], q [y, f [y, a]], q [b, f [b, a]]]
lf = [p [x, f [y]], p [g [y, a], f [b]], p [g [b, z], w]]
lg = [q [a, z, g [a, b, c]], q [a, f [x], g [a, b, y]], q [a, f [f [w]], g [a, x, g [c, b, a]]]]
lh = [p [x, f [x], g [y]], p [a, f [g [a]], g [a]], p [y, f [y], g [a]]]
li = [r [f [a], y, z], r [x, y, f [z]], r [y, f [a], b]]
lj = [p [x, f [x], c], p [u, b, z]]
lk = [q [y, z], q [x, f [a]], q [f [z], z]]
ll = [r [w, f [b], f [g [y]]], r [a, x, f [g [y]]], r [z, f [z], f [u]]]
