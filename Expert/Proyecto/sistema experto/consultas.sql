

-- Incluir y excluir ingredientes:
-- Ejemplo: todos los id de recetas que incluyan 'tomate' pero que no tengan 'harina':
(SELECT DISTINCT id_recipe
 FROM public.ingredients
 WHERE public.ingredients.ingredient LIKE '%tomato%')
INTERSECT
(SELECT DISTINCT id_recipe
 FROM public.ingredients
 WHERE public.ingredients.ingredient NOT LIKE '%flour%')

 
-- Requerimientos dietéticos numéricos: bajo en grasa, bajo en azucares, etc
-- en este caso, se considerará 'bajo' en algo, cualquier cosa que esté debajo del promedio
-- Ejemplo: id de receta que sean bajos en carbohidratos:
SELECT DISTINCT id_recipe
FROM public.nutrition
WHERE carbohydrates < (SELECT AVG(carbohydrates) FROM public.nutrition)


-- Requerimientos dietéticos por categorías: vegan, gluten free, etc.
-- Ejemplo: id de recetas veganas
SELECT DISTINCT id_recipe
FROM public.tags
WHERE tag LIKE 'vegan'


-- Tiempo: desayuno, comida o cena
-- Ejemplo: id de recetas que sean breakfast
SELECT DISTINCT id_recipe
FROM public.tags
WHERE tag LIKE 'breakfast'


-- Pasos a seguir dada una receta
-- Ejemplo: seleccionar los pasos ordenados de la receta número 50
SELECT step
FROM public.steps
WHERE id_recipe = 50
ORDER BY id


-- Seleccionar ingredientes dada una receta
-- Ejemplo: seleccionar los ingredientes de la receta número 30
SELECT ingredient
FROM public.ingredients
WHERE id_recipe = 30


-- Seleccionar ingredientes dada una lista de recetas
-- Ejemplo: seleccionar los ingredientes de las primeras 10 recetas
SELECT DISTINCT ingredient
FROM public.ingredients, public.recipes
WHERE public.ingredients.id_recipe = public.recipes.id AND public.recipes.id < 10


-- Seleccionar varias recetas dada una lista de id's (en este caso, la lista [10, 20, 50])
SELECT id, name
FROM public.recipes
WHERE id = 10 OR id = 20 OR id = 50

