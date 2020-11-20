# texte
Ceci est une tentative de créer un logiciel d'assistance à la production d'un roman. Il s'agit donc d'utiliser ici le code comme ouvroir de littérature potentiel, de créer une littérature qui en produit d'autres, aléatoirement ou selon des contraintes fixées dans des algorithmes.

Précédents

Les Cent mille milliards de poèmes de Raymond Queneau avaient été adaptés sous forme informatique par Dmitri Starynkevitch en 1961. Mais la dimension entièrement aléatoire du procédé informatique avait d'abord repoussé les Oulipiens. Une autre adaptation informatique de Cent mille milliards de poèmes dont le générateur était basé sur le nom de la personne qui lançait l'application avait été mieux reconnue par le groupe. Natalie Berkman écrit un [article intéressant à ce sujet](http://digitalhumanities.org/dhq/vol/11/3/000325/000325.html).

Plutôt que la littérature "potentielle", les algorithmes permettent une forme de littérature "exponentielle", telle qu'évoquée [ici](http://nt2.uqam.ca/en/repertoire/machines-ecrire-0). Parmi les exemples concrets et actifs de cette littérature exponentielle algorithmique, il est possible d'évoquer la version robot de dril sur [Twitter](https://twitter.com/dril_gpt2).

Approche

L'idée est d'élaborer un corpus d'environ 15'000 vocables. Ce nombre a été choisi à la louche, en considérant les statistiques de vocables de piliers ronflants de la littérature française. C'est un nombre empiriquement suffisant pour garantir une œuvre si ce programme se mettait à fonctionner un jour. Ce répertoire de vocables est réparti entre des lexiques de différentes fonctions syntaxiques. Les détails sont à voir dans le dépôt, mais je parle ici de verbes, de substantifs, d'adverbes, d'adjectifs, etc.

Il s'agit ensuite de créer un moteur à générer des phrases - de différentes variétés, avec différentes contraintes. À ce générateur de phrases, s'ajoute un générateur de chapitres qui répète un certain nombre de fois le générateur de phrases selon certaines contraintes. Par exemple, il générera 1000 phrases différentes avec une moyenne de 5 mots, offrant au lecteur un chapitre de roman.
