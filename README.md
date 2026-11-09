# human-writing

A skill for coding agents (Hermes, Claude Code, Cursor, anything that reads a `SKILL.md`): how to write and edit prose so it does not read as machine-generated.

What is inside is not a list of banned words but the habits that give machine text away: even rhythm, evaluation instead of fact, a thought announced instead of made, importance attached to objects, formatting used as punctuation. Word lists expire with each model release; the habits last years.

There is also a script that measures what can be measured: density of dashes, bold, lists and headings, the spread of sentence lengths, matches against per-language phrase lists. Offline, standard library only, no model calls.

## Where the numbers come from

Not from guesswork. The frequencies come from published corpus work, with citations and figures in `references/evidence.md`.

- Wikipedia:Signs of AI writing, and a separate Russian field guide used by patrollers.
- Pangram: nine tells with rates per 10,000 words.
- Graphite, September 2026: 10,000 human and 90,000 generated articles across nine models. They found 12,877 words and frames used at least twice as often by machines.
- Science Advances, 2025: vocabulary spikes in PubMed abstracts after 2023.
- arXiv and PLOS ONE, 2026: stylometry, and how badly humans do at telling text apart by eye.

One finding contradicts the common advice: by 2026 the em dash had stopped working as a tell, because newer models use it less than humans do. What still shows is density and function, not presence.

## Install

Hermes:

```sh
cp -r human-writing ~/.hermes/skills/
```

Claude Code:

```sh
cp -r human-writing ~/.claude/skills/
```

Anything else: feed `SKILL.md` as the instruction and `references/` as reference material.

## Use the checker

```sh
python3 scripts/ai_tells.py text.md                # language detected automatically
python3 scripts/ai_tells.py text.md --lang ru      # force a language
python3 scripts/ai_tells.py text.md --json         # numbers only
```

Languages: English, Russian, German, Spanish, French. The languages are detected from script and stopwords; `--lang` overrides.

`!!` means look at it with your eyes, ` ~` means borderline, ` ·` means a soft signal that proves nothing on its own. Thresholds come from the corpora but remain heuristics: the script shows where to look, the decision stays with a human.

Code, URLs, quotations and `> ` blocks are stripped before counting. Without that, a guide about stock phrases would score a hundred hits on its own examples. Bare bullet lists are not stripped, so a document that lists markers (like the language packs here) will report those lists as hits. That is the known weak spot, and it is documented in `SKILL.md`.

## Example

Before:

> In today's fast-paced world, note-taking plays a key role. It is not just a tool, it is a second brain. It is important to note that a good system provides clarity and fosters productivity.

After:

> I kept a notebook for eleven years and then stopped. The reason is boring: I got tired of my own handwriting. What I remember is the household stuff. Buy stamps. Call the dentist back. The phone number of the man who fixed the boiler in 2016 and never picked up again.

The first version compresses to one sentence without losing anything. The second cannot be compressed, because it has details in it, and that is the difference that matters.

Live examples sit in `examples/`: ten short files, machine-style and human-style versions in five languages. Running the checker over them shows the separation.

## Layout

```
SKILL.md                  the instruction an agent reads
references/patterns.md    the structural catalogue, language-neutral
references/evidence.md    figures, studies, limits
references/lang-en.md     English markers, model families, the em dash
references/lang-ru.md     Russian: bureaucratic style, calques, dangling gerunds, the dash
references/lang-de.md     German: nominal style, -ung chains, typography
references/lang-es.md     Spanish: stock phrases, gerundio, regional variation
references/lang-fr.md     French: stock phrases, nominalisation, spacing and guillemets
scripts/ai_tells.py       the checker, stdlib, offline
examples/                 machine and human texts for testing
```

## Limits

The script measures surface. It cannot tell that a phrase sits in quotation marks as an example, and it does not know that the file in front of it is an instruction where an even tone is required. That is why it marks rather than judges.

People distinguish machine text from human text barely better than chance (PLOS ONE, 2025), detectors err in both directions, and human writing has absorbed some machine habits since 2023. One tell proves nothing. The pattern does.

## Scope note

The Russian and English lists come from published field guides. The German, Spanish and French lists are compiled from observed model output: they are the same English habits translated, not corpus measurements. If you publish something built on them, say so.

## License

MIT, except `examples/`, which are just examples written for this repository.
