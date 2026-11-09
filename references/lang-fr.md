# French

Compiled from observed model output, not from a published field guide. The structural catalogue in `patterns.md` applies unchanged; this file covers what French does with the same habits.

## Stock phrases

- Dans le monde d'aujourd'hui, à l'ère du numérique, de nos jours, dans la société actuelle
- il est important de noter, il convient de souligner, force est de constater, il est essentiel de
- non seulement... mais aussi
- joue un rôle crucial / clé / essentiel, s'inscrit dans, témoigne de, met en lumière
- un élément incontournable, un pilier essentiel, une partie intégrante
- véritable, authentique, riche, incontournable, remarquable
- En effet, Par ailleurs, De plus, En outre, En conclusion, Pour résumer, En définitive

> Before: Dans le monde d'aujourd'hui, la lecture joue un rôle essentiel. Il est important de noter qu'elle ne se limite pas au vocabulaire.
> After: Un enfant qui lit vingt minutes par jour apprend environ mille mots nouveaux par an.

## Nominalisation

French already prefers nouns. The machine version stacks them: "la mise en place de la mise à jour de la politique de gestion des accès".

> Before: La réalisation d'une analyse des besoins permet l'optimisation des processus internes.
> After: L'analyse des besoins a réduit le délai de traitement de trois jours à un.

## The -ant rider

French's version of the English -ing tail: ", permettant de...", ", offrant...", ", garantissant...", ", favorisant...", ", contribuant à...". Same grammar, same machine signature.

> Before: La plateforme centralise les données, permettant une meilleure prise de décision et favorisant la transparence.
> After: La plateforme réunit les données des trois services dans un seul tableau. Le responsable voit où en est chaque demande.

## Anglicisms that mark a translation

- "basé sur" where French wants "fondé sur", "à partir de", "d'après"
- "au niveau de" as a universal connector (English "at the level of"); French uses "en matière de", "pour ce qui est de", "dans le domaine de"
- "réaliser" for "to realise" in the sense of noticing; the French is "se rendre compte"
- "supporter" for software support; French uses "prendre en charge", "être compatible avec"
- "adresser un problème" (English "address a problem"); French uses "résoudre", "traiter"
- "délivrer" for delivering value; French prefers "apporter"

## Typography

- Guillemets « ... » with a narrow no-break space inside. English “...” in French text is the clearest single sign of a model that was not told which language it was writing.
- A space before : ; ! ? and inside the guillemets. Typing "Bonjour!" instead of "Bonjour !" is an English habit and looks wrong at once.
- Decimal comma: "3,5". Thousands separated by a space: "10 000".
- Months and days lowercase: "lundi", "janvier".
- Accented capitals where the word needs them: "À", "É". A model that writes "A noter" instead of "À noter" reveals the keyboard it learned on.
- No Oxford comma; "et" closes the list.
- Numbers and units: "10 kg" with a space, "20 %" with a space in French.

## Register

"vous" and "tu" are not interchangeable, and a text that switches was assembled. Business and documentation French uses "vous"; a personal post may use "tu", but only one of them per text.
