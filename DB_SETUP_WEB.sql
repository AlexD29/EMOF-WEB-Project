--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-06-07 12:41:51
--
-- TOC entry 853 (class 1247 OID 27301)
-- Name: form_status; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.form_status AS ENUM (
    'draft',
    'active',
    'closed'
);


ALTER TYPE public.form_status OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 216 (class 1259 OID 27243)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id character varying(16) PRIMARY KEY,
    username character varying NOT NULL,
    email character varying NOT NULL,
    created_at date DEFAULT now() NOT NULL,
    updated_at date DEFAULT now() NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 27229)
-- Name: forms; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.forms (
    id character varying(16) PRIMARY KEY,
    id_creator character varying(16) NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name character varying NOT NULL,
    created_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    expires_at timestamp with time zone,
    public boolean DEFAULT false NOT NULL,
    questions json NOT NULL,
    image bytea,
    status public.form_status DEFAULT 'draft'::public.form_status NOT NULL
);


ALTER TABLE public.forms OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 27237)
-- Name: responses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.responses (
    id character varying(16) PRIMARY KEY,
    response json NOT NULL,
    id_form character varying(16) NOT NULL REFERENCES forms(id) ON DELETE CASCADE,
    submitted_at timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.responses OWNER TO postgres;

--
-- TOC entry 217 (class 1255 OID 27250)
-- Name: delete_all(); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.delete_all()
    LANGUAGE plpgsql
    AS $$
BEGIN
	DELETE FROM responses;
	DELETE FROM forms;
	DELETE FROM users;
END;
$$;


ALTER PROCEDURE public.delete_all() OWNER TO postgres;

--
-- TOC entry 218 (class 1255 OID 27251)
-- Name: generateid(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.generateid() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_cuv CHARACTER VARYING(16) := '';
	v_alphabet TEXT := 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
	v_c RECORD;
BEGIN
	LOOP
		FOR i IN 1..16 LOOP
			v_cuv := CONCAT(v_cuv,SUBSTRING(v_alphabet,(random() * (LENGTH(v_alphabet) - 1))::INT + 1,1));
		END LOOP;
		EXECUTE FORMAT('SELECT * FROM %s WHERE id = %L', TG_TABLE_NAME, NEW.id) INTO v_c;
		IF v_c IS NULL THEN EXIT; END IF;
	END LOOP;
	NEW.id := v_cuv;
	RETURN NEW;
END;
$$;


ALTER FUNCTION public.generateid() OWNER TO postgres;

--
-- TOC entry 232 (class 1255 OID 27252)
-- Name: populare(integer, integer, integer, integer, integer, integer); Type: PROCEDURE; Schema: public; Owner: postgres
--

CREATE PROCEDURE public.populare(IN p_nr_users integer DEFAULT 20, IN p_min_nr_forms_per_user integer DEFAULT 0, IN p_max_nr_forms_per_user integer DEFAULT 10, IN p_min_nr_questions integer DEFAULT 1, IN p_max_nr_questions integer DEFAULT 5, IN p_total_nr_responses integer DEFAULT 200)
    LANGUAGE plpgsql
    AS $$
DECLARE
	v_usernames_list CHARACTER VARYING[] := array['KebabRonin','AlexD26','stefan1anuby','roanokebamboo', 'firstfd', 'soldiercustomize', 'nutrientsaxes', 'tucsonyorkshire', 'emulationfd', 'nzhappier', 'emiratescd', 'auditingbilingual', 'qualitieschristine', 'fragmentsrapid', 'squirtthesis', 'perfumesfd', 'noaajudged', 'thugredeem', 'witnesssmooth', 'ufcontroversial', 'alamoduplication', 'junglemoisture', 'manipulationaffirmed', 'rolledtransit', 'kickingchan', 'troublespocketpc', 'hingesheating', 'towingkane', 'motivationalinvestments', 'allegationsgibraltar', 'sskfd', 'emotionspetersen', 'looksmartalabama', 'rfccultured', 'divideemerald', 'gammascrolling', 'initializefairs', 'oathpeoplesoft', 'assurancethoroughly', 'imitationnewbie', 'adjournednapa', 'fdputative', 'hotproton', 'accelerationtransition', 'capabilitytimeliness', 'aluminumtissues', 'armscomp', 'alcatelfd', 'blowslonghorn', 'encodingcleanliness', 'dumpaviv', 'movementmandates', 'similaritiesknowingly', 'tacomatreating', 'flaavoiding', 'concessionstop', 'fdcharset', 'megapixelsfd', 'tolerantdawn', 'fdpigeon', 'districtadmits', 'improvedneighbours', 'enquiryfd', 'rawpossibly', 'vancouversupplier', 'fdmcbride', 'mediateddist', 'trapers', 'dexinaccuracies', 'ecstasysect', 'wichitafd', 'entiretybooster', 'wrappingshopper', 'humiliationabbott', 'geniusstraw', 'lagunademonstrates', 'saloondiaries', 'bmpvampires', 'entranceattendance', 'slowbangbus', 'foreignersmayotte', 'relaxedisd', 'provenpromises', 'autumnleader', 'immigrantplugs', 'communistunit', 'achievedoakwood', 'statisticmexican', 'fdcapsules', 'presumedbryan', 'hotelfertility', 'statspoe', 'cratercyclone', 'uniprotkbfd', 'fdconfused', 'autographedfd', 'texturegorgeous', 'zebradissolution', 'symantectao', 'refusewhisper', 'rusreviewing', 'carbbarre', 'fdfictional', 'saladdysfunction', 'wordsturkey', 'aprilfd', 'fdvoucher', 'footballvibration', 'albanyfd', 'brewinglasers', 'almanaclotto', 'transcendbots', 'expendituresanalyze', 'wacgrow', 'willinghopes', 'enrollanime', 'originatingdeclarations', 'rhymesseat', 'pathologypostcode', 'tasksailors', 'coatingmulticultural', 'findersem', 'planetshostels', 'fdimmunization', 'fridaysveil', 'fdprospect', 'kosoverhead', 'welchtight', 'inductiongev', 'fdhickory', 'certaininspect', 'xaapartments', 'targusfd', 'describesbindings', 'wonderlandcohen', 'highermine', 'ukraineresidence', 'sidneyfd', 'computingimplement', 'connorleft', 'isaiahunisex', 'subversionwished', 'majestymethod', 'unanimouslyreports', 'richlandleakage', 'unstablerecycled', 'voicemailsampler', 'individuallycafe', 'equalsfd', 'susanfd', 'sonnyfomit', 'soulincorporating', 'jackpotadopting', 'registrationsdryer', 'rodneyfd', 'mikementioned', 'distbei', 'crazythong', 'fdrugs', 'gramsfd', 'pvproteins', 'ashlandhandled', 'unsuccessfulimpossible', 'clanfd', 'conventionalimplementation', 'mommycubs', 'singbeneficial', 'coldplayarbor', 'amgpostcards', 'altitudebackground', 'clarksonste', 'rebatestold', 'evaopinion', 'heathsouvenirs', 'viewrhapsody', 'derivativesbuddha', 'participantszoloft', 'kmfd', 'shavedfd', 'afwatchers', 'participatehorizons', 'petersask', 'maestrojabber', 'contestfd', 'crackeddownstairs', 'enjoyelectric', 'citizenshipspreadsheets', 'hormoneben', 'musicianvarieties', 'suppforeclosure', 'fwdblowout', 'joyfd', 'licenseeplaylist', 'managerialfd', 'passionateblu', 'jumpsvideotape', 'terriblealmond', 'survivedisles', 'gentleepisodes', 'governorcompiling', 'issuanceworkstation', 'elseviercashmere', 'toescassette', 'feedbackcr', 'chestprivacy', 'choraldubai', 'finnfd', 'citrixsweeney', 'eighteendrainage', 'portraitreject', 'batonaclu', 'tokendpi', 'involvingdecker', 'twistedconsequential', 'tabsfd', 'debutfd', 'mazeinvented', 'cosponsorsedits', 'hellosaul', 'outputsproviders', 'decadecarol', 'wildernessdidrex', 'colourlawson', 'numberingdoncaster', 'barcodelaps', 'gentlyevidenced', 'battleshelmets', 'webcambegin', 'chaserdavis', 'pedestrianfd', 'luxuriousreuse', 'consensuslawrence', 'suburbfd', 'worksheetpopular', 'newsgroupgaps', 'nasutp', 'pornographyphilippine', 'fddave', 'fdvon', 'exilefd', 'folkcycles', 'fillertranslation', 'arrangementscannon', 'janissyrian', 'authorizationracial', 'pembrokewilling', 'panelsrefinancing', 'downloadablesingular', 'rejectsreveal', 'sufferspic', 'fdpsi', 'employersrealty', 'pegdesigners', 'tailedpipe', 'strollerlookup', 'tuckcirculating', 'ombpile', 'piercemill', 'lloydrelevance', 'listenfd', 'fdpf', 'appraisalslength', 'measurednest', 'hathcarol', 'skypesea', 'applypete', 'logicalcontracts', 'fduse', 'indemnityexam', 'fdstyling', 'fdfunk', 'psalmexpedition', 'chublue', 'localizedphenotype', 'fdcancers', 'tawneebmw', 'unemploymentimpotence', 'descriptiverd', 'dummymemorandum', 'puffysimilarly', 'tracksinventor', 'fasovm', 'boutfd', 'backendspc', 'erroneousinvasive', 'complainantfd', 'bonecollected', 'gusutc', 'kindnesssolely', 'pharmacyleonard', 'fddom', 'apisiu', 'caterpillarpor', 'lucnudist', 'neuralfd', 'papuaasian', 'fdjustin', 'solodarwin', 'notchtip', 'fenderfd', 'viestrollers', 'creekloch', 'raymondgovernment', 'couponsmissed', 'lizworks', 'minimalcommon', 'converterpile', 'leslieaforementioned', 'erectiletelnet', 'how', 'prayersname', 'recordershud', 'legallykobe', 'bizarrestephens', 'bacteriaadam', 'athletesmodifying', 'fruitsuspect', 'defectiveagency', 'rehabhaha', 'amazontraveler', 'dztents', 'abortionexpedited', 'restartrutgers', 'parkacting', 'regardlessknock', 'sambaessence', 'cardiologymeasurement', 'menrichie', 'fiercelikewise', 'barbecuerefinancing', 'respectingsize', 'discloseresidency', 'gabrielchunk', 'commodoresaturday', 'attainexpression', 'children', 'italia', 'toolsprudent', 'pool', 'scenterp', 'oprahdatabases', 'arinnovelties', 'gathercloud', 'vivalost', 'songexterior', 'gwentied', 'lockedpenny', 'attempt', 'techrepublic', 'turinprosecutors', 'buckletoaster', 'proteinswwf', 'amyfencing', 'nesteddifficulties', 'loggerskull', 'soccermotorized', 'pimpminutes', 'retrievingcould', 'foundationsprinceton', 'abatf', 'lockreceive', 'statingcider', 'blackberrybishops', 'njnortel', 'rutgersuna', 'oslooutsourcing', 'emc', 'downtownhat', 'hereinmaurice', 'ampmanagerial', 'latinathreaten', 'outingqi', 'vegetableszoe', 'lightlyspeaking', 'aliexcuses', 'proceduresamericana', 'vt', 'malcolmpresumably', 'areasphrases', 'charteredsudan', 'macedoniaspeaking', 'lecreceivable', 'featuredtechnical', 'scientologypipelines', 'downspantie', 'ascconsist', 'employeewatch', 'controlled', 'platinumcardboard', 'seatsshapiro', 'mate', 'possessedsafaris', 'vubakery', 'cationchest', 'vampireoregon', 'expedition', 'apprenticeshipfilme', 'twinkinvoke', 'lavenderburr', 'sanyohighland', 'televisionspaperbacks', 'darkre', 'leasespressures', 'deceasedtournaments', 'repeatingbl', 'qualifiermonroe', 'immediatescanner', 'surveyorsab', 'abnormalitiesjacobs', 'discomfort', 'barncooling', 'dependence', 'warezecosystem', 'letteringbred', 'milfflooding', 'taxisems', 'pausefsa', 'championshipsregulations', 'watchlistauditor', 'entriessniper', 'retailsore', 'lipdanielle', 'tysonships', 'maintain', 'cashierthere', 'dooyoorudolph', 'dove', 'hoganrunners', 'melbournemammoth', 'viewpictureinstructions', 'psurainfall', 'places', 'stefani', 'scout', 'ivanduluth', 'fragmentssm', 'flaws', 'tubs', 'speecheslopez', 'female', 'aurafuckers', 'disconnectedhardship', 'scientificopenly', 'preparedchiropractic', 'cor', 'govtjpg', 'ellenaided', 'storm', 'outlawpalm', 'mississippifable', 'afromassive', 'obediencetaliban', 'witnessdecreased', 'bodies', 'pascalspeedway', 'villagersxslt', 'monkeysmds', 'tenthexercised', 'scientistsjudgement', 'entityoutlines', 'ribscalculator', 'segregation', 'washersmetacritic', 'schedulingannette', 'romansbiomedical', 'gensk', 'lawmakerstolkien', 'chaserconcentrated', 'lattermalaysia', 'shortcutdime', 'gridtonight', 'narrativesaver', 'ethnicityoverture', 'payabledisturbance', 'blanksealed', 'drawingcancer', 'withouthungary', 'pistondq', 'ditlatina', 'blackpoolphishing', 'refereestrictly', 'shiningcouncillor', 'catcharsenal', 'dll', 'staffingcumshot', 'instructorsinvestigator', 'tendssorted', 'articlerolls', 'discounted', 'dvd', 'doohoover', 'obsessedvega', 'congratsplayhouse', 'showroomalso', 'realizece', 'verifiedstreets', 'tributeinaccurate', 'smspd', 'estecutie', 'spam', 'guild', 'incubuscole', 'negotiateliteral', 'saoredistributed', 'statementstaxes', 'surelyankle', 'disabilitybooklet', 'invernessterre', 'dancing', 'aloe', 'psychologist', 'posts', 'syndicatedaids', 'nanochimney', 'regressionremind', 'soul', 'checkerstrikes', 'thievesproducer', 'occurrencesought', 'lynchsusceptible', 'hardyharley', 'pconfirmed', 'polynesiakernel', 'micahcertifications', 'unknownsvn', 'indie', 'transformmerchants', 'fireflysetup', 'impulsehilary', 'breakdownbunker', 'distributingfractures', 'barrflashlight', 'montyindustrial', 'aggregatorvibration', 'clearlyextending', 'msotous', 'entered', 'remodelingtoc', 'fearsadapt', 'acknowledge', 'guitarmodification', 'doctordress', 'ironintl', 'occupywtf', 'xf', 'seeksplaid', 'sacksdeviations', 'caymantravelling', 'oxygen', 'analysedamazon', 'boeingsubscriber', 'imposedexpense', 'producers', 'highbeamwrong', 'objectionthong', 'carrie', 'operative', 'variationcycle', 'ttlpossible', 'attendingconstantly', 'mccoymetaphor', 'alternativelyverses', 'suspended', 'actors', 'rihannaphotograph', 'texturedconditioners', 'stoveonboard', 'optionalasn', 'desertbrightness', 'dcplat', 'shiftreceive', 'brotherstransformers', 'rentedsurely', 'pursuantsheer', 'fewinvision', 'tonguefacials', 'ligandpam', 'karengeeks', 'contemporarypumps', 'secsgsetting', 'commentedsafeguards', 'scatteringsudbury', 'subtotaltrigger', 'strollersusie', 'instantworkflow', 'pipeslea', 'spunmanually', 'emulationbas', 'techsvault', 'realizenos', 'acornvigorous', 'collarscaptures', 'barrels', 'battalionharrisburg', 'wsenchanted', 'bookingshighlight', 'eliminatedcinnamon', 'iosalert', 'hhrotterdam', 'bilingualphone', 'mooddetector', 'believersusda', 'flirtbeacon'];
	v_username CHARACTER VARYING;
	v_user_id CHARACTER VARYING(16);
	v_emotions_list CHARACTER VARYING[] := array['joy', 'anger', 'disgust', 'excitement','sadness','fear'];
BEGIN
	-- NORMALIZE
	p_nr_users := CASE (p_nr_users > 0) WHEN TRUE THEN p_nr_users ELSE 0 END CASE;
	p_min_nr_forms_per_user := CASE (p_min_nr_forms_per_user > 0) WHEN TRUE THEN p_min_nr_forms_per_user ELSE 0 END CASE;
	p_min_nr_questions := CASE (p_min_nr_questions > 0) WHEN TRUE THEN p_min_nr_questions ELSE 0 END CASE;
	p_total_nr_responses := CASE (p_total_nr_responses > 0) WHEN TRUE THEN p_total_nr_responses ELSE 0 END CASE;
	-- ERROR HANDLING
	IF p_max_nr_forms_per_user < p_min_nr_forms_per_user THEN
		RAISE EXCEPTION 'Forms max less than min';
	END IF;
	IF p_max_nr_questions < p_min_nr_questions THEN
		RAISE EXCEPTION 'Questions max less than min';
	END IF;
	
	

	-- INSERT USERS
	FOR v_i IN 1..p_nr_users LOOP
		LOOP BEGIN
			v_username := v_usernames_list[(random() * (ARRAY_LENGTH(v_usernames_list,1) - 1))::INTEGER];
			INSERT INTO users(username, email, password) VALUES (v_username, v_username || '@hotmail.com', v_username) RETURNING id INTO v_user_id;
			EXIT;
		EXCEPTION WHEN OTHERS THEN NULL;
		END; END LOOP;
		
		--INSERT FORMS
		FOR v_i IN 1..((random() * ((p_max_nr_forms_per_user - p_min_nr_forms_per_user)))::INTEGER + p_min_nr_forms_per_user) LOOP
			DECLARE
				v_public BOOLEAN := random() > 0.5;
				v_published FORM_STATUS;
				v_name TEXT := 'topic' || v_i ||'_'||v_user_id;
				v_questions TEXT := '{ "description" : "This form is about something very interesting" , "ending" : "Thank you for your time" , "questions" : {';
			BEGIN
				IF random() < 0.33 THEN
					v_published := 'draft';
				ELSIF random() < 0.5 THEN 
					v_published := 'active';
				ELSE
					v_published := 'closed';
				END IF;
			
				FOR v_j IN 1..((random() * ((p_max_nr_questions - p_min_nr_questions)))::INTEGER + p_min_nr_questions) LOOP
					v_questions := CONCAT(v_questions,'"'|| v_j ||'":"What about '|| v_j || '_' || v_name || '?",');
				END LOOP;
				v_questions := SUBSTR(v_questions, 1, LENGTH(v_questions) - 1);
				v_questions := CONCAT(v_questions, '} }');
				
				INSERT INTO forms(id_creator, name, public, status, questions) VALUES(v_user_id, v_name, v_public, v_published, v_questions::JSON);
			END;
		END LOOP;
	END LOOP;
	
	-- INSERT RESPONSES
	FOR v_i IN 1..p_total_nr_responses LOOP
		DECLARE
			v_id CHARACTER VARYING(16);
			v_response TEXT := '{';
		BEGIN
			SELECT id INTO v_id FROM forms WHERE status <> 'draft' ORDER BY RANDOM() LIMIT 1;
			FOR v_j IN 1..(SELECT count(*) FROM jsonb_object_keys((select questions FROM forms where id = v_id)::jsonb)) LOOP
					v_response := CONCAT(v_response,'"'|| v_j ||'":[');
					DECLARE
						v_emotions CHARACTER VARYING[] := array[]::CHARACTER VARYING[];
						v_emotion CHARACTER VARYING;
						v_flag BOOLEAN;
					BEGIN
						v_flag := FALSE;
						FOR v_k IN 1..(random() * 3)::INTEGER LOOP
							v_emotion := v_emotions_list[(random()*(ARRAY_LENGTH(v_emotions_list,1) -1 ) + 1)::INTEGER];
							IF NOT (v_emotions @> array[v_emotion]) THEN
								v_emotions := v_emotions || v_emotion;
								v_response := CONCAT(v_response, '"'||v_emotion||'",');
								v_flag := TRUE;
							END IF;
						END LOOP;
						IF v_flag = TRUE THEN 
							v_response := SUBSTR(v_response, 1, LENGTH(v_response) - 1);
						END IF;
					END;
					v_response := CONCAT(v_response,'],');
			END LOOP;
			v_response := SUBSTR(v_response, 1, LENGTH(v_response) - 1);
			v_response := CONCAT(v_response, '}');
			INSERT INTO responses(id_form, response) VALUES(v_id, v_response::JSON);
		END;
	END LOOP;
END;
$$;


ALTER PROCEDURE public.populare(IN p_nr_users integer, IN p_min_nr_forms_per_user integer, IN p_max_nr_forms_per_user integer, IN p_min_nr_questions integer, IN p_max_nr_questions integer, IN p_total_nr_responses integer) OWNER TO postgres;

--
-- TOC entry 219 (class 1255 OID 27254)
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
-- TOC entry 220 (class 1255 OID 27255)
-- Name: update_updated_at(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.update_updated_at() RETURNS trigger
    LANGUAGE plpgsql
    AS $$BEGIN
	NEW.updated_at := NOW();
	RETURN NEW;
END;$$;


ALTER FUNCTION public.update_updated_at() OWNER TO postgres;

--
-- TOC entry 3201 (class 2606 OID 27263)
-- Name: users users_username_username1_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_username1_key UNIQUE (username) INCLUDE (username);


--
-- TOC entry 3204 (class 2620 OID 27264)
-- Name: forms tg_forms_generate_id; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER tg_forms_generate_id BEFORE INSERT ON public.forms FOR EACH ROW EXECUTE FUNCTION public.generateid();


--
-- TOC entry 3205 (class 2620 OID 27265)
-- Name: responses tg_responses_generate_id; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER tg_responses_generate_id BEFORE INSERT ON public.responses FOR EACH ROW EXECUTE FUNCTION public.generateid();


--
-- TOC entry 3206 (class 2620 OID 27266)
-- Name: users tg_users_generate_id; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER tg_users_generate_id BEFORE INSERT ON public.users FOR EACH ROW EXECUTE FUNCTION public.generateid();


--
-- TOC entry 3207 (class 2620 OID 27267)
-- Name: users trg_users_updated_at; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_users_updated_at BEFORE UPDATE ON public.users FOR EACH ROW EXECUTE FUNCTION public.update_updated_at();

-- Completed on 2023-06-07 12:41:51

--
-- PostgreSQL database dump complete
--

