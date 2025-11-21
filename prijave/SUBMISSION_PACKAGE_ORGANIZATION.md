# SUBMISSION PACKAGE ORGANIZATION
## Logičan redosled dokaza za tužilaštvo i međunarodne institucije

**Pripremljeno:** 22. novembar 2025
**Status:** Strukturni vodič za submission
**Verzija:** 1.0 – finalna organizacija

---

## I. OVERVIEW – STRATEGIJA SUBMISSION-a

Dokumenti su organizovani u tri paralelne grane:
1. **Domaća tužilaštva** – srpski sudovi (Viši javni tužilac, Tužilaštvo za organizovani kriminal)
2. **Međunarodne institucije** – EU, OLAF, EPPO, EUROPOL, GRECO
3. **Javnost** – prosljeđivanje medijima i humanitarnim organizacijama (opciono)

---

## II. FAZA 1: POČETNA SUBMISSION – DOMAĆA TUŽILAŠTVA

### Redosled čitanja i submission-a:

**KORAK 1 – Pravni okvir (PRIJAVA_III_POLITIČKA_ODGOVORNOST.md)**
- **Primordijalno:** Etablira imunitet i razloge zašto opšta tužilaštva ne mogu da postupaju
- **Dužina:** ~50 strana + 22 screenshot dokaza
- **Adresat:** Republički javni tužilac + Viši javni tužilac (Beograd)
- **Format:** Kao PRVI dokument – postavlja pravni kontekst
- **Razlog:** Ako je tužilaštvo blokirano imunitetom, pokazuje da je potreban poseban pristup

**KORAK 2 – Sistemska korupcija (PRIJAVA_I_KORUPCIJA.md)**
- **Fokus:** Konkretne zloupotebe zdravstva i socijalne zaštite
- **Dužina:** ~45 strana + 17 screenshot dokaza
- **Dokazi:** 13 smrti u požarima domova bez odobrenja, 60.000 građana bez nege
- **Adresat:** Viši javni tužilac (Beograd)
- **Razlog:** Osnova za sve domaće postupke – pokazuje šta se desilo i gdje je failed sistem

**KORAK 3 – Organizovani kriminal (PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md)**
- **Fokus:** Struktura grupe, koordinacija između Brnabić–Mali–Lončar
- **Dužina:** ~35 strana + 5 screenshot dokaza
- **Adresat:** Tužilaštvo za organizovani kriminal (Beograd)
- **Razlog:** Pokazuje da nije slučaj već sistematska grupa sa financijskim tokom

**KORAK 4 – Lični slučajevi (PRILOZI_LICNI_SLUCAJEVI.md)**
- **Fokus:** 4 dokumentovana slučaja (3 mrtva pacijenta + 1 aktivni slučaj)
- **Dužina:** ~40 strana
- **Adresat:** Javno tužilaštvo (za građanske odštetne zahteve + krivični postupak)
- **Razlog:** Neposredni dokazni osnov za pokretanje postupka, tipični primeri sistemskog problema

---

## III. FAZA 2: MEĐUNARODNE INSTITUCIJE

### Paralelna submission – simultano sa domaćim ili odmah nakon:

**ZA OLAF (EU Anti-Fraud Office):**
1. PRIJAVA_IV_EU_FONDOVI_MEĐUNARODNO.md (~40 strana + 17 screenshot dokaza)
2. PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md (~6 strana)
3. PRILOG_LEGAL_APPENDIX_EVIDENCE.md (citati i literatura)
4. SCREENSHOT_EVIDENCE_MANIFEST.md (pregled svih vizuelnih dokaza)
- **Razlog:** OLAF ima direktnu nadležnost nad zlouporebom EU fondova (IPA III 450M+ EUR)

**ZA EPPO (Evropski javni tužilac):**
- Ista kao OLAF + dodatne finansijske analize
- **Razlog:** PIF Direktiva – sučesništvo EU funkcionera u zloupotrebi EU novca

**ZA EUROPOL (Organized Crime):**
- PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md
- Финансијска analiza Sinise Malog (45 bankovnih računa)
- **Razlog:** Organizovani kriminal sa međunarodnom dimenzijom (offshore, Kipar, Crna Gora)

**ZA GRECO (Council of Europe – Anti-Corruption):**
- PRIJAVA_III_POLITIČKA_ODGOVORNOST.md
- Izvještaj o imunitetu i nedostatku odgovornosti
- **Razlog:** Evaluacija srpskog sistema za borbu protiv korupcije

---

## IV. FAZA 3: DOKAZNA PODRŠKA

### Dokumenti koji prate sve submission-e:

**1. PRILOG_LEGAL_APPENDIX_EVIDENCE.md**
- Bibliografske reference (6 ključnih izvora)
- Direktni citati iz međunarodnih izveštaja
- Kako citirati dokaze u srpskim sudovima
- **Korišćenje:** Kao prilog uz sve PRIJAVE – tužilaštvo može direktno citirati

**2. SCREENSHOT_EVIDENCE_MANIFEST.md**
- Indeks svih 30 screenshot dokaza
- Mapiranje na konkretne PRIJAVE
- Procena pravne branljivosti
- **Korišćenje:** Tužilaštvo zna gdje su vizuelni dokazi i kako se koriste

**3. DOKAZ_NEKOORDINACIJA_KIKINDA.md**
- Detaljni sled emails/SMS između institucija
- Konkretan primjer sistemske disfunkcije
- **Korišćenje:** Za PRIJAVU_I i PRIJAVA_IV – kao studija slučaja

---

## V. TABELA SUBMISSION-a

| **Institucija** | **Prioritet** | **Dokumenti** | **Redosled** | **Napomena** |
|---|---|---|---|---|
| **Viši javni tužilac (Beograd)** | 1 | III → I → II → Lični slučajevi | Sekvencijalno | Establira imunitet, onda dokazuje korupciju |
| **Tužilaštvo za org. kriminal** | 1 | II + Finanse Mali | Simultano sa VJT | Struktura grupe i tokovi novca |
| **OLAF (EU)** | 1 | IV + B + Legal appendix | Simultano sa domaćim | EU fondovi (450M+) – direktna nadležnost |
| **EPPO (EU)** | 1 | IV + B + PIF Direktiva | Simultano sa OLAF | Sučesništvo EU funkcionera |
| **EUROPOL** | 2 | II + Mali finansije | Nakon OLAF | Organizovani kriminal sa OF elementima |
| **GRECO** | 2 | III + sistem analiza | Nakon OLAF | Anti-korupcija evaluacija |

---

## VI. STRUKTURA FIZIČKOG PAKETA

```
SUBMISSION_PAKET_DOMAĆE_TUŽILAŠTVO/
├── 00_COVER_LETTER_VJT.md         [Pismo tužilacu]
├── 01_PRIJAVA_III_POLITIČKA_ODGOVORNOST.md    [PRVI dokument]
├── 02_PRIJAVA_I_KORUPCIJA.md
├── 03_PRIJAVA_II_ORGANIZOVANI_KRIMINAL.md
├── 04_PRILOZI_LICNI_SLUCAJEVI.md
├── 05_PRILOG_LEGAL_APPENDIX_EVIDENCE.md
├── 06_SCREENSHOT_EVIDENCE_MANIFEST.md
├── 07_DOKAZ_NEKOORDINACIJA_KIKINDA.md
└── EVIDENCE_FOLDER/
    └── [30 screenshot PNG fajlova]

SUBMISSION_PAKET_OLAF/
├── 00_COVER_LETTER_OLAF.md
├── 01_PRIJAVA_IV_EU_FONDOVI_MEĐUNARODNO.md
├── 02_PRILOG_B_EU_FUNKCIONERI_PRIKRIVANJE.md
├── 03_PRILOG_LEGAL_APPENDIX_EVIDENCE.md
├── 04_SCREENSHOT_EVIDENCE_MANIFEST.md
└── EVIDENCE_FOLDER/
    └── [Relevantni screenshot-ovi]
```

---

## VII. TIMELINE SUBMISSION-a

### **Sedmica 1 – Domače tužilaštva (simultano)**
- **Dan 1:** Submission VJT (Beograd) + Tužilaštvo za org. kriminal
- **Dan 2-3:** Follow-up pozivi, potvrde prijema
- **Dan 4:** Provjera da li su dokumenti dostavljeni

### **Sedmica 2 – Međunarodne institucije (simultano)**
- **Dan 8:** OLAF (email + portal podnošenja)
- **Dan 8:** EPPO (usmjeravanje kroz OLAF ili direktno)
- **Dan 9:** EUROPOL (kroz domaće tužilaštvo ili direktno)
- **Dan 9-10:** GRECO (otvoreni zahtjev za evaluaciju)

### **Sedmica 3 – Javnost (opciono)**
- **Dan 15:** Mediji (KRIK, BIRN, Balkan Insight)
- **Dan 15:** Amnesty International, Human Rights Watch
- **Dan 15:** Novinari (Direktno.rs, N1, RTS)

---

## VIII. STRATEGIJA ZA SVAKU INSTITUCIJU

