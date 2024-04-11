--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3 (Debian 15.3-1.pgdg120+1)
-- Dumped by pg_dump version 15.3 (Debian 15.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: fuzzystrmatch; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;


--
-- Name: EXTENSION fuzzystrmatch; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';


--
-- Name: pg_trgm; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;


--
-- Name: EXTENSION pg_trgm; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- Name: tagat; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tagat (
    object text,
    idobject text,
    shortname text,
    inn text,
    tarif numeric,
    idsystem bigint,
    kpp text,
    name text,
    dbeg timestamp without time zone,
    dend timestamp without time zone,
    id integer NOT NULL
);


--
-- Name: TABLE tagat; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.tagat IS 'Дополнительная разбивка одной учетной записи по ИНН. Впервые возникла необходимость для агат-проекта';


--
-- Name: tdata; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tdata (
    login text,
    idlogin text,
    idsystem integer,
    object text,
    idobject text,
    isactive text,
    id bigint NOT NULL,
    dimport timestamp without time zone
);


--
-- Name: tklient; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tklient (
    name text,
    shortname text,
    type text,
    inn text,
    kpp text,
    id bigint NOT NULL,
    tarif numeric
);


--
-- Name: twialon100; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.twialon100 (
    klient text,
    login text,
    id bigint NOT NULL,
    logintd text,
    tkid bigint
);


--
-- Name: TABLE twialon100; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.twialon100 IS 'Таблица учетных записей Клиента. Исторически сформированная на основания Google таблицы Wialon100. Является вспомогательной таблицей для соединения объекта мониторинга и клиента.';


--
-- Name: foremail; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.foremail AS
 SELECT
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.name
            ELSE tk.name
        END AS "Контрагент",
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.inn
            ELSE tk.inn
        END AS "ИНН",
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.kpp
            ELSE tk.kpp
        END AS "КПП",
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.tarif
            ELSE tk.tarif
        END AS "Тариф",
    round(sum((1.0 / (1)::numeric)), 2) AS "Коэффициент тарифа"
   FROM (((public.tdata t2
     LEFT JOIN public.twialon100 tw ON ((tw.logintd = t2.login)))
     LEFT JOIN public.tklient tk ON ((tk.id = tw.tkid)))
     LEFT JOIN public.tagat ta ON (((ta.idsystem = t2.idsystem) AND (ta.idobject = t2.idobject))))
  WHERE ((t2.isactive = ' Да'::text) AND (tk.inn IS NOT NULL) AND (t2.dimport > '2023-05-08 01:40:00'::timestamp without time zone) AND (upper(t2.object) !~~ '%ТЕСТ%'::text) AND (NOT ((upper(t2.object) ~~ '%TEST%'::text) AND (upper(t2.object) !~~ '%MICROTEST%'::text))) AND (upper(t2.object) !~~ '%ПРИОСТ%'::text) AND (upper(t2.object) !~~ '%ППРО%'::text) AND (upper(t2.object) !~~ '%НОВТ%'::text) AND (NOT ((upper(t2.object) ~~ '%ПЕРЕ%'::text) AND (t2.idsystem = ANY (ARRAY[11, 16])))) AND (NOT ((upper(t2.login) ~~ '%ТЕСТ%'::text) AND (t2.idsystem = 15))) AND (tk.id <> ALL (ARRAY[(2752)::bigint, (1925)::bigint, (3287)::bigint])))
  GROUP BY
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.name
            ELSE tk.name
        END,
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.inn
            ELSE tk.inn
        END,
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.kpp
            ELSE tk.kpp
        END,
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.tarif
            ELSE tk.tarif
        END
  ORDER BY
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.name
            ELSE tk.name
        END,
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.inn
            ELSE tk.inn
        END,
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.kpp
            ELSE tk.kpp
        END,
        CASE
            WHEN (ta.inn IS NOT NULL) THEN ta.tarif
            ELSE tk.tarif
        END;


--
-- Name: tagat_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tagat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: tagat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.tagat_id_seq OWNED BY public.tagat.id;


--
-- Name: temail; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.temail (
    email text,
    name text,
    inn text,
    kpp text,
    id integer NOT NULL
);


--
-- Name: temail_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.temail_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: temail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.temail_id_seq OWNED BY public.temail.id;


--
-- Name: tklient_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.tklient ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.tklient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tsveta; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.tsveta (
    name text,
    skol numeric,
    kol1 numeric,
    kol2 numeric,
    tar1 numeric,
    tar2 numeric,
    sum numeric,
    id bigint NOT NULL
);


--
-- Name: TABLE tsveta; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public.tsveta IS 'для проставки тарифов в таблицу tklient, вспомогательная';


--
-- Name: tsveta_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.tsveta ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.tsveta_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: ttarif; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.ttarif (
    tkid bigint,
    tarif numeric,
    dbeg timestamp without time zone,
    dend timestamp without time zone,
    id bigint NOT NULL
);


--
-- Name: ttarif_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.ttarif ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.ttarif_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: twialon100_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.twialon100 ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.twialon100_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: vdubles; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.vdubles AS
 SELECT rez.goznak,
    count(*) AS count
   FROM ( SELECT
                CASE
                    WHEN (ta.inn IS NOT NULL) THEN ta.name
                    ELSE tk.name
                END AS klient,
            t2.object,
                CASE
                    WHEN ("substring"(upper(replace(t2.object, ' '::text, ''::text)), '[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}'::text) IS NOT NULL) THEN "substring"(upper(replace(t2.object, ' '::text, ''::text)), '[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}'::text)
                    ELSE
                    CASE
                        WHEN ("substring"(upper(replace(t2.object, ' '::text, ''::text)), '\d{4}(?<!000)[АВЕКМНОРСТУХ]{2}'::text) IS NOT NULL) THEN "substring"(upper(replace(t2.object, ' '::text, ''::text)), '\d{4}(?<!000)[АВЕКМНОРСТУХ]{2}'::text)
                        ELSE NULL::text
                    END
                END AS goznak
           FROM ((((public.tdata t2
             LEFT JOIN public.twialon100 tw ON ((tw.logintd = t2.login)))
             LEFT JOIN public.tklient tk ON ((tk.id = tw.tkid)))
             LEFT JOIN public.tagat ta ON (((ta.idsystem = t2.idsystem) AND (ta.idobject = t2.idobject) AND ((t2.dimport >= ta.dbeg) AND (t2.dimport <= ta.dend)))))
             LEFT JOIN public.temail tm ON (((tm.inn =
                CASE
                    WHEN (ta.inn IS NOT NULL) THEN ta.inn
                    ELSE tk.inn
                END) AND
                CASE
                    WHEN ((tm.kpp IS NULL) AND (
                    CASE
                        WHEN (ta.inn IS NOT NULL) THEN ta.kpp
                        ELSE tk.kpp
                    END IS NULL)) THEN true
                    ELSE (tm.kpp =
                    CASE
                        WHEN (ta.inn IS NOT NULL) THEN ta.kpp
                        ELSE tk.kpp
                    END)
                END)))
          WHERE ((t2.isactive = ' Да'::text) AND (tk.inn IS NOT NULL) AND (upper(t2.object) !~~ '%ТЕСТ%'::text) AND (NOT ((upper(t2.object) ~~ '%TEST%'::text) AND (upper(t2.object) !~~ '%MICROTEST%'::text))) AND (upper(t2.object) !~~ '%ПРИОСТ%'::text) AND (upper(t2.object) !~~ '%ППРО%'::text) AND (upper(t2.object) !~~ '%НОВТ%'::text) AND (NOT ((upper(t2.object) ~~ '%ПЕРЕ%'::text) AND (t2.idsystem = ANY (ARRAY[11, 16])))) AND (NOT ((upper(t2.login) ~~ '%ТЕСТ%'::text) AND (t2.idsystem = 15))) AND (tk.id <> ALL (ARRAY[(2752)::bigint, (1925)::bigint, (3287)::bigint])) AND (t2.dimport = ( SELECT max(tdata.dimport) AS max
                   FROM public.tdata)))) rez
  WHERE (rez.goznak IS NOT NULL)
  GROUP BY rez.goznak
 HAVING (count(*) > 1);


--
-- Name: vtofind; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.vtofind AS
 SELECT DISTINCT t2.login
   FROM public.tdata t2
  WHERE ((t2.isactive ~~ '%Да%'::text) AND (NOT (EXISTS ( SELECT tw.klient,
            tw.login,
            tw.id,
            tw.logintd
           FROM public.twialon100 tw
          WHERE (tw.logintd = t2.login)))));


--
-- Name: vwialon; Type: VIEW; Schema: public; Owner: -
--

CREATE VIEW public.vwialon AS
 SELECT tw.login,
    count(*) AS count
   FROM public.twialon100 tw
  GROUP BY tw.login
 HAVING (count(*) > 1);


--
-- Name: tagat id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tagat ALTER COLUMN id SET DEFAULT nextval('public.tagat_id_seq'::regclass);


--
-- Name: temail id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temail ALTER COLUMN id SET DEFAULT nextval('public.temail_id_seq'::regclass);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: tdata t20221218_0140_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tdata
    ADD CONSTRAINT t20221218_0140_pkey PRIMARY KEY (id);


--
-- Name: tagat tagat_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tagat
    ADD CONSTRAINT tagat_pkey PRIMARY KEY (id);


--
-- Name: temail temail_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.temail
    ADD CONSTRAINT temail_pkey PRIMARY KEY (id);


--
-- Name: tklient tklient_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.tklient
    ADD CONSTRAINT tklient_pkey PRIMARY KEY (id);


--
-- Name: ttarif ttarif_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ttarif
    ADD CONSTRAINT ttarif_pkey PRIMARY KEY (id);


--
-- Name: twialon100 twialon100_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.twialon100
    ADD CONSTRAINT twialon100_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ttarif fk_tklient; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.ttarif
    ADD CONSTRAINT fk_tklient FOREIGN KEY (tkid) REFERENCES public.tklient(id);


--
-- PostgreSQL database dump complete
--
