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

5 representative chunks:
- {'source_path': 'documents\\data\\cleaned\\source_10_Quora.txt',
 'category': 'short',
 'chunk_index': 1,
 'chunk_size': 300,
 'overlap': 30,
 'chunk_text': 'Should I consider CS at UC Merced?\n'
               'Joshua Gross\n'
               'NaTa Chou\n'
               ', master Computer Science & Shopping, Belgorod State '
               'Technological University (2017) and\n'
               "Jack O'Quin\n"
               'jfc, three nearly identical ChatGPT answers.\n'
               '\n'
               'Shame on you, Nagesh K, Naresh Kumar, and Licensed Soft.\n'
               '\n'
               'So a real answer.'}
- {'source_path': 'documents\\data\\cleaned\\source_10_Quora.txt',
 'category': 'short',
 'chunk_index': 2,
 'chunk_size': 300,
 'overlap': 30,
 'chunk_text': 'Soft.\n'
               '\n'
               'So a real answer.\n'
               '\n'
               'Merced gets a bad rap because:\n'
               '\n'
               'It’s the youngest of the UCs\n'
               'It’s the least competitive of the UCs\n'
               'It’s not located near... well, pretty much any urban place '
               'that Californians are eager to go to\n'
               'But is it a bad choice? No.'}
- {'source_path': 'documents\\data\\cleaned\\source_1_RateMyCourses.txt',
 'category': 'medium',
 'chunk_index': 1,
 'chunk_size': 500,
 'overlap': 50,
 'chunk_text': '=========================================\n'
               'CSE 100: Algorithm Design and Analysis\n'
               '=========================================\n'
               'Prof: Ross Greer, Hua Huang / Spring 2026\n'
               '\n'
               'Apr 23, 2026\n'
               '\n'
               'Course Content\n'
               'As a result of the 80% weight of exams, the class is extremely '
               'lecture-heavy. Code is rarely to never discussed, displayed, '
               'or demonstrated in lecture, with the focus being on the '
               'concepts instead. Conversely, the labs are entirely code.'}
- {'source_path': 'documents\\data\\cleaned\\source_2_RateMyProfessors.txt',
 'category': 'medium',
 'chunk_index': 1,
 'chunk_size': 500,
 'overlap': 50,
 'chunk_text': '=========================================\n'
               'Angelo Kyrilov\n'
               '=========================================\n'
               'Quality 3.0 / Difficulty 3.0\n'
               'CSE024\n'
               'Apr 10th, 2026\n'
               'For Credit: Yes\n'
               'Attendance: Mandatory\n'
               'Would Take Again: Yes\n'
               'Grade: Not sure yet\n'
               'Textbook: Yes\n'
               '"STEAMplug kingpin"'}
- {'source_path': 'documents\\data\\cleaned\\source_2_RateMyProfessors.txt',
 'category': 'medium',
 'chunk_index': 9,
 'chunk_size': 500,
 'overlap': 50,
 'chunk_text': 'grades. Also, sometimes he will curve the exam."\n'
               '\n'
               '=========================================\n'
               'Giovanni Gonzalez Araujo\n'
               '=========================================\n'
               'Quality 2.0 / Difficulty 4.0\n'
               'CSE024\n'
               'Mar 5th, 2026\n'
               'For Credit: Yes\n'
               'Attendance: Mandatory\n'
               'Grade: Incomplete\n'
               'Textbook: N/A\n'
               '"Araujo doesn\'t structure his classes well. This current '
               'semester, he designed the course to be extremely lecture '
               'dependent. We have a quiz every friday and 2 lectures on '
               'Tuesday and Thursday. Meaning he gives us ONE day'}

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

3 Retrieval Tests:
==================== TESTING EVALUATION QUERY ====================
Query: How was the CSE 100 workload in Spring 2026?
[search] Course pattern detected: 'CSE 100'. Applying soft-boost scoring.

[Distance: 0.378] Source: documents\data\cleaned\source_1_RateMyCourses.txt
Content: =========================================
CSE 100: Algorithm Design and Analysis
=========================================
Prof: Ross Greer, Hua Huang / Spring 2026

Apr 23, 2026

Course Content
As a result of the 80% weight of exams, the class is ex...

[Distance: 0.532] Source: documents\data\cleaned\source_4_UCM_Electives_Reddit.txt
Content: in 160 and 176 right now.

160 with Cerpa is pretty hardcore; the reading and homework’s aren’t too too bad in terms of concepts, understanding them, doing basic computations and calculations with network related stuff. That class is hard because of ...

[Distance: 0.575] Source: documents\data\cleaned\source_5_UCM_CSE_Impact_Reddit.txt
Content: it be impacted in the future?

