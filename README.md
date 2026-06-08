# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Demo
Video Link: https://drive.google.com/file/d/1xdbWXN4BAlEerMvIJ3rHU_HBqZ6ej86s/view?usp=sharing

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->
My system covers about the student reviews of CSE courses and professors in UC Merced. This is a valuable knowledge because CSE courses have heavy workload with some projects, and peer feedback can clarify either the professor is engaged actively on class or not. This is hard to find through official channels because the universities will share the peer feedback to the professor anonymously, and there are some algorithmic and demographic biases included that affects the universities to post the department and faculty rankings publicly.

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Rate My Courses | UC Merced CSE Courses Reviews | https://www.ratemycourses.io/uc-merced/department/cse |
| 2 | Rate My Professors | UC Merced CSE Professors Ratings | https://www.ratemyprofessors.com/search/professors/4767?q=*&did=11 |
| 3 | Reddit | UC Merced & Computer Science & Engineering Reviews | https://www.reddit.com/r/ucmerced/comments/m08y2s/uc_merced_and_computer_science_and_engineering/ |
| 4 | Reddit | What CSE electives do you think are the hardest and easiest? | https://www.reddit.com/r/ucmerced/comments/1nu6w64/cse_majors_what_cse_electives_do_you_think_are/ |
| 5 | Reddit | Will cse ever be impacted at ucm? | https://www.reddit.com/r/ucmerced/comments/1gvksls/will_cse_ever_be_impacted_at_ucm/ |
| 6 | Reddit | CSE Major Advice | https://www.reddit.com/r/ucmerced/comments/1b6wttq/cse_major_advice/ |
| 7 | UC Merced | CSE Courses Descriptions | https://catalog.ucmerced.edu/content.php?filter%5B27%5D=CSE&filter%5B29%5D=&filter%5Bcourse_type%5D=-1&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D=1&cur_cat_oid=23&expand=&navoid=2517&search_database=Filter#acalog_template_course_filter |
| 8 | UC Merced | CSE Faculty | https://engineering.ucmerced.edu/departments/computer-science-engineering-cse |
| 9 | UC Merced | Computer Science & Engineering Advising | https://engr-advising.ucmerced.edu/majors/cse |
| 10 | Quora | Should I consider CS at UC Merced? | https://www.quora.com/Should-I-consider-CS-at-UC-Merced |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**
- Sources 1-2: 500 characters
- Sources 3-6, 10: 300 characters
- Sources 7-9: 200 characters

**Overlap:**
- Sources 1-2: 50 characters
- Sources 3-6, 10: 30 characters
- Sources 7-9: 10 characters

**Why these choices fit your documents:**
- Sources 1-2: They are the review platforms for showing the student ratings and reviews of the CSE courses and professors with short comments.
- Sources 3-6, 10: They are Social Media platforms and it includes a forum style text. Some people will say at least 3 bullet points and explain them in detail.
- Sources 7-9: They are from the UC Merced website. Course catalogs and faculty lists (Sources 7 & 8) of the CSE courses includes structional institutional data. Source 9 explains how the CSE in UC Merced works with the faculty members.

**Final chunk count:**
149 chunks total

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**
all-MiniLM-L6-v2 via sentence-transformers

**Why this choice:**
Some sources, such as the contents from UC Merced website, were needed to transform the sentences with many small chunks.

**Production tradeoff reflection:**
- Less context length due to small chunk size
- Structural search targets are ignored from the retrieval
- Much unorganized context and high latency
- False negatives and biases

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**
I stated first that this is an unofficial guide to UC Merced CSE courses and professors. Then I told answer the question using the numbered contexts only and cite the sources you use at that number. 

