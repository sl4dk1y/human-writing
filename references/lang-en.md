# English

The structural catalogue is language-neutral. This file holds what is specific to English: the word lists, the model-family differences, and two typography questions.

## Words and phrases

Highest-value offenders in 2025-2026 corpora, roughly ordered by how much they stand out:

delve, tapestry, intricate, pivotal, robust, seamless, leverage, underscore, showcase, testament, ever-evolving, navigating the landscape, in today's fast-paced world, unlock, elevate, empower, foster, crucial, paramount, meticulous, myriad, plethora, vibrant, nestled, in the heart of, groundbreaking, renowned, must-visit, stunning, breathtaking, game-changer, cutting-edge, state-of-the-art, it's worth noting, moreover, furthermore, additionally, in conclusion, in summary, overall.

Two of these are also ordinary technical vocabulary, and cutting them wholesale breaks real writing: "robust" in engineering, "gates" in compilers, "landscape" in a paper about landscape ecology. Look at whether the word is doing work or filling space.

Ratios from a corpus of millions of documents, per 10,000 words: markdown formatting 8 human vs 90 machine (12x), AI-favoured phrases 3 vs 30 (12x), em dashes 2 vs 17 (10x), bullet lists 3 vs 28 (9x), triads 5 vs 19 (4x), "not just X but Y" 1 vs 3 (3x). Individual phrases are worse: "delve into" 45x, "in today's fast-paced world" 35x, "crucial to note that" 22x.

Academic vocabulary moved measurably after 2023. In PubMed abstracts, "delves" appears about 28 times more often than its pre-ChatGPT baseline, "underscores" 13.8 times, "showcasing" 10.7 times. This matters outside academia too: it shows how fast a single word becomes a signature and how fast it stops being one after everyone notices.

## Model families

Families differ. From a 2026 study of 90,000 generated articles across nine models:

| Family | Its own tells |
|---|---|
| GPT-class | hedges: "may provide", "can provide", "not necessarily", "rather than focusing" |
| Claude-class | superlatives: "single most", "arguably the most", "every single", "enormously", "less like a _ and more like", "is genuinely" |
| Gemini-class | intensifiers and formal transitions: "incredibly", "absolutely", "furthermore", "additionally", "this comprehensive guide", "exactly", "precisely" |

65% of the tells found are unique to one family, and between two consecutive versions of the same model, 55-72% of the tells are new. So a fixed word list is a 2024 instrument. Read for the habit underneath the word.

## The em dash

Around 2024-2025 the em dash became the internet's favourite tell, and by 2026 it had stopped working. Measured rates: GPT-class models use it about an eighth as often as humans, Claude-class about the same rate as humans, Gemini-class almost never.

What remains true is the function. One or two in a document is style. A dash in every third sentence, always doing the work of a comma or a colon, is a habit. Because many writers now avoid the dash on purpose, heavy use reads slightly more suspicious than it did in 2024, which is a strange outcome of the discourse and not a reason to ban it.

Replacement test: if a substitute punctuation mark leaves the sentence with one meaning, the dash was not adding a relationship, it was avoiding a decision.

## Typography

- Straight quotes in plain text, curly quotes in word processors. Match the file you are editing, and never mix.
- British and American spelling inside one document is a separate tell, and a common one when a model imitates several sources. Pick one and check for "organise"/"organize".
- One space after a full stop. Double spaces survive in American legal and older technical writing, and nowhere else.
- Serial comma: keep it consistent. Inconsistency is more visible than either choice.
- Single quotes inside double (American) or the reverse (British). Do not mix the two systems in one text.

## Phrases to cut on sight

it is important to note, it's worth noting, needless to say, at the end of the day, when it comes to, in the realm of, the world of, plays a vital role, a testament to, stands as, serves as, sheds light on, paves the way, beacon of, whether you're a ... or a ..., and the closer "I hope this helps".

## Sources

Wikipedia:Signs of AI writing; Pangram, 9 Signs of AI Writing, Backed by Data; Graphite, AI Tells (September 2026); Kobak et al., Science Advances, 2025. Full citations in `evidence.md`.
