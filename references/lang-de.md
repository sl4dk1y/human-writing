# German

Compiled from observed model output, not from a published field guide. Treat these as the English habits translated into German, which is what they mostly are. The structural catalogue in `patterns.md` applies unchanged.

## Nominal style

German academic prose already loves nouns, so the tell is not nominalisation as such but the machine version of it: verbs replaced by `-ung` nouns plus a light verb, in every sentence.

- "die Durchführung einer Analyse vornehmen" instead of "analysieren"
- "ermöglicht eine Verbesserung" instead of "macht es besser"
- "erfolgt eine Bewertung" instead of "wird bewertet"
- "leistet einen Beitrag zur Steigerung" instead of "steigert"

> Before: Die Einführung des neuen Systems ermöglicht eine Optimierung der internen Abläufe.
> After: Das neue System verkürzt die Bearbeitung von drei Tagen auf einen.

## Stock phrases

- In der heutigen schnelllebigen Welt, in einer zunehmend digitalisierten Welt, im Zeitalter der Digitalisierung
- spielt eine entscheidende / zentrale / wichtige Rolle
- es ist wichtig zu beachten, es ist anzumerken, es gilt zu bedenken
- nicht nur... sondern auch
- unterstreicht, verdeutlicht, spiegelt wider, zeugt von, bildet die Grundlage für
- ein wesentlicher Bestandteil, ein zentraler Baustein
- ganzheitlich, nahtlos, innovativ, einzigartig, vielfältig, beeindruckend
- Zudem, Darüber hinaus, Ferner, Letztendlich, Abschließend lässt sich sagen, Zusammenfassend
- "wodurch ... ermöglicht wird" is the German -ing rider: an appended clause that adds evaluation rather than fact

> Before: Die Plattform spielt eine zentrale Rolle und unterstreicht die Bedeutung datengetriebener Entscheidungen.
> After: Auf der Plattform stehen die Zahlen aller drei Abteilungen in einer Tabelle.

## Copula avoidance

"stellt ... dar", "bildet ... ab", "verfügt über", "zeichnet sich aus durch" where "ist" or "hat" would be clearer and shorter.

> Before: Die Stadt verfügt über eine vielfältige Kulturszene und zeichnet sich durch ein breites Veranstaltungsangebot aus.
> After: Die Stadt hat drei Theater, zwei Clubs und im Sommer ein Festival.

## Typography

These are the marks that give away an English-trained model in German text.

- Quotation marks: German uses „so“ or »so«. English “...” inside German text is an instant sign, and it survives because the model reproduces whatever the prompt used.
- The Gedankenstrich takes spaces: "Das ist – wie gesagt – nicht neu." An unspaced em dash is English.
- ß vs ss: Swiss German has no ß. Mixing Swiss and German conventions in one document is a translation artifact.
- Compounds are written together: "Kundenservice", not "Kunden Service". Models insert spaces when they translated the English phrase.
- "z. B.", "d. h.", "u. a." keep a space after the abbreviation.
- Dates as "09.11.2026", not "11/09/2026".
- Capitalised nouns. A model imitating English lowercases them occasionally, and it looks wrong immediately.

## Register

German business writing is formal, so "du" vs "Sie" inconsistency is the tell, not formality itself. A text that starts with "Sie" and slips into "du" three paragraphs later was assembled from several generations.
