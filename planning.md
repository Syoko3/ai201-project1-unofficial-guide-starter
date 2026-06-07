# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
I chose the UC Merced students ratings and reviews of CSE courses and professors. This is a valuable knowledge because CSE courses have heavy workload with some projects, and peer feedback can clarify either the professor is engaged actively on class or not. This is hard to find through official channels because the universities will share the peer feedback to the professor anonymously, and there are some algorithmic and demographic biases included that affects the universities to post the department and faculty rankings publicly. 

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Coursicle | UC Merced CSE Courses & Professors Ratings | https://www.coursicle.com/ucmerced/courses/CSE/ |
| 2 | Rate My Professors | UC Merced CSE Professors Ratings | https://www.ratemyprofessors.com/search/professors/4767?q=*&did=11 |
| 3 | Rate My Courses | UC Merced CSE Courses Reviews | https://www.ratemycourses.io/uc-merced/department/cse |
| 4 | Reddit | UC Merced & Computer Science & Engineering Reviews | https://www.reddit.com/r/ucmerced/comments/m08y2s/uc_merced_and_computer_science_and_engineering/ |
| 5 | Reddit | What CSE electives do you think are the hardest and easiest? | https://www.reddit.com/r/ucmerced/comments/1nu6w64/cse_majors_what_cse_electives_do_you_think_are/ |
| 6 | UC Merced | CSE Courses Descriptions | https://catalog.ucmerced.edu/content.php?filter%5B27%5D=CSE&filter%5B29%5D=&filter%5Bcourse_type%5D=-1&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=1&cur_cat_oid=23&expand=&navoid=2517&search_database=Filter#acalog_template_course_filter |
| 7 | UC Merced | CSE Faculty | https://engineering.ucmerced.edu/departments/computer-science-engineering-cse |
| 8 | Facebook | Computer Science at UC Merced vs SJSU | https://www.facebook.com/groups/collegeadmissionscorner/posts/1464265537775004/ |
| 9 | UC Merced | Computer Science & Engineering Advising | https://engr-advising.ucmerced.edu/majors/cse |
| 10 | Reddit | Will cse ever be impacted at ucm? | https://www.reddit.com/r/ucmerced/comments/1gvksls/will_cse_ever_be_impacted_at_ucm/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
- Sources 1, 2, 3, 9: 150-200 characters
- Sources 3, 4, 5, 8, 9, 10: 200-300 characters
- Sources 6, 7: 400-500 characters

**Overlap:**
- Sources 1, 2, 3, 9: 0 characters
- Sources 4, 5, 8, 10: 20 characters
- Sources 6, 7: 50 characters

**Reasoning:**
- Sources 1, 2, 3, 9: Sources 1-3 are the ratings and reviews of the CSE courses and professors with short comments. Source 9 shows how does the CSE in UC Merced works with the faculty members.
- Sources 4, 5, 8, 10: They are Reddit, Facebook, or Quora posts with long comments, and some people will say at least 3 bullet points and explain them in detail.
- Sources 6, 7: It includes course catalogs and faculty lists, and includes GitHub repo for the contents of each CSE course.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 via sentence-transformers

**Top-k:**
5

**Production tradeoff reflection:**
- Less context length
- Much unorganized context and high latency
- False negatives and biases

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | How was the CSE 100 workload in Fall 2026? | CSE 100 had 4 midterms with 14% weight each (56% total), and the final had 24%. Students said there is no real incentive to learn besides surviving the 80% tank and gaining access to required classes. |
| 2 | What is the hardest CSE course in the UC Merced? | The hardest CSE course is CSE 160 because one student said the projects are in very high level, so you need to completely understand the environment and implementation by your own time. |
| 3 | How did the faculty design the UC Merced CSE curriculum to balance theory and modern technology? | Computer science and engineering students at UC Merced work with the world's top computer scientists and engineers, and their faculty members worked on development of a program of study that combines practical exposure to the most modern technologies available with a theoretical foundation. |
| 4 | How was the professor Santosh Chandrasekhar's grading policy in CSE 31? | His grading policy was very balanced, with only 35% worth on exams. Presenting your lab coding assignments/project to the TA was very helpful. |
| 5 | What do students say about the quality of CS classes in UC Merced? | Students said that many lectures used in some classes are outdated. Most professors focus on the theoretical parts of the clases instead of teaching us more technical skills used in the industry, but others also care about your technical growth. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. The chunks that split key information across boundaries could go wrong because the vector embedding will have no idea to determine who is the professor or what class is discussed.

2. Ingestion of noisy or inconsistent documents with specified chunks will go wrong because sometimes it will end up with thousands of tokens of garbage text.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

ASCII Art:
Document Ingestion --> Chunking --> Embedding + Vector Store
                                             |
                                             |
                                             v
               Generation     <----      Retrieval     
                    ^                        ^
                    |                        |
                    |                        |
              Student Query   ---->      ----
                    |
                    |
                    v
            Answers + Citations
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**
I will use Copilot for my Chunking Strategy section and ask it to implement the chunking text function with my specified chunk size and overlap based on selected documents. I expect to produce the clear chunking text when the documents are loaded, and I will verify the output matches my spec by printing out the exact token/character count, character lengths, and boundary text snippets of your first few generated chunks.

**Milestone 4 — Embedding and retrieval:**
I will use Gemini for my Retrieval Approach section and ask it to implement the embedding text function and retrieval text function with my specified top-k. I expect to produce a list of the top-k most semantically relevant text chunks alongside their metadata whenever a student query is executed. I will verify this output by checking that the retrieved snippets directly contain the answers to my test questions.

**Milestone 5 — Generation and interface:**
I will use Claude Code for generation and interface section and ask it to implement the interactive chat UI components, API integration layers, and frontend UI layout. I expect with the user inputting in the chat UI, and the response should be structured and similar or exactly same as the expected answers I mentioned in the Evaluation Plan section, including the citations. I will verify by testing end-to-end data binding between user queries and the local-to-Groq pipeline.
