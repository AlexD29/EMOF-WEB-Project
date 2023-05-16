--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-05-16 19:57:45

--
-- TOC entry 223 (class 1255 OID 24696)
-- Name: delete_all_data(); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.delete_all_data()
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM RESPONSES;
	DELETE FROM QUESTIONS;
	DELETE FROM FORMS;
	DELETE FROM USERS;
END;
$$;


ALTER PROCEDURE public.delete_all_data() OWNER TO postgres;

--
-- TOC entry 224 (class 1255 OID 24699)
-- Name: populate_tables(integer, integer, integer, integer); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.populate_tables(IN p_nr_users integer, IN p_nr_forms integer, IN p_nr_q_per_form integer, IN p_nr_resp_per_q integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_id_q BIGINT;
BEGIN
	FOR j IN 1..200 LOOP
		INSERT INTO users(username) VALUES(random_str(7));
	END LOOP;

	FOR i IN 1..200 LOOP
		INSERT INTO forms(id_creator, name) VALUES((select id from users order by random() limit 1), random_str(7));
		FOR j IN 1..10 LOOP
			INSERT INTO questions(id_form, text) VALUES((select id from forms order by random() limit 1), random_str(7)) RETURNING id INTO v_id_q;
			FOR k IN 1..100 LOOP
				INSERT INTO responses(id_question, emotion) VALUES(v_id_q, 'Extatic');
			END LOOP;
		END LOOP;
	END LOOP;
END; $$;


ALTER PROCEDURE public.populate_tables(IN p_nr_users integer, IN p_nr_forms integer, IN p_nr_q_per_form integer, IN p_nr_resp_per_q integer) OWNER TO postgres;

--
-- TOC entry 222 (class 1255 OID 24698)
-- Name: random_str(integer); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.random_str(p_length integer) RETURNS character varying
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_str CHARACTER VARYING;
BEGIN
	SELECT ARRAY_TO_STRING(ARRAY(SELECT SUBSTR(' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_', (random()*(64-1) + 1)::INTEGER,1) FROM generate_series(1,p_length)),'') INTO v_str;
	RETURN v_str;
END; $$;


ALTER FUNCTION public.random_str(p_length integer) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 24647)
-- Name: forms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.forms (
    id bigint NOT NULL,
    id_creator bigint NOT NULL,
    name character varying NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    expires_at timestamp with time zone,
    public boolean DEFAULT false NOT NULL
);


ALTER TABLE public.forms OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 24692)
-- Name: forms_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.forms ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.forms_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 215 (class 1259 OID 24654)
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.questions (
    text text,
    image text,
    id bigint NOT NULL,
    id_form bigint NOT NULL
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 24693)
-- Name: questions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.questions ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.questions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 216 (class 1259 OID 24659)
-- Name: responses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.responses (
    emotion character varying,
    text text,
    id bigint NOT NULL,
    id_question bigint NOT NULL
);


ALTER TABLE public.responses OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 24694)
-- Name: responses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.responses ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.responses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 217 (class 1259 OID 24664)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24695)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);

--
-- TOC entry 3359 (class 0 OID 0)
-- Dependencies: 218
-- Name: forms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.forms_id_seq', 874, true);


--
-- TOC entry 3360 (class 0 OID 0)
-- Dependencies: 219
-- Name: questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.questions_id_seq', 9794, true);


--
-- TOC entry 3361 (class 0 OID 0)
-- Dependencies: 220
-- Name: responses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.responses_id_seq', 961085, true);


--
-- TOC entry 3362 (class 0 OID 0)
-- Dependencies: 221
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 784, true);


--
-- TOC entry 3194 (class 2606 OID 24672)
-- Name: forms forms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.forms
    ADD CONSTRAINT forms_pkey PRIMARY KEY (id);


--
-- TOC entry 3196 (class 2606 OID 24674)
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- TOC entry 3198 (class 2606 OID 24676)
-- Name: responses responses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_pkey PRIMARY KEY (id);


--
-- TOC entry 3200 (class 2606 OID 24670)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3201 (class 2606 OID 24677)
-- Name: forms forms_id_creator_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.forms
    ADD CONSTRAINT forms_id_creator_fkey FOREIGN KEY (id_creator) REFERENCES public.users(id);


--
-- TOC entry 3202 (class 2606 OID 24682)
-- Name: questions questions_id_form_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_id_form_fkey FOREIGN KEY (id_form) REFERENCES public.forms(id) NOT VALID;


--
-- TOC entry 3203 (class 2606 OID 24687)
-- Name: responses responses_id_question_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_id_question_fkey FOREIGN KEY (id_question) REFERENCES public.questions(id) NOT VALID;


-- Completed on 2023-05-16 19:57:45

--
-- PostgreSQL database dump complete
--

