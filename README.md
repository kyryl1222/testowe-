# Testowanie aplikacji - przykład repozytorium Git/GitHub

To repozytorium zawiera prostą aplikację w Pythonie oraz przykładowe testy PyTest.

## Zawartość
```
src/
 ├── app.py         # kod źródłowy aplikacji
 └── test_app.py    # testy jednostkowe
docs/
 ├── README.md      # opis projektu
 └── TEST_PLAN.md   # plan testów
.github/
 └── workflows/
     └── tests.yml  # automatyczne testowanie (GitHub Actions)
```

## Uruchamianie testów lokalnie
1. Zainstaluj bibliotekę PyTest:
   ```bash
   pip install pytest
   ```
2. Uruchom testy:
   ```bash
   pytest src/test_app.py
   ```

## Automatyzacja testów
Repozytorium zawiera plik konfiguracyjny GitHub Actions (`.github/workflows/tests.yml`), który automatycznie uruchamia testy po każdym commicie.
