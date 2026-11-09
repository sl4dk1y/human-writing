#!/usr/bin/env python3
"""Measure the usual tells of machine-written prose in a text file.

    python3 ai_tells.py FILE [--lang ru|en|de|es|fr|auto] [--json]

Prints counts against rough human reference ranges. No dependencies, no
network, no model call. Code, URLs, quotations and blockquotes are stripped
before measuring, because a guide about tells would otherwise flag its own
examples.

The thresholds are heuristics built from published corpora (see
references/evidence.md), not laws. Russian uses the dash as ordinary grammar,
so its dash thresholds are far looser than the Latin-script ones.
"""

import json
import re
import statistics
import sys

# ---------------------------------------------------------------- lexicons

EN_TELLS = [
    r"\bdelve[sd]?\b", r"\bdelving\b", r"\btapestry\b", r"\bintricate\b",
    r"\bintricacies\b", r"\bpivotal\b", r"\bseamless(ly)?\b",
    r"\bleverage\b", r"\bunderscore[sd]?\b", r"\bunderscoring\b",
    r"\bshowcas(e|es|ing)\b", r"\btestament to\b", r"\bever-evolving\b",
    r"\bever-changing\b", r"\bin today'?s\b", r"\bfast-paced\b",
    r"\bnavigat(e|ing) the\b", r"\bunlock(ing)? the\b", r"\belevate\b",
    r"\bempower(s|ing)?\b", r"\bfoster(s|ing)?\b", r"\bcrucial\b",
    r"\bparamount\b", r"\bmeticulous(ly)?\b", r"\bmyriad\b",
    r"\bplethora\b", r"\bvibrant\b", r"\bnestled\b", r"\bgroundbreaking\b",
    r"\brenowned\b", r"\bmust-visit\b", r"\bstunning\b", r"\bbreathtaking\b",
    r"\bgame-chang(er|ing)\b", r"\bcutting-edge\b", r"\bstate-of-the-art\b",
    r"\bit'?s worth noting\b", r"\bimportant to note\b",
    r"\bit is important to\b", r"\bneedless to say\b",
    r"\bthat said,", r"\bmoreover\b", r"\bfurthermore\b", r"\badditionally\b",
    r"\bin conclusion\b", r"\bto sum up\b", r"\bin summary\b", r"\boverall,",
    r"\blet'?s dive\b", r"\blet'?s explore\b", r"\bhere'?s what you need to know\b",
    r"\bdive into\b", r"\bin the realm of\b", r"\bthe world of\b",
    r"\bplays? a (key|vital|crucial|significant) role\b",
    r"\ba testament\b", r"\bstands? as\b", r"\bserves? as\b",
    r"\brich (cultural|history|heritage)\b", r"\bstoried\b",
    r"\bleaves? (a )?(lasting|indelible)\b",
    r"\bpaves? the way\b", r"\bsheds? light\b", r"\bbeacon of\b",
    r"\bwhen it comes to\b", r"\bat the end of the day\b",
    r"\bnot (just|only|merely)\b[^.!?]{0,80}\bbut\b",
    r"\bisn'?t (just|only|merely)\b[^.!?]{0,80}\bit'?s\b",
    r"\bless (like|about)\b[^.!?]{0,60}\bmore (like|about)\b",
    r"\brather than\b", r"\bnot simply\b", r"\bnot merely\b",
    r"\bwhether you'?re\b", r"\bwhether you are\b",
    r"\bexperts (say|argue|believe|note)\b",
    r"\bstudies (show|suggest|have shown)\b",
    r"\bcan vary depending\b", r"\bvaries depending\b",
    r"\bi hope this helps\b", r"\bhope (this|that) helps\b",
    r"\bgreat question\b", r"\byou'?re absolutely right\b",
    r"\blet me know if\b", r"\bfeel free to\b",
    r"\bas an ai\b", r"\blanguage model\b",
    r"\bmy (training|knowledge) (data|cutoff)\b",
    r"\bas of (my|the) (last|latest)\b",
]

