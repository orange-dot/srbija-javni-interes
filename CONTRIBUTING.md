# 🤝 DOPRINOŠENJE PROJEKTU

Hvala što želiš da pomogneš u dokumentovanju korupcije!

Ovaj projekat je **otvoreni, javni projekat** - svako može doprineti.

---

## 📋 KAKO DOPRINETI

### Tip 1: PRONAŠAO SAM GREŠKU

**Što uraditi:**

1. Otvori [GitHub Issue](../../issues/new)
2. Naslov: `[GREŠKA] - Kratak opis`
3. Opis: Gde je greška, šta je pogrešno, kako treba biti

**Primer:**
```
Naslov: [GREŠKA] - Pogrešan datum mandata Ane Brnabić

Opis:
- Prijava kaže: "18. oktobar 2017"
- Trebalo bi: "29. jun 2017"
- Dokaz: https://www.vlada.rs/[link]
```

### Tip 2: NOVA ISTRAŽIVANJA / DOKAZI

**Što uraditi:**

1. Prikupli novi dokaz/istraživanje
2. Verificiraj iz **najmanje 2 pozitivna izvora** (BIRN, KRIK, DRI, EU, RTS, N1)
3. Otvori [GitHub Issue](../../issues/new) sa:
   - Naslov: `[DOKAZ] - Naslov nove afere`
   - Opis: Šta je novo, gde je iz, zašto je važno
4. Ili direktno napravi Pull Request sa novim fajlom

**Primer:**
```
Naslov: [DOKAZ] - Afera Respiratori u Vranju

Opis:
Pronašao sam dodatnu aferuje sa respiratorima u Vranju:
- 50 respiratora, €300K, nema isporuke
- Izvor: BIRN izveštaj "Respiratori: Vranje" (2021)
- Direktno povezano sa BTL Medical aferom
- Trebalo bi dodati u Prijavu IV
```

### Tip 3: NOVI DOKUMENT / ANALIZA

**Što uraditi:**

1. Napiši analizu ili dokument
2. Koristi struktur od drugih dokumenata
3. Svaku tvrdnju podrži sa barem 1 izvorom
4. Napiši u Markdown formatu
5. Otvori Pull Request sa:
   - Naslov: `[NOVI DOKUMENT] - Naziv`
   - Opis: Šta je dokument, šta dokazuje
   - Format: Markdown (.md)

**Struktura dokumenta:**
```markdown
# NAZIV DOKUMENTA

**Tip:** Analiza / Istraživanje / Izveštaj
**Fokus:** O čemu je
**Izvori:** Gde je iz

---

## Sažetak
[Kratak pregled]

---

## Detaljno

[Sadržaj sa citacijama]
```

### Tip 4: PREVOD NA DRUGI JEZIK

**Što uraditi:**

1. Odaberi jedan dokument
2. Prevedi na ceo jezik (en, de, fr, ru, hu itd)
3. Napiši kao `DOKUMENT.JEZIK.md`
   - Primer: `PRIJAVA_I_KORUPCIJA.en.md`
4. Otvori Pull Request sa:
   - Naslov: `[PREVOD] - Dokumenta na [JEZIK]`

### Tip 5: POBOLJŠANJA / REFAKTORISANJE

**Što uraditi:**

1. Vidiš da se nešto može bolje
2. Formatuješ, čitljiviju strukturu itd
3. Otvori Pull Request sa:
   - Naslov: `[POBOLJŠANJE] - Šta je poboljšano`
   - Opis: Zašto je bolje

---

## 🚀 GIT WORKFLOW

### Za Male Izmene (Greške, Male Dopune)

```bash
# 1. Forkan projekt
# (Klikni "Fork" na GitHub-u)

# 2. Klonira svoj fork
git clone https://github.com/TVOJ_USERNAME/prijava.git
cd prijava

# 3. Napravi novu granu
git checkout -b fix/greska-u-datumu

# 4. Napravi izmene
# (Uredi fajlove)

# 5. Commit sa dobrim porukom
git add .
git commit -m "Ispravka: Pogrešan datum mandata Ane Brnabić (18.10 -> 29.06)"

# 6. Push na svoj fork
git push origin fix/greska-u-datumu

# 7. Otvori Pull Request na GitHub-u
```

### Za Nove Dokumente

```bash
# 1-3. Isto kao gore, ali sa drugom granom
git checkout -b feature/nova-analiza-respiratora

# 4. Napravi novi fajl
# prijave/ANALIZA_RESPIRATORI.md

# 5. Commit sa porukom
git commit -m "Dodaj: Analiza respiratorske afere u Vranju"

# 6-7. Push i Pull Request
```

---

## 📏 STANDARDI ZA DOPRINOŠENJE

### Zahtevi za Sve Dokumente

1. **Verifikovani Dokazi**
   - Svaka tvrdnja mora biti iz javnog izvora
   - Preporučeno: 2+ izvora za važne tvrdnje
   - Navedi izvor na kraju čini ili u tabeli

