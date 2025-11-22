# Plan Analiza i Prevođenja Srpskih Dokumenata - NOVI (sa dostupnim agentima)

## Pregled procesa
Kompletan process obrade svih srpskih fajlova iz foldera `/prijave/` kroz sledeće faze sa dostupnim agentima:

1. **FAZA 1: Provera srpskog pravnog teksta** (srpski-pravni-provera + eu-legal-grammar-checker)
2. **FAZA 2: Pravna analiza i validacija** (srdja + process-oversight-monitor)
3. **FAZA 3: Konverzija Latinica → Ćirilica** (Python skript)
4. **FAZA 4: Prevod Latinica → Engleski** (serbian-english-legal-translator)
5. **FAZA 5: Simulacije sudskih postupaka** (sudija-simulator + witness-simulator + expert testimony)
6. **FAZA 6: Analiza proceduralne odbrane** (proceduralni-odbrameni-mehanizmi + ujo)

---

## FAZA 1: PROVERA SRPSKOG PRAVNOG TEKSTA

### Opis
Detaljni pregled srpskog jezika i pravnog tekstualnog kvaliteta kroz dva agenta:
- **srpski-pravni-provera**: Gramatika, stil, logička struktura, konzistentnost srpskog jezika
- **eu-legal-grammar-checker**: Specijalizovana provera za EU institucionalni diskurs, formalne reference

### Fajlovi za proveru

| Redni broj | Fajl | srpski-pravni-provera | eu-legal-grammar-checker | Status |
|-----------|------|----------------------|-------------------------|--------|
| 1 | PRIJAVA_I_KORUPCIJA.md | ✓ | ✓ | Pending |
| 2 | PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md | ✓ | ✓ | Pending |
| 3 | PRIJAVA_III_POLITICKA_ODGOVORNOST.md | ✓ | ✓ | Pending |
| 4 | PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO.md | ✓ | ✓ | Pending |
| 5 | PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md | ✓ | ✓ | Pending |
| 6 | PRILOZI_LICNI_SLUCAJEVI.md | ✓ | ✓ | Pending |
| 7 | DOKAZ_NEKOORDINACIJA_KIKINDA.md | ✓ | ✓ | Pending |

### Napomena
- **srpski-pravni-provera**: Proverava gramatiku, stil, logičku strukturu
- **eu-legal-grammar-checker**: Specijalizovana za EU institucionalni kontekst i formalne reference
- Rezultati: Detaljni izveštaji sa preporukama za oba agenta

---

## FAZA 2: PRAVNA ANALIZA I VALIDACIJA

### Opis
Detaljne pravne analize kroz dva agenta:
- **srdja**: Pravna analiza srpske krivične procedure, primena krivičnog zakonodavstva i EU acquisa
- **process-oversight-monitor**: Analiza proceduralne pravilnosti i identifikacija mogućih procedurnih povreda

### Fajlovi za analizu

| Redni broj | Fajl | srdja | process-oversight-monitor | Status |
|-----------|------|-------|--------------------------|--------|
| 1 | PRIJAVA_I_KORUPCIJA.md | ✓ | ✓ | Pending |
| 2 | PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md | ✓ | ✓ | Pending |
| 3 | PRIJAVA_III_POLITICKA_ODGOVORNOST.md | ✓ | ✓ | Pending |
| 4 | PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO.md | ✓ | ✓ | Pending |
| 5 | PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md | ✓ | ✓ | Pending |
| 6 | PRILOZI_LICNI_SLUCAJEVI.md | ✓ | ✓ | Pending |
| 7 | DOKAZ_NEKOORDINACIJA_KIKINDA.md | ✓ | ✓ | Pending |

### Napomena
- **srdja**: Fokus na correctness prema srpskom zakonodavstvu i EU regulativama
- **process-oversight-monitor**: Analiza proceduralne pravilnosti, mogućih povrada i validnosti
- Rezultati: Strukturirane pravne analize sa identifikovanim problemima

---

## FAZA 3: KONVERZIJA LATINICA → ĆIRILICA

### Opis
Konverzija svih srpskih dokumenata iz Latinice u Ćirilicu (Python skript ili manual)

### Fajlovi za konverziju

| Izvorni fajl (Latinica) | Cilj fajl (Ćirilica) | Status |
|------------------------|-------------------|--------|
| PRIJAVA_I_KORUPCIJA.md | PRIJAVA_I_KORUPCIJA_CIRILICA.md | Pending |
| PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md | PRIJAVA_II_ORGANIZOVANI_KRIMINAL_CIRILICA.md | Pending |
| PRIJAVA_III_POLITICKA_ODGOVORNOST.md | PRIJAVA_III_POLITICKA_ODGOVORNOST_CIRILICA.md | Pending |
| PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO.md | PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO_CIRILICA.md | Pending |
| PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md | PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE_CIRILICA.md | Pending |
| PRILOZI_LICNI_SLUCAJEVI.md | PRILOZI_LICNI_SLUCAJEVI_CIRILICA.md | Pending |
| DOKAZ_NEKOORDINACIJA_KIKINDA.md | DOKAZ_NEKOORDINACIJA_KIKINDA_CIRILICA.md | Pending |

