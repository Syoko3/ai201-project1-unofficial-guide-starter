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
| 9 | GitHub | UC Merced CSE Courses Repository | https://github.com/hajin-park/ucmerced-cse |
| 10 | Reddit | Will cse ever be impacted at ucm? | https://www.reddit.com/r/ucmerced/comments/1gvksls/will_cse_ever_be_impacted_at_ucm/ |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

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

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