RU_TELLS = [
    r"\bважно (отметить|подчеркнуть|учитывать|понимать)\b",
    r"\b(стоит|следует) (отметить|подчеркнуть|учесть|обратить внимание)\b",
    r"\bнеобходимо (отметить|подчеркнуть|учитывать)\b",
    r"\bкрайне важно\b", r"\bключев(ой|ая|ое|ые|ую|ым)\b",
    r"\bиграет (важную|ключевую|значительную|решающую|центральную) роль\b",
    r"\bиграют (важную|ключевую|значительную|решающую) роль\b",
    r"\bвыступает (как|в качестве|символом|свидетельством|примером)\b",
    r"\bявляется (важным|ключевым|неотъемлемой|основой|символом)\b",
    r"\bслужит (напоминанием|символом|примером|свидетельством)\b",
    r"\bсимволизирует\b", r"\bолицетворяет\b", r"\bвоплощает\b",
    r"\bподчёркивает\b", r"\bподчеркивает\b", r"\bотражает\b",
    r"\bдемонстрирует\b", r"\bсвидетельствует о\b",
    r"\bспособствует\b", r"\bсодействует\b", r"\bобеспечивает\b",
    r"\bнеизгладимый след\b", r"\bбогатое (культурное|историческое) наследие\b",
    r"\bбогат(а|ый|ое|ые) (культурой|историей|традициями)\b",
    r"\bзахватывающ\w+\b", r"\bпотрясающ\w+\b", r"\bуникальн\w+\b",
    r"\bв самом сердце\b", r"\bжемчужин\w+\b",
    r"\bмногогранн\w+\b", r"\bнеотъемлем\w+\b", r"\bкомплексн\w+\b",
    r"\bданный (подход|метод|текст|случай|факт)\b",
    r"\bданная (тема|проблема|работа)\b",
    r"\bв современном мире\b", r"\bв наше время\b",
    r"\bв заключение\b", r"\bподводя итог\b", r"\bтаким образом\b",
    r"\bв целом,", r"\bвкратце\b", r"\bрезюмируя\b",
    r"\bследует помнить\b", r"\bважно помнить\b", r"\bне стоит забывать\b",
    r"\bзначения могут (варьироваться|различаться)\b",
    r"\bне (только|просто|лишь)\b[^.!?]{0,90}\b(а|но) (также|и)\b",
    r"\bне (только|просто|лишь)\b[^.!?]{0,90}, (это|а)\b",
    r"\bэто не просто\b[^.!?]{0,60}, это\b",
    r"\bот \w+ до \w+\b",
    r"\bпо состоянию на\b", r"\bна момент (написания|обновления|моего обучения)\b",
    r"\bв предоставленных (источниках|результатах)\b",
    r"\bпо (имеющейся|доступной) информации\b",
    r"\bключевые (выводы|аспекты|моменты|факторы)\b",
    r"\bосновные (выводы|аспекты|моменты|факторы)\b",
    r"\bдинамично развивающ\w+\b", r"\bстремительно (меняющ|развивающ)\w+\b",
    r"\bширокий спектр\b", r"\bцелый ряд\b",
    r"\bряд (факторов|причин|особенностей)\b",
    r"\bв рамках (данного|этого)\b",
    r"\bявляется (одним|одной) из\b",
    r"\bне секрет, что\b", r"\bкак известно\b",
    r"\bнадеюсь, (это|что) (помогло|поможет)\b",
    r"\bдайте (мне )?знать\b", r"\bсообщите мне\b",
    r"\bотличный вопрос\b", r"\bвы абсолютно правы\b",
]

DE_TELLS = [
    r"\bin der heutigen\b", r"\bin einer zunehmend\w*\b", r"\bim zeitalter\b",
    r"\bspielt eine (entscheidende|zentrale|wichtige|wesentliche) rolle\b",
    r"\bes ist wichtig zu (beachten|betonen|erwähnen)\b",
    r"\bes ist anzumerken\b", r"\bes gilt zu bedenken\b",
    r"\bunterstreicht\b", r"\bverdeutlicht\b", r"\bspiegelt? wider\b",
    r"\bzeugt von\b", r"\bbildet die grundlage\b",
    r"\bein wesentlicher bestandteil\b", r"\bein zentraler baustein\b",
    r"\bganzheitlich\w*\b", r"\bnahtlos\w*\b", r"\binnovativ\w*\b",
    r"\beinzigartig\w*\b", r"\bvielfältig\w*\b", r"\bbeeindruckend\w*\b",
    r"\bzudem\b", r"\bdarüber hinaus\b", r"\bferner\b",
    r"\bletztendlich\b", r"\banschließend lässt sich sagen\b",
    r"\bzusammenfassend\b", r"\bwodurch\b[^.!?]{0,80}\b(wird|werden)\b",
    r"\bverfügt über\b", r"\bzeichnet sich aus\b",
    r"\bermöglicht (eine|es)\b", r"\bvon großer bedeutung\b",
    r"\bim hinblick auf\b", r"\bim rahmen\b", r"\bmittels\b",
    r"\bich hoffe, das hilft\b", r"\bgerne weiterhelfen\b",
]

