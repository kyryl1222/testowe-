To repozytorium zawiera prostą aplikację w Pythonie oraz przykładowe testy PyTest.

## Zawartość
```

aplikacja.py    # kod źródłowy aplikacji 
test_app.py    # testy jednostkowe
README.md      # opis projektu

```

## Uruchamianie testów lokalnie
1. Zainstaluj bibliotekę PyTest:
   ```bash
   pip install pytest
   ```
2. Uruchom testy:
   ```bash
   pytest test_app.py
   ```

## Automatyzacja testów
Repozytorium zawiera plik konfiguracyjny GitHub Actions (`.github/workflows/tests.yml`), który automatycznie uruchamia testy po każdym commicie.
