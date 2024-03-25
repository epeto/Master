-- Table: public.ingredients

-- DROP TABLE IF EXISTS public.ingredients;

CREATE TABLE IF NOT EXISTS public.ingredients
(
    id integer NOT NULL,
    ingredient character varying COLLATE pg_catalog."default",
    id_recipe integer,
    CONSTRAINT pkingredients PRIMARY KEY (id),
    CONSTRAINT id_recipe FOREIGN KEY (id_recipe)
        REFERENCES public.recipes (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.ingredients
    OWNER to postgres;
    

-- Table: public.nutrition

-- DROP TABLE IF EXISTS public.nutrition;

CREATE TABLE IF NOT EXISTS public.nutrition
(
    id integer NOT NULL,
    calories double precision DEFAULT 0.0,
    total_fat double precision DEFAULT 0.0,
    sugar double precision DEFAULT 0.0,
    sodium double precision DEFAULT 0.0,
    protein double precision DEFAULT 0.0,
    saturated_fat double precision DEFAULT 0.0,
    carbohydrates double precision DEFAULT 0.0,
    id_recipe integer,
    CONSTRAINT pknutrition PRIMARY KEY (id),
    CONSTRAINT id_recipe FOREIGN KEY (id_recipe)
        REFERENCES public.recipes (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.nutrition
    OWNER to postgres;
    

-- Table: public.recipes

-- DROP TABLE IF EXISTS public.recipes;

CREATE TABLE IF NOT EXISTS public.recipes
(
    id integer NOT NULL,
    name character varying COLLATE pg_catalog."default",
    minutes integer DEFAULT 0,
    n_steps integer,
    description character varying COLLATE pg_catalog."default",
    n_ingredients integer,
    CONSTRAINT recipes_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.recipes
    OWNER to postgres;
    

-- Table: public.steps

-- DROP TABLE IF EXISTS public.steps;

CREATE TABLE IF NOT EXISTS public.steps
(
    id integer NOT NULL,
    step character varying COLLATE pg_catalog."default",
    id_recipe integer,
    CONSTRAINT pksteps PRIMARY KEY (id),
    CONSTRAINT id_recipe FOREIGN KEY (id_recipe)
        REFERENCES public.recipes (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.steps
    OWNER to postgres;
    

-- Table: public.tags

-- DROP TABLE IF EXISTS public.tags;

CREATE TABLE IF NOT EXISTS public.tags
(
    id integer NOT NULL,
    tag character varying COLLATE pg_catalog."default",
    id_recipe integer,
    CONSTRAINT pktag PRIMARY KEY (id),
    CONSTRAINT id_recipe FOREIGN KEY (id_recipe)
        REFERENCES public.recipes (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tags
    OWNER to postgres;