### Napomena
- **Novi fajlovi** - ne menjati originalne
- Python skript: `python-cyrillic-converter.py` (ako dostupan)
- Ili korišćenje online konvertera

---

## FAZA 4: PREVOD LATINICA → ENGLESKI

### Opis
Prevod svih srpskih dokumenata (u Latinici) na engleski kroz specijalizovanu agenta:
- **serbian-english-legal-translator**: Fokus na preciznu pravnu terminologiju i očuvanje EU institucionalnog konteksta

### Fajlovi za prevod

| Srpski fajl (Latinica) | Engleski fajl | Status |
|----------------------|--------------|--------|
| PRIJAVA_I_KORUPCIJA.md | PRIJAVA_I_KORUPCIJA_EN.md | Pending |
| PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md | PRIJAVA_II_ORGANIZOVANI_KRIMINAL_EN.md | Pending |
| PRIJAVA_III_POLITICKA_ODGOVORNOST.md | PRIJAVA_III_POLITICKA_ODGOVORNOST_EN.md | Pending |
| PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO.md | PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO_EN.md | Pending |
| PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md | PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE_EN.md | Pending |
| PRILOZI_LICNI_SLUCAJEVI.md | PRILOZI_LICNI_SLUCAJEVI_EN.md | Pending |
| DOKAZ_NEKOORDINACIJA_KIKINDA.md | DOKAZ_NEKOORDINACIJA_KIKINDA_EN.md | Pending |

### Napomena
- **Novi fajlovi** - ne menjati originalne
- **serbian-english-legal-translator**: Specijalizovana za srpsko-engleski prevod sa fokusom na EU regulativu
- Fokus na preciznu pravnu terminologiju
- Čuvanje reference na srpsko zakonodavstvo

---

## FAZA 5: SIMULACIJE SUDSKIH POSTUPAKA

### Opis
Validacija dokumenata kroz simulacije sudskih postupaka sa tri agenta:
- **sudija-simulator**: Simulacija sudskog postupka i revizije dokumenata kao sudija
- **witness-simulator**: Simulacija svedočenja i mogućeg ospora od strane odbrane
- **sudski-vestaćina-expert**: Analiza dokaza kroz stručnjačko veštačenje

### Fajlovi za simulaciju

| Redni broj | Fajl | sudija-simulator | witness-simulator | expert-testimony | Status |
|-----------|------|-----------------|------------------|-----------------|--------|
| 1 | PRIJAVA_I_KORUPCIJA.md | ✓ | ✓ | ✓ | Pending |
| 2 | PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md | ✓ | ✓ | ✓ | Pending |
| 3 | PRIJAVA_III_POLITICKA_ODGOVORNOST.md | ✓ | ✓ | ✓ | Pending |
| 4 | PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO.md | ✓ | ✓ | ✓ | Pending |
| 5 | PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md | ✓ | ✓ | ✓ | Pending |
| 6 | PRILOZI_LICNI_SLUCAJEVI.md | ✓ | ✓ | ✓ | Pending |
| 7 | DOKAZ_NEKOORDINACIJA_KIKINDA.md | ✓ | ✓ | ✓ | Pending |

### Napomena
- **sudija-simulator**: Ocena dokumenata sa sudijske perspective, analiza proceduralne korektnosti
- **witness-simulator**: Simulacija mogućih ispitivanja i ospora od strane odbrane
- **sudski-vestaćina-expert**: Ekspertna analiza dokaza, finansijskih transakcija, IT forensike
- Rezultati: Detaljni izveštaji o jačini slučaja iz sudske perspective

---

## FAZA 6: ANALIZA PROCEDURALNE ODBRANE

### Opis
Analiza mogućih procedurnih mehanizama koji bi mogli biti korišćeni u odbrani kroz dva agenta:
- **proceduralni-odbrameni-mehanizmi**: Mapiranje svih procedurnih odbrana dostupnih prema ZKP-u
- **ujo**: Analiza mehanizama za otkazivanje krivičnog postupka ili odbijanja optužbe

### Fajlovi za analizu

| Redni broj | Fajl | proceduralni-odbrameni | ujo-analiza | Status |
|-----------|------|----------------------|------------|--------|
| 1 | PRIJAVA_I_KORUPCIJA.md | ✓ | ✓ | Pending |
| 2 | PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md | ✓ | ✓ | Pending |
| 3 | PRIJAVA_III_POLITICKA_ODGOVORNOST.md | ✓ | ✓ | Pending |
| 4 | PRIJAVA_IV_EU_FONDOVI_MEDJUNARODNO.md | ✓ | ✓ | Pending |
| 5 | PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md | ✓ | ✓ | Pending |
| 6 | PRILOZI_LICNI_SLUCAJEVI.md | ✓ | ✓ | Pending |
| 7 | DOKAZ_NEKOORDINACIJA_KIKINDA.md | ✓ | ✓ | Pending |

