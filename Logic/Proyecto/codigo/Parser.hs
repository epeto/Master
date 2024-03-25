
module Parser where

import LogPO


lastParen'::String->String->Int->(String,String)
lastParen' str1 str2 0 = (str2, str1)
lastParen' (caracter:resto1) str2 n = case caracter of
    '(' -> lastParen' resto1 (str2++"(") (n+1)
    ')' -> lastParen' resto1 (str2++")") (n-1)
    otherwise -> lastParen' resto1 (str2++[caracter]) n

-- Separa una cadena en 2: a partir del primer paréntesis hasta donde se cierra
-- y luego el resto de la cadena.
lastParen::String->(String,String)
lastParen cadena = if (head cadena) == '('
                   then lastParen' (tail cadena) "(" 1
                   else ("empty","empty")

separaTerminos::String->[String]
separaTerminos "" = []
separaTerminos (',':cs) = separaTerminos cs
separaTerminos ('v':cs) = ('v':[(head cs)]) : (separaTerminos (tail cs))
separaTerminos ('c':cs) = ('c':[(head cs)]) : (separaTerminos (tail cs))
separaTerminos ('f':cs) = let par = lastParen (tail cs)
    in [("f"++[(head cs)]++(fst par))] ++ (separaTerminos (snd par))

parseTermComas::String->[Term]
parseTermComas cadena = map parseTerm (separaTerminos cadena)

-- Parser de términos. Recibe un string y construye un término.
parseTerm::String->Term
parseTerm "" = error ("Un término no puede ser cadena vacía")
parseTerm (c:cs) = case c of
    'c' -> Fun cs []
    'v' -> Var cs
    'f' -> Fun [head cs] (parseTermComas (init $ tail $ tail cs))

-- Decide si un caracter es cuantificador.
esCuantif::Char->Bool
esCuantif '∀' = True
esCuantif '∃' = True
esCuantif _ = False

-- Decide si un caracter es conector.
esConector::Char->Bool
esConector '¬' = True
esConector '∧' = True
esConector '∨' = True
esConector '→' = True
esConector '⇔' = True
esConector _ = False

-- Separa una cadena (que representa una fórmula) en tokens.
tokenizer::String->[(String,String)]
tokenizer "" = []
tokenizer (x:xs)
    | esCuantif x = ("cuantificador", [x,head xs]) : (tokenizer (tail xs))
    | esConector x = ("conector", [x]) : (tokenizer xs)
    | x == '(' = ("(", "(") : (tokenizer xs)
    | x == '[' = ("(", "(") : (tokenizer xs)
    | x == ')' = (")", ")") : (tokenizer xs)
    | x == ']' = (")", ")") : (tokenizer xs)
    | otherwise = let par = lastParen xs
                  in ("predicado", x:(fst par)) : (tokenizer (snd par))

-- Recibe una pila con tokens, una expresión con tokens y extrae elementos de la pila hasta
-- que sea vacía o encuentre un paréntesis izquierdo.
extraePila :: [(String,String)] -> [(String,String)] -> ([(String,String)],[(String,String)])
extraePila [] expr = ([],expr)
extraePila (x:xs) expr = if (fst x) == "("
                         then ((x:xs), expr)
                         else extraePila xs (expr++[x])

-- Cambia una expresión lógica de forma infija a forma postfija.
-- El primer argumento es la expresión de entrada.
-- El segundo argumento es una pila, inicialmente vacía.
-- El tercer argumento es la expresión de salida que se está construyendo.
infApostCola :: [(String,String)] -> [(String,String)] -> [(String,String)] -> [(String,String)]
infApostCola [] [] exprSal = exprSal --Si la entrada y la pila están vacías, se devuelve la expresión construida.
infApostCola [] (x:xs) exprSal = infApostCola [] xs (exprSal++[x]) --Si la entrada está vacía pero la pila no, se mueve el tope de la pila a la salida.
infApostCola (("(","("):xs) p exprSal = infApostCola xs (("(","("):p) exprSal
infApostCola ((con, "¬"):xs) p exprSal = infApostCola xs ((con, "¬"):p) exprSal
infApostCola (("cuantificador", q):xs) p exprSal = infApostCola xs (("cuantificador", q):p) exprSal
infApostCola ((")",")"):xs) p exprSal = let tupla = extraePila p exprSal
    in infApostCola xs (tail (fst tupla)) (snd tupla)
