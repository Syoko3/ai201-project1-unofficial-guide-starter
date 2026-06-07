# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

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
- Sources 1-2: 100 characters
- Sources 3-6, 10: 250 characters
- Sources 7-9: 400 characters

**Overlap:**
- Sources 1-2: 0 characters
- Sources 3-6, 10: 20 characters
- Sources 7-9: 50 characters

**Why these choices fit your documents:**
- Sources 1-2: They are the ratings and reviews of the CSE courses and professors with short comments.
- Sources 3-6, 10: They are Reddit (sources 3-6) or Quora (source 10) posts with long comments, and some people will say at least 3 bullet points and explain them in detail.
- Sources 7-9: It includes course catalogs and faculty lists, and includes GitHub repo for the contents of each CSE course. Source 9 also explains how the CSE in UC Merced works with the faculty members.

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

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**


**How source attribution is surfaced in the response:**


---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

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


**What the system returned:**


**Root cause (tied to a specific pipeline stage):**


**What you would change to fix it:**


---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**


**One way your implementation diverged from the spec, and why:**


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

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
