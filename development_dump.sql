--
-- Start with a fresh database
--

DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'SQL_ASCII';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

CREATE TABLE users_t (
    email character varying(64) NOT NULL UNIQUE,
    token character varying(32) NOT NULL
);

ALTER TABLE public.users_t OWNER TO adicu;

--
-- Name: courses_v2_t; Type: TABLE; Schema: public; Owner: adicu; Tablespace: 
--

CREATE TABLE courses_v2_t (
    course character varying(32) NOT NULL,
    coursefull character varying(32),
    prefixname character varying(32),
    divisioncode character varying(32),
    divisionname character varying(64),
    schoolcode character varying(32),
    schoolname character varying(64),
    departmentcode character varying(32),
    departmentname character varying(64),
    subtermcode character varying(32),
    subtermname character varying(64),
    enrollmentstatus character varying(32),
    numfixedunits integer,
    minunits integer,
    maxunits integer,
    coursetitle character varying(64),
    coursesubtitle character varying(64),
    approval character varying(32),
    bulletinflags character varying(32),
    classnotes character varying(64),
    prefixlongname character varying(32),
    description text
);


ALTER TABLE public.courses_v2_t OWNER TO adicu;

--
-- Name: housing_amenities_t; Type: TABLE; Schema: public; Owner: adicu; Tablespace: 
--

CREATE TABLE housing_amenities_t (
    building character varying(32),
    apartmentstyle boolean,
    suitestyle boolean,
    corridorstyle boolean,
    privatebathroom boolean,
    semiprivatebathroom boolean,
    sharedbathroom boolean,
    privatekitchen boolean,
    semiprivatekitchen boolean,
    sharedkitchen boolean,
    lounge character varying(32)
);


ALTER TABLE public.housing_amenities_t OWNER TO adicu;

--
-- Name: housing_t; Type: TABLE; Schema: public; Owner: adicu; Tablespace: 
--

CREATE TABLE housing_t (
    roomlocationarea character varying(32),
    residentialarea character varying(32),
    roomlocation character varying(32),
    roomlocationsection character varying(32),
    roomlocationfloorsuite character varying(32),
    issuite boolean,
    floorsuitewebdescription character varying(32),
    room character varying(32),
    roomarea integer,
    roomspace character varying(32),
    roomtype character varying(32),
    ay1213rsstatus character varying(32),
    pointvalue double precision,
    lotterynumber integer
);


ALTER TABLE public.housing_t OWNER TO adicu;

--
-- Name: sections_v2_t; Type: TABLE; Schema: public; Owner: adicu; Tablespace: 
--

CREATE TABLE sections_v2_t (
    callnumber integer,
    sectionfull character varying(32),
    course character varying(32),
    term character varying(32),
    numenrolled integer,
    maxsize integer,
    typecode character varying(32),
    typename character varying(32),
    meets1 character varying(64),
    meets2 character varying(64),
    meets3 character varying(64),
    meets4 character varying(64),
    meets5 character varying(64),
    meets6 character varying(64),
    meetson1 character varying(32),
    starttime1 time without time zone,
    endtime1 time without time zone,
    building1 character varying(32),
    room1 character varying(32),
    meetson2 character varying(32),
    starttime2 time without time zone,
    endtime2 time without time zone,
    building2 character varying(32),
    room2 character varying(32),
    meetson3 character varying(32),
    starttime3 time without time zone,
    endtime3 time without time zone,
    building3 character varying(32),
    room3 character varying(32),
    meetson4 character varying(32),
    starttime4 time without time zone,
    endtime4 time without time zone,
    building4 character varying(32),
    room4 character varying(32),
    meetson5 character varying(32),
    starttime5 time without time zone,
    endtime5 time without time zone,
    building5 character varying(32),
    room5 character varying(32),
    meetson6 character varying(32),
    starttime6 time without time zone,
    endtime6 time without time zone,
    building6 character varying(32),
    room6 character varying(32),
    exammeetson character varying(32),
    examstarttime time without time zone,
    examendtime time without time zone,
    exambuilding character varying(32),
    examroom character varying(32),
    exammeet character varying(64),
    examdate character varying(32),
    instructor1name character varying(32),
    instructor2name character varying(32),
    instructor3name character varying(32),
    instructor4name character varying(32),
    campuscode character varying(32),
    campusname character varying(32)
);


ALTER TABLE public.sections_v2_t OWNER TO adicu;

--
-- Data for Name: courses_v2_t; Type: TABLE DATA; Schema: public; Owner: adicu
--