internetbooker134
OP
I agree more hiring needs to be done for the CSE department although from what I've heard it's hard to hire faculty and get them to move to Merced in general as it's not as attractive compared to ot...

[Distance: 0.592] Source: documents\data\cleaned\source_7_UCM_Catalog.txt
Content: Science & Engineering (Undergraduate) - CSE

Concepts of computer operating systems including concurrency, memory management, file systems, multitasking, performance analysis, and security.

Conjoined with: EECS 251
Laboratory included
Normal Letter ...

[Distance: 0.593] Source: documents\data\cleaned\source_5_UCM_CSE_Impact_Reddit.txt
Content: faculty member, not in CSE.

It's hard for computer science and software engineering programs to hire faculty because they can make much, much more money working in industry. I can imagine that this might be changing due to the tech industry layoffs ...

==================== TESTING EVALUATION QUERY ====================
Query: What is the hardest CSE course in the UC Merced?

[Distance: 0.286] Source: documents\data\cleaned\source_4_UCM_Electives_Reddit.txt
Content: CSE majors: what CSE electives do you think are the hardest and easiest?
Was talking with my friends about the cse electives at UC Merced and we came to conclusion that the easiest ones are cse 108, 107, and 111. On the harder side ive heard cse 160 ...

[Distance: 0.404] Source: documents\data\cleaned\source_10_Quora.txt
Content: Should I consider CS at UC Merced?
Joshua Gross
NaTa Chou
, master Computer Science & Shopping, Belgorod State Technological University (2017) and
Jack O'Quin
jfc, three nearly identical ChatGPT answers.

Shame on you, Nagesh K, Naresh Kumar, and Lic...

[Distance: 0.404] Source: documents\data\cleaned\source_3_UCM_Review_Reddit.txt
Content: ers. It will just be a little bit more difficult if you go to UCM....

[Distance: 0.425] Source: documents\data\cleaned\source_3_UCM_Review_Reddit.txt
Content: UC Merced and Computer Science and Engineering

As students of the most recent UC campus, I'd like some responses for the following things:

Why'd you go all the way to UC Merced considering it's out in the middle of California?...

[Distance: 0.431] Source: documents\data\cleaned\source_7_UCM_Catalog.txt
Content: Experience: Scientific Method

Requisites and Restrictions
Prerequisite Courses: CSE 031 and CSE 100 and MATH 024
Cannot also be taken due to similarity of content: ENGR 190, ENGR 193, ENGR 194
Open only to the following class level(s):
Senior

Cross...

==================== TESTING EVALUATION QUERY ====================
Query: Should CS in UC Merced has to be considered as a bad choice?

[Distance: 0.237] Source: documents\data\cleaned\source_10_Quora.txt
Content: is it a bad choice? No.

Second, if you’re a standout, you’ll get special attention (if you want it), and it’s easier to be a standout at Merced than someother UC campuses.

So, should you consider UC Merced? Absolutely. Should you go there? Well, w...

[Distance: 0.251] Source: documents\data\cleaned\source_10_Quora.txt
Content: Soft.

So a real answer.

Merced gets a bad rap because:

It’s the youngest of the UCs
It’s the least competitive of the UCs
It’s not located near... well, pretty much any urban place that Californians are eager to go to
But is it a bad choice? No....

[Distance: 0.255] Source: documents\data\cleaned\source_10_Quora.txt
Content: Should I consider CS at UC Merced?
Joshua Gross
NaTa Chou
, master Computer Science & Shopping, Belgorod State Technological University (2017) and
Jack O'Quin
jfc, three nearly identical ChatGPT answers.

Shame on you, Nagesh K, Naresh Kumar, and Lic...

[Distance: 0.316] Source: documents\data\cleaned\source_3_UCM_Review_Reddit.txt
Content: UC Merced and Computer Science and Engineering

As students of the most recent UC campus, I'd like some responses for the following things:

Why'd you go all the way to UC Merced considering it's out in the middle of California?...

[Distance: 0.393] Source: documents\data\cleaned\source_5_UCM_CSE_Impact_Reddit.txt
Content: it be impacted in the future?

internetbooker134
OP
I agree more hiring needs to be done for the CSE department although from what I've heard it's hard to hire faculty and get them to move to Merced in general as it's not as attractive compared to ot...

- 1st query: Partially relevant; Right source but less content for 1st chunk; all other 4 chunks have wrong sources
- 2nd query: Partially relevant; Specific, on topic, right source for the 1st chunk; 2nd to 4th chunk have right source but less content; 5th chunk has wrong source
- 3rd query: Relevant; Specific, on topic, right source for the first three chunks; last two chunks are also relevant, on topic, right source, but less content

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
