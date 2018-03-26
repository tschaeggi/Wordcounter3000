import string
import operator

STOPWORDS = {'der', 'die', 'das', 'aus', 'in', 'eine', 'und', 'ich', 'sein', 'nach', 'ein', 'wie', 'zu', 'ihr',
                'von', 'um', 'haben', 'aber', 'werden', 'so', 'mit', 'jahr', 'an', 'nur', 'noch', 'auf', 'über', 'sich',
                'wir', 'für', 'viel', 'nicht', 'man', 'es', 'oder', 'sie', 'vor', 'er', 'müssen', 'auch', 'all', 'als',
                'sollen', 'bei', 'kein', 'dies', 'bis', 'dass', 'sagen', 'können', 'wollen', 'jahr', 'neu', 'werden',
                'land', 'machen', 'uhr', 'haben', 'alt', 'gehen', 'prozent', 'gross', 'sein', 'hoch', 'stehen',
                'können', 'ende', 'jung', 'lassen', 'viel', 'müssen', 'nahe', 'sehen', 'sollen', 'finden', 'gut',
                'sagen', 'seite', 'lang', 'bleiben', 'weit', 'geben', 'vergangen', 'liegen', 'klein', 'kommen', 'leben',
                'wenig', 'dürfen', 'eigen', 'wollen', 'ganz', 'stellen', 'haben', 'lang', 'machen', 'klein', 'sein',
                'jung', 'geben', 'hand', 'werden', 'blick', 'weit', 'auge', 'gut', 'den', 'ist', 'des', 'im', 'dem',
                'hat', 'sind', 'sei', 'war', 'einem', 'wird', 'wenn', 'sagt', 'am', 'einer', 'einen', 'mehr', 'zum',
                'diese', 'gegen', 'habe', 'zur', 'sagte', 'hatte', 'nun', 'keine', 'unter', 'seit', 'damit', 'seien',
                'will', 'soll', 'kann', 'wurde', 'ihre', 'vom', 'bereits', 'gibt', 'jedoch', 'weiterhin', 'wegen',
                'geht', 'hätten', 'allerdings', '', 'derselben', 'allen', 'ja', 'eben', 'wieder', 'ersten', 'einiges', 'ins', 'offen', 'welche',
             'hattest', 'ohne', 'zu', 'ihrem', 'weiteres', 'jenem', 'darin', 'anders', 'richtig', 'na', 'u', 'wahr?',
             'viel', 'sechste', 'rund', 'fünfte', 'zwölf', 'gott', 'geschweige', 'bei', 'gut', 'durften', 'sowie',
             'ging', 'grosses', 'manchem', 'dritten', 'jener', 'und?', 'lang', 'einmal', 'machte', 'wenn', 'meiner',
             'ganze', 'vielleicht', 'unsen', 'diesen', 'etwa', 'wäre', 'hinter', 'los', 'zweite', 'ganzes', 'solche',
             'manchen', 'soll', 'wenigstens', 'zwischen', 'erste', 'solang', 'wollten', 'endlich', 'zwei', 'jetzt',
             'außer', 'dieselben', 'demgemäss', 'etwas', 'davon', 'können', 'bekannt', 'gehen', 'ausserdem', 'mussten',
             'danach', 'sollst', 'grosser', 'der', 'gute', 'wessen', 'auch', 'ach', 'uhr', 'daran', 'daneben', 'kann',
             'dem', 'seinem', 'alles', 'jemanden', 'zum', 'mag', 'c', 'solchen', 'l', 'solchem', 'ihr', 'sind', 'achte',
             'gedurft', 'worden', 'deines', 'könnt', 'trotzdem', 'rechte', 'werden', 'zwanzig', 'besser', 'gehabt',
             'wirklich', 'diejenigen', 'jeden', 'keines', 'neue', 'nicht', 'währenddessen', 'konnten', 'kommen',
             'seien', 'unse', 'darauf', 'ab', 'ganzer', 'dessen', 'sie', 'muß', 'meinem', 'neun', 'müßt', 'anderer',
             'sechs', 'vor', 'dürft', 'wie', 'nie', 'a', 'zugleich', 'zehnter', 'd', 'einem', 'er', 'will', 'i',
             'denselben', 'für', 'darfst', 'steht', 'großer', 'meines', 'siebentes', 'damals', 'dieser', 'gross',
             'würden', 'wer', 'zehnten', 'weg', 'acht', 'gar', 'warst', 'b', 'achter', 'jedem', 'bin', 'früher',
             'dementsprechend', 'damit', 'großen', 'es', 'q', 'später', 'niemandem', 'achten', 'besonders', 'eigenen',
             'natürlich', 'übrigens', 'zeit', 'dies', 'andern', 'aus', 'ei,', 'ihres', 'seiner', 'euren', 'eine', 'hin',
             'ob', 'dein', 'was', 'eurem', 'wurde', 'haben', 'schluss', 'erster', 'dir', 'j', 'eigenes', 'und', 'sei',
             'fünf', 'außerdem', 'soweit', 'entweder', 'seit', 'seine', 'r', 'sieben', 'über', 'mögt', 'zehn',
             'einigem', 'ordnung', 'indem', 'solcher', 'tage', 'vierten', 'große', 'hätte', 'habt', 'dort', 'her',
             'unter', 'mir', 'daher', 'wird', 'meinen', 'darunter', 'in', 'dazu', 'macht', 'dahin', 'vergangenen',
             'dermassen', 'seines', 'wenige', 'heisst', 'ei', 'welcher', 'demzufolge', 'jedermanns', 'konnte',
             'weniges', 'allerdings', 'demselben', 'wollt', 'hab', 'viertes', 'dann', 'kaum', 'derjenige', 'gutes',
             'deinen', 'eurer', 'zuerst', 'd.h', 'sagte', 'derer', 'kurz', 'niemand', 'zweiten', 'wurden', 'ich',
             'unserer', 'dich', 'dafür', 'neunter', 'meine', 'wieso', 'ebenso', 'mußt', 'werde', 'startseite', 'den',
             'tag', 'sich', 'gegenüber', 'bald', 'schlecht', 'sehr', 'z.b', 'je', 'n', 'derjenigen', 'muss', 'manches',
             'musst', 'das', 'x', 'gewesen', 'ein', 'unses', 'gemacht', 'p', 'jahr', 'seinen', 'unsere', 'dahinter',
             'auf', 'sollte', 'du', 'alle', 'fünfter', 'beide', 'die', 'währenddem', 'eure', 'jemand', 'jedes',
             'magst', 'morgen', 'anderem', 's', 'o', 'hier', 'mann', 'viele', 'wegen', 'gern', 'davor', 'grosse',
             'solches', 'jede', 'sollten', 'sollt', 'ganz', 'diesem', 'mal', 'aller', 'erstes', 'gleich', 'zehntes',
             'dadurch', 'so', 'siebente', 'einander', 'welchem', 'oft', 'nach', 'wir', 'mein', 'nein', 'gegen', 'dass',
             'bist', 'zweites', 'möglich', 'derselbe', 'weiteren', 'schon', 'überhaupt', 'dagegen', 'seid', 'w', 'war',
             'ende', 'jeder', 'andere', 'gab', 'uns', 'gewollt', 'waren', 'welchen', 'infolgedessen', 'durfte', 'woher',
             'wollte', 'ihnen', 'gekannt', 'irgend', 'drei', 'jemandem', 'y', 'mit', 'darum', 'jenes', 'seitdem',
             'mittel', 'fünftes', 'nachdem', 'erst', 'allem', 'siebenter', 'neuntes', 'durchaus', 'mehr', 'keiner',
             'euch', 'tritt', 'niemanden', 'zehnte', 'demgemäß', 'dank', 'vierte', 'sache', 'hast', 'vielen', 'unser',
             'einer', 'zwar', 'dazwischen', 'zusammen', 'habe', 'ihn', 'dasselbe', 'dasein', 'wollen', 'eigene',
             'einigen', 'ernst', 'unsem', 'ihrer', 'oder', 'deren', 'ag', 'beim', 'wohl', 'mensch', 'vom', 'könnte',
             'hoch', 'gerade', 'vielem', 'hätten', 'tun', 'jene', 'dieselbe', 't', 'machen', 'wirst', 'jenen',
             'keine', 'neuen', 'weil', 'oben', 'f', 'daraus', 'mahn', 'deine', 'jahren', 'sagt', 'während', 'z',
             'drittes', 'vier', 'ihre', 'wen', 'wohin', 'mögen', 'wissen', 'einiger', 'besten', 'darf', 'einen',
             'geworden', 'tel', 'keinem', 'eigener', 'denn', 'mochten', 'darüber', 'wann', 'dabei', 'neunten', 'man',
             'also', 'anderen', 'nahm', 'drin', 'keinen', 'wart', 'willst', 'hatte', 'rechten', 'neunte', 'diese',
             'ander', 'au', 'ist', 'dürfen', 'zur', 'demgegenüber', 'bereits', 'lieber', 'gemocht', 'selbst', 'kleinen',
             'wem', 'tat', 'weitere', 'würde', 'recht', 'deshalb', 'da', 'hattet', 'mich', 'gibt', 'deiner', 'immer',
             'ihren', 'aber', 'teil', 'kleiner', 'werdet', 'deswegen', 'dieses', 'menschen', 'kein', 'hat', 'sa',
             'deinem', 'großes', 'von', 'anderes', 'ehrlich', 'anderm', 'weniger', 'rechter', 'suche', 'allein',
             'zunächst', 'grossen', 'einig', 'sechstes', 'jedermann', 'an', 'statt', 'ihm', 'rechtes', 'möchte',
             'hatten', 'ausser', 'heute', 'daselbst', 'euer', 'beiden', 'musste', 'sechsten', 'nur', 'im', 'durch',
             'siebenten', 'folgende', 'ganzen', 'denen', 'zweiter', 'k', 'sondern', 'kommt', 'welches', 'g', 'm', 'am',
             'jahre', 'en', 'vierter', 'leide', 'bis', 'sein', 'jedoch', 'eigen', 'elf', 'weit', 'bisher', 'e',
             'müssen', 'groß', 'kam', 'dritte', 'dritter', 'mochte', 'desselben', 'einige', 'eines', 'nun', 'sollen',
             'allgemeinen', 'satt', 'daß', 'tagen', 'leicht', 'manche', 'kleine', 'gemusst', 'noch', 'lange', 'v',
             'weshalb', 'eins', 'achtes', 'nichts', 'weiter', 'fünften', 'diejenige', 'gesagt', 'doch', 'wenig',
             'kannst', 'beispiel', 'zurück', 'warum', 'sah', 'kleines', 'anderr', 'wo', 'guter', 'sonst', 'mancher',
             'eures', 'dermaßen', 'müsst', 'sechster', 'h', 'genug', 'als', 'des', 'neben', 'gekonnt', 'geht', 'um',
             'Zudem', 'document',
             }

datei = input("Textdatei: ")
content = open(datei).read()
for zeichen in string.punctuation:
  content = content.replace(zeichen, " ").lower()
woerter = content.split()
word = [w for w in woerter if w not in STOPWORDS]
dict = {}
for i in word:
  dict[i] = word.count(i)

sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
sorted_dict.reverse()
print(sorted_dict)  