### Napomena
- **proceduralni-odbrameni-mehanizmi**: Identifikacija svih mogućih procedurnih defenzi
- **ujo**: Mapiranje mehanizama za odbijanje krivičnog postupka
- Rezultati: Analiza mogućih slabosti u procesnom pogledu

---

## REDOSLED IZVRŠAVANJA

### Preporuka: PARALELNO PO FAZA

```
FAZA 1: srpski-pravni-provera + eu-legal-grammar-checker na svih 7 fajlova (paralelno)
↓
FAZA 2: srdja + process-oversight-monitor na svih 7 fajlova (paralelno)
↓
FAZA 3: Konverzija Latinica → Ćirilica za svih 7 fajlova
↓
FAZA 4: serbian-english-legal-translator na svih 7 fajlova (paralelno)
↓
FAZA 5: Sudske simulacije (sudija, svedoci, eksperti) na svih 7 fajlova (paralelno)
↓
FAZA 6: Proceduralna analiza na svih 7 fajlova (paralelno)
```

### Alternativa: SEKVENCIJALNO PO FAJLU

```
Za svaki od 7 fajlova:
  1. Faza 1: Provera teksta
  2. Faza 2: Pravna analiza
  3. Faza 3: Konverzija u Ćirilicu
  4. Faza 4: Prevod na Engleski
  5. Faza 5: Sudske simulacije
  6. Faza 6: Proceduralna analiza
```

---

## OČEKIVANI REZULTATI

### Nakon Faze 1
- Detaljni izveštaji o jezičkim greškama
- Preporuke za poboljšanja srpskog teksta
- Provera EU institucionalnog standarda

### Nakon Faze 2
- Pravne analize prema ZKP-u i EU acquisu
- Identifikacija procedurnih problema
- Procena osnovanosti prijava

### Nakon Faze 3
- 7 novih fajlova u Ćirilici (u `/prijave/` folderu)
- Originalni fajlovi ostaju nepromenjeni

### Nakon Faze 4
- 7 novih engleskih verzija (u `/prijave/` folderu)
- Originalni fajlovi ostaju nepromenjeni
- Termiložka konzistentnost održana

### Nakon Faze 5
- Simulacijski izveštaji iz sudske perspektive
- Analiza jačine slučaja u sudskom procesu
- Identifikacija mogućih slabosti u dokazu

### Nakon Faze 6
- Analiza procedurnih mehanizama odbrane
- Identifikacija mogućih povrada procedurnog prava
- Procena rizika od procedurnih izazova

---

## STATUS PRAĆENJA

- [ ] Faza 1: Provera teksta - 0/7 fajlova (2 agenta)
- [ ] Faza 2: Pravna analiza - 0/7 fajlova (2 agenta)
- [ ] Faza 3: Ćirilica konverzija - 0/7 fajlova (Python)
- [ ] Faza 4: Engleski prevod - 0/7 fajlova (1 agent)
- [ ] Faza 5: Sudske simulacije - 0/7 fajlova (3 agenta)
- [ ] Faza 6: Proceduralna analiza - 0/7 fajlova (2 agenta)

**Ukupno: 0/42 koraka**

---

## DOSTUPNI AGENTI

### Jezički i korekturni agenti (jezicki_i_korekturni_agenti/)
1. **srpski-pravni-provera** - Provera srpskog pravnog teksta za gramatiku, stil, logiku
2. **eu-legal-grammar-checker** - Specijalizovana provera za EU institucionalni diskurs
3. **serbian-english-legal-translator** - Prevod srpski-engleski sa fokusom na pravnu terminologiju

### Simulacijski agenti (sim_agenti/)
1. **sudija-simulator** - Simulacija sudskog postupka i revizije dokumenata
2. **witness-simulator** - Simulacija svedočenja i mogućeg ospora
3. **sudski-vestaćina-expert** - Ekspertna analiza dokaza i finansijskih transakcija
4. **srdja** - Pravna analiza prema srpskom zakonodavstvu i EU acquisu
5. **process-oversight-monitor** - Analiza proceduralne pravilnosti
6. **proceduralni-odbrameni-mehanizmi** - Mapiranje procedurnih mehanizama odbrane
7. **ujo** - Analiza mehanizama za odbijanje krivičnog postupka

---

## NAPOMENE

1. **Originalni fajlovi**: Ostaju nepromenjeni tokom celog procesa
2. **Novi fajlovi**: Kreiraju se samo u fazama 3, 4
3. **Agenti**: Svi dostupni u `/prijave/instrukcije/` folderu (jezicki_i_korekturni_agenti/ + sim_agenti/)
4. **Paralelizacija**:
   - Faza 1: Oba agenta mogu biti pokrenuta na 7 fajlova paralelno
   - Faza 2: Oba agenta mogu biti pokrenuta na 7 fajlova paralelno
   - Faza 4: Agent može biti pokrenut na 7 fajlova paralelno
   - Faza 5: Sva 3 agenta mogu biti pokrenuta na 7 fajlova paralelno
   - Faza 6: Oba agenta mogu biti pokrenuta na 7 fajlova paralelno
5. **Redosled**: Faze se izvršavaju redom - sledeća faza počinje kada je prethodna završena