**How source attribution is surfaced in the response:**
The source attribution is surfaced in the response by using inline numbered context citations. These numbers map sequentially to a compiled reference list appended to the response, showing exactly which document source text was utilized to construct each specific part of the answer.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | How was the CSE 100 workload in Spring 2026? | CSE 100 had 4 midterms with 14% weight each (56% total), and the final had 24%. Students said there is no real incentive to learn besides surviving the 80% tank and gaining access to required classes. | The CSE 100 workload in Spring 2026 was "extremely lecture-heavy" with an 80% weight of exams, and the class focused on concepts rather than code, while the labs were entirely code-based. | Off-target | Inaccurate |
| 2 | What is the hardest CSE course in the UC Merced? | The hardest CSE course is CSE 160 because one student said the projects are in very high level, so you need to completely understand the environment and implementation by your own time. |  CSE 160 is considered a hard course because the class is hard because of the projects. However, it is not explicitly stated as the hardest CSE course. The context does not provide a definitive answer to what the hardest CSE course is, only that CSE 160 is considered challenging. | Relevant | Accurate |
| 3 | Should CS in UC Merced has to be considered as a bad choice? | No, because CS isn’t taught or learned better as you get closer to the coast, and UC Merced students are bright, even if they don't have same academic track record as their peers at some other UCs. | No, CS at UC Merced should not be considered a bad choice. In fact, Source 9 states that "Should you consider UC Merced? Absolutely." It also says that "But is it a bad choice? No." | Relevant | Partially accurate |
| 4 | How was the professor Santosh Chandrasekhar's grading policy in CSE 31? | His grading policy was very balanced, with only 35% worth on exams. Presenting your lab coding assignments/project to the TA was very helpful. | Professor Santosh Chandrasekhar's grading policy in CSE 031 was "overall very balanced, with exams being worth only 35% of your grade." | Relevant | Accurate |
| 5 | What do students say about the quality of CS classes in UC Merced? | Students said that many lectures used in some classes are outdated. Most professors focus on the theoretical parts of the clases instead of teaching us more technical skills used in the industry, but others also care about your technical growth. | A student states that the CS program "is not the best" because many lectures are outdated and most professors focus on theoretical parts instead of teaching technical skills used in the industry. However, there may be some variability in the quality of CS classes at UC Merced, with some classes being more effective than others. | Relevant | Partially accurate |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**
How was the CSE 100 workload in Spring 2026?

**What the system returned:**
A summary of the CSE 100 workload to specify that it was "extremely lecture-heavy" with an 80% weight of exams, and the class focused on concepts rather than code, while the labs were entirely code-based.

**Root cause (tied to a specific pipeline stage):**
The relevant paragraph was specified in the source_1_RateMyCourses.txt, but it only matched the substring pattern "comments?", and dropped the entire text block. The details under that substring was never reached the vector store.

**What you would change to fix it:**
I would apply boilerplate filtering at the line level by dropping only the offending label line to keep the review, instead of discarding the whole block, and anchor the comments pattern to avoid matching any other mid-sentences.

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
The spec helped me during implementation by referencing the sources and chunking strategy to break down the documents in bunch of chunks. It also helped me which AI model I used to implement so that I could reflect easier what goes right and what goes wrong at the end.

**One way your implementation diverged from the spec, and why:**
My implementation diverged from the spec by loading the source files that were copied and pasted from the websites that I referenced, so the chunking size that I mentioned in the planning.md was different. This was because some of the questions used chunks that were off-target that I was expected. I fixed it by modifying the chunking size and overlap to have each chunk to include main content that could be useful for answering my questions.

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:* I gave Copilot my documents and my Chunking Strategy section from planning.md and asked it to implement chunk_text() with my specified chunk size and overlap based on selected documents.
- *What it produced:* It produced a downloaded documents folder with extracted text from each sources. However, some sources, such as Reddit and Quora, did not produce any output after loading them because of JavaScript rendering and blocking requests.
- *What I changed or overrode:* I made a transition to copying the texts from all sources that I would need to use for my evaluation, pasting them in a plain text for each source, and saving them in a data folder, which was created in the documents folder. I also changed the logic of loading the documents by implementing the functions to load the source files and normalize the texts and paragraphs.

**Instance 2**

- *What I gave the AI:* I gave Gemini for my Retrieval Approach section and asked it to implement the embedding text function and retrieval text function with my specified top-k, which was 5.
- *What it produced:* It produced a list of the top-k most semantically relevant text chunks alongside their metadata whenever a student query is executed. I verified this output by checking that the retrieved snippets directly contain the answers to my test questions. All chunks had the distance score of less than 0.6.
- *What I changed or overrode:* I changed the chunking size of each source to the current one specified in the Chunking Strategy section, and changed the top-k to 8 instead of 5. It was because when I tested the first question, there were some irrelevant chunks are produced as an output, which were very different from my expected answer. I also added the extraction of structural search targets, such as "CSE 100" and "CSE 31". This helped the retrieval to produce relevant chunks for each question, using all of the available sources I included.