COPY courses_v2_t (course, coursefull, prefixname, divisioncode, divisionname, schoolcode, schoolname, departmentcode, departmentname, subtermcode, subtermname, enrollmentstatus, numfixedunits, minunits, maxunits, coursetitle, coursesubtitle, approval, bulletinflags, classnotes, prefixlongname, description) FROM stdin;
COMS0001	COMSE0001	COMPUT SCI	EN	SCH OF ENGR & APP SCI: UGRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	0	0	0	FOUND OF COMPUT SCI-TRACK	FOUND OF COMPUTER SCI-TRACK		CEFX		COMPUTER SCIENCE	\N
COMS0002	COMSE0002	COMPUT SCI	EN	SCH OF ENGR & APP SCI: UGRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	0	0	0	SOFTWARE SYSTEMS TRACK	SOFTWARE SYSTEMS TRACK		CEFX		COMPUTER SCIENCE	\N
COMS0003	COMSE0003	COMPUT SCI	EN	SCH OF ENGR & APP SCI: UGRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	0	0	0	ARTIFICIAL INTELLIGENCE TRACK	ARTIFICIAL INTELLIGENCE-TRACK		CEFX		COMPUTER SCIENCE	\N
COMS0004	COMSE0004	COMPUT SCI	EN	SCH OF ENGR & APP SCI: UGRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	0	0	0	APPLICATIONS-TRACK	APPLICATIONS-TRACK		CEFX		COMPUTER SCIENCE	\N
COMS0005	COMSE0005	COMPUT SCI	EN	SCH OF ENGR & APP SCI: UGRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	0	0	0	VISION & GRAPHICS-TRACK	VISION & GRAPHICS-TRACK		CEFX		COMPUTER SCIENCE	\N
COMS0006	COMSE0006	COMPUT SCI	EN	SCH OF ENGR & APP SCI: UGRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	0	0	0	DIGITAL SYSTEMS TRACK	DIGITAL SYSTEMS TRACK		CEFX		COMPUTER SCIENCE	\N
COMS1001	COMSW1001	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	INTRO TO INFORMATION SCIENCE	INTRO TO INFORMATION SCIENCE		CEFKRX9		COMPUTER SCIENCE	              Basic Introduction to concepts and skills in Information Sciences: human-computer interfaces, representing information digitally, organizing and searching information on the World Wide Web, principles of algorithmic problem solving, introduction to database concepts, introduction to programming in Python.
CSEE6868	CSEEE6868	COMPTSCIEE	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	SYSTEM-ON-CHIP PLATFORMS	SYSTEM-ON-CHIP PLATFORMS	INS	GI	INSTRUCTOR'S PERMISSION IS NECESSARY TO REG FOR THE COURSE	COMPUTER SCI-ELECTRICAL ENGIN	\N
COMS4231	COMSS4231	COMPUT SCI	SS	CE & SPEC PRG: SUMMER SESSION	SPEC	SCHOOL OF CONTINUING EDUCATION	COMS	COMPUTER SCIENCE	D	1ST 6 WEEKS	O	30	0	0	ANALYSIS OF ALGORITHMS	ANALYSIS OF ALGORITHMS		S		COMPUTER SCIENCE	Introduction to the design and analysis of efficient algorithms. Topics include models of computation, efficient sorting and searching, algorithms for algebraic problems, graph algorithms, dynamic programming, probabilistic methods, approximation algorithms, and NP-completeness. Note: This course is the same as CSOR W4231 (CS and IEOR Department).
CSOR4246	CSORW4246	COMS-OPRE	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	ALGORITHMS FOR DATA SCIENCE	ALGORITHMS FOR DATA SCIENCE		I		COMPUTER SCI-OPERATIONS RES	\N
CSEE4823	CSEEW4823	COMPTSCIEE	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	ADVANCED LOGIC DESIGN	ADVANCED LOGIC DESIGN		CEFKGRUXI		COMPUTER SCI-ELECTRICAL ENGIN	An introduction to modern digital system design.  Advanced topics in digital logic: controller synthesis (Mealy and Moore machines); adders and multipliers; structured logic blocks (PLDs, PALs, ROMs); iterative circuits.  Modern design methodology: register transfer level modeling (RTL); algorithmic state machines (ASMs); introduction to hardware description languages (VHDL or Verilog); system-level modeling and simulation; design examples.
COMS1404	COMSW1404	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	10	0	0	EMERGING SCHOLARS PROG SEMINAR	EMERGING SCHOLARS PROG SEMINAR	INS	CEFKRX9	STUDENTS MAY ONLY ENROLL WITH INSTRUCTOR PERMISSION	COMPUTER SCIENCE	Peer led weekly seminar intended for first and second year undergraduates considering a major in Computer Science. Pass/Fail only. May not be used towards satisfying the major or SEAS credit requirements.
COMS1004	COMSW1004	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	INTRO-COMPUT SCI/PROG IN JAVA	INTRO-COMPUT SCI/PROG IN JAVA		CEFKRX9		COMPUTER SCIENCE	A general introduction to computer science for science and engineering students interested in majoring in computer science or engineering. Covers fundamental concepts of computer science, algorithmic problem-solving capabilities, and introductory Java programming skills. Assumes no prior programming background. Columbia University students may receive credit for only one of the following three courses: 1003, 1004, and 1005.
COMS1005	COMSW1005	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	INTRO-COMPUT SCI/PROG-MATLAB	INTRO-COMPUT SCI/PROG-MATLAB		CEFKRX9		COMPUTER SCIENCE	A general introduction to computer science concepts, algorithmic problem-solving capabilities, and programming skills in MATLAB. Assumes no prior programming background. Columbia University students may receive credit for only one of the following three courses: 1003, 1004, and 1005.
ENGI1006	ENGIE1006	ENGINEERNG	EN	SCH OF ENGR & APP SCI: UGRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	INTRO TO COMP FOR ENG/APP SCI	INTRO TO COMP FOR ENG/APP SCI		CEFX		ENGINEERING	An interdisciplinary course in computing intended for first year SEAS students. Introduces computational thinking, algorithmic problem solving and Python programming with applications in science and engineering. Assumes no prior programming background.
COMS1007	COMSW1007	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	HONORS INTRO TO COMPUTER SCI	OBJECT-ORIENTED PROG/DES(JAVA		CEFKRX9		COMPUTER SCIENCE	An honors-level introduction to computer science, intended primarily for students considering a major in computer science. Computer science as a science of abstraction. Creating models for reasoning about and solving problems. The basic elements of computers and computer programs. Implementing abstractions using data structures and algorithms. Taught in java.
COMS3101	COMSW3101	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	10	0	0	PROGRAMMING LANGUAGES	PROGRAMMING LANG:RUBY ON RAILS		CEFKGRUXI	STARTS: 3/25 - 4/29/13	COMPUTER SCIENCE	Introduction to a programming language. Each section is devoted to a specific language. Intended only for those who are already fluent in at least one programming language. Sections may meet for one hour per week for the whole term, for three hours per week for the first third of the term, or for two hours per week for the first six weeks. May be repeated for credit if different languages are involved.
COMS3134	COMSW3134	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	DATA STRUCTURES IN JAVA	DATA STRUCTURES IN JAVA		CEFKGRUXI		COMPUTER SCIENCE	Data types and structures: arrays, stacks, singly and doubly linked lists, queues, trees, sets, and graphs. Programming techniques for processing such structures: sorting and searching, hashing, garbage collection. Storage management. Rudiments of the analysis of algorithms. Taught in Java. Note: Due to significant overlap, students may receive credit for only one of the following four courses: COMS W3134, COMS W3136, COMS W3137
COMS3136	COMSW3136	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	40	0	0	ESSENTIAL DATA STRUCTURES	ESSENTIAL DATA STRUCTURES		CEFKGRUXI		COMPUTER SCIENCE	A second programming course intended for non-majors with at least one semester of introductory programming experience. Basic elements of programming in C and C++, array-based data structures, heaps, linked lists, C programming in UNIX environment, object-oriented programming in C++, trees, graphs, generic programming, hash tables.
COMS3137	COMSW3137	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	40	0	0	HONORS DATA STRUCTURES & ALGOL	HONORS DATA STRUCTURES & ALGOL		CEFKGRUXI		COMPUTER SCIENCE	An honors introduction to data types and structures: arrays, stacks, singly and doubly linked lists, queues, trees, sets, and graphs. Programming techniques for processing such structures: sorting and searching, hashing, garbage collection. Storage management. Design and analysis of algorithms. Taught in Java. Note: Due to significant overlap, students may receive credit for only one of the following four courses: COMS W3133, W3134, W3137.
COMS3157	COMSW3157	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	40	0	0	ADVANCED PROGRAMMING	ADVANCED PROGRAMMING		CEFKGRUXI		COMPUTER SCIENCE	Practical, hands-on introduction to programming techniques and tools for professional software construction, including learning how to write code to given specifications as well as document the results. Provides introductory overview of C and C++ in a UNIX environment, for students with Java background. Also introduces scripting languages (perl) and basic web programming. UNIX programming utilities are also covered.
COMS3203	COMSW3203	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	DISCRETE MATHEMATICS	COMBINATORICS/GRAPH THEORY		CEFKGRUXI		COMPUTER SCIENCE	Logic and formal proofs, sequences and summation, mathematical induction, binomial coefficients, elements of finite probability, recurrence relations, equivalence relations and partial orderings, and topics in graph theory (including isomorphism, traversability, planarity, and colorings).
COMS3210	COMSW3210	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	SCIENTIFIC COMPUTATION	SCIENTIFIC COMPUTATION		CEFKGRUXI		COMPUTER SCIENCE	Introduction to computation on digital computers. Design and analysis of numerical algorithms. Numerical solution of equations, integration, recurrences, chaos, differential equations. Introduction to Monte Carlo methods. Properties of floating point arithmetic. Applications to weather prediction, computational finance, computational science, and computational engineering.
COMS3251	COMSW3251	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTATIONAL LINEAR ALGEBRA	COMPUTATIONAL LINEAR ALGEBRA		CEFKGRUXI		COMPUTER SCIENCE	Computational linear algebra, solution of linear systems, sparse linear systems, least squares, eigenvalue problems, and numerical solution of other multivariate problems as time permits.
COMS3261	COMSW3261	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTER SCIENCE THEORY	COMPUTER SCIENCE THEORY		CEFKGRUXI		COMPUTER SCIENCE	Regular languages: deterministic and non-deterministic finite automata, regular expressions. Context-free languages: context-free grammars, push-down automata. Turing machines, the Chomsky hierarchy, and the Church-Turing thesis. Introduction to Complexity Theory and NP-Completeness.
COMS4160	COMSW4160	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTER GRAPHICS	COMPUTER GRAPHICS		CEFKGIRUX		COMPUTER SCIENCE	Introduction to computer graphics. Topics include 3D viewing and projections, geometric modeling using spline curves, graphics systems such as OpenGL, lighting and shading, and global illumination. Significant implementation is required: the final project involves writing an interactive 3D video game in OpenGL.
CSEE3827	CSEEW3827	COMPTSCIEE	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	FUNDAMENTALS OF COMPUTER SYSTS	FUNDAMENTALS OF COMPUTER SYSTS		CEFKGRUXI		COMPUTER SCI-ELECTRICAL ENGIN	Fundamentals of computer organization and digital logic. Boolean algebra, Karnaugh maps, basic gates and components, flipflops and latches, counters and state machines, basics of combinational and sequential digital design. Assembly language, instruction sets, ALUs, single-cycle and multi-cycle processor design, introduction to pipelined processors, caches, and virtual memory.
COMS3902	COMSW3902	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			F	0	0	0	UNDERGRADUATE THESIS	UNDERGRADUATE THESIS	INS	CEFKGRUXI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	An independent theoretical or experimental investigation by an undergraduate major of an appropriate problem in computer science carried out under the supervision of a faculty member. A formal written report is mandatory and an oral presentation may also be required. May be taken over more than one term, in which case the grade is deferred until all 6 points have been completed. Consult the department for section assignment.
COMS3998	COMSW3998	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			F	0	0	0	UNDERGRAD PROJECTS IN COMP SCI	UNDERGRAD PROJECTS IN COMP SCI	INS	CEFKGRUXI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	Independent project involving laboratory work, computer programming, analytical investigation, or engineering design. May be repeated for credit, but not for a total of more than 3 points of degree credit. Consult the department for section assignment.
COMS4111	COMSW4111	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	INTRODUCTION TO DATABASES	INTRODUCTION TO DATABASES		CEFKGIRUX		COMPUTER SCIENCE	The fundamentals of database design and application development using databases: entity-relationship modeling, logical design of relational databases, relational data definition and manipulation languages, SQL, XML, query processing, physical database tuning, transaction processing, security. Programming projects are required.
COMS4112	COMSW4112	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	DATABASE SYSTEM IMPLEMENTATION	DATABASE SYSTEM IMPLEMENTATION		CEFKGIRUX		COMPUTER SCIENCE	The principles and practice of building large-scale database management systems. Storage methods and indexing, query processing and optimization, materialized views, transaction processing and recovery, object-relational databases, parallel and distributed databases, performance considerations.  Programming projects are required.
COMS4115	COMSW4115	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			F	30	0	0	PROGRAMMING LANG & TRANSLATORS	PROGRAMMING LANG & TRANSLATORS		CEFKGIRUX		COMPUTER SCIENCE	Modern programming languages and compiler design. Imperative, object-oriented, declarative, functional, and scripting languages. Language syntax, control structures, data types, procedures and parameters, binding, scope, run-time organization, and exception handling. Implementation of language translation tools including compilers and interpreters. Lexical, syntactic and semantic analysis; code generation; introduction to code optimization. Teams implement a language and its compiler.
COMS4118	COMSW4118	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	OPERATING SYSTEMS I	OPERATING SYSTEMS I		CEFKGIRUX		COMPUTER SCIENCE	Design and implementation of operating systems. Topics include process management, process synchronization and interprocess communication, memory management, virtual memory, interrupt handling, processor scheduling, device management, I/O, and file systems. Case study of the UNIX operating system. A programming project is required.
COMS4130	COMSW4130	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	PARALLEL PROGRAMMING	PARALLEL PROGRAMMING		CEFGIX		COMPUTER SCIENCE	Principles of parallel software design. Topics include task and data decomposition, load-balancing, reasoning about correctness, determinacy, safety, and deadlock-freedom. Application of techniques through semester-long design project implementing performant, parallel application in a modern parallel programming language.
COMS4156	COMSW4156	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	ADVANCED SOFTWARE ENGINEERING	ADVANCED SOFTWARE ENGINEERING		CEFGIX		COMPUTER SCIENCE	Software lifecycle from the viewpoint of designing and implementing N-tier applications (typically utilizing web browser, web server, application server, database). Major emphasis on quality assurance (code inspection, unit and integration testing, security and stress testing). Centers on a student-designed team project that leverages component services (e.g., transactions, resource pooling, publish/subscribe) for an interactive multi-user application such as a simple game.
COMS4167	COMSW4167	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTER ANIMATION	COMPUTER ANIMATION		CEFGIX		COMPUTER SCIENCE	Previous familiarity with C is recommended. Intensive introduction to computer animation, including: fundamental theory and algorithms for computer animation, keyframing, kinematic rigging, simulation, dynamics, free-form animation, behavioral/procedural animation, particle systems, post-production; small groups implement a significant animation project; advanced topics as time permits.
COMS4170	COMSW4170	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			F	30	0	0	USER INTERFACE DESIGN	USER INTERFACE DESIGN		CEFGIX		COMPUTER SCIENCE	Introduction to the theory and practice of computer user interface design, emphasizing the software design of graphical user interfaces. Topics include basic interaction devices and techniques, human factors, interaction styles, dialogue design, and software infrastructure. Design and programming projects are required.
COMS4172	COMSW4172	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	3D UI AND AUGMENTED REALITY	3D UI AND AUGMENTED REALITY		CEFKGIRUX		COMPUTER SCIENCE	Design, development, and evaluation of 3D user interfaces. Interaction techniques and metaphors, from desktop to immersive. Selection and manipulation. Travel and navigation. Symbolic, menu, gestural, and multimodal interaction. Dialogue design. 3D software support. 3D interaction devices and displays. Virtual and augmented reality. Tangible user interfaces. Review of relevant 3D math.
COMS4187	COMSW4187	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	SECURITY ARCH & ENGINEERING	SECURITY ARCH & ENGINEERING		CEFGIX		COMPUTER SCIENCE	Secure programming. Cryptograhic engineering and key handling. Access controls. Tradeoffs in security design. Design for security.
COMS4203	COMSW4203	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	GRAPH THEORY	GRAPH THEORY		CEFGIX		COMPUTER SCIENCE	General introduction to graph theory. Isomorphism testing, algebraic specification, symmetries, spanning trees, traversability, planarity, drawings on higher-order surfaces, colorings, extremal graphs, random graphs, graphical measurement, directed graphs, Burnside-Polya counting, voltage graph theory.
CSOR4231	CSORW4231	COMS-OPRE	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	ANALYSIS OF ALGORITHMS I	ANALYSIS OF ALGORITHMS I		CEFKGIRUX		COMPUTER SCI-OPERATIONS RES	Introduction to the design and analysis of efficient algorithms. Topics include models of computation, efficient sorting and searching, algorithms for algebraic problems, graph algorithms, dynamic programming, probabilistic methods, approximation algorithms, and NP-completeness.
COMS4236	COMSW4236	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	INTRO-COMPUTATIONAL COMPLEXITY	INTRO-COMPUTATIONAL COMPLEXITY		CEFKGIRUX		COMPUTER SCIENCE	Develops a quantitative theory of the computational difficulty of problems in terms of the resources (eg. time, space) needed to solve them. Classification of problems into complexity classes, reductions and completeness. Power and limitations of different modes of computation such as nondeterminism, randomization, interaction and parallelism.
COMS4241	COMSW4241	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	NUMERICL ALGORITHMS-COMPLEXITY	NUMERICL ALGORITHMS-COMPLEXITY		CEFKGRUXI		COMPUTER SCIENCE	Modern theory and practice of computation on digital computers. Introduction to concepts of computational complexity. Design and analysis of numerical algorithms. Applications to computational finance, computational science, and computational engineering.
COMS4252	COMSW4252	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	INTRO-COMPUTATIONAL LEARN THRY	INTRO-COMPUTATIONAL LEARN THRY		CEFGIX		COMPUTER SCIENCE	Possibilities and limitations of performing learning by computational agents. Topics include computational models of learning, polynomial time learnability, learning from examples and learning from queries to oracles. Computational and statistical limitations of learning. Applications to Boolean functions, geometric functions, automata.
COMS4281	COMSW4281	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	INTRO TO QUANTUM COMPUTING	INTRO TO QUANTUM COMPUTING		CEFKGRUXI		COMPUTER SCIENCE	Introduction to quantum computing. Shor''s factoring algorithm, Grover''s database search algorithm, the quantum summation algorithm. Relationship between classical and quantum computing. Potential power of quantum computers.
COMS4444	COMSW4444	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	PROGRAMMING & PROBLEM SOLVING	PROGRAMMING & PROBLEM SOLVING		CEFGIX		COMPUTER SCIENCE	Hands-on introduction to solving open-ended computational problems. Emphasis on creativity, cooperation, and collaboration. Projects spanning a variety of areas within computer science, typically requiring the development of computer programs. Generalization of solutions to broader problems, and specialization of complex problems to make them manageable. Team-oriented projects, student presentations, and in-class participation required.
COMS4995	COMSW4995	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	TOPICS IN COMPUTER SCIENCE	CRYPTO & FINANCIAL PROCESSES		CEFKGIRUX		COMPUTER SCIENCE	Special topics arranged as the need and availability arises. Topics are usually offered on a one-time basis. Since the content of this course changes each time it is offered, it may be repeated for credit. Consult the department for section assignment.
COMS4460	COMSW4460	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	PRIN-INNOVATN/ENTREPRENEURSHIP	PRIN-IMMOVATN/ENTREPRENEURSHP		CEFKGIRUX		COMPUTER SCIENCE	Team project centered course focused on principles of planning, creating, and growing a technology venture. Topics include: indentifying and analyzing opportunities created by technology paradigm shifts, designing innovative products, protecting intellectual property, engineering innovative business models.
COMS4701	COMSW4701	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	ARTIFICIAL INTELLIGENCE	ARTIFICIAL INTELLIGENCE		CEFKGIRUX		COMPUTER SCIENCE	Provides a broad understanding of the basic techniques for building intelligent computer systems. Topics include state-space problem representations, problem reduction and and-or graphs, game playing and heuristic search, predicate calculus, and resolution theorem proving, AI systems and languages for knowledge representation, machine learning and concept formation and other topics such as natural language processing may be included as time permits.
COMS4705	COMSW4705	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	NATURAL LANGUAGE PROCESSING	NATURAL LANGUAGE PROCESSING		CEFGIX		COMPUTER SCIENCE	Computational approaches to natural language generation and understanding. Recommended preparation: some previous or concurrent exposure to AI or Machine Learning. Topics include information extraction, summarization, machine translation, dialogue systems, and emotional speech. Particular attention is given to robust techniques that can handle understanding and generation for the large amounts of text on the Web or in other large corpora. Programming exercises in several of these areas.
COMS4731	COMSW4731	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTER VISION	COMPUTER VISION		CEFKGIRUX		COMPUTER SCIENCE	Introductory course in computer vision. Topics include image formation and optics, image sensing, binary images, image processing and filtering, edge extraction and boundary detection, region growing and segmentation, pattern classification methods, brightness and reflectance, shape from shading and photometric stereo, texture, binocular stereo, optical flow and motion, 2-D and 3-D object representation, object recognition, vision systems and applications.
COMS4733	COMSW4733	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTATNL ASPECTS OF ROBOTICS	COMPUTATNL ASPECTS OF ROBOTICS		CEFKGRUXI		COMPUTER SCIENCE	Introduction to robotics from a computer science perspective. Topics include coordinate frames and kinematics, computer architectures for robotics, integration and use of sensors, world modeling systems, design and use of robotic programming languages, and applications of artificial intelligence for planning, assembly, and manipulation.
COMS4735	COMSW4735	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	VISUAL INTERFACES TO COMPUTERS	VISUAL INTERFACES TO COMPUTERS		CEFKGIRUX		COMPUTER SCIENCE	Visual input as data and for control of computer systems. Survey and analysis of architecture, algorithms, and underlying assumptions of commercial and research systems that recognize and interpret human gestures, analyze imagery such as fingerprint or iris patterns, generate natural language descriptions of medical or map imagery. Explores foundations in human psychophysics, cognitive science, and artificial intelligence.
COMS4737	COMSW4737	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	BIOMETRICS	BIOMETRICS		CEFGIX		COMPUTER SCIENCE	In this course we will explore the latest advances in biometrics as well as the machine learning techniques behind them. Students will learn how these technologies work and how they are sometimes defeated. Grading will be based on homework assignments and a final project. There will be no midterm or final exam. This course shares lectures with COMS E6737. Students taking COMS E6737 are required to complete additional homework problems and undertake a more rigorous final project. Students will only be allowed to earn credit for COMS W4737 or COMS E6737 and not both.
CBMF4761	CBMFW4761	COM/BIOE/MED	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTATIONAL GENOMICS	COMPUTATIONAL GENOMICS		CEFKGRUXI		COMPUTER SCI,BIOENG & MED INFO	Provides comprehensive introduction to computational techniques for analyzing genomic data including DNA, RNA and protein structures; microarrays; transcription and regulation; regulatory, metabolic and protein interaction networks. The course covers sequence analysis algorithms, dynamic programming, hidden Markov models, phylogenetic analysis, Bayesian network techniques, neural networks, clustering algorithms, support vector machines, Boolean models of regulatory networks, flux based analysis of metabolic networks and scale-free network models. The course provides self-contained introduction to relevant biological mechanisms and methods.
COMS4771	COMSW4771	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	MACHINE LEARNING	MACHINE LEARNING		CEFKGRUXI		COMPUTER SCIENCE	Topics from generative and discriminative machine learning including least squares methods, support vector machines, kernel methods, neural networks, Gaussian distributions, linear classification, linear regression, maximum likelihood, exponential family distributions, Bayesian networks, Bayesian inference, mixture models, the EM algorithm, graphical models and hidden Markov models. Algorithms implemented in Matlab.
COMS4772	COMSW4772	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	ADVANCED MACHINE LEARNING	ADVANCED MACHINE LEARNING		CEFKGIRUX		COMPUTER SCIENCE	An exploration of advanced machine learning tools for perception and behavior learning. How can machines perceive, learn from, and classify human activity computationally? Topics include Appearance-Based Models, Principal and Independent Components Analysis, Dimensionality Reduction, Kernel Methods, Manifold Learning, Latent Models, Regression, Classification, Bayesian Methods, Maximum Entropy Methods, Real-Time Tracking, Extended Kalman Filters, Time Series Prediction, Hidden Markov Models, Factorial HMMS, Input-Output HMMs, Markov Random Fields, Variational Methods, Dynamic Bayesian Networks, and Gaussian/Dirichlet Processes. Links to cognitive science.
COMS4901	COMSW4901	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			F	0	0	0	PROJECTS IN COMPUTER SCIENCE	PROJECTS IN COMPUTER SCIENCE	INS	CEFKGRUXI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	A second-level independent project involving laboratory work, computer programming, analytical investigation, or engineering design. May be repeated for credit, but not for a total of more than 3 points of degree credit. Consult the department for section assignment.
COMS4910	COMSW4910	COMPUT SCI	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			F	10	0	0	CURRICULAR PRACTICAL TRAINING	CURRICULAR PRACTICAL TRAINING		CEFKGRUXI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SECTION 1	COMPUTER SCIENCE	Only for MS students in the Computer Science department who need relevant work experience as part of their program of study. Final report required. This course may not be taken for pass/fail credit or audited.
COMS6232	COMSE6232	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	ANALYSIS OF ALGORITHMS II	ANALYSIS OF ALGORITHMS II		GI		COMPUTER SCIENCE	Continuation of CSOR W4231.
COMS6261	COMSE6261	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	ADVANCED CRYPTOGRAPHY	ADVANCED CRYPTOGRAPHY		GI		COMPUTER SCIENCE	A study of advanced cryptographic research topics such as: secure computation, zero knowledge, privacy, anonymity, cryptographic protocols.  Concentration on theoretical foundations, rigorous approach, and provable security.  Contents varies between offerings. May be repeated for credit.
COMS6732	COMSE6732	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTATIONAL IMAGING	COMPUTATIONAL IMAGING		CEFGI	IF YOU CANT REGISTER, CONTACT COMPUTER SCIENCE DEPARTMENT	COMPUTER SCIENCE	Computational imaging uses a combination of novel imaging optics and a computational module to produce new forms of visual information. Survey of the state of art in computational imaging. Review of recent papers on: omni directional and panoramic imaging, catadioptric imaging, high dynamic range imaging, mosaicing and superresolution. Classes are seminars with the instructor, guest speakers, and students presenting papers and discussing them.
COMS6737	COMSE6737	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	BIOMETRICS	BIOMETRICS		CEGFI	REGISTER FOR W4737 OR E6737 BUT NOT BOTH	COMPUTER SCIENCE	In this course we will explore the latest advances in biometrics as well as the machine learning techniques behind them. Students will learn how these technologies work and how they are sometimes defeated. Grading will be based on homework assignments and a final project. There will be no midterm or final exam. This course shares lectures with COMS W4737. Students taking COMS E6737 are required to complete additional homework problems and undertake a more rigorous final project. Students will only be allowed to earn credit for COMS W4737 or COMS E6737 and not both.
COMS6900	COMSE6900	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			F	0	0	0	TUTORIAL IN COMPUTER SCIENCE	TUTORIAL IN COMPUTER SCIENCE	INS	GI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	A reading course in an advanced topic for a small number of students, under faculty supervision.
COMS6901	COMSE6901	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			F	0	0	0	PROJECTS IN COMPUTER SCIENCE	PROJECTS IN COMPUTER SCIENCE	INS	GI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	Software or hardware projects in computer science. Before registering, the student must submit a written proposal to the instructor for review. The proposal should give a brief outline of the project, estimated schedule of completion, and computer resources needed. Oral and written reports are required. May be taken over more than one semester, in which case the grade will be deferred until all 12 points have been completed. No more than 12 points of COMS E6901 may be taken. Consult the department for section assignment.
COMS6902	COMSE6902	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			F	0	0	0	THESIS	THESIS	INS	GI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	Available to MS and CSE candidates. An independent investigation of an appropriate problem in computer science carried out under the supervision of a faculty member. A formal written report is essential and an oral presentation may also be required. May be taken over more than one semester, in which case the grade will be deferred until all 9 points have beem completed.  No more than 9 points of COMS E6902 may be taken. Consult the department for section assignment.
COMS6915	COMSE6915	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	10	0	0	TECH WRITING FOR CS AND ENGINRS	ACADEMIC WRITING		GI		COMPUTER SCIENCE	Topics to help CS/CE graduate students’ communication skills. Emphasis on writing, presenting clear, concise proposals, journal articles, conference papers, theses, and technical presentations. May be repeated for credit. Credit may not be used to satisfy degree requirements.
COMS6998	COMSE6998	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	TOPICS IN COMPUTER SCIENCE	CV & ML ON MOBILE PLATFORMS		GI		COMPUTER SCIENCE	Selected topics in computer science. Content varies from year to year. May be repeated for credit.
COMS9800	COMSE9800	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			F	0	0	0	DIRECTED RESEARCH IN COMP SCI	DIRECTED RESEARCH IN COMP SCI	INS	GI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	The department must approve the number of points.  May be repeated for credit.  This course is only for Eng.Sc.D. candidates.
COMS9910	COMSE9910	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			F	0	0	0	GRADUATE RESEARCH I	GRADUATE RESEARCH I	INS	GI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	The department must approve the number of credits. May be repeated for credit.  This course is only for MS candidates holding GRA or TA appointments.  Note: It is NOT required that a student take Graduate Research I prior to taking Graduate Research II. Consult the department for section assignment.
COMS9911	COMSE9911	COMPUT SCI	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			F	0	10	150	GRADUATE RESEARCH II	GRADUATE RESEARCH II	INS	GI	SIGN UP FOR SECTIONS IN DEPT. DO NOT SIGN UP FOR SEC 1	COMPUTER SCIENCE	The department must approve the number of points. May be repeated for credit. This course is only for MS/PhD and PhD students. Note: It is NOT required that a student take Graduate Research I prior to taking Graduate Research II. Consult the department for section assignment.
CSEE4119	CSEEW4119	COMPTSCIEE	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	COMPUTER NETWORKS	COMPUTER NETWORKS		CEFKGRUXI		COMPUTER SCI-ELECTRICAL ENGIN	Introduction to computer networks and the technical foundations of the Internet, including applications, protocols, local area networks, algorithms for routing and congestion control, security, elementary performance evaluation. Several written and programming assignments required.
CSEE4840	CSEEW4840	COMPTSCIEE	IF	INTERFACULTY	INTF	INTERFACULTY	COMS	COMPUTER SCIENCE			O	30	0	0	EMBEDDED SYSTEMS	EMBEDDED SYSTEMS		CEFKGRUXI		COMPUTER SCI-ELECTRICAL ENGIN	Embedded system design and implementation combining hardware and software. I/O, interfacing, and peripherals. Weekly laboratory sessions and term project on design of a microprocessor-based embedded system including at least one custom peripheral. Knowledge of C programming and digital logic required.
CSEE6824	CSEEE6824	COMPTSCIEE	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	PARALLEL COMPUTER ARCH	PARALLEL COMPUTER ARCH		GI		COMPUTER SCI-ELECTRICAL ENGIN	Parallel computer principles, machine organization and design of parallel systems including parallelism detection methods, synchronization, data coherence and interconnection networks. Performance analysis and special purpose parallel machines. 
CSEE6861	CSEEE6861	COMPTSCIEE	EP	SCH OF ENGR & APP SCI: GRAD	SEAS	ENGINEERING & APPLIED SCIENCE	COMS	COMPUTER SCIENCE			O	30	0	0	CAD OF DIGITAL SYSTEMS	CAD OF DIGITAL SYSTEMS		GI		COMPUTER SCI-ELECTRICAL ENGIN	Introduction to modern digital CAD synthesis and optimization techniques. Topics include: modern digital system design (high-level synthesis, register-transfer level modeling, algorithmic state machines, optimal scheduling algorithms, resource allocation and binding, retiming), controller synthesis and optimization, exact and heuristic two-level logic minimization, advanced multi-level logic optimization, optimal technology mapping to library cells (for delay, power and area minimization), advanced data structures (binary decision diagrams), SAT solvers and their applications, static timing analysis, and introduction to testability. Includes hands-on small design projects using and creating CAD tools.
\.


--
-- Data for Name: housing_amenities_t; Type: TABLE DATA; Schema: public; Owner: adicu
--

COPY housing_amenities_t (building, apartmentstyle, suitestyle, corridorstyle, privatebathroom, semiprivatebathroom, sharedbathroom, privatekitchen, semiprivatekitchen, sharedkitchen, lounge) FROM stdin;
\.


--
-- Data for Name: housing_t; Type: TABLE DATA; Schema: public; Owner: adicu
--

COPY housing_t (roomlocationarea, residentialarea, roomlocation, roomlocationsection, roomlocationfloorsuite, issuite, floorsuitewebdescription, room, roomarea, roomspace, roomtype, ay1213rsstatus, pointvalue, lotterynumber) FROM stdin;
\.


--
-- Data for Name: sections_v2_t; Type: TABLE DATA; Schema: public; Owner: adicu
--

COPY sections_v2_t (callnumber, sectionfull, course, term, numenrolled, maxsize, typecode, typename, meets1, meets2, meets3, meets4, meets5, meets6, meetson1, starttime1, endtime1, building1, room1, meetson2, starttime2, endtime2, building2, room2, meetson3, starttime3, endtime3, building3, room3, meetson4, starttime4, endtime4, building4, room4, meetson5, starttime5, endtime5, building5, room5, meetson6, starttime6, endtime6, building6, room6, exammeetson, examstarttime, examendtime, exambuilding, examroom, exammeet, examdate, instructor1name, instructor2name, instructor3name, instructor4name, campuscode, campusname) FROM stdin;
69280	CBMF4761W001	CBMF4761	20131	14	75	LC	LECTURE	MW     04:10P-05:25PMUD SEELEY W. MU1127						MW	16:10:00	17:25:00	SEELEY W. MU	1127	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	16:10:00	19:00:00	SEELEY W. MU	1127	M      04:10P-07:00PMUD SEELEY W. MU1127	May 13	PE'ER, ITSHACK				MORN	MORNINGSIDE
61248	COMS6900E001	COMS6900	20131	0	0	TU	TUTORIAL							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
87249	COMS6901E001	COMS6901	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
85999	COMS6902E001	COMS6902	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
13151	COMS0001E001	COMS0001	20131	7	999	DM	DUMMY COURSE							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
15901	COMS0002E001	COMS0002	20131	12	999	DM	DUMMY COURSE							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
16250	COMS0003E001	COMS0003	20131	13	999	DM	DUMMY COURSE							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
16548	COMS0004E001	COMS0004	20131	19	999	SM	SEMINAR							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
68453	COMS0005E001	COMS0005	20131	1	999	SM	SEMINAR							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
12354	COMS0006E001	COMS0006	20131	1	999	SM	SEMINAR							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
60784	COMS1001W001	COMS1001	20131	52	120	LC	LECTURE	TR     11:40A-12:55PMUD SEELEY W. MU627						TR	11:40:00	12:55:00	SEELEY W. MU	627	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	16:10:00	19:00:00	SEELEY W. MU	627	R      04:10P-07:00PMUD SEELEY W. MU627	May 16	AGARWAL, APOORV				MORN	MORNINGSIDE
16448	COMS1004W001	COMS1004	20131	232	999	LC	LECTURE	MW     04:10P-05:25PHAV HAVEMEYER HA309						MW	16:10:00	17:25:00	HAVEMEYER HA	309	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	16:10:00	19:00:00	HAVEMEYER HA	309	M      04:10P-07:00PHAV HAVEMEYER HA309	May 13	CANNON, ADAM H				MORN	MORNINGSIDE
79698	COMS1005W001	COMS1005	20131	74	999	LC	LECTURE	MW     10:10A-11:25AMUD SEELEY W. MU833						MW	10:10:00	11:25:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	09:00:00	12:00:00	SEELEY W. MU	833	M      09:00A-12:00PMUD SEELEY W. MU833	May 13	BLAER, PAUL S				MORN	MORNINGSIDE
26286	COMS1007W001	COMS1007	20131	74	120	LC	LECTURE	TR     04:10P-05:25PMUD SEELEY W. MU833						TR	16:10:00	17:25:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	16:10:00	19:00:00	SEELEY W. MU	833	T      04:10P-07:00PMUD SEELEY W. MU833	May 14	SHETH, SWAPNEEL K				MORN	MORNINGSIDE
92101	COMS1404W001	COMS1404	20131	26	999	SM	SEMINAR							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			CANNON, ADAM H				MORN	MORNINGSIDE
78300	COMS3101W001	COMS3101	20131	42	999	LC	LECTURE	M      06:10P-08:00PMUD SEELEY W. MU825						M	18:10:00	20:00:00	SEELEY W. MU	825	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			STOLFO, EMILY				MORN	MORNINGSIDE
27952	COMS3101W002	COMS3101	20131	6	999	LC	LECTURE	T      04:10P-06:00PENG ENGINEERING 253						T	16:10:00	18:00:00	ENGINEERING	253	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ISUKAPALLI, RAMANA				MORN	MORNINGSIDE
75517	COMS3134W001	COMS3134	20131	139	180	LC	LECTURE	TR     10:10A-11:25AHAV HAVEMEYER HA309						TR	10:10:00	11:25:00	HAVEMEYER HA	309	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	09:00:00	12:00:00	HAVEMEYER HA	309	T      09:00A-12:00PHAV HAVEMEYER HA309	May 14	HERSHKOP, SHLOMO				MORN	MORNINGSIDE
93401	COMS3136W001	COMS3136	20131	59	999	LC	LECTURE	TR     05:40P-06:55PMAT MATHEMATICS 417						TR	17:40:00	18:55:00	MATHEMATICS	417	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			LEE, JAE W				MORN	MORNINGSIDE
24707	COMS3157W001	COMS3157	20131	137	999	LC	LECTURE	TR     04:10P-05:25PPUP PUPIN LABORA301						TR	16:10:00	17:25:00	PUPIN LABORA	301	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	16:10:00	19:00:00	PUPIN LABORA	301	T      04:10P-07:00PPUP PUPIN LABORA301	May 14	LEE, JAE W				MORN	MORNINGSIDE
20958	COMS3203W001	COMS3203	20131	129	999	LC	LECTURE	MW     05:40P-06:55PNWC NORTHWEST CO501						MW	17:40:00	18:55:00	NORTHWEST CO	501	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	16:10:00	19:00:00	NORTHWEST CO	501	W      04:10P-07:00PNWC NORTHWEST CO501	May 15	STRICKLAND, DAWN M				MORN	MORNINGSIDE
17546	COMS3210W001	COMS3210	20131	34	999	LC	LECTURE	TR     01:10P-02:25PMUD SEELEY W. MU644						TR	13:10:00	14:25:00	SEELEY W. MU	644	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	13:10:00	16:00:00	SEELEY W. MU	644	T      01:10P-04:00PMUD SEELEY W. MU644	May 14	TRAUB, JOSEPH F				MORN	MORNINGSIDE
62897	COMS3261W001	COMS3261	20131	99	999	LC	LECTURE	TR     11:40A-12:55PNWC NORTHWEST CO501						TR	11:40:00	12:55:00	NORTHWEST CO	501	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	16:10:00	19:00:00	PUPIN LABORA	301	R      04:10P-07:00PPUP PUPIN LABORA301	May 16	CHOI, SEUNG G				MORN	MORNINGSIDE
73400	COMS3902W001	COMS3902	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
78783	COMS3998W001	COMS3998	20131	0	0	IS	INDEPENDENT	W      02:10P-04:00P						W	14:10:00	16:00:00	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
85037	COMS4111W001	COMS4111	20131	73	81	LC	LECTURE	W      01:10P-03:40PMUD SEELEY W. MU1127						W	13:10:00	15:40:00	SEELEY W. MU	1127	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	16:10:00	19:00:00	SCHERMERHORN	501	W      04:10P-07:00PSCH SCHERMERHORN501	May 15	BILIRIS, ALEXANDROS				MORN	MORNINGSIDE
11104	COMS4111W002	COMS4111	20131	84	80	LC	LECTURE	W      04:10P-06:40PMAT MATHEMATICS 207						W	16:10:00	18:40:00	MATHEMATICS	207	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	16:10:00	19:00:00	SCHERMERHORN	501	W      04:10P-07:00PSCH SCHERMERHORN501	May 15	BILIRIS, ALEXANDROS				MORN	MORNINGSIDE
63043	COMS4112W001	COMS4112	20131	59	999	LC	LECTURE	MW     01:10P-02:25PMUD SEELEY W. MU535						MW	13:10:00	14:25:00	SEELEY W. MU	535	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	13:10:00	16:00:00	SEELEY W. MU	535	M      01:10P-04:00PMUD SEELEY W. MU535	May 13	ROSS, KENNETH A				MORN	MORNINGSIDE
93458	COMS4115W001	COMS4115	20131	105	100	LC	LECTURE	MW     02:40P-03:55PMUD SEELEY W. MU535						MW	14:40:00	15:55:00	SEELEY W. MU	535	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			AHO, ALFRED				MORN	MORNINGSIDE
63454	COMS4118W001	COMS4118	20131	82	120	LC	LECTURE	MW     02:40P-03:55PMUD SEELEY W. MU833						MW	14:40:00	15:55:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	13:10:00	16:00:00	SEELEY W. MU	833	W      01:10P-04:00PMUD SEELEY W. MU833	May 15	JOSHI, KAUSTUBH R				MORN	MORNINGSIDE
68496	COMS4160W001	COMS4160	20131	29	60	LC	LECTURE	TR     11:40A-12:55PMUD SEELEY W. MU535						TR	11:40:00	12:55:00	SEELEY W. MU	535	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ZHENG, CHANGXI				MORN	MORNINGSIDE
18503	COMS4172W001	COMS4172	20131	22	999	LC	LECTURE	TR     01:10P-02:25PMUD SEELEY W. MU633						TR	13:10:00	14:25:00	SEELEY W. MU	633	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	13:10:00	16:00:00	SEELEY W. MU	627	T      01:10P-04:00PMUD SEELEY W. MU627	May 14	FEINER, STEVEN K				MORN	MORNINGSIDE
76498	COMS4236W001	COMS4236	20131	22	85	LC	LECTURE	MW     01:10P-02:25PHAM HAMILTON HAL503						MW	13:10:00	14:25:00	HAMILTON HAL	503	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	13:10:00	16:00:00	HAMILTON HAL	503	M      01:10P-04:00PHAM HAMILTON HAL503	May 13	CHEN, XI				MORN	MORNINGSIDE
17499	COMS4241W001	COMS4241	20131	35	999	LC	LECTURE	MW     04:10P-05:25PMUD SEELEY W. MU825						MW	16:10:00	17:25:00	SEELEY W. MU	825	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	16:10:00	19:00:00	SEELEY W. MU	825	M      04:10P-07:00PMUD SEELEY W. MU825	May 13	TRAUB, JOSEPH F				MORN	MORNINGSIDE
22214	COMS4281W001	COMS4281	20131	37	999	LC	LECTURE	TR     04:10P-05:25PHAM HAMILTON HAL703						TR	16:10:00	17:25:00	HAMILTON HAL	703	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	16:10:00	19:00:00	HAMILTON HAL	703	T      04:10P-07:00PHAM HAMILTON HAL703	May 14	PAPAGEORGIOU, ANARGYROS				MORN	MORNINGSIDE
19266	COMS4460W001	COMS4460	20131	74	80	LC	LECTURE	T      04:10P-06:40PMAT MATHEMATICS 207						T	16:10:00	18:40:00	MATHEMATICS	207	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			REINISCH, WILLIAM	YEMINI, YECHIAM			MORN	MORNINGSIDE
22556	COMS4701W001	COMS4701	20131	102	125	LC	LECTURE	TR     02:40P-03:55PMUD SEELEY W. MU833						TR	14:40:00	15:55:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	13:10:00	16:00:00	SEELEY W. MU	833	R      01:10P-04:00PMUD SEELEY W. MU833	May 16	STOLFO, SALVATORE J				MORN	MORNINGSIDE
63284	COMS4731W001	COMS4731	20131	57	999	LC	LECTURE	TR     10:10A-11:25AHAM HAMILTON HAL702						TR	10:10:00	11:25:00	HAMILTON HAL	702	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	09:00:00	12:00:00	HAMILTON HAL	702	T      09:00A-12:00PHAM HAMILTON HAL702	May 14	REITER, AUSTIN D				MORN	MORNINGSIDE
89697	COMS4735W001	COMS4735	20131	33	999	LC	LECTURE	TR     10:10A-11:25AMUD SEELEY W. MU545						TR	10:10:00	11:25:00	SEELEY W. MU	545	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	09:00:00	12:00:00	SEELEY W. MU	545	T      09:00A-12:00PMUD SEELEY W. MU545	May 14	KENDER, JOHN R				MORN	MORNINGSIDE
13748	COMS4771W001	COMS4771	20131	64	86	LC	LECTURE	TR     01:10P-02:25PHAM HAMILTON HAL702						TR	13:10:00	14:25:00	HAMILTON HAL	702	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	13:10:00	16:01:00	HAMILTON HAL	717	T      01:10P-04:01PHAM HAMILTON HAL717	May 14	WELLER, ADRIAN V	VOVSHA, ILIA			MORN	MORNINGSIDE
27599	COMS4772W001	COMS4772	20131	44	60	LC	LECTURE	TR     02:40P-03:55PMUD SEELEY W. MU1127						TR	14:40:00	15:55:00	SEELEY W. MU	1127	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	13:10:00	16:00:00	SEELEY W. MU	1127	R      01:10P-04:00PMUD SEELEY W. MU1127	May 16	JEBARA, TONY				MORN	MORNINGSIDE
26099	COMS4901W001	COMS4901	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
18349	COMS4910W001	COMS4910	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
14035	COMS4995W001	COMS4995	20131	34	999	LC	LECTURE	TR     10:10A-11:25AMUD SEELEY W. MU535						TR	10:10:00	11:25:00	SEELEY W. MU	535	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	09:00:00	12:00:00	SEELEY W. MU	535	T      09:00A-12:00PMUD SEELEY W. MU535	May 14	RABIN, MICHAEL				MORN	MORNINGSIDE
12050	COMS6232E001	COMS6232	20131	26	999	LC	LECTURE	R      12:10P-02:00PMUD SEELEY W. MU545						R	12:10:00	14:00:00	SEELEY W. MU	545	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			YANNAKAKIS, MIHALIS				MORN	MORNINGSIDE
66805	COMS6261E001	COMS6261	20131	8	999	LC	LECTURE	T      02:10P-04:00PMUD SEELEY W. MU1024						T	14:10:00	16:00:00	SEELEY W. MU	1024	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	13:10:00	16:00:00	SEELEY W. MU	1024	T      01:10P-04:00PMUD SEELEY W. MU1024	May 14	HALEVI, SHAI	MALKIN, TAL			MORN	MORNINGSIDE
92099	COMS6915E001	COMS6915	20131	20	26	SM	SEMINAR	TR     10:00A-12:00PMUD SEELEY W. MU1220A						TR	10:00:00	12:00:00	SEELEY W. MU	1220A	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KAYFETZ, JANET				MORN	MORNINGSIDE
92201	COMS6915E002	COMS6915	20131	9	15	SM	SEMINAR	MW     10:00A-12:00PMUD SEELEY W. MU1220A						MW	10:00:00	12:00:00	SEELEY W. MU	1220A	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KAYFETZ, JANET				MORN	MORNINGSIDE
19275	COMS6915E003	COMS6915	20131	3	12	SM	SEMINAR	TR     02:00P-04:00PBTBA            RTBA						TR	14:00:00	16:00:00	\N	RTBA	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KAYFETZ, JANET				MORN	MORNINGSIDE
72298	COMS6998E001	COMS6998	20131	21	999	LC	LECTURE	W      02:10P-04:00PENG ENGINEERING 253						W	14:10:00	16:00:00	ENGINEERING	253	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	13:10:00	16:00:00	ENGINEERING	253	W      01:10P-04:00PENG ENGINEERING 253	May 15	BELHUMEUR, PETER				MORN	MORNINGSIDE
83248	COMS6998E002	COMS6998	20131	12	70	LC	LECTURE	T      10:10A-12:00PMUD SEELEY W. MU1127						T	10:10:00	12:00:00	SEELEY W. MU	1127	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	09:00:00	12:00:00	SEELEY W. MU	1127	T      09:00A-12:00PMUD SEELEY W. MU1127	May 14	NIEH, JASON				MORN	MORNINGSIDE
97350	COMS6998E003	COMS6998	20131	30	35	LC	LECTURE	W      04:10P-06:00PFAY FAYERWEATHER313						W	16:10:00	18:00:00	FAYERWEATHER	313	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	16:10:00	19:00:00	FAYERWEATHER	313	W      04:10P-07:00PFAY FAYERWEATHER313	May 15	MASKEY, SAMEER R				MORN	MORNINGSIDE
27352	COMS6998E004	COMS6998	20131	23	100	LC	LECTURE	M      04:10P-06:00PMAT MATHEMATICS 203						M	16:10:00	18:00:00	MATHEMATICS	203	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	16:10:00	19:00:00	MATHEMATICS	203	M      04:10P-07:00PMAT MATHEMATICS 203	May 13	GEAMBASU, ROXANA				MORN	MORNINGSIDE
23351	COMS6998E005	COMS6998	20131	11	999	LC	LECTURE	R      07:00P-09:30PENG ENGINEERING 253						R	19:00:00	21:30:00	ENGINEERING	253	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	19:10:00	22:00:00	ENGINEERING	253	R      07:10P-10:00PENG ENGINEERING 253	May 16	BEIGI, HOMAYOON S				MORN	MORNINGSIDE
11037	COMS6998E006	COMS6998	20131	51	54	LC	LECTURE	W      04:10P-06:00PHAM HAMILTON HAL503						W	16:10:00	18:00:00	HAMILTON HAL	503	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	16:10:00	19:00:00	HAMILTON HAL	503	W      04:10P-07:00PHAM HAMILTON HAL503	May 15	LI, KEVIN A				MORN	MORNINGSIDE
26400	COMS6998E007	COMS6998	20131	53	60	LC	LECTURE	M      06:10P-08:00PKNT KENT HALL   413						M	18:10:00	20:00:00	KENT HALL	413	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	19:10:00	22:00:00	KENT HALL	413	M      07:10P-10:00PKNT KENT HALL   413	May 13	SAHU, SAMBIT				MORN	MORNINGSIDE
88602	COMS6998E008	COMS6998	20131	13	40	LC	LECTURE	R      04:10P-06:00PMUD SEELEY W. MU327						R	16:10:00	18:00:00	SEELEY W. MU	327	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	16:10:00	19:00:00	SEELEY W. MU	327	R      04:10P-07:00PMUD SEELEY W. MU327	May 16	HABASH, NIZAR				MORN	MORNINGSIDE
86648	COMS6998E009	COMS6998	20131	31	999	LC	LECTURE	F      02:10P-04:00PMUD SEELEY W. MU627						F	14:10:00	16:00:00	SEELEY W. MU	627	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	F	13:10:00	16:00:00	SEELEY W. MU	627	F      01:10P-04:00PMUD SEELEY W. MU627	May 10	GLIOZZO, ALFIO				MORN	MORNINGSIDE
97850	COMS6998E010	COMS6998	20131	49	45	LC	LECTURE	T      06:10P-08:00PMUD SEELEY W. MU1220A						T	18:10:00	20:00:00	SEELEY W. MU	1220A	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			LI, LI E				MORN	MORNINGSIDE
25567	COMS6998E011	COMS6998	20131	18	999	LC	LECTURE	M      10:10A-12:00PPUP PUPIN LABORA424						M	10:10:00	12:00:00	PUPIN LABORA	424	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			COHEN, SHAY				MORN	MORNINGSIDE
26652	COMS9800E001	COMS9800	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
76099	COMS9910E001	COMS9910	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
13248	COMS9911E001	COMS9911	20131	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
78400	CSEE3827W001	CSEE3827	20131	127	999	LC	LECTURE	MW     01:10P-02:25PNWC NORTHWEST CO501						MW	13:10:00	14:25:00	NORTHWEST CO	501	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	13:10:00	16:00:00	NORTHWEST CO	501	M      01:10P-04:00PNWC NORTHWEST CO501	May 13	RUBENSTEIN, DANIEL S				MORN	MORNINGSIDE
21446	CSEE4119W001	CSEE4119	20131	66	999	LC	LECTURE	TR     01:10P-02:25PMAT MATHEMATICS 203						TR	13:10:00	14:25:00	MATHEMATICS	203	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	T	13:10:00	16:00:00	MATHEMATICS	203	T      01:10P-04:00PMAT MATHEMATICS 203	May 14	CHAINTREAU, AUGUSTIN				MORN	MORNINGSIDE
82286	CSEE4840W001	CSEE4840	20131	76	999	LC	LECTURE	TR     02:40P-03:55PHAM HAMILTON HAL717						TR	14:40:00	15:55:00	HAMILTON HAL	717	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			EDWARDS, STEPHEN A	LARIVIERE, DAVID A			MORN	MORNINGSIDE
13027	CSEE6824E001	CSEE6824	20131	14	75	LC	LECTURE	R      06:10P-08:00PPUP PUPIN LABORA420						R	18:10:00	20:00:00	PUPIN LABORA	420	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	19:10:00	22:00:00	PUPIN LABORA	420	R      07:10P-10:00PPUP PUPIN LABORA420	May 16	SETHUMADHAVAN, SIMHA				MORN	MORNINGSIDE
11146	CSEE6861E001	CSEE6861	20131	29	30	LC	LECTURE	R      04:10P-06:00PMUD SEELEY W. MU233						R	16:10:00	18:00:00	SEELEY W. MU	233	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	R	16:10:00	19:00:00	HAMILTON HAL	702	R      04:10P-07:00PHAM HAMILTON HAL702	May 16	NOWICK, STEVEN M				MORN	MORNINGSIDE
93500	CSEE6868E001	CSEE6868	20131	18	30	LC	LECTURE	MW     01:10P-02:25PMUD SEELEY W. MU825						MW	13:10:00	14:25:00	SEELEY W. MU	825	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	M	13:10:00	16:00:00	SEELEY W. MU	825	M      01:10P-04:00PMUD SEELEY W. MU825	May 13	CARLONI, LUCA				MORN	MORNINGSIDE
98197	CSOR4231W001	CSOR4231	20131	104	120	LC	LECTURE	MW     08:40P-09:55PNWC NORTHWEST CO501						MW	20:40:00	21:55:00	NORTHWEST CO	501	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ZHANG, YIHAO				MORN	MORNINGSIDE
13542	ENGI1006E001	ENGI1006	20131	71	999	LC	LECTURE	MW     02:40P-03:55PMUD SEELEY W. MU633						MW	14:40:00	15:55:00	SEELEY W. MU	633	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	W	13:10:00	16:00:00	SEELEY W. MU	633	W      01:10P-04:00PMUD SEELEY W. MU633	May 15	CANNON, ADAM H				MORN	MORNINGSIDE
13596	COMS1004S001	COMS1004	20132	37	999	LC	LECTURE	TR     05:30P-08:40PMUD SEELEY W. MU633						TR	17:30:00	20:40:00	SEELEY W. MU	633	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			CANNON, ADAM H				MORN	MORNINGSIDE
23246	COMS1005S001	COMS1005	20132	15	999	LC	LECTURE	MW     05:30P-08:40PMUD SEELEY W. MU627						MW	17:30:00	20:40:00	SEELEY W. MU	627	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BLAER, PAUL S				MORN	MORNINGSIDE
25779	COMS3134S001	COMS3134	20132	25	999	LC	LECTURE	TR     05:30P-08:40PMUD SEELEY W. MU337						TR	17:30:00	20:40:00	SEELEY W. MU	337	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			HERSHKOP, SHLOMO				MORN	MORNINGSIDE
92066	COMS3157S001	COMS3157	20132	14	999	LC	LECTURE	TR     05:30P-08:40PMUD SEELEY W. MU644						TR	17:30:00	20:40:00	SEELEY W. MU	644	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			HERSHKOP, SHLOMO				MORN	MORNINGSIDE
63004	COMS3203S001	COMS3203	20132	27	999	LC	LECTURE	MW     05:30P-08:40PMUD SEELEY W. MU644						MW	17:30:00	20:40:00	SEELEY W. MU	644	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			HOLLIDAY, ROBERT L				MORN	MORNINGSIDE
86029	COMS3261S001	COMS3261	20132	17	999	LC	LECTURE	MW     05:30P-08:40PMUD SEELEY W. MU644						MW	17:30:00	20:40:00	SEELEY W. MU	644	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			HOLLIDAY, ROBERT L				MORN	MORNINGSIDE
84691	COMS4111S001	COMS4111	20132	19	999	LC	LECTURE	TR     05:30P-08:40PMUD SEELEY W. MU233						TR	17:30:00	20:40:00	SEELEY W. MU	233	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BILIRIS, ALEXANDROS				MORN	MORNINGSIDE
15997	COMS4115S001	COMS4115	20132	17	999	LC	LECTURE	MW     05:30P-08:40PMUD SEELEY W. MU627						MW	17:30:00	20:40:00	SEELEY W. MU	627	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			EDWARDS, STEPHEN A				MORN	MORNINGSIDE
61446	COMS4231S001	COMS4231	20132	17	999	LC	LECTURE	MW     06:00P-09:10PMUD SEELEY W. MU825						MW	18:00:00	21:10:00	SEELEY W. MU	825	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			PLUMETTAZ, MATTHIEU				MORN	MORNINGSIDE
63346	COMS4701S001	COMS4701	20132	13	999	LC	LECTURE	MW     06:00P-09:10PMUD SEELEY W. MU337						MW	18:00:00	21:10:00	SEELEY W. MU	337	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			CREAMER, GERMAN G				MORN	MORNINGSIDE
21896	COMS4910S001	COMS4910	20132	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
83352	COMS0001E001	COMS0001	20133	3	999	DM	DUMMY COURSE							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
86068	COMS0002E001	COMS0002	20133	2	999	DM	DUMMY COURSE							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
86549	COMS0003E001	COMS0003	20133	2	999	DM	DUMMY COURSE							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
86696	COMS0004E001	COMS0004	20133	2	999	SM	SEMINAR							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
86896	COMS0005E001	COMS0005	20133	0	999	SM	SEMINAR							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
90965	COMS0006E001	COMS0006	20133	0	999	SM	SEMINAR							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
14300	COMS1001W001	COMS1001	20133	11	40	LC	LECTURE	MW     11:40A-12:55PSCEPSCHAPIRO CEP415						MW	11:40:00	12:55:00	SCHAPIRO CEP	415	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			XIE, BOYI				MORN	MORNINGSIDE
29558	COMS1004W001	COMS1004	20133	306	999	LC	LECTURE	MW     04:10P-05:25PHAV HAVEMEYER HA309						MW	16:10:00	17:25:00	HAVEMEYER HA	309	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			CANNON, ADAM H				MORN	MORNINGSIDE
26529	COMS1005W001	COMS1005	20133	51	999	LC	LECTURE	MW     10:10A-11:25AMUD SEELEY W. MU633						MW	10:10:00	11:25:00	SEELEY W. MU	633	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BLAER, PAUL S				MORN	MORNINGSIDE
63241	COMS1007W001	COMS1007	20133	73	999	LC	LECTURE	TR     01:10P-02:25PNWC NORTHWEST CO501						TR	13:10:00	14:25:00	NORTHWEST CO	501	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KENDER, JOHN R				MORN	MORNINGSIDE
93700	COMS3101W001	COMS3101	20133	13	999	LC	LECTURE	M      04:10P-06:00PPUP PUPIN LABORA224						M	16:10:00	18:00:00	PUPIN LABORA	224	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			VOVSHA, ILIA				MORN	MORNINGSIDE
11105	COMS3101W002	COMS3101	20133	13	999	LC	LECTURE	M      04:10P-06:00PPUP PUPIN LABORA224						M	16:10:00	18:00:00	PUPIN LABORA	224	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			VOVSHA, ILIA				MORN	MORNINGSIDE
65805	COMS3101W003	COMS3101	20133	13	999	LC	LECTURE	R      02:10P-04:00PENG ENGINEERING 253						R	14:10:00	16:00:00	ENGINEERING	253	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			JEE, KANGKOOK				MORN	MORNINGSIDE
21698	COMS3101W004	COMS3101	20133	9	999	LC	LECTURE	T      06:10P-08:00PPHI PHILOSOPHY H201D						T	18:10:00	20:00:00	PHILOSOPHY H	201D	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ISUKAPALLI, RAMANA				MORN	MORNINGSIDE
68597	COMS3134W001	COMS3134	20133	195	999	LC	LECTURE	MW     05:40P-06:55PNWC NORTHWEST CO501						MW	17:40:00	18:55:00	NORTHWEST CO	501	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			PASIK, ALEXANDER J				MORN	MORNINGSIDE
67000	COMS3136W001	COMS3136	20133	34	999	LC	LECTURE	TR     05:40P-06:55PHAM HAMILTON HAL516						TR	17:40:00	18:55:00	HAMILTON HAL	516	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			LEE, JAE W				MORN	MORNINGSIDE
28780	COMS3137W001	COMS3137	20133	80	86	LC	LECTURE	MW     11:40A-12:55PHAM HAMILTON HAL702						MW	11:40:00	12:55:00	HAMILTON HAL	702	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			HERSHKOP, SHLOMO				MORN	MORNINGSIDE
70238	COMS3157W001	COMS3157	20133	137	140	LC	LECTURE	TR     11:40A-12:55PPUP PUPIN LABORA428						TR	11:40:00	12:55:00	PUPIN LABORA	428	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			LEE, JAE W				MORN	MORNINGSIDE
73476	COMS3203W001	COMS3203	20133	125	125	LC	LECTURE	MW     01:10P-02:25PMUD SEELEY W. MU833						MW	13:10:00	14:25:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			GROSS, JONATHAN L				MORN	MORNINGSIDE
60225	COMS3251W001	COMS3251	20133	91	120	LC	LECTURE	TR     02:40P-03:55PPUP PUPIN LABORA428						TR	14:40:00	15:55:00	PUPIN LABORA	428	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			PAPAGEORGIOU, ANARGYROS				MORN	MORNINGSIDE
28863	COMS3261W001	COMS3261	20133	100	110	LC	LECTURE	MW     01:10P-02:25PHAV HAVEMEYER HA209						MW	13:10:00	14:25:00	HAVEMEYER HA	209	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			YANNAKAKIS, MIHALIS				MORN	MORNINGSIDE
27797	COMS3902W001	COMS3902	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
88780	COMS3998W001	COMS3998	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
62612	COMS4111W001	COMS4111	20133	80	80	LC	LECTURE	W      01:10P-03:40PMUD SEELEY W. MU1024						W	13:10:00	15:40:00	SEELEY W. MU	1024	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BILIRIS, ALEXANDROS				MORN	MORNINGSIDE
27890	COMS4111W002	COMS4111	20133	86	86	LC	LECTURE	W      04:10P-06:40PHAM HAMILTON HAL702						W	16:10:00	18:40:00	HAMILTON HAL	702	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BILIRIS, ALEXANDROS				MORN	MORNINGSIDE
73630	COMS4115W001	COMS4115	20133	112	120	LC	LECTURE	MW     04:10P-05:25PMUD SEELEY W. MU833						MW	16:10:00	17:25:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			EDWARDS, STEPHEN A				MORN	MORNINGSIDE
69201	COMS4118W001	COMS4118	20133	138	160	LC	LECTURE	TR     04:10P-05:25PMUD SEELEY W. MU833						TR	16:10:00	17:25:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			YANG, JUNFENG				MORN	MORNINGSIDE
17885	COMS4130W001	COMS4130	20133	30	48	LC	LECTURE	MW     02:40P-03:55PMUD SEELEY W. MU233						MW	14:40:00	15:55:00	SEELEY W. MU	233	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KIM, MARTHA A				MORN	MORNINGSIDE
72870	COMS4156W001	COMS4156	20133	77	80	LC	LECTURE	TR     10:10A-11:25AHAM HAMILTON HAL702						TR	10:10:00	11:25:00	HAMILTON HAL	702	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KAISER, GAIL E				MORN	MORNINGSIDE
62450	COMS4167W001	COMS4167	20133	78	88	LC	LECTURE	R      06:10P-08:00PMUD SEELEY W. MU535						R	18:10:00	20:00:00	SEELEY W. MU	535	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			GRINSPUN, EITAN				MORN	MORNINGSIDE
16563	COMS4170W001	COMS4170	20133	72	70	LC	LECTURE	TR     01:10P-02:25PHAM HAMILTON HAL517						TR	13:10:00	14:25:00	HAMILTON HAL	517	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			FEINER, STEVEN K				MORN	MORNINGSIDE
17398	COMS4187W001	COMS4187	20133	55	65	LC	LECTURE	MW     02:40P-03:55PMUD SEELEY W. MU545						MW	14:40:00	15:55:00	SEELEY W. MU	545	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BELLOVIN, STEVEN M				MORN	MORNINGSIDE
29129	COMS4203W001	COMS4203	20133	35	48	LC	LECTURE	MW     04:10P-05:25PMUD SEELEY W. MU1024						MW	16:10:00	17:25:00	SEELEY W. MU	1024	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			GROSS, JONATHAN L				MORN	MORNINGSIDE
28142	COMS4252W001	COMS4252	20133	82	88	LC	LECTURE	MW     01:10P-02:25PMUD SEELEY W. MU535						MW	13:10:00	14:25:00	SEELEY W. MU	535	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			SERVEDIO, ROCCO				MORN	MORNINGSIDE
67934	COMS4444W001	COMS4444	20133	30	40	LC	LECTURE	MW     01:10P-02:25PMUD SEELEY W. MU233						MW	13:10:00	14:25:00	SEELEY W. MU	233	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ROSS, KENNETH A				MORN	MORNINGSIDE
23247	COMS4460W001	COMS4460	20133	40	40	LC	LECTURE	R      04:10P-06:40PSCEPSCHAPIRO CEP415						R	16:10:00	18:40:00	SCHAPIRO CEP	415	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			YEMINI, YECHIAM	REINISCH, WILLIAM			MORN	MORNINGSIDE
20699	COMS4701W001	COMS4701	20133	113	125	LC	LECTURE	TR     02:40P-03:55PMUD SEELEY W. MU833						TR	14:40:00	15:55:00	SEELEY W. MU	833	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			VORIS, JONATHAN A				MORN	MORNINGSIDE
20830	COMS4705W001	COMS4705	20133	95	100	LC	LECTURE	TR     04:10P-05:25PMUD SEELEY W. MU535						TR	16:10:00	17:25:00	SEELEY W. MU	535	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			COLLINS, MICHAEL				MORN	MORNINGSIDE
23412	COMS4733W001	COMS4733	20133	67	999	LC	LECTURE	TR     11:40A-12:55PMUD SEELEY W. MU627						TR	11:40:00	12:55:00	SEELEY W. MU	627	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ALLEN, PETER K				MORN	MORNINGSIDE
61919	COMS4737W001	COMS4737	20133	20	25	LC	LECTURE	TR     01:10P-02:25PMUD SEELEY W. MU627						TR	13:10:00	14:25:00	SEELEY W. MU	627	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BELHUMEUR, PETER				MORN	MORNINGSIDE
61743	COMS4771W001	COMS4771	20133	150	150	LC	LECTURE	TR     02:40P-03:55PMAT MATHEMATICS 207						TR	14:40:00	15:55:00	MATHEMATICS	207	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			JEBARA, TONY				MORN	MORNINGSIDE
22856	COMS4772W001	COMS4772	20133	30	30	LC	LECTURE	W      04:10P-06:00PMUD SEELEY W. MU834						W	16:10:00	18:00:00	SEELEY W. MU	834	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			HSU, DANIEL				MORN	MORNINGSIDE
98446	COMS4901W001	COMS4901	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
87997	COMS4910W001	COMS4910	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
12804	COMS4995W001	COMS4995	20133	36	40	LC	LECTURE	TR     11:40A-12:55PMUD SEELEY W. MU337						TR	11:40:00	12:55:00	SEELEY W. MU	337	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			GEAMBASU, ROXANA				MORN	MORNINGSIDE
23515	COMS4995W002	COMS4995	20133	25	30	LC	LECTURE	M      04:10P-06:00PMUD SEELEY W. MU337						M	16:10:00	18:00:00	SEELEY W. MU	337	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ARABSHIAN, KNARIG				MORN	MORNINGSIDE
86152	COMS4995W003	COMS4995	20133	18	36	LC	LECTURE	T      06:10P-08:00PPUP PUPIN LABORA414						T	18:10:00	20:00:00	PUPIN LABORA	414	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ABRAMS, STEVEN				MORN	MORNINGSIDE
68757	COMS6732E001	COMS6732	20133	19	999	LC	LECTURE	M      04:10P-06:00PCSC COMPUTER SCI453						M	16:10:00	18:00:00	COMPUTER SCI	453	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			NAYAR, SHREE K				MORN	MORNINGSIDE
69879	COMS6737E001	COMS6737	20133	19	30	LC	LECTURE	TR     01:10P-02:25PMUD SEELEY W. MU627						TR	13:10:00	14:25:00	SEELEY W. MU	627	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BELHUMEUR, PETER				MORN	MORNINGSIDE
25279	COMS6900E001	COMS6900	20133	0	0	TU	TUTORIAL							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
80946	COMS6901E001	COMS6901	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
78646	COMS6902E001	COMS6902	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
67549	COMS6915E001	COMS6915	20133	9	999	SM	SEMINAR	TR     10:00A-12:00PMUD SEELEY W. MU644						TR	10:00:00	12:00:00	SEELEY W. MU	644	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KAYFETZ, JANET				MORN	MORNINGSIDE
81801	COMS6915E002	COMS6915	20133	7	999	SM	SEMINAR	MW     10:00A-12:00PMUD SEELEY W. MU1220A						MW	10:00:00	12:00:00	SEELEY W. MU	1220A	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KAYFETZ, JANET				MORN	MORNINGSIDE
83503	COMS6915E003	COMS6915	20133	6	999	SM	SEMINAR	MW     02:00P-04:00PMUD SEELEY W. MU327						MW	14:00:00	16:00:00	SEELEY W. MU	327	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KAYFETZ, JANET				MORN	MORNINGSIDE
15671	COMS6998E001	COMS6998	20133	73	90	LC	LECTURE	W      06:10P-08:00PHAM HAMILTON HAL602						W	18:10:00	20:00:00	HAMILTON HAL	602	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			CHAINTREAU, AUGUSTIN				MORN	MORNINGSIDE
64928	COMS6998E002	COMS6998	20133	25	25	LC	LECTURE	R      04:10P-06:00PMUD SEELEY W. MU834						R	16:10:00	18:00:00	SEELEY W. MU	834	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			ZHENG, CHANGXI				MORN	MORNINGSIDE
18532	COMS6998E003	COMS6998	20133	19	20	LC	LECTURE	T      06:10P-08:00PMUD SEELEY W. MU644						T	18:10:00	20:00:00	SEELEY W. MU	644	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			CHEN, XI				MORN	MORNINGSIDE
14987	COMS6998E004	COMS6998	20133	16	52	LC	LECTURE	T      06:10P-08:00PMUD SEELEY W. MU227						T	18:10:00	20:00:00	SEELEY W. MU	227	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			BOSE, PRADIP				MORN	MORNINGSIDE
68201	COMS6998E005	COMS6998	20133	53	999	LC	LECTURE	R      06:10P-08:00PMUD SEELEY W. MU644						R	18:10:00	20:00:00	SEELEY W. MU	644	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			THEOBALD, MICHAEL				MORN	MORNINGSIDE
88038	COMS6998E006	COMS6998	20133	53	50	LC	LECTURE	W      06:10P-08:00PIAB INTERNATIONA410						W	18:10:00	20:00:00	INTERNATIONA	410	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			RADEV, DRAGOMIR R				MORN	MORNINGSIDE
81351	COMS6998E008	COMS6998	20133	30	30	LC	LECTURE	T      06:10P-08:00PSCEPSCHAPIRO CEP415						T	18:10:00	20:00:00	SCHAPIRO CEP	415	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			LI, LI E				MORN	MORNINGSIDE
78288	COMS6998E010	COMS6998	20133	103	103	LC	LECTURE	F      04:10P-06:00PMAT MATHEMATICS 207						F	16:10:00	18:00:00	MATHEMATICS	207	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			SAHU, SAMBIT				MORN	MORNINGSIDE
84691	COMS9800E001	COMS9800	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
18297	COMS9910E001	COMS9910	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
84530	COMS9911E001	COMS9911	20133	0	0	IS	INDEPENDENT							\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
75145	CSEE3827W001	CSEE3827	20133	110	110	LC	LECTURE	TR     10:10A-11:25AHAV HAVEMEYER HA209						TR	10:10:00	11:25:00	HAVEMEYER HA	209	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			KIM, MARTHA A				MORN	MORNINGSIDE
19056	CSEE4119W001	CSEE4119	20133	85	90	LC	LECTURE	TR     01:10P-02:25PSCH SCHERMERHORN614						TR	13:10:00	14:25:00	SCHERMERHORN	614	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			MISRA, VISHAL				MORN	MORNINGSIDE
18837	CSEE4823W001	CSEE4823	20133	75	80	LC	LECTURE	MW     07:10P-08:25PHAM HAMILTON HAL702						MW	19:10:00	20:25:00	HAMILTON HAL	702	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			VEZYRTZIS, CHRISTOS				MORN	MORNINGSIDE
11535	CSOR4231W001	CSOR4231	20133	146	164	LC	LECTURE	TR     11:40A-12:55PNWC NORTHWEST CO501						TR	11:40:00	12:55:00	NORTHWEST CO	501	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			STEIN, CLIFFORD				MORN	MORNINGSIDE
23466	CSOR4246W001	CSOR4246	20133	38	50	LC	LECTURE	MW     07:40P-08:55PCSC COMPUTER SCI453						MW	19:40:00	20:55:00	COMPUTER SCI	453	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N							MORN	MORNINGSIDE
65814	ENGI1006W001	ENGI1006	20133	52	999	LC	LECTURE	MW     05:40P-06:55PMUD SEELEY W. MU633						MW	17:40:00	18:55:00	SEELEY W. MU	633	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N			CANNON, ADAM H				MORN	MORNINGSIDE
\.


--
-- Name: courses_v2_t_pkey; Type: CONSTRAINT; Schema: public; Owner: adicu; Tablespace: 
--

ALTER TABLE ONLY courses_v2_t
    ADD CONSTRAINT courses_v2_t_pkey PRIMARY KEY (course);


--
-- Name: sections_v2_t_course_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adicu
--

ALTER TABLE ONLY sections_v2_t
    ADD CONSTRAINT sections_v2_t_course_fkey FOREIGN KEY (course) REFERENCES courses_v2_t(course);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