infApostCola (x:xs) p exprSal = if (fst x) == "conector"
    then
        let tupla = extraePila p exprSal
        in infApostCola xs (x:(fst tupla)) (snd tupla)
    else infApostCola xs p (exprSal++[x]) --Si llega a este caso es porque x es predicado.

-- Recibe los tokens de una expresión infija y la transforma a postfija.
infApost :: [(String, String)] -> [(String, String)]
infApost expr = infApostCola expr [] []

-- Recibe una expresión infija y devuelve sus tokens en notación postfija.
infApost2 :: String -> [(String, String)]
infApost2 expr = infApost (tokenizer expr)

-- Recibe un caracter que representa un operador lógico, un par de fórmulas y devuelve una fórmula nueva.
creaForm :: String -> Form -> Form -> Form
creaForm op f1 f2 = case op of
    "∧" -> And f1 f2
    "∨" -> Or f1 f2
    "→" -> Impl f1 f2
    "⇔" -> Syss f1 f2

creaFormCuanti :: String -> Form -> Form
creaFormCuanti ('∀':cs) f = Forall cs f
creaFormCuanti ('∃':cs) f = Exists cs f

-- Recibe una fórmula lógica en forma postfija y la transforma a una formula definida en LogPO.
-- Utiliza una pila para evaular.
parseForm' :: [(String,String)] -> [Form] -> Form
parseForm' [] p = head p
parseForm' (x:xs) p = if (fst x) == "conector"
    then
        if (snd x) == "¬" -- operador unario
        then let f = head p
                 p2 = tail p
             in parseForm' xs ((Neg f):p2)
        else let f1 = head (tail p) -- operador binario
                 f2 = head p
                 p2 = tail (tail p)
             in parseForm' xs ((creaForm (snd x) f1 f2):p2)
    else if (fst x) == "cuantificador"
         then let f = head p
                  p2 = tail p
              in parseForm' xs ((creaFormCuanti (snd x) f):p2)
    else let listaTerm = parseTermComas (tail $ tail $ init (snd x)) -- x es predicado
             nomPred = [head (snd x)]
         in parseForm' xs ((Pred nomPred listaTerm):p)


-- Transforma un String que representa una fórmula a una expresión Form.
parseForm :: String -> Form
parseForm expr = parseForm' (infApost2 expr) []

-- A partir de aquí se maneja la parte de locally nameless representation.

-- Incrementa en uno cada número en los pares.
incUno :: [(String, Integer)] -> [(String, Integer)]
incUno [] = []
incUno ((var, n):xs) = (var, n+1):(incUno xs)

-- Recibe un término y lo transforma a su equivalente en locally nameless representation.
transTermLNR :: Term -> [(String, Integer)] -> TermLNR
transTermLNR (Var x) env = let indMaybe = lookup x env
    in case indMaybe of
       Just indice -> Bvar indice
       Nothing -> Fvar x
transTermLNR (Fun f terms) env = FunLNR f (map (\t -> transTermLNR t env) terms)

-- Transforma una fórmula normal a una fórmula en locally nameless representation.
-- La lista que recibe contiene las variables ligadas.
transFormLNR' :: Form -> [(String, Integer)] -> FormLNR
transFormLNR' Top _ = TopLNR
transFormLNR' Bot _ = BotLNR
transFormLNR' (Pred p lt) env = PredLNR p (map (\t -> transTermLNR t env) lt)
transFormLNR' (Eq t1 t2) env = EqLNR (transTermLNR t1 env) (transTermLNR t1 env)
transFormLNR' (Neg f) env = NegLNR (transFormLNR' f env)
transFormLNR' (Or f1 f2) env = OrLNR (transFormLNR' f1 env) (transFormLNR' f2 env)
transFormLNR' (And f1 f2) env = AndLNR (transFormLNR' f1 env) (transFormLNR' f2 env)
transFormLNR' (Impl f1 f2) env = ImplLNR (transFormLNR' f1 env) (transFormLNR' f2 env)
transFormLNR' (Syss f1 f2) env = SyssLNR (transFormLNR' f1 env) (transFormLNR' f2 env)
transFormLNR' (Forall x f) env = let newEnv = (x, 0):(incUno env)
    in ForallLNR (transFormLNR' f newEnv)
transFormLNR' (Exists x f) env = let newEnv = (x, 0):(incUno env)
    in ExistsLNR (transFormLNR' f newEnv)

-- Transforma una fórmula normal a su equivalente en LNR
transFormLNR :: Form -> FormLNR
transFormLNR f = transFormLNR' f []