ES_TELLS = [
    r"\ben el mundo actual\b", r"\bhoy en día\b", r"\ben la era digital\b",
    r"\ben la sociedad actual\b", r"\bes importante (destacar|señalar|notar)\b",
    r"\bcabe (mencionar|señalar|destacar)\b", r"\bconviene recordar\b",
    r"\bno solo\b[^.!?]{0,80}\bsino también\b",
    r"\bjuega un papel (crucial|fundamental|clave|importante)\b",
    r"\bresulta fundamental\b", r"\bse erige como\b",
    r"\brepresenta un hito\b", r"\bun antes y un después\b",
    r"\bpone en valor\b", r"\bun elemento esencial\b",
    r"\buna parte integral\b", r"\bun pilar fundamental\b",
    r"\bsumamente\b", r"\baltamente\b", r"\bverdaderamente\b",
    r"\bsin duda\b", r"\basimismo\b", r"\bpor otro lado\b",
    r"\ben conclusión\b", r"\ben resumen\b", r"\bpara finalizar\b",
    r"\ben definitiva\b", r"\ba nivel de\b", r"\bde cara a\b",
    r"\ben aras de\b", r"\bcon el objetivo de\b",
    r"\bproporciona una solución\b", r"\bbrinda\b", r"\bconstituye\b",
    r"\bespero que (esto )?(ayude|sirva)\b", r"\bno dudes en\b",
]

FR_TELLS = [
    r"\bdans le monde d'aujourd'hui\b", r"\bà l'ère du numérique\b",
    r"\bde nos jours\b", r"\bdans la société actuelle\b",
    r"\bil est important de (noter|souligner|préciser)\b",
    r"\bil convient de (souligner|noter|rappeler)\b",
    r"\bforce est de constater\b", r"\bil est essentiel de\b",
    r"\bnon seulement\b[^.!?]{0,80}\bmais aussi\b",
    r"\bjoue un rôle (crucial|clé|essentiel|important)\b",
    r"\bs'inscrit dans\b", r"\btémoigne de\b", r"\bmet en lumière\b",
    r"\bun élément incontournable\b", r"\bune partie intégrante\b",
    r"\bun pilier essentiel\b", r"\bvéritable\b", r"\bauthentique\b",
    r"\bincontournable\b", r"\bremarquable\b",
    r"\ben effet,\b", r"\bpar ailleurs\b", r"\bde plus,\b",
    r"\ben outre\b", r"\ben conclusion\b", r"\bpour résumer\b",
    r"\ben définitive\b", r"\bau niveau de\b", r"\bbasé sur\b",
    r"\bpermet(tant)? de\b", r"\boffrant\b", r"\bgarantissant\b",
    r"\bfavorisant\b", r"\bcontribuant à\b",
    r"\bj'espère que cela (vous )?aidera\b", r"\bn'hésitez pas à\b",
]

CLOSERS = {
    "en": [r"^in conclusion\b", r"^in summary\b", r"^to sum up\b",
           r"^overall,", r"^ultimately,", r"^at the end of the day\b",
           r"^the real win\b", r"^that (distinction|difference) matters\b",
           r"^this (shows|highlights|underscores)\b"],
    "ru": [r"^в заключение\b", r"^подводя итог\b", r"^таким образом\b",
           r"^в итоге\b", r"^в целом\b", r"^именно поэтому\b",
           r"^это (показывает|подчёркивает|подчеркивает)\b"],
    "de": [r"^zusammenfassend\b", r"^abschließend\b", r"^letztendlich\b",
           r"^insgesamt\b", r"^fazit:"],
    "es": [r"^en conclusión\b", r"^en resumen\b", r"^para finalizar\b",
           r"^en definitiva\b", r"^al final del día\b"],
    "fr": [r"^en conclusion\b", r"^pour résumer\b", r"^en définitive\b",
           r"^au final\b", r"^en somme\b"],
}