2. **Struktura**
   - Koristi Markdown format (.md)
   - Koristi naslove (# ## ###)
   - Koristi tabele za podatke
   - Koristi liste za stavke

3. **Kvalitet Pisanja**
   - Jasno i precizno
   - Kratke rečenice
   - Bez emocionalnog jezika
   - Profesionalni ton

4. **Izvori**
   - BIRN (Balkan Investigative Reporting Network)
   - KRIK (Centar za istraživačko novinarstvo Srbije)
   - CINS (Centar za istraživačko novinarstvo)
   - DRI (Državna revizorska institucija)
   - EU Komisija (Progress reports)
   - Mediji: RTS, N1, Danas, Telegraf, Beta, Tanjug
   - Transparentnost Srbija
   - APR (Agencija za privredne registre)
   - Paragraf.rs (Zakonski tekstovi)

5. **Izbegavati**
   - ❌ Spekulacije bez dokaza
   - ❌ Privatne informacije
   - ❌ Lične podatke (osim javnih ličnosti)
   - ❌ Teorije zavere
   - ❌ Emocije umesto dokaza

### Specifični Zahtevi po Tipu

#### Za Nove Prijave
- Minimum 5-10 dokumentovanih afere
- Pravni okvir sa člancima
- Barem 3 različita izvora
- Lanca dokaza (A → B → C)

#### Za Analize
- Početni kontekst
- Glavne tvrdnje sa podacima
- Tabele ili grafikone ako je moguće
- Zaključci i preporuke

#### Za Prevode
- Tačan prevod (nije parafrazirani)
- Ista struktura kao original
- Proveren od strane roditelja
- Gramatički ispravan

---

## 📝 COMMIT PORUKE

Piši dobre commit poruke:

**Format:**
```
[TIP] - Kratko objašnjenje (do 50 karaktera)

Duže objašnjenje ako je potrebno
(do 72 karaktera po liniji)

Referenca: GitHub issue #123 ako je primenjivo
```

**Tipovi:**
- `[ISPRAVKA]` - Greške / Bug fix
- `[DODAJ]` - Novi dokument ili sadržaj
- `[AŽURI]` - Ažuriranje postojećeg dokumenta
- `[REFAKTOR]` - Poboljšanja bez novih sadržaja
- `[PREVOD]` - Novi prevod

**Primeri:**
```
[ISPRAVKA] - Pogrešan datum mandata Ane Brnabić (18.10 → 29.06)

[DODAJ] - Nova analiza respiratorske afere u Vranju

[AŽURI] - Dodaj novu BIRN referencu u PRIJAVU_I

[PREVOD] - PRIJAVA_I na English
```

---

## 🔍 REVIEW PROCES

### Šta Se Dešava Posle PR-a

1. **Automatska Provera**
   - Markdown sintaksa
   - Speling (ako je dostupno)
   - Linkovi (da li rade)

2. **Ručna Provera** (od strane održavača)
   - Jesu li dokazi validni?
   - Jesu li izvori pouzdani?
   - Jesu li ispravljeni standardi?
   - Jesu li komenti jasni?

3. **Zahtevi za Izmene** (ako je potrebno)
   - Dodaj više dokaza
   - Ispravi grešku
   - Pojasni formaciju itd.

4. **Merge** ✅
   - PR je odobren
   - Tvoj dokument je del projekta

---

## 💡 SAVETI ZA DOBRE DOPRINOSE

### Prvo Otvori Issue

Pre nego što radiš velikom promenom:

1. Otvori Issue sa naslovom
2. Čekaj povratnu informaciju
3. Onda radiš dokument
4. Sprečavaš bacenu trud

### Čitaj Postojeće Dokumente

- Nauči stil od Prijava I-IV
- Koristi iste strukture
- Sledi istim standardima
- Budi konzistentan

### Verifikuj Podatke Malo Više

- Ako koristiš BIRN podatak, koristi original BIRN izveštaj
- Ako koristiš DRI podatak, koristi original DRI izveštaj
- Nikada ne koristi "čuo sam da..."
- Uvek napiši gdje je iz

### Komuniciraj

- Ako nešto nije jasno, pitaj u Issue-u
- Ako imaš ideju, otvori diskusiju
- Ako vidiš problem, javi ga

---

## 📧 KONTAKT I PITANJA

**Ako imaš pitanja:**

1. Pogledaj postojeće Issues - možda je već odgovoren
2. Otvori novi Issue sa naslovom `[PITANJE] - Šta te zanima`
3. Čekaj odgovor od održavača

**Za brže odgovore:**
- Budi konkretan u pitanju
- Obezbeđi kontekst
- Linkovati relevantne dokumente

---

## 🎓 NAUČITI VIŠE O AFERAMA

Ako želiš da razumeš afere bolje:

1. Čitaj originalne BIRN, KRIK članke
2. Pogledaj DRI izveštaje
3. Sledi EU Progress Report-e
4. Čitaj medijske izveštaje (RTS, N1, Danas)
5. Traži javne tužilačke dokumente

---

## 🌍 UTICAJ DOPRINOŠENJA

Svaki doprinos je važan:

- **Ispravka datuma** → Prijavlja je validnija za sud
- **Novi dokaz** → Tužilac ima još materijala za istragu
- **Prevod** → Međunarodno postaje dostupnije
- **Analiza** → Građani razumeju kompleksnost
- **Poboljšanja** → Projekat je čitljiviji

---

## ✅ CHECKLIST PRE PODNOŠENJA PR-a

```
□ Čitao sam CONTRIBUTING.md
□ Dokumentao sam sve tvrdnje sa izvorima
□ Korišćeni su samo javni/dostupni izvori
□ Markdown sintaksa je ispravna
□ Nema privatnih informacija
□ Nema teorija zavere
□ Dokument je čitljiv i jasno napisan
□ Linkovi rade (ili sam siguran da će uskoro)
□ Commit poruke su dobre
□ Tekst je proveran (nema očiglednih grešaka)
```

---

## 🙏 HVALA NA DOPRINOŠENJU!

Svaki doprinos, od male ispravke do novog istraživanja, pomaže u:

✅ Dokumentovanju korupcije
✅ Prikupljanju dokaza za sud
✅ Edukaciji javnosti
✅ Jačanju demokratije
✅ Zaštiti ljudskih prava

**Zajedno možemo da promenimo stvari.**

---

**Verzija:** 1.0
**Datum:** 20. novembar 2025
**Status:** Aktivno čeka doprinose
