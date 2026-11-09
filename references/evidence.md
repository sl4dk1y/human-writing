# What is actually known: numbers and sources

Dates matter. Everything below is from 2025-2026, and some conclusions expire with a single model release. Re-read before leaning on a specific number.

## Field guides

English Wikipedia, [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). Maintained by WikiProject AI Cleanup and updated as models change. Most internet lists of tells derive from this essay, including the popular Claude Code plugin released in January 2026.

Russian Wikipedia, [Википедия:Признаки сгенерированности текста](https://ru.wikipedia.org/wiki/Википедия:Признаки_сгенерированности_текста). A separate document, not a translation, with its own Russian markers. It is referenced by the C7 speedy-deletion criterion.

Both are observations, not rules. Both say plainly that the presence of a tell does not prove authorship.

## Rates: Pangram

[9 Signs of AI Writing, Backed by Data](https://pangram.com/signs-of-ai-writing). Corpus in millions of documents, frequency per 10,000 words.

| Tell | Human | AI | Ratio |
|---|---|---|---|
| Markdown formatting in plain text | 8 | 90 | 12x |
| AI-favoured phrases | 3 | 30 | 12x |
| Em dashes | 2 | 17 | 10x |
| Bullet lists | 3 | 28 | 9x |
| Triads | 5 | 19 | 4x |
| "Not just X but Y" | 1 | 3 | 3x |
| Unusual unicode | 28 | 71 | 3x |
| Assistant-style headers | 1 | 2 | 2x |
| Emoji | 0.1 | 0.2 | 2x |

By markdown variant: bold 2 vs 65 (43x), headers 0.5 vs 11 (23x), inline code 0.2 vs 0.8.

Individual phrases: "delve into" 45x, "in today's fast-paced world" 35x, "crucial to note that" 22x, "navigate the tapestry of" 18x.

## What changed by 2026: Graphite

[AI Tells](https://graphite.io/research/ai-tells), September 2026. 10,000 human articles and 90,000 generated ones on the same topics, nine models.

There are not ten tells but 12,877: that many words, phrases and frames appear at least twice as often as in human writing. Each model has between 2,355 and 3,746 of them. 65% are unique to one model family, and between two consecutive versions of the same model 55-72% are new. Fixed word lists therefore expire with each release.

The em dash stopped working. GPT-6 Astra uses it about an eighth as often as humans, Gemini 3.1 Pro almost never, Claude Opus 5 at roughly the human rate. Banning it in 2026 fights the 2024 model.

Families differ in character. GPT-class hedges: "may provide", "can provide", "not necessarily", "rather than focusing". Claude-class reaches for superlatives: "single most", "arguably the most", "every single", "enormously", "less like a _ and more like". Gemini-class uses intensifiers and formal transitions: "incredibly", "absolutely", "furthermore", "additionally", "this comprehensive guide", "exactly", "precisely".

Humans do what models mostly do not: speak in the first person, address the reader, use contractions, drop casual qualifiers ("pretty", "sort of"), tell anecdotes, reference personal experience, use exclamation marks more than a hundred times as often as current models, and interrupt themselves with parenthetical asides far more often.

The study also notes its own limit: its human corpus was published before ChatGPT, so writing that changed after 2022 because of ChatGPT looks like a tell when it is just people.

## Stylometry: what is measured

Shan, Lee, Hao, [AI Writers Have a Consistent Stylometric Footprint, but AI Editors Do Not](https://arxiv.org/abs/2608.27855), 2026. 45,000 texts, eight models, five domains, plus 273,420 AI-edited texts.

Fourteen features: lexical diversity, lexical density (share of content words), percentage of long words, document length in words and sentences, mean sentence length, percentage of vowels, consonants and punctuation, maximum parse-tree depth, entropy, burstiness, and two readability scores.

Two findings worth remembering.

Fully generated text is distinguished mainly by higher lexical diversity and higher entropy. So "rich vocabulary" is not a human signature; it is the opposite.

AI editing behaves differently: it lowers lexical density, meaning it adds function words and dilutes content. "Edited by AI" and "written by AI" therefore leave different traces, and one feature will not catch both.

## Vocabulary spikes in academic text

Kobak and co-authors, [Delving into LLM-assisted writing in biomedical publications through excess vocabulary](https://www.science.org/doi/10.1126/sciadv.adt3813), Science Advances, 2025. PubMed abstracts, 2010-2024.

Words with the largest excess after 2023: "delves" (rate ratio 28.0), "underscores" (13.8), "showcasing" (10.7), plus their grammatical forms. The lesson is about frequency rather than the word: in 2023 these words simply started appearing many times more often than before.

## People are bad at this, stylometry is better

[Stylometry can reveal artificial intelligence authorship, but humans struggle](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335369), PLOS ONE, 2025. Japanese corpus, ten texts, seven models.

Stylometric features separate authors reliably. Human readers do barely better than chance. So "I can tell by looking" is a weak argument, and faith in detectors does not rescue it: Russian Wikipedia notes that detectors such as GPTZero check themselves and err in both directions.

## Limits

The corpora are web articles and posts. In chat, email and personal writing the distribution is different and some conclusions do not transfer.

Generations used one fixed prompt per model. With a different prompt some tells disappear: you can order a model to use contractions and the second person, and it will, and the tell is gone while the authorship is unchanged.

One tell proves nothing. Neither does a detector. The pattern of evidence is what carries, and even that is a judgement about probability.