OPENERS = {
    "en": [r"^let'?s\b", r"^here'?s\b", r"^so,", r"^look,", r"^honestly,",
           r"^the thing is\b", r"^it'?s worth (noting|mentioning)\b"],
    "ru": [r"^давайте\b", r"^итак,", r"^смотрите,", r"^честно говоря,",
           r"^начнём с того\b", r"^начнем с того\b", r"^стоит сказать\b"],
    "de": [r"^lassen sie uns\b", r"^werfen wir\b", r"^schauen wir\b",
           r"^beginnen wir\b"],
    "es": [r"^vamos a\b", r"^veamos\b", r"^empecemos\b", r"^hablemos de\b"],
    "fr": [r"^plongeons\b", r"^voyons\b", r"^commençons\b", r"^examinons\b"],
}

# Stopwords are used only to pick a language; short and unambiguous on purpose.
STOPWORDS = {
    "en": {"the", "and", "that", "with", "this", "from", "have", "which", "not", "you"},
    "de": {"der", "die", "das", "und", "nicht", "mit", "sich", "auch", "eine", "wird"},
    "es": {"el", "la", "los", "las", "que", "una", "para", "con", "por", "como"},
    "fr": {"le", "la", "les", "des", "une", "pour", "dans", "avec", "est", "que"},
    "ru": {"и", "не", "что", "как", "это", "для", "все", "она", "они", "был"},
}

# Dash thresholds per 1000 words: (watch, tell). Russian needs its own scale
# because the dash is required grammar there.
DASH = {"ru": (3.0, 6.0), "de": (1.5, 3.0), "fr": (1.5, 3.0),
        "es": (0.8, 1.6), "en": (0.5, 1.0)}

TELLS = {"en": EN_TELLS, "ru": RU_TELLS, "de": DE_TELLS,
         "es": ES_TELLS, "fr": FR_TELLS}

# ---------------------------------------------------------------- helpers

CODE_FENCE = re.compile(r"```.*?```", re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")
URL = re.compile(r"https?://\S+")
WORD = re.compile(
    r"[A-Za-zÀ-ÖØ-öø-ÿА-Яа-яЁё0-9]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿА-Яа-яЁё0-9]+)*")
QUOTED = re.compile(r"«[^»\n]*»|\"[^\"\n]{2,200}\"|„[^“”\n]*[“”]|[“”][^“”\n]{2,200}[“”]")
BLOCKQUOTE = re.compile(r"^\s*>.*$", re.M)


def strip_code(text):
    return INLINE_CODE.sub(" ", CODE_FENCE.sub(" ", text))


def mask_quotes(text):
    """Blank out quoted speech and blockquotes, keeping offsets intact.

    A guide about AI tells quotes the tells. Measuring a quotation as if the
    author had written it turns the report into noise, so quoted material is
    replaced with spaces of the same length before the phrase lists run.
    """
    text = BLOCKQUOTE.sub(lambda m: " " * len(m.group(0)), text)
    return QUOTED.sub(lambda m: " " * len(m.group(0)), text)


def sentences(text):
    parts = re.split(r"(?<=[.!?…])\s+|\n{2,}", text)
    return [p.strip() for p in parts if len(WORD.findall(p)) >= 2]


def per_k(value, words):
    return 0.0 if not words else value * 1000.0 / words


def is_emoji(ch):
    o = ord(ch)
    return (0x1F300 <= o <= 0x1FAFF) or (0x2600 <= o <= 0x27BF) or o in (0x2B50, 0x1F004)


def count_hits(text, patterns):
    """Find every lexicon match once, even when two patterns overlap."""
    seen = set()
    hits = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.I | re.M):
            key = (m.start(), m.end())
            if key in seen:
                continue
            seen.add(key)
            line = text.count("\n", 0, m.start()) + 1
            hits.append((line, m.group(0).strip(), pat))
    hits.sort()
    return hits


