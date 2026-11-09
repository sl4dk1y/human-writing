---
name: human-writing
description: Write and edit prose that does not read as AI-generated.
license: MIT
metadata:
  version: "2.0.0"
---

# Human writing

Machine-written text gives itself away through habits, not through passphrases. The rhythm is even, every thought is announced before it is made, importance is attached to things instead of to people, and nothing is left unfinished. Word lists rot with each model release. The habits last years. So the work goes from structure down to vocabulary, not the other way round.

## When to use this

- Writing something a person will read as human: a post, an email, an article, docs, a product page, a PR comment.
- Editing text that already smells like a chatbot.
- Reviewing someone else's text before it goes out.
- Writing in any language. `references/patterns.md` holds the structural catalogue, `references/evidence.md` holds the measurements and sources, and `references/lang-*.md` holds per-language markers and typography.

Not for code, logs, legal wording, or anything where the exact formulation is the point. There the goal is the opposite: remove variation.

## The one idea

A model picks the wording that fits the widest range of readers and topics. A real author writes for one reader and one occasion, so their choices are uneven and specific. Everything below is a special case of one rule: the concrete over the average.

Two consequences follow.

Every sentence you keep must tell the reader something they did not already have, either from earlier in the text or from the conversation around it.

A tell counts in proportion to how rarely a careful writer would do it on purpose. One dash means nothing. A dash in every paragraph means a lot.

## How to work

1. Decide what the text is and who reads it. A personal post may say "I don't know". An onboarding doc may not.
2. If you have a sample of the author's own writing, read it first: sentence length, vocabulary, punctuation, openings. The sample outranks every rule below, including the dash rule.
3. Write from the fact. Each paragraph starts with what happened or what is known, not with how important it is.
4. Read it back and cut everything that adds no fact: announcements, run-ups, closers, statements of significance.
5. Check the rhythm aloud. Three sentences in a row of the same length means one of them gets shorter or longer, but not by formula.
6. Run `scripts/ai_tells.py` (below) and look at what survived.
7. Check the facts: nothing added, nothing lost. An invented detail is worse than a stock phrase.

## Ten rules that carry most of the weight

1. Every sentence adds a fact or a consequence. A line that only signals "something important is coming" is waste.
2. Concrete over evaluative. Not "a revolutionary approach" but what was done and what it changed.
3. Uneven rhythm. A short sentence after a long one works. An even paragraph of twenty-word sentences never does.
4. No "not X but Y", no "it's not just a tool, it's a philosophy". The negative half invents an opponent, which makes the second half feel heavier without saying more.
5. No summary closer. "In conclusion, it is worth noting" restates the text in the same words. The last line should carry a fact, not a promise.
6. Say it instead of announcing it. "Let's dive in", "it's important to understand", "here's what you need to know" replace a thought with a trailer for the thought.
7. Do not attach importance to objects. An event does not "underscore" anything, a town does not "symbolise" anything, an approach does not "play a key role". A person does that, and only if they said so.
8. Formatting by need, not by rhythm. Bold, lists, headings and rules go where the text is unreadable without them. A four-item list almost always reads better as a paragraph.
9. Do not hide the author. First person and doubt are normal in personal writing. Impersonal constructions belong in reference material.
10. Leave things imperfect. An opinion, an aside in brackets, a thought you did not finish, an admission that you do not know. Completeness and smoothness are the machine signature.

## Language packs

Structure transfers across languages. Markers and typography do not, and each pack lists what is specific.

| Pack | Covers |
|---|---|
| `references/lang-en.md` | English word lists, model-family favourites, the em dash history, British and American spelling |
| `references/lang-ru.md` | Calques, канцелярит, dangling gerunds, and the dash question, which is a real grammar mark and cannot simply be banned |
| `references/lang-de.md` | Nominal style, `-ung` chains, "In der heutigen...", dash and quotation conventions |
| `references/lang-es.md` | "No solo... sino también", "juega un papel crucial", gerundio riders, regional variation |
| `references/lang-fr.md` | "Il est important de noter", "dans le monde d'aujourd'hui", nominalisation, French spacing an English writer breaks by accident |

The Russian and English lists come from published field guides. The German, Spanish and French lists are compiled from observed model output: they are the same English habits translated, not corpus measurements. Say so if you lean on them in public.

## Checking

```sh
python3 scripts/ai_tells.py text.md                # language detected
python3 scripts/ai_tells.py text.md --lang ru      # force a language
python3 scripts/ai_tells.py text.md --json         # numbers only
```

The script counts dash, bold, list and heading density, the spread of sentence lengths, matches against per-language phrase lists, closing formulas and staged openers. It strips code, URLs, quotations and `> ` blocks before counting, because a guide about stock phrases would otherwise flag its own examples. The cost is that a quoted phrase never shows up in the report, which does not mean it is absent.

The thresholds come from published corpora, but they are heuristics, not verdicts. `!!` means look at it with your eyes, ` ·` means a soft signal that proves nothing alone. The script will happily flag headings and lists in any structured document, so check that mark against the genre instead of editing it away: an instruction needs headings, an email does not.

One limitation to expect: a document that lists markers as examples (like these language packs) reports its own lists as phrase hits, because only quotations and blockquotes are masked, not bare bullet points. On that kind of file, read the counts and ignore them.

Work order: fix `!!` from the top, then reread the whole thing. The phrase list is useful less for naming bad words than for printing line numbers, which gets you to the spot where a thought was replaced by an evaluation.

## Example

Before:

> In today's fast-paced world, note-taking plays a key role. It is not just a tool, it is a second brain. It is important to note that a good system provides clarity and fosters productivity.

After:

> I kept a notebook for eleven years and then stopped. The reason is boring: I got tired of my own handwriting. What I remember from it is the household stuff. Buy stamps. Call the dentist back. The phone number of the man who fixed the boiler in 2016 and never picked up again.

The first version compresses to one sentence without losing anything, and that is the diagnosis. The second cannot be compressed, because it has details in it.

## When not to touch it

- The word or phrase sits in a quotation, a title, a name, or a text that discusses the phrase rather than uses it.
- The author writes that way on purpose and it is their voice: repetition, dashes, exclamations, bureaucratic style used as a device.
- The text was written before 30 November 2022. It cannot be machine-written by definition.
- The genre needs evenness: an instruction, a regulation, a legal text, a reference entry. There the job is to remove ambiguity, not to add character.
- AI detectors and a reviewer's gut feeling are wrong more often than people think. In one Japanese-corpus study, readers did barely better than chance while stylometry did much better. Judge on the pattern of evidence, not on one word.

## What to keep when editing

- An odd specific detail: a real address, someone's actual words, "the lawyer whose office was one floor above my dentist's".
- Unresolved tension: "I think this is mostly fine, and it bothers me, and I cannot say why".
- Period markers: slang, a meme, a joke that only lands in this year.
- A choice the author can explain.
- A real aside or self-correction: "(I wanted to write 'almost', but it really was certain)".

## Sources

Numbers and links in `references/evidence.md`. Briefly: field guides are maintained by WikiProject AI Cleanup on English Wikipedia and separately on Russian Wikipedia, rates are measured by Pangram and Graphite on corpora in the millions of documents, vocabulary spikes are documented in Science Advances, and stylometry is covered in arXiv and PLOS ONE.

One finding worth carrying: by 2026 the em dash had stopped being a reliable tell, because newer models use it less than humans do. Individual words also differ per model family, so check the habit, not the word.