### **Viši javni tužilac (Beograd)**

**Pismo:**
> Poštovani,
>
> U prilogu dostavljam četiri krivične prijave koje dokumentuju:
> 1. Institucijsku imunitetnu zaštitu određenih zvaničnika (PRIJAVA III)
> 2. Sistemsku korupciju u zdravstvu i socijalnoj zaštiti (PRIJAVA I)
> 3. Organizovanu strukturu zloupotrebljivanja (PRIJAVA II)
> 4. Specifične slučajeve sa dokumentovanim štetama (Lični slučajevi)
>
> Svi dokumenti su potpuno anonimizovani, potkrepljeni međunarodnim izveštajima i 30 screenshot dokaza od javnih institucija i novinara.
>
> Primjena zahtijeva:
> - Ukidanje imuniteta (preko Skupštine) ili
> - Specijalni postupak pred nekim tijelima (npr. za finansijske tokove)
>
> Dostavio/a sam i sve dokazne materijale (30 PNG screenshot-a, email prepisku, medicinske dokumente).

**Čekati:**
- Potvrdu prijema (obično do 5 dana)
- Raspodjelu između odjeljenja (politička, korupcija, org. kriminal)
- Mogući zahtjev za dodatnim dokazima

---

### **OLAF (EU Anti-Fraud Office)**

**Pismo:**
> Dear OLAF,
>
> I hereby submit a formal complaint regarding the misuse of EU IPA III funds in Serbia (450M+ EUR) involving:
> 1. Respiratory procurement fraud (8.9M EUR – undelivered)
> 2. Phantom IT companies (18M EUR – non-existent)
> 3. Systematic weakening of EU oversight by officials (Varhelyi, Bilcik, etc.)
> 4. Systemic dysfunction in healthcare and social services funded by EU
>
> All evidence is documented with screenshots, international reports, and email correspondence. This involves both domestic actors and EU officials' complicity through report manipulation.
>
> I request:
> - Formal investigation
> - Recovery of misappropriated funds
> - Disciplinary action against EU officials
> - Coordination with Serbian authorities

**Portal za submission:** https://anti-fraud.ec.europa.eu/

---

### **EPPO (European Public Prosecutor)**

**Pismo:**
> Similar to OLAF but emphasizing:
> - Direktiva 2017/1371 (PIF) – zaštita finansijskih interesa EU
> - Sučesništvo EU funkcionera kroz nečinjenje (passivity)
> - Procjena štetnih efekata: najmanje 131.9M EUR

---

## IX. OČEKIVANI ODGOVORI I SLJEDEĆI KORACI

### **Worst-case scenario:**
- Tužilaštva ne poklapaju postupak zbog imuniteta
- OLAF počinje istragu ali polako
- Potreban je medijski pritisak

### **Best-case scenario:**
- VJT počinje istragu u roku 2-3 mjeseca
- OLAF otvara istragu u roku 4-6 mjeseci
- Mediji počinju pokrivati u roku 1 mjeseca

### **Plan B – ako tužilaštva ne reaguju:**
- Submission kroz EU Delegaciju (EU Ambassador Serbia)
- Izvještaj Amnesty International (trebala bi inicijativa)
- Pokretanje građanskih tužbi za odštetne zahtjeve

---

## X. CHECKLIST ZA SUBMISSION

- [ ] Svi dokumenti prebačeni u PDF format (ako trebaju) ili ostaju kao .md
- [ ] Svaki dokument ima cover page sa imenom institucije
- [ ] Lični podaci jasno označeni kao [Pacijent], [Srodnik], [GC radnik] itd.
- [ ] Screenshot dokazi organizovani sa jasnim indeksom
- [ ] Svaki submission ima personalizirano pismo
- [ ] Dokumenti su dostavljeni u 2 formata: elektronski (email) + papirni (ako trebaju)
- [ ] Čuvan je backup svih dokumenata
- [ ] Sastavljena je korespondencija sa evidencijom datuma i primatelja

---

## XI. DOKUMENTA KOJA OSTAJU PRIVATNA

Ova dokumenta se **NE dostavljaju** javno već samo tužilaštvu pod striktnom zaštitom:

- **VERZIJA SA STVARNIM IMENIMA** – samo za tužilaštvo
- **Medicinska dokumentacija** – samo lekari i tužilaštvo
- **Email prepiski sa privatnim adresama** – samo za tužilaštvo
- **Bankarski podaci Sinise Malog** – samo za istragu

---

**Status:** Spreman za submission
**Verzija:** 1.0 – finalna organizacija
**Datum:** 22. novembar 2025