def detect_lang(text):
    lowered = text.lower()
    cyrillic = len(re.findall(r"[а-яё]", lowered))
    latin = len(re.findall(r"[a-z]", lowered))
    if cyrillic > latin:
        return "ru"
    words = set(WORD.findall(lowered))
    scored = {lang: len(words & sw) for lang, sw in STOPWORDS.items() if lang != "ru"}
    best = max(scored, key=scored.get)
    return best if scored[best] > 0 else "en"


# ---------------------------------------------------------------- analysis

def analyse(raw, lang="auto"):
    text = strip_code(URL.sub(" ", raw))
    if lang == "auto":
        lang = detect_lang(text)
    if lang not in TELLS:
        lang = "en"

    words = WORD.findall(text)
    nwords = len(words)
    sents = sentences(text)
    lens = [len(WORD.findall(s)) for s in sents] or [0]

    lines = [l for l in text.split("\n") if l.strip()]
    bold = len(re.findall(r"\*\*[^*]+\*\*", text)) + len(re.findall(r"__[^_]+__", text))
    headers = len([l for l in lines if re.match(r"^\s{0,3}#{1,6}\s", l)])
    bullets = len([l for l in lines if re.match(r"^\s*([-*+•]|\d+[.)])\s+", l)])
    tables = len([l for l in lines if l.count("|") >= 2])

    dashes = text.count("—") + text.count("–")
    paired_dashes = len(re.findall(r"—[^—\n]{1,80}—", text))
    hyphens_as_dash = len(re.findall(r"\s--?\s", text))
    colons = len(re.findall(r":", text))
    semis = text.count(";")
    exclaims = text.count("!")
    questions = text.count("?")
    parens = len(re.findall(r"\([^)\n]{3,}\)", text))
    curly = len(re.findall(r"[“”]", text))

    pronouns = {
        "ru": (r"\b(я|меня|мне|мой|моя|мы|нас|наш)\b",
               r"\b(ты|тебя|тебе|твой|вы|вас|вам|ваш)\b"),
        "en": (r"\b(I|me|my|we|us|our)\b", r"\b(you|your)\b"),
        "de": (r"\b(ich|mich|mir|mein|wir|uns)\b",
               r"\b(du|dich|dir|dein|ihr|euch)\b"),
        "es": (r"\b(yo|me|mi|nosotros|nos)\b",
               r"\b(tú|te|tu|ti|ustedes|vosotros)\b"),
        "fr": (r"\b(je|me|moi|nous)\b", r"\b(tu|toi|vous|votre)\b"),
    }[lang]
    first_person = len(re.findall(pronouns[0], text, re.I))
    second_person = len(re.findall(pronouns[1], text, re.I))
    contractions = len(re.findall(r"\b\w+'(s|t|re|ll|ve|d|m)\b", text))

    sent_std = statistics.pstdev(lens) if len(lens) > 2 else 0.0
    uniq = len({w.lower() for w in words})
    ttr = uniq / nwords if nwords else 0.0

    masked = mask_quotes(text)
    phrase_hits = count_hits(masked, TELLS[lang])
    closers = count_hits(masked, CLOSERS[lang])
    openers = count_hits(masked, OPENERS[lang])

    emoji = sum(1 for c in text if is_emoji(c))

    def level(value, watch, tell, reverse=False):
        if reverse:
            return "tell" if value <= tell else ("watch" if value <= watch else "ok")
        return "tell" if value >= tell else ("watch" if value >= watch else "ok")

    dash_watch, dash_tell = DASH[lang]
    # Rhythm measures need volume to mean anything: on a few hundred words the
    # spread of sentence lengths varies as much inside one author as between
    # authors, so below this size they are reported but never judged.
    enough = nwords >= 200 and len(sents) >= 12
    checks = [
        ("dash", per_k(dashes, nwords), "per 1000 words",
         level(per_k(dashes, nwords), dash_watch, dash_tell)),
        ("paired dashes", per_k(paired_dashes, nwords), "per 1000 words",
         level(per_k(paired_dashes, nwords), 0.6, 1.2)),
        ("bold", per_k(bold, nwords), "per 1000 words",
         level(per_k(bold, nwords), 1.5, 3.0)),
        ("headings", per_k(headers, nwords), "per 1000 words",
         level(per_k(headers, nwords), 1.5, 3.0)),
        ("list items", per_k(bullets, nwords), "per 1000 words",
         level(per_k(bullets, nwords), 4.0, 8.0)),
        ("sentence length sd", sent_std, "words",
         level(sent_std, 6.0, 4.5, reverse=True) if enough else "soft"),
        ("mean sentence", statistics.fmean(lens), "words",
         level(statistics.fmean(lens), 26, 30) if enough else "soft"),
        ("phrases", len(phrase_hits), "hits", level(len(phrase_hits), 2, 4)),
        ("closers", len(closers), "hits", level(len(closers), 1, 2)),
        ("staged openers", len(openers), "hits", level(len(openers), 1, 2)),
        # Rarer exclamation marks and asides hint at machine prose, but plenty
        # of human writing has none of either, so these never count as tells.
        ("exclamation", per_k(exclaims, nwords), "per 1000 words (soft)", "soft"),
        ("parentheses", per_k(parens, nwords), "per 1000 words (soft)", "soft"),
        ("emoji", emoji, "chars", level(emoji, 1, 3)),
    ]

    return {
        "lang": lang,
        "words": nwords,
        "sentences": len(sents),
        "dash_per_k": round(per_k(dashes, nwords), 2),
        "paired_dash_per_k": round(per_k(paired_dashes, nwords), 2),
        "hyphen_dash": hyphens_as_dash,
        "colon_per_k": round(per_k(colons, nwords), 2),
        "semicolon_per_k": round(per_k(semis, nwords), 2),
        "exclaim_per_k": round(per_k(exclaims, nwords), 2),
        "paren_per_k": round(per_k(parens, nwords), 2),
        "question_per_k": round(per_k(questions, nwords), 2),
        "curly_quotes": curly,
        "bold_per_k": round(per_k(bold, nwords), 2),
        "headings_per_k": round(per_k(headers, nwords), 2),
        "list_per_k": round(per_k(bullets, nwords), 2),
        "tables": tables,
        "emoji": emoji,
        "mean_sent": round(statistics.fmean(lens), 1),
        "sd_sent": round(sent_std, 1),
        "min_sent": min(lens) if lens else 0,
        "max_sent": max(lens) if lens else 0,
        "ttr": round(ttr, 3),
        "first_person": first_person,
        "second_person": second_person,
        "contractions": contractions,
        "checks": [(name, round(float(v), 2), unit, lvl) for name, v, unit, lvl in checks],
        "phrases": phrase_hits,
        "closers": closers,
        "openers": openers,
    }


