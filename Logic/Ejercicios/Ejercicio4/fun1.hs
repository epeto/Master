
import Data.List

reversa :: [a] -> [a]
reversa [] = []
reversa (x:l) = (reversa l)++[x]

pegar :: [a] -> [a] -> [(a,a)]
pegar [] _ = []
pegar _ [] = []
pegar (x:xs) (y:ys) = (x,y):(pegar xs ys)


