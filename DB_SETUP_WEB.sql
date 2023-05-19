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
-- TOC entry 235 (class 1255 OID 24755)
-- Name: populate_tables(integer, integer, integer, integer); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.populate_tables(IN p_nr_users integer, IN p_nr_forms integer, IN p_nr_q_per_form integer, IN p_nr_resp_per_q integer)
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_id_q BIGINT;
	v_id_f BIGINT;
BEGIN
	FOR j IN 1..p_nr_users LOOP
		INSERT INTO users(username) VALUES(random_str(7));
	END LOOP;

	FOR i IN 1..p_nr_forms LOOP
		INSERT INTO forms(id_creator, name) VALUES((select id from users order by random() limit 1), random_str(7)) RETURNING id INTO v_id_f;
		FOR j IN 1..p_nr_q_per_form LOOP
			INSERT INTO questions(id_form, text, q_index) VALUES(v_id_f, random_str(7), j) RETURNING id INTO v_id_q;
			FOR k IN 1..p_nr_resp_per_q LOOP
				INSERT INTO responses(id_question, emotion) VALUES(v_id_q, 'Extatic');
			END LOOP;
		END LOOP;
	END LOOP;
END; $$;


ALTER PROCEDURE public.populate_tables(IN p_nr_users integer, IN p_nr_forms integer, IN p_nr_q_per_form integer, IN p_nr_resp_per_q integer) OWNER TO postgres;

--
-- TOC entry 223 (class 1255 OID 24756)
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

--
-- TOC entry 236 (class 1255 OID 24811)
-- Name: set_question_index(bigint, bigint); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.set_question_index(IN p_id_question bigint, IN p_new_index bigint)
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_id_form BIGINT;
	v_old_index BIGINT;
	v_i BIGINT;
	v_till BIGINT;
BEGIN
	SELECT id_form, q_index INTO v_id_form, v_old_index FROM questions WHERE id = p_id_question;
	
	IF p_new_index < 1 OR p_new_index > (SELECT MAX(q_index) FROM questions WHERE id_form = v_id_form) THEN
		RAISE EXCEPTION USING MESSAGE = 'New index not in range';
	END IF;
					
	IF p_new_index < v_old_index THEN
		v_i := p_new_index;
		v_till := v_old_index;
	ELSE
		v_i := v_old_index;
		v_till := p_new_index;
	END IF;
	
	UPDATE questions SET q_index = q_index - 1 WHERE id_form = v_id_form AND q_index BETWEEN v_i AND v_till;
	UPDATE questions SET q_index = p_new_index WHERE id = p_id_question;
	
END;
$$;


ALTER PROCEDURE public.set_question_index(IN p_id_question bigint, IN p_new_index bigint) OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 24757)
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
-- TOC entry 215 (class 1259 OID 24764)
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
-- TOC entry 216 (class 1259 OID 24765)
-- Name: questions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.questions (
    text text,
    image text,
    id bigint NOT NULL,
    id_form bigint NOT NULL,
    q_index bigint NOT NULL
);


ALTER TABLE public.questions OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 24770)
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
-- TOC entry 218 (class 1259 OID 24771)
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
-- TOC entry 219 (class 1259 OID 24776)
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
-- TOC entry 220 (class 1259 OID 24777)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 24782)
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
-- TOC entry 3347 (class 0 OID 24757)
-- Dependencies: 214
-- Data for Name: forms; Type: TABLE DATA; Schema: public; Owner: postgres


--
-- TOC entry 3360 (class 0 OID 0)
-- Dependencies: 215
-- Name: forms_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.forms_id_seq', 1, true);


--
-- TOC entry 3361 (class 0 OID 0)
-- Dependencies: 217
-- Name: questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.questions_id_seq', 1, true);


--
-- TOC entry 3362 (class 0 OID 0)
-- Dependencies: 219
-- Name: responses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.responses_id_seq', 1 true);


--
-- TOC entry 3363 (class 0 OID 0)
-- Dependencies: 221
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- TOC entry 3195 (class 2606 OID 24784)
-- Name: forms forms_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.forms
    ADD CONSTRAINT forms_pkey PRIMARY KEY (id);


--
-- TOC entry 3197 (class 2606 OID 24786)
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


--
-- TOC entry 3199 (class 2606 OID 24788)
-- Name: responses responses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_pkey PRIMARY KEY (id);


--
-- TOC entry 3201 (class 2606 OID 24790)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3202 (class 2606 OID 24791)
-- Name: forms forms_id_creator_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.forms
    ADD CONSTRAINT forms_id_creator_fkey FOREIGN KEY (id_creator) REFERENCES public.users(id);


--
-- TOC entry 3203 (class 2606 OID 24796)
-- Name: questions questions_id_form_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_id_form_fkey FOREIGN KEY (id_form) REFERENCES public.forms(id) NOT VALID;


--
-- TOC entry 3204 (class 2606 OID 24801)
-- Name: responses responses_id_question_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.responses
    ADD CONSTRAINT responses_id_question_fkey FOREIGN KEY (id_question) REFERENCES public.questions(id) NOT VALID;


-- Completed on 2023-05-19 14:37:53

--
-- PostgreSQL database dump complete
--