def report(a):
    print(f"language {a['lang']} · {a['words']} words · {a['sentences']} sentences")
    print(f"rhythm: mean {a['mean_sent']} words, sd {a['sd_sent']}, "
          f"range {a['min_sent']}-{a['max_sent']}")
    print(f"tells: {sum(1 for c in a['checks'] if c[3] == 'tell')} strong, "
          f"{sum(1 for c in a['checks'] if c[3] == 'watch')} borderline\n")

    marks = {"tell": "!!", "watch": " ~", "ok": "  ", "soft": " ·"}
    for name, value, unit, lvl in a["checks"]:
        print(f"{marks[lvl]} {name:<18} {value:>7} {unit}")

    print()
    for label in ("phrases", "closers", "openers"):
        if a[label]:
            print(f"{label}:")
            for line, hit, _ in a[label][:40]:
                print(f"   line {line:>4}: {hit[:80]}")
    print(f"\ninformality: first person {a['first_person']}, second person "
          f"{a['second_person']}, contractions {a['contractions']}, "
          f"exclamations {a['exclaim_per_k']}/1k, asides {a['paren_per_k']}/1k")


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    lang = "auto"
    as_json = "--json" in argv
    if "--lang" in argv:
        lang = argv[argv.index("--lang") + 1]
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    a = analyse(raw, lang)
    if as_json:
        print(json.dumps(
            {k: v for k, v in a.items()
             if k not in ("checks", "phrases", "closers", "openers")},
            ensure_ascii=False, indent=2))
    else:
        report(a)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
